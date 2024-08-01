---
title: Öneri Sistemi
description: Öneri Sistemi Yardım Dokümanı
sidebar_position: 21
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::


**Öneri Sistemi Modülü(v.5.24) Kullanıcı Yardım Dokümanı**

Modül Versiyonu: 5.24



1.  **GİRİŞ: “QDMS Öneri Modülü”** önerilerin girildiği, değerlendirildiği, sonuçlandırıldığı ve raporlandığı bir modüldür.
2.  **AMAÇ:** Bu yardım kılavuzunun amacı, öneri modülünün çalışma sürecini anlatmaktır. Öneri modülünün ne için kullanılması gerektiği, QDMS üzerinde nasıl tasarlanması gerektiği, altyapısında neler yapılması ve veri girişinde nelere dikkat edilmesi gerektiği anlatılmaktadır. Sistemde öneri girişlerinin nasıl yapıldığı, nasıl değerlendirildiği, nasıl puanlandığı ve önerinin nasıl kapatıldığı anlatılmaktadır.
3.  **SORUMLULUKLAR:** Öneri Proje Ekibi, Tüm Çalışanlar
4.  **İŞ AKIŞI:**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2880d87d-da08-41de-bc77-5e1a35162aa1)



# **Öneri Modülü**

Öneri; şikayet, dilek, istek, talep gibi yaklaşımların dışında kalan; sistemin, personelin, süreçlerin geliştirilmesinin hedeflendiği modüldür. Sisteme girilen bir önerinin belli onaylardan geçtikten sonra sistemde bir öneri kaydı olarak oluşması sağlanır.

Öneri sistemde verildikten sonra bir ön değerlendirme aşamasından geçer. Ön değerlendirme yapılmasının amacı; önerileri diğer bildirimlerden ayırmaktır. Açılan öneri ön değerlendirmeci tarafından değerlendirilerek bu bir öneri midir yoksa şikayet/ talep/ istek midir belirlenir. Ön değerlendirmeci tarafından kabul edilen öneri, seçilen uzmana değerlendirmeye gönderilir. Uzman değerlendirmeci öneriyi değerlendirirken bunun kendi bölümü ile ilgii olup olmadığını belirler. Eğer kendi bölümü ile ilgili değilse farklı bir uzmana yönlendirebilir. Uzman değerlendirmeci,verilen önerinin öneri olup olmadığına karar verir. Aksiyon ihtiyacı belirlenir. Aksiyon ihtiyacı varsa aksiyon planlamak üzere bir sonraki statüye geçilir. Eğer aksiyon ihtiyacı yoksa aksiyon planlama aşaması atlanarak kazanç/ maliyet analizine gidilir. Aksiyon Planlama statüsünde aksiyonlar planlandıktan sonra aksiyon gerçekleştirme aşamasını tamamlanır. Tamamlanan aksiyonlardan sonra kazanç/ maliyet analizine geçilir. Kazanç/ maliyet analizinde verilen önerinin maddi kazancı belirlenir. Kazanç/ maliyet analizinde başka departmanlara/ işyerlerine yaygınlaştırma yapılıp yapılmayacağı belirlenir. Puanlama aşamasında öneriye puan verilir. Puanlama işleminden sonra öneri kapatılır. Öneri verene sistem tarafından “Sonuçlanmış Önerilerim” olarak geri bildirim yapılır

## **Sistem Altyapı Tanımları/ Öneri – 1.Kısım**

**Menü Adı**: Sistem Altyapı Tanımları/ Öneri

Öneri modülünün altyapısını oluşturmak amacıyla gerekli tanımlamaların yapıldığı kısımdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadff006da4-5189-46d7-99e9-b533a4ecd5d5)

### **Uzman/Lider Tanımlama**

**Menü Adı**: Sistem Altyapı Tanımları/Öneri/Uzman/Lider Tanımlama

Öneri alındıktan sonra, bu menüden öneri ile ilgili Değerlendirme, Kazanç/ Maliyet, Puanlama gibi işlemleri sürdürecek kişiler tanımlanır. Yani bu alanda uzman değerlendirme statüsünde yer alacak kullanıcıların tanımlanması gerekir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf0dc98fd-f037-4afa-9a2f-1f6a19847676)

**Ekrandaki bulunan butonlar yardımıyla,**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9b69f324-16af-4a4b-b5e6-d87dfe3018ee): Yeni bir uzman değerlendirici tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf86c9042-ce5d-4e0b-8d16-5d726daff63a): Listede seçili olan uzman değerlendirici için değişiklik yapılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadab620467-0827-4e14-9555-980ebbfd3e8a): Listede seçili olan uzman değerlendirici silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbdb494b8-c881-4a6f-8d79-700b51ee6646): Kayıtlar filtrelenerek arama yapılır.

Yeni bir uzman/ lider eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3411874e-25eb-42b9-8ba2-9d9b628fd701)(yeni) butonu tıklanarak Uzman Tanımlama/ Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload79deb326-eec9-476e-86d3-002417bad632)

**Açılan ekranda aşağıdaki alanlar tanımlanır;**

**Uzman Adı Soyadı:** Sistemde tanımlı personel listesinden uzman değerlendirici seçilir.

**Yetkisi:** Seçilen uzmanın yetkisi belirlenir. “Puanlama” yetkisi en geniş yetki olup, “İnceleme/Değerlendirme” yetkisini de kapsar. Puanlama yetkisine sahip olan uzman değerlendirme basamağındaki tüm işlemleri gerçekleştirebilir. “İnceleme/ Değerlendirme” yetkisine sahip uzman ise puanlama dışındaki diğer işlemleri gerçekleştirebilir.

**Dahil No:** Uzmanın Dahili No bilgisi tanımlanabilir, bilgi amaçlıdır.

**Asil/ Yedek:** Uzmanın Asil/ Yedek bilgisinin seçilebildiği alandır. Bilgi amaçlıdır.

**Proje Grubu:** Uzmanın hangi proje grubunda yer aldığı seçilir. Proje grubu kullanılacaksa bu alan uzman tanımlama ekranında görüntülenir.

**Aktif/Pasif:** Uzmanın Aktif/ Pasif durumu seçilir.

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1b3d6181-4f04-4b9c-9430-d12c15032cbc) (kaydet) butonuna tıklanarak Uzman Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbd0b966c-7b06-4374-9634-be0531fe53fc)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload50457fa6-659b-4119-833b-8b824e90c004)

### **Kazanç Kategorisi Tanımlama**

**Menü Adı**: Sistem Altyapı Tanımları/Öneri/ Kazanç Kategorisi Tanımlama

Verilen önerilerin firmaya ne tür kazançlar sağlayacağının kategorize edildiği menüdür. Gelir arttırıcı, iş güvenliği, motivasyon arttırıcı, verimlilik arttırıcı olabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9cb952dd-c92c-4885-b12b-0aad7241afc0)

**Ekranda bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9b69f324-16af-4a4b-b5e6-d87dfe3018ee): Yeni bir kazanç/maliyet kategorisi tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf86c9042-ce5d-4e0b-8d16-5d726daff63a): Listede seçili olan kazanç/maliyet kategorisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadab620467-0827-4e14-9555-980ebbfd3e8a): Listede seçili olan kazanç/maliyet kategorisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbdb494b8-c881-4a6f-8d79-700b51ee6646): Kayıtlar filtrelenerek arama yapılabilir.

Yeni bir kazanç/ maliyet kategorisi eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3411874e-25eb-42b9-8ba2-9d9b628fd701) (yeni) butonuna tıklanarak Kazanç/Maliyet Tanımları/ Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2978797e-2d19-40e2-8bb9-6546a81c3826)

**Açılan ekranda aşağıdaki alanlar tanımlanır;**

**Üst Kategori:** Kazanç kategorileri ağaç kırılımı şeklinde oluşturulabilir. Örneğin; “iş güvenliği” ana kategori iken alt kategori olarak “kaza sayısı azaltıcı” tanımlanabilir. Üst kategori olarak daha önce sisteme ana kategori olarak tanımlanan “01-İş Güvenliği” seçilir ya da kazanç/ maliyet kategorisi tanımlama ekranında “01-İş Güvenliği” seçili iken yeni kayıt butonuna tıklanır. Böylece üst kategori kodu tanımlı olarak gelir. Bağlı olduğu üst kırılım silinmek istenildiğinde sağ yanda bulunan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadab2729f7-70cf-445a-9dbb-5483edb1feb4) (sil) butonu veya değiştirilmek istenildiğinde sağ yanda bulunan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload85ca3a7e-886c-49f2-a5ec-50763a23895c) (seç) butonu kullanılır. Bağlı olduğu bir üst kategori yok ise bu alan boş bırakılır.

**Kazanç/ Maliyet Tanımı:** Önerinin firmaya ne tür kazanç/ maliyet sağladığı bilgisi tanımlanır. Gelir arttırıcı, gider azaltıcı, standartlaştırma, verimlilik arttırıcı gibi.

**İş Yeri:** Tanımlanan kazanç/ maliyet bilgisi hangi işyerine aitse sistemde tanımlı olan işyeri listesinde seçilir.

**Aktif/ Pasif:** Tanımlanan Kazanç/ Maliyet Kategorisinin Aktif/ Pasif görünme durumu seçilir.

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1b3d6181-4f04-4b9c-9430-d12c15032cbc) (kaydet) butonu tıklanarak Kazanç/Maliyet Tanımı kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1428a818-1fff-4951-b835-ed2134f95ff4)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1fcae8a5-5fb9-4640-9066-d453298e18f3)

### **Kampanya Tanımlama**

**Menü Adı**: Sistem Altyapı Tanımları/ Öneri/ Kampanya Tanımlama

Belirli süreler için kampanya dönemleri tanımlanarak bu sürelerde verilen önerilere ekstra puan veya ödüller verebilir. Örneğin: önerinin az olduğu yaz aylarında kampanya uygulaması yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade9d5400e-d456-4762-bce3-231b5b55b18e)

**Ekranda bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9b69f324-16af-4a4b-b5e6-d87dfe3018ee): Yeni bir kampanya tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf86c9042-ce5d-4e0b-8d16-5d726daff63a): Listede seçili olan kampanya bilgisi ile ilgili değişiklik yapılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadab620467-0827-4e14-9555-980ebbfd3e8a): Listede seçili olan kampanya silinir.

Yeni bir kampanya eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3411874e-25eb-42b9-8ba2-9d9b628fd701)(yeni) butonu tıklanarak Kampanya Tanımlama/ Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6d704b0f-a1aa-4127-9eb7-b411f32305e2)

“Kampanya Tanımı” ve kampanyanın “Son Geçerlilik Tarihi” bilgisi girilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1b3d6181-4f04-4b9c-9430-d12c15032cbc) (kaydet) butonu ile kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2e3377ef-3c9f-405b-87d3-cb55f1e9d722)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload683c43a5-b658-4459-8e59-4237aa1d9c5a)

### **Puanlama Yönteminin Belirlenmesi**

Öneri puanlama aşamasında 3 tür puanlama yöntemi kullanılabilir; 1.si formüle bağlı puan tanımlama yöntemi, 2.si puan cetveli yöntemidir. Formüle bağlı puan tanımlama aşamasında değişkenler ve formül belirlendikten sonra hangi öneride hangi formül kullanılacaksa eşleştirmesi yapılır. Puan cetvelinde ise tüm öneri tiplerinde (personel önerisi, müşteri önerisi, tedarikçi önerisi) aynı puan cetveli kullanılabilir. 3. yöntem önerinin anket modülü üzerinden puanlama işlemidir.

Puanlama işlemi için 2 yöntemden biri tercih edilerek kullanılır. Eğer öneri puanlamada formül kullanılması isteniyorsa öneri modülü parametrelerinden “38. Puanlama kriterleri kullanılacak mı?” parametresi “Hayır” olarak ayarlanır. Eğer öneri puanlamada puan cetvelinin kullanılması isteniyorsa 38. parametre “Evet” olarak ayarlanır.

#### **Formül Kullanımı**

##### **Değişken Tanımlama**

**Menü Adı**: Sistem Altyapı Tanımları/ Öneri/ Değişken Tanımlama

Firmalar öneri puanlamalarını hesaplamak için birtakım formüller kullanır. Bu formülleri QDMS’e tanımlamak için öncelikle formülün içindeki değişkenlerin sisteme tanımlanması gerekir.

Değişken tanıtılırken, eğer bu değişken bir sorgu ile çekilecekse Bimser tarafından destek sağlanıp sorgunun yazılması sağlanmalıdır, kullanıcı seçimli olacaksa eğitim sırasında danışmanlar tarafından kolaylıkla formüller yazılabilir.

**![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade0ede7ef-f1e2-4097-9aca-28dbd6edd5ae)**

**Ekranda bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9b69f324-16af-4a4b-b5e6-d87dfe3018ee): Yeni bir değişken tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf86c9042-ce5d-4e0b-8d16-5d726daff63a): Listede seçili olan değişken bilgisi için değişiklik yapılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadab620467-0827-4e14-9555-980ebbfd3e8a): Listede seçili olan değişken silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbdb494b8-c881-4a6f-8d79-700b51ee6646): Kayıtlar filtrelenerek arama yapılır.

Öneri formülünde yer alan değişkenlerin sisteme tanımlanması için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3411874e-25eb-42b9-8ba2-9d9b628fd701) (Yeni) butonuna tıklanarak Değişken Tanımlama /Yeni Kayıt ekranı görüntülenir.

**![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc2a578d4-359d-4304-914a-faeb5cf39e62)**

**Açılan ekranda ilgili alanlar tanımlanır:**

**Değişken Tipi:** Sisteme kullanıcı tarafından bir değişken tanımlanacaksa “Kullanıcı Tanımlı” işaretlenir. Değişken, bir sistemden sorgu ile çekilecekse “Sorgu” seçeneği işaretlenir, Bimser teknik ekibinden destek sağlanmalıdır. Manuel tanımlama işleminde “Kullanıcı Tanımlı” seçilir.

**Değişken Tanımı:** Öneri formülündeki değişkenin tanımı yapılır. Örneğin; Maddi Katkı.

**Değişken Sembolü:** Tanımlanan değişkenin sembolü yazılır. Örneğin; Maddi Katkı için M. Değişken sembolleri formül tanımlamada kullanılır.

**Aktif/ Pasif:** Değişkenin görüntülenip görüntülenmeyeceği bilgisi için aktif/ pasif olma durumu belirlenir.

İlgili alanlar dolduruldaktan sonra, tanımlanan değişkenin sisteme kaydedilmesi için sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1b3d6181-4f04-4b9c-9430-d12c15032cbc) (Kaydet) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8c6c7ce4-5c6c-4402-9b34-0d9e9720e981)

Öneri formülünde kullanılan tüm değişkenler sisteme tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9eab8b8e-cef0-4183-a880-d1695c6d0c5f)

##### **Formül Tanımlama**

**Menü Adı**: Sistem Altyapı Tanımları/ Öneri/ Formül Tanımlama

Puanlama aşamasında kullanılacak öneri formülü bu menüden tanımlanır. Sisteme tanımlanan değişkenler kullanılarak öneri formülü sistemde oluşturulur. “Genel Öneri Formülü, Tedarikçi Öneri Formülü, Müşteri Öneri Formülü, İSG Öneri Formülü” gibi birden çok formülü sisteme tanımlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1ac87685-f943-4664-9097-caeec5385a42)

**Ekranda bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9b69f324-16af-4a4b-b5e6-d87dfe3018ee): Yeni bir formül tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf86c9042-ce5d-4e0b-8d16-5d726daff63a): Listede seçili olan formül için değişiklik yapılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadab620467-0827-4e14-9555-980ebbfd3e8a): Listede seçili olan formül silinir.

Yeni bir formül eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3411874e-25eb-42b9-8ba2-9d9b628fd701) (Yeni) butonuna tıklanarak Formül Tanımlama/ Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc647a71f-3e84-4bbd-ae15-215f14a437bf)

Açılan ekranda ilgili alanlar tanımlanır:

**Formül Adı:** Formül adı tanımlanır. Örneğin; Öneri Puan Formülü, Müşteri Öneri Formülü gibi.

**Formül:** Sistemde tanımlı olan değişkenlerin sembolleri kullanılarak öneri formülü tanımlanır.

Açılan sayfada daha önce tanıtılan değişkenler görülür. Alt kısımda ise formül adını verildiği formülün yazılacağı alanlar vardır. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbe89ebb8-9c1a-49d9-a5a2-fa13135d58fb) (Kaydet) butonuna tıklanarak formül tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload62760ebb-7f79-4826-908e-efba0ba229ab)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload16b84075-4c81-4584-ab83-bc86fb90f196)

##### **Formül-Öneri Tipi Eşleştirme**

**Menü Adı**: Sistem Altyapı Tanımları/ Öneri/ Formül-Öneri Tipi Eşleştirme

3 tip öneri vardır; personel önerileri, müşteri önerileri ve tedarikçi önerileri. Hangi öneri tipi için hangi formül kullanılacaksa eşleştirmesi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaa64cfc3-ef95-4ab1-9a93-9b0a73bd1ab5)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Müşteri Önerisi:** Müşteri önerisinde puanlama için kullanılacak formül seçilir.

**Personel Önerisi:** Personel önerisinde puanlama için kullanılacak formül seçilir.

**Tedarikçi Önerisi:** Tedarikçi önerisinde puanlama için kullanılacak formül seçilir.

Açılan ekranda Müşteri Önerisi&Müşteri Formülü, Personel Önerisi&Personel Formülü ve Tedarikçi Önerisi&Tedarikçi Formülü seçilip ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1b3d6181-4f04-4b9c-9430-d12c15032cbc) (Kaydet) butonuna tıklanarak Öneri Tipi- Formül Eşleştirme Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf483a4cd-079a-469f-b00d-46ad649e8430)

#### **Puanlama Cetveli Kullanımı**

**Menü Adı**: Sistem Altyapı Tanımları/ Öneri/ Puanlama Cetveli

Firmada kullanılacak puan cetveli sisteme tanımlanır. Puanlar sabit ve bellidir, değişkenlik göstermez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload68896817-5d7c-4a9f-b958-f8dc9893c11a)

**Ekranda bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9b69f324-16af-4a4b-b5e6-d87dfe3018ee): Yeni bir öneri puan cetveli tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf86c9042-ce5d-4e0b-8d16-5d726daff63a): Listede seçili olan öneri puan cetveli için değişiklik yapılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadab620467-0827-4e14-9555-980ebbfd3e8a): Listede seçili olan öneri puan cetveli silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbdb494b8-c881-4a6f-8d79-700b51ee6646): Kayıtlar filtrelenerek arama yapılır.

Yeni bir öneri puan cetveli eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3411874e-25eb-42b9-8ba2-9d9b628fd701) (Yeni) butonuna tıklanarak Öneri Puan Cetveli/ Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1b86f5e3-1b92-4cb3-9bd1-3fe3ddec1d7e)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Puan Kriteri:** Puan Kriterinin tanım bilgisi (adı) tanımlanır. Örneğin; Bireysel Puan Cetveli, Grup Puan Cetveli, Kampanya Bireysel Puan Cetveli, Kampanya Grup Puan Cetveli, İSG Puan Cetveli, Kaizen Puan Cetveli gibi.

**Bireysel Öneri Puanı:** Bireysel olarak verilen önerilerin puan bilgisi tanımlanır.

**Grup Öneri Puanı:** Grup olarak verilen önerilerin puan bilgisi tanımlanır.

**Bireysel Öneri Kampanya Puanı:** Bireysel olarak verilen kampanya önerilerinin puan bilgisi tanımlanır.

**Grup Öneri Kampanya Puanı:** Grup olarak verilen kampanya önerilerinin puan bilgisi tanımlanır.

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1b3d6181-4f04-4b9c-9430-d12c15032cbc) (Kaydet) butonuna tıklanarak “Puan Tanımlama Kayıt İşlemi” gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload84421bb8-308b-47a3-a39e-c8792f887db4)

#### **Anket Kullanımı**

Öneri puanlamada anketin kullanılabilmesi için firmada anket modülünün bulunması gerekir. Öneri parametrelerinde “116. Puanlamada anket kullanılacak mı?” parametresi “Evet” olarak ayarlanır. “117. Puanlamada kullanılacak şablon anket kodu” parametresine anket modülünde iç anket menüsünde hazırlanan puanlama anketinin kodu tanımlanır.

### **Kabul Tanımları**

**Menü Adı**: Sistem Altyapı Tanımları/ Öneri/ Kabul Tanımları

Öneri verildikten sonra gerçekleşen değerlendirme aşamalarında, önerinin kabul edilmesi durumunda sistemden seçilecek olan öneri kabul tanımı sisteme tanımlanır. Örneğin: Uygulanabilir, Proje Olarak Uygulanabilir, İleri Bir Tarihte Uygulanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc7191d9c-2166-431a-bae7-14acbf7357f6)

**Ekranda bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9b69f324-16af-4a4b-b5e6-d87dfe3018ee): Yeni bir öneri kabul tanımı yapılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf86c9042-ce5d-4e0b-8d16-5d726daff63a): Listede seçili olan öneri kabul tanımı için değişiklik yapılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadab620467-0827-4e14-9555-980ebbfd3e8a): Listede seçili olan öneri kabul tanımı silinir.

Yeni bir öneri kabul tanımı eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3411874e-25eb-42b9-8ba2-9d9b628fd701) (Yeni) butonu tıklanarak “Kabul Tanımları /Yeni Kayıt” ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload611fd141-3010-4d80-afcc-6c8c4e702396)

Açılan ekranda kabul tanımı girilir ve sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1b3d6181-4f04-4b9c-9430-d12c15032cbc) (Kaydet) butonuna tıklanarak “Kabul Tanımları Kayıt İşlemi” gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade1991287-c725-4356-ae84-22b3c65af5c4)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf6401003-47bb-4b85-998e-9c0af3e1771e)

### **Ret Nedenleri**

**Menü Adı**: Sistem Altyapı Tanımları/ Öneri/ Ret Nedenleri

Öneri verildikten sonra gerçekleşen değerlendirme aşamalarında, önerinin red edilmesi durumunda sistemden seçilecek olan öneri red tanımı sisteme tanımlanır. Örneğin: Yasaya Aykırı, Belirsiz-Soyut Öneri, Tekrarlanan Öneri, Yatırım Maliyeti Uygun Değil gibi.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload76022a9f-23c9-43d6-85e1-097d74b613fa)

**Ekranda bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9b69f324-16af-4a4b-b5e6-d87dfe3018ee): Yeni bir ret nedeni tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf86c9042-ce5d-4e0b-8d16-5d726daff63a): Listede seçili olan ret nedeni için değişiklik yapılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadab620467-0827-4e14-9555-980ebbfd3e8a): Listede seçili olan ret nedeni silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbdb494b8-c881-4a6f-8d79-700b51ee6646): Kayıtlar filtrelenerek arama yapılır.

Yeni bir ret nedeni eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3411874e-25eb-42b9-8ba2-9d9b628fd701) (Yeni) butonu tıklanarak “Ret Nedenleri /Yeni Kayıt” ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload30774d68-a2ec-4ee2-b4ed-6fcf44a4b076)

Açılan ekranda ret nedeninin tanımı girilir. Ret Nedeni durum bilgisi seçilir. Sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1b3d6181-4f04-4b9c-9430-d12c15032cbc) (Kaydet) butonuna tıklanarak “Ret Nedenleri Kayıt İşlemi” gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload724db9cf-a80f-4a7e-ad9e-abe8825ce58c)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f654bf2-ca74-4329-ad06-40add6692e8e)

### **Proje Grupları**

**Menü Adı**: Sistem Altyapı Tanımları/ Öneri/ Proje Grupları

Firma bünyesinde gerçekleştirilen 5S, Kaizen, Yalın Üretim projeler sisteme tanımlanarak proje grupları oluşturulur. Uzman/ Lider tanımlama menüsünde tanımlanan uzmanın hangi proje grubunda olduğu seçilerek “Proje Grubu - Uzman/ Lider Eşleştirmesi” yapılır. Proje grubu tanımlamadaki amaç; verilen öneri hangi proje kapsamındaysa o proje grubu ile ilgili uzmanın değerlendirmesini sağlamaktır.

Proje grubu menüsü firmada proje grupları varsa kullanılır. Eğer herhangi bir proje grubu yoksa bu menüde herhangi bir tanımlama işlemi gerçekleştirilmez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb671e5a9-050d-4bbc-bb6e-9a4fa3f97a0e)

**Ekranda bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9b69f324-16af-4a4b-b5e6-d87dfe3018ee): Yeni bir proje grubu tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf86c9042-ce5d-4e0b-8d16-5d726daff63a): Listede seçili olan proje grubu için değişiklik yapılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadab620467-0827-4e14-9555-980ebbfd3e8a): Listede seçili olan proje grubu silinir.

Yeni bir proje grubu eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3411874e-25eb-42b9-8ba2-9d9b628fd701) (Yeni) butonuna tıklanarak “Proje Grupları/ Yeni Kayıt” ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0032db38-b966-4f2a-98cc-c99842e5e379)

Proje Grubu Kodu bilgisi sistem tarafından otomatik verilir. Proje Grubu Tanımı bilgisi girilir ve sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1b3d6181-4f04-4b9c-9430-d12c15032cbc) (Kaydet) butonuna tıklanarak “Proje Grupları Kayıt İşlemi” gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd0c1a44a-39fe-4602-9314-44c33c26084b)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload31a2e31d-793b-43f9-8429-3c9e355a0499)

### **Bölüm Hedefleri**

**Menü Adı**: Sistem Altyapı Tanımları/ Öneri/ Bölüm Hedefleri

Firma bulunan departmanlar için günlük, haftalık, aylık ve yıllık olarak öneri hedeflerinin girildiği menüdür. Bilgi amaçlı tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8de45360-58c9-4eec-917d-7fd149e32195)

**Ekranda bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9b69f324-16af-4a4b-b5e6-d87dfe3018ee): Yeni bir bölüm hedefi tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf86c9042-ce5d-4e0b-8d16-5d726daff63a): Listede seçili olan bölüm hedefi için değişiklik yapılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadab620467-0827-4e14-9555-980ebbfd3e8a): Listede seçili olan bölüm hedefi silinir.

Yeni bir bölüm hedefi eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3411874e-25eb-42b9-8ba2-9d9b628fd701) (Yeni) butonuna tıklanarak “Bölüm Hedefleri Tanımlama/ Yeni Kayıt” ekranı görüntülenir. “Departman” alanından hedef girilecek departman seçilir. Günlük, haftalık, aylık ve yıllık öneri hedefleri girilir ve kayıt işlemi tamamlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload487302a1-a063-4b75-b66d-5d4e3c8e706a)

Eğer departman hedefi tanımlama ekranında giriş yapan kişinin bölümü otomatik olarak gelsin isteniyorsa; öneri modülünün parametrelerinden “60. Bölüm hedefi girerken bölüm otomatik gelsin mi?” parametresi “Evet” olarak ayarlanır. Eğer “Hayır” seçilirse bölüm hedefi tanımlamada departman bilgisi sisteme giren kullanıcı tarafından seçilir.

### **Kişi Hedefleri**

**Menü Adı**: Sistem Altyapı Tanımları/ Öneri/ Kişi Hedefleri

Firma bulunan kullanıcılar için günlük, haftalık, aylık ve yıllık olarak öneri hedeflerinin girildiği menüdür. Bilgi amaçlı tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc88377f7-8d4b-4660-a1dc-692a6618fe3b)

**Ekranda bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9b69f324-16af-4a4b-b5e6-d87dfe3018ee): Yeni bir kişi hedefi tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf86c9042-ce5d-4e0b-8d16-5d726daff63a): Listede seçili olan kişi hedefi için değişiklik yapılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadab620467-0827-4e14-9555-980ebbfd3e8a): Listede seçili olan kişi hedefi silinir.

Yeni bir kişi hedefi eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3411874e-25eb-42b9-8ba2-9d9b628fd701) (Yeni) butonuna tıklanarak “Kişi Hedefleri Tanımlama/ Yeni Kayıt” ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload438ebf4a-8641-495e-aa54-6c7111b361e0)

Hedef tanımlanacak personel sistemde tanımlı olan personel listesinden seçilir. Günlük, haftalık, aylık ve yıllık kişi hedef bilgisi girilir ve kayıt işlemi tamamlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeeb71867-7305-43b9-86f8-78bb471c9775)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload993b34a3-64d7-439c-aa11-6f5220b7d175)

### **E-Posta Ayarları**

**Menü Adı**: Sistem Altyapı Tanımları/ Öneri/ E-Posta Ayarları

Öneri süreçlerinin hangi aşamasında kimlere e-posta/ mesaj gönderimi yapılacağı belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaded37d1fc-a641-4c9f-b816-dfcd0731a309)

Hangi basamakta e-posta/ mesaj gitmesi isteniyorsa seçilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada2757073-6678-40ac-914c-718415c253c6) (Değiştir) butonu ile görüntülenir. Roller kısmı; e-posta ve mesaj bildirimimin gideceği rolü yani kişiyi göstermektedir. Kime E-Posta gitmesi isteniyorsa, o rolle ilgili “E-Posta Gitsin Mi/ SMS Gitsin Mi” kutucuğu işaretlenir. Mesaj gitmesi için rolde tanımlı olan kişinin cep telefon numarası personel tanımlama ekranında tanımlı olmalıdır. Daha sonra gönderilecek mesaj gövdesi ilgili listeden seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf03dc1f4-9f30-4b9b-9dae-b9d8fc64d17f)

Değişiklikler yapıldıktan sonra sağ üstte yer alan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc947f00d-2302-4736-b12a-b7df8d6a11dd)(Kaydet) butonuna tıklanır. Hiçbir değişiklik yapmadan çıkmak için ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload216e5e10-870f-4ff0-8ed3-9db43f0e2192)(Geri) butonu kullanılır.

### **Öneri Parametreleri**

**Menü Adı**: Sistem Altyapı Tanımları/ Öneri/ Öneri Parametreleri

Öneri modülü için kullanıcının istek ve ihtiyaçlarına göre çeşitli ayarlamaların yapabildiği ve bunlara göre parametrelerin belirlendiği menüdür. Parametrelerde yapılan değişikler tüm QDMS kullanıcılarını kapsar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4e549171-cef2-49e0-88fa-787a5287ea42)

Bir parmatreden değişiklik yapılmak isteniyorsa, değişiklik yapılmak istenilen parametre seçilerek, ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf86c9042-ce5d-4e0b-8d16-5d726daff63a) (Değiştir) butonu ile işlem yapılır. Parametre değeri tanımlanır ve kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4b275cca-e081-4d31-9fe1-9d92e0dd9b8a)

### **5.1.12.Anket Soru Listeleri**

**Menü Adı:** **Menü Adı:** Sistem Altyapı Tanımları/ Öneri / Anket Soru Listeleri

Öneri Sistemi Modülü için Anket Soru listelerin ilgili fonksiyonlar için hazırlandığı menüdür. Anket işlemleri Modülü olmayan kullanıcıların Anket işlemleri modülü açılan Anket şablonu ekranında olduğu gibi bu modülde ilgili fonksiyon için Anket şablonu tasarlaması amacıyla kullanılmaktadır. Bu fonksiyon “Öneri Puanlama” fonksiyonudur. Anket Soru Listeleri (Öneri Sistemi) ekranında fonksiyon olarak “Öneri Puanlama” fonksiyonu seçildiğinde sağ üstteki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload77ff676b-d785-45e5-96ea-ba09e91878f7)(sorular) butonu tıklanarak Tedarikçi Değerlendirme modülü mantığında sistemde şablon anketler bu menüde tasarlanıp kaydedilmesi sağlanmaktadır. Şablon anketler tasarlandıktan sonra Öneri Sistemi modülün 1. fonksiyonla ilgili parametresi olan 117 numaralı “Puanlamada kullanılacak şablon anket kodu”parametresinin parametre değeri boş ise sistem otomatik olarak anket kodunu parametre değerine tanımlamaktadır. Bu parametrenin aktif olması için Öneri Sistemi Modülü parametrelerinden “Puanlamada anket kullanılacak mı?” parametresi seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada76ae715-9343-4a41-95a6-138c55a348a1)(Değiştir) butonu tıklanarak açılan parametreler ekranında parametre değeri “Evet” seçilerek aktif edilmesi gerekir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3c7320db-0419-40a9-9c5b-bbe304ec04d5)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload77ff676b-d785-45e5-96ea-ba09e91878f7):Tanımlanacak ankete soru ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload77ff676b-d785-45e5-96ea-ba09e91878f7)(Sorular) butonu tıklanarak Anket işlemleri Modülün yapısındaki soru ekleme işlemin yapıldı ekran gibi Öneri Sistemi modülü için ilgili fonksiyon için soru ekleme ekranı görüntülenerek soru seçeneklerinden soru ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload76b22d7a-6197-43b2-886b-b4d2d12f383b)

Öneri Sistemi Parametrelerinden 117 numaralı “Puanlamada kullanılacak şablon anket kodu” parametresinin parametre değerine herhangi bir parametre kodu tanımlı olmadığında sistem “Yeni bir anket oluşturulacaktır. Onaylıyor musunuz?” uyarı mesajına tamam butonu tıklanarak anket soruları ekranı görüntülenir. Anket Soruları ekranında soru seçenekleri kullanılarak bir şablon Anket tasarlanır.Şayet parametreye sistemde bir anket kodu tanımlı ise tanımlı olan anketin sorular ekranı güncelleme modunda açılır. Anket Soruları ekranı açılarak sorular ilgili düzenleme, güncelleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcd238e88-c2b6-4dbb-8707-391d85d070cd)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf95052cf-7ef6-4d1e-87ee-8f3a826414c6)**: Geri Butonu:** Bir önceki sayfaya geçişi sağlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf5ff5b33-031b-4f1a-beba-93f6f69b76b2)**: Yazdır Butonu:** Sorularınızı yazdırmaya sağlayan butondur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9c2fe71a-96dc-4e0f-afb4-72a90b36401b)**: Başlık Ekle Butonu:** Anketi bölümlendirerek başlık eklemek istenilirse bu buton kullanılır. Her başlık ayıracından sonra tanımlanan sorunun numarası 1 olarak gelir. Butona tıklanıldığında açılan sayfa aşağıdaki gibidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc491805d-a29e-48f9-be70-a2b830c0c55e) : **Bilgi Girişi Ekle Butonu:** Anketi dolduran kişilere, serbest bilgi girilmesi gereken sorular sorulduğunda, kullanılan soru tipidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload85850031-44f0-4fca-b107-81339f3ad639)**: Seçenek Ekle Butonu:** Verilen cevapların belirtilen seçenekler içinden seçilmesi durumunda kullanılır.

**![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0b144ed6-bbfa-42ca-859a-e6a2b45e7267): Sıralama Ekle Butonu:** Bir sorunun seçeneklerinden tüm seçeneklerin tercih edilip, öncelik sırasına göre listelendiği durumda kullanılır. Seçenekler çoktan\>aza veya azdan\>çoğa doğru sıralanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd1f912f2-bca6-4446-b715-496d0c4417be): **Çoklu Seçim Listesi Ekle Butonu:** Oluşturmak istenilen soruda çok fazla şık mevcutsa ve bunların check list gibi seçilmesi gerekiyor ise, çoklu seçim listesi tipinde soru eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbece2a36-2238-4c61-9fdb-5caf1057b18f)**: Açılır Liste Ekle Butonu:** Sorulan sorunun açılır listeden tek cevap seçilmesi durumunda kullanılacak soru tipidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4083405b-04a8-4efd-b0fa-bb12fd558ace)**:Ön Tanımlı Seçim Ekle butonu:** Bu soru tipi QDMS’de tanımlı personel, müşteri, departman ve ürün alanlarındaki listelerin seçilmesini sağlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfe66179e-c81a-4d93-af60-812857965859):**Tarih Ekle butonuna:** Tıklanarak açılan ekranda, kullanıcıya tarih seçtirilecek soru eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload467bb1ea-091e-4ced-aa7c-e070b421a40c)**:Ek Dosya Ekle Botunu:** Ankete Ek dosya ekleme işlemi için Ek Dosya alanı oluşturur.

**Örnek Soru seçenekleri ekleme;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9c2fe71a-96dc-4e0f-afb4-72a90b36401b) (Başlık Ekle) butonu tıklanarak Anket bölümlendirilerek başlık eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5966e65b-c9ef-4189-8e2b-0c9e69e4fce4)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf244395e-16b3-4c6c-ad80-eb943691141e)

Başlık ekle alanına ilgili başlık eklenilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb65112d6-0e8a-4e46-bd65-45b0cac50c0c) (kaydet) butonuyla kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb5416364-c3fd-4bee-b2b1-782df361d981)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc491805d-a29e-48f9-be70-a2b830c0c55e) (Bilgi Girişi Ekle) butonu tıklanarak serbest bilgi girilmesi için tanımlanacak soru tanımlanır. Bir metin alanı oluşturulur ve bu metin alanın kaç satırdan oluşacağında soru tanımlama ekranında ayarlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1509cd5b-cafb-45eb-b591-252cef53a791)

**Soru Metni:** Sorulacak soru metni, Türkçe alana yazılır. Diğer dillerde kullanım olması durumunda ilgili dillerin olduğu alana sorulacak soru verisi girilir.

**Satır Sayısı:** Satır sayısı, metnin büyüklüğünü belirlemek için kullanılır. 0 veya 1 olması durumunda cevap verilecek alan tek satır olarak görülür.

Sorulacak sorunun cevap verme zorunluluğu bu alandan belirlenir. Cevap zorunluluğu var ise soru cevaplanmadığında kaydetmeye izin verilmez, uyarı mesajı verilir.

**İlişkili Soru/Seçenek:** Bir sorunun, seçeneklerinden biri ile ilişki kurulduğunda, ilişkili sorunun çıkması istenilirse ilişkili soru/seçenek kısmından bağlantı sağlanır.

Sorulacak soru metni Türkçe alana yazılırak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb65112d6-0e8a-4e46-bd65-45b0cac50c0c) (kaydet) butonuyla kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload30e0bf94-4696-4479-9e2b-8b6f1db0824e)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload85850031-44f0-4fca-b107-81339f3ad639) **(**Seçenek Ekle) butonu tıklanarak verilen cevapların belirtilen seçeneklerden seçilme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd89d609b-7632-47f0-b2fc-58763017b080) **Soru Metni:** Sorulacak soru metni, Türkçe alana yazılır. Diğer dillerde kullanım olması durumunda ilgili dillerin olduğu alana sorulacak soru verisi girilir.

**Seçenek/Puan:** Bu alana sorunun seçenekleri girilir. Eğer anket, puanlı bir anket olacaksa, girilen seçenekler için puan da yazılmalıdır.

Sorulacak sorunun cevap verme zorunluluğu bu alandan belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload372d2473-0762-40e3-8252-7639cc0a6b4e)

Seçeneklerden 1 veya 1’den fazlasının seçilebilmesi bu alandaki check box’a göre belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06764a98-c7ca-4fd6-81ff-599a9234d0a3)

Seçeneklerin yan yana (Tek Satırlı) veya alt altta (Çok Satırlı) dizili olarak görülmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbfc63f67-584e-4b10-835d-5daf218da354)

Eğer çok satırlı seçeneği işaretlenirse kolon sayısı diye bir alan çıkar ve sorunun seçenekleri belirlenen değer kadar, kolonda görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadde3f7865-4a95-4452-9426-2f4c45f5dd17)

**Hesaplama Yöntemi:** Anketin puanlı anket olması durumunda, bu sorunun seçeneklerine verilen puanların hangi yöntemle hesaplanılacağının belirlendiği alandır. Örneğin; 10 kişinin cevaplayacağı anketteki bir sorunun 4 seçeneği ve her bir seçeneğin kendine has puanları vardır. İlk seçeneğin puanının 5 olduğunu varsayarsak, 10 kullanıcının ilk seçeneği seçmesi halinde, bu puanlar toplanarak mı (50) veya ortalaması alınarak mı (5) anketin ortalama puanına dahil edilme durumu belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb6e701f1-df1f-4ac2-b0fc-61e51ebfd5cc)

**Ağırlıklı Puan:** Anketin puanlı anket olması durumunda sorunun anket içindeki ağırlığının belirlendiği alandır. Tüm sorular eş değer ağırlıktaysa 1 değeri yazılmalıdır. 0 olarak yazıldığı durumda anket puanı hesaplanmaz.

**İlişkili Soru/ Seçenek:** Bir sorunun başka bir sorunun seçeneğindeki şarta bağlı olarak görünmesi istenirse ilişkili soru/seçenek mantığı kullanılır.

İlgili alanlar doldurulduktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb65112d6-0e8a-4e46-bd65-45b0cac50c0c) (kaydet) butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload43b8e660-3e34-4f1b-addd-f699e23005de)Anket Soru Listeleri(Öneri Sistemi) menüsünde İlgili fonksiyon seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload77ff676b-d785-45e5-96ea-ba09e91878f7)(Sorular) butonu tıklanarak açılan Anket soruları ekranında örnek olarak birkaç soru seçeneği tanımlanarak Anket Soru Listeleri(Öneri Sistemi) tanımlama işlemi yapılır. Diğer soru seçeneklerin tanımlama işlemi Anket İşlemleri Modülünün soru tanımlama ekranındaki aynı şekilde yapılmaktadır. Soru tanımlama işlemi yapıldıktan sonra Anket Soru Listeleri Öneri Sistemi) menüsü ilgili modülün ilgili parametresi olan 117 numaralı “Puanlamada kullanılacak şablon anket kodu” parametresine sistem otomatik olarak anket kodu tanımlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d1db658-5a94-43a4-8acd-2d85c2b8f828)

Anket Soru Listeleri(Öneri Sistemi) menüsü için olduğu gibi sistemde Sistem Altyapı Tanımları/ İlgili Modüller (DÖF, Dış-İç Müşteri Şikayetleri, Denetim, , Eğitim, İç İş İzni, Yüklenici İş İzni, Aksiyon Yönetimi ) modüllerinde menü yetkilendirmesi yapıldığında içeriğinde bu modüllerin bulunmaktadır. Açılan menüde ilgili fonksiyon seçilerek sağ üstteki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload77ff676b-d785-45e5-96ea-ba09e91878f7)(Sorular) butonu tıklanır. Eğer bu fonksiyon için daha önceden ilgili parametreye bir anket kodu verilmişse ve bu anket sistemde mevcutsa, o anketin soru listesi güncelleme modunda açılır ve sorular düzenlenebilir. Diğer durumlarda yeni bir anket oluşturulur, anket kodu ilgili parametreye yazılır. Ondan sonra yine bu yeni oluşturulan anketin soruları güncelleme modunda açılır ve sorular düzenlenebilir.

Bu parametreleri uygulama içinde kullanan yerler, daha önceden olduğu gibi aynı şekilde çalışmaya devam ederler. Anket Modülü satın almamış kullanıcıların anket kullanan modüller için anket oluşturabilmeleri sağlanmıştır.

İlgili Modüller için Modüller içerisinde Anket lisanslı olmasa bile Anket tanımlanabilir. Bu amaçla kullanılan menünün menü yetkisi verildiğinde Qdms Modüllerin ilgili fonksiyonları ve ilgili modüllerin sistemde tanımlı parametrelerinin numaraları aşağıdaki tabloda yer almaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada49c37ef-015d-448e-8192-e138e4474b77)

## **Öneri Değerlendirme Akışlarının Belirlenmesi**

### **Rol Tanımlama**

**Menü Adı**: Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Rol Tanımlama

Öneri modülünde kullanılan onay akışlarında onaycı olarak hangi role gideceği bilgisinin tanımlandığı menüdür. Sistemde öneri modülü için otomatik olarak tanımlanmış roller bulunmaktadır. Firma ihtiyacına göre bu roller Bimser destek personelinden yardım alınarak düzenlenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2a585a85-eb5c-4b0b-a7ee-ce6208fb4f5d)

Ön Değerlendirme ve Öneri Komisyonu rolleri firmadan firmaya değişiklik göstereceği için, bu roller ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada76ae715-9343-4a41-95a6-138c55a348a1) (Değiştir) butonu ile açılarak firmanın yapısına uygın olarak düzenlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload020bb4a2-3c28-43e5-b988-6d300e6afd05)

### **Akış Tanımlama**

**Menü Adı**: Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Akış Tanımlama

Öneri modülünde kullanılacak onay akışlarının ilgili rollerle eşleştirilerek düzenlemesi yapılır. Sistemde tanımlı olarak “Öneri Ön Değerlendirme Süreci, Öneri Komisyon Değerlendirme Süreci, Öneri Uzman Değerlendirme Süreci, Öneri Puanlama Süreci, Öneri Aksiyon Planlaması ve Öneri Kazanç Maliyet Analizi” akışları yer almaktadır.

Bir önerinin, değerlendirme aşamasında reddedildiği zaman öneriyi veren tarafından itiraz edilerek bir komisyona gönderilip yeniden değerlendirilmesi isteniyorsa “Öneri Komisyon Değerlendirme Süreci” kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6088e6a0-0d80-4ae3-babd-741fccddc6ab)

Düzenlenmek istenilen akış seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada76ae715-9343-4a41-95a6-138c55a348a1) (Değiştir) butonu ile görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadad0e1db1-1e54-4dcf-8aad-6c75a4eeb198)

Onay akışında kullanılacak rol sistemde tanımlı olan rol havuzundan seçilerek kayıt işlemi gerçekleştirilir.

## **Entegre Yönetim Sistemi/ Öneri Sistemi İşlemleri**

**Menü Adı**: Entegre Yönetim Sistemi/ Öneri Sistemi

Bir önerinin sisteme girilerek öneri sürecinin başlatılıp, takip edildiği menülerdir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade2e3926f-94ed-42e8-93dc-7bc07adaa645)

### **Öneri Girişi**

**Menü Adı**: Entegre Yönetim Sistemi/Öneri Sistemi/ Öneri Girişi

Sisteme öneri girişinin yapıldığı menüdür.

**Öneri Bilgileri sekmesi,** öneri hakkında genel bilgilerin girildiği sekmedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddbd354da-083a-4783-afe2-55ba6a778ab8) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb2bfa5e5-e46f-45c6-b980-d2f3433c7f0d)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Öneri Kaynağı:** Sisteme girilen önerinin müşteri önerisi mi, tedarikçi önerisi mi yoksa personel önerisi mi olduğu seçilir. Müşteri önerisi seçilirse öneriyi verenler sistemde tanımlı olan müşteri listesinden seçilir. Tedarikçi önerisi seçilirse öneriyi verenler sistemde tanımlı olan tedarikçi listesinden seçilir. Personel önerisi seçilirse öneriyi verenler sistemde tanımlı olan personel listesinden seçilir.

**Öneriyi Verenler:** Öneri kaynağı olarak müşteri önerisi seçilirse öneriyi verenler sistemde tanımlı olan müşteri listesinden seçilir. Tedarikçi önerisi seçilirse öneriyi verenler sistemde tanımlı olan tedarikçi listesinden seçilir. Personel önerisi seçilirse öneriyi verenler sistemde tanımlı olan personel listesinden seçilir.

Eğer sadece personel önerisi kullanılıyorsa öneri parametrelerinden “79. Kullanılacak öneri kaynakları (Birden fazla kullanım için virgülle ayırınız, boş ise tamamı kullanılır) M-Müşteri Önerisi,P-Personel Önerisi,T-Tedarikçi Önerisi” parametresi “P” olarak tanımlanır.

Öneri parametrelerinden “1. Bir öneriyi en fazla kaç kişi verebilir?” parametresinde tanımlanan değere bir öneriyi en fazla kaç kişinin verebileceği belirlenir.

**Verildiği Tarih:** Önerinin verildiği tarih bilgisi seçilir. Öneri parametrelerinden “35. Dikkate alınacak tarih (S)isteme kayıt tarihi, (V)erildiği tarih” parametresi “S” olarak tanımlanırsa önerinin sisteme girdiği tarih otomatik olarak gelir ve değiştirilemez. Eğer parametre değeri “V” olarak tanımlanırsa önerinin verildiği tarih değiştirilerek geçmiş bir tarih seçilebilir.

**İş yeri:** Verilen önerinin hangi işyeri kapsamında verildiği sistemde tanımlı olan işyeri listesinden seçilir.

Öneriyi veren kullanıcının işyeri bilgisi otomatik gelsin isteniyorsa öneri parametrelerinden “144. Öneri girişinde açanın iş yeri seçili gelsin mi?” parametresi “Evet” olarak tanımlanır.

**Önerinin Verildiği Hafta:** Önerinin verildiği hafta bilgisi kullanılacaksa öneri parametrelerinden “13. Hafta bilgisi kullanılsın mı?” parametresi “Evet” olarak tanımlanır. Önerinin verildiği hafta bilgisi sistemde tanımlı olarak gelir. Ancak öneri geçmiş haftalardan birinde verildiyse o hafta bilgisi alan düzenlenerek yeniden tanımlanır.

**Özet:** Verilen öneri için özet bilgi tanımı yapılır. (Örneğin; yüksekten düşmeyi engelleme.)

**Mevcut Durum/ Problemin Tanımı:** Mevcut durum belirlenerek problemin tanımı yapılır. (Örneğin; yüksekte çalışma platformlarında düşme tehlikesi)

**Önerilen Durum/ Çözümün Tanımı:** Problemin çözümü için durum tanımlaması yapılır. (Örneğin; 1,5 metre üzerindeki çalışma alanlarında platformların korkuluklarla çevrilmesi)

**Kazanç/ Maliyet Tanımı:** Verilen önerinin hayata geçirilmesi firmaya ne gibi kazançlar sağlıyorsa altyapıda tanımlanan kazanç kategorisi listesinden seçilir. (Örneğin; kaza sayısını azaltma).

Birden fazla kazanç kategorisinin seçilmesi isteniyorsa öneri parametrelerinden “61. Birden fazla kazanç kategorisi seçilebilsin mi?” parametresi “Evet” olarak ayarlanır.

**İlgili Departman:** Verilen önerinin hangi departman kapsamında verildiği sistemde tanımlı olan departman listesinden seçilir.

Öneriyi veren kullanıcının departman bilgisi otomatik gelsin isteniyorsa öneri parametrelerinden “103. Öneri departmanı öneri verenin departmanı seçilsin mi?” parametresi “Evet” olarak tanımlanır.

Öneri ile ilgili eklenmek istenen doküman, resim vb. dosya varsa “**Ek Dosyalar”** sekmesinden ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0e78c0a6-7514-4970-9916-fff068fa9791) (Ek Dosya Yükle) butonu ile sisteme yüklenir. Birden çok ek dosya yüklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload067f0a4d-57bc-4414-895e-1cd9c85edfa2)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc24b726d-ea5f-4c1c-bd60-7b78d4bbe181)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1191e3d2-2027-4b1d-9fd4-7518b2ae42c9)

Öneri girişi yapıldıktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3b58ce24-2e1d-4294-b1a2-4e2300dfdaff) (Kaydet) butonuna tıklanırsa öneri taslak olarak kaydedilir. Öneriyi giren kullanıcının “Bekleyen İşlerim” sayfasında “Taslak Durumdaki Öneriler” olarak görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade98c1f5f-29f2-4858-836e-135e74fddea6)

Taslak durumdaki önerinin koduna tıklanarak öneri giriş ekranı görüntülenir. Öneri kodu “Yıl.\*\*\*\*” olarak görüntülenir.Örneğin; (20.0005 öneri kodu; verilen önerinin 2020 yılının 5.önerisi olduğunu gösterir).

Öneri giriş ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload08bd36f1-68e3-46ad-a020-8299d973faff) (Kaydet/ Onay Gönder) butonu ile öneri ön değerlendirme yapılmak üzere sistemde tanımlanan ön değerlendirmeci rolüne gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1191e3d2-2027-4b1d-9fd4-7518b2ae42c9)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddf3b9c64-3d99-44aa-b71c-d7c5e51e52b3)

#### **Ön Değerlendirme Süreci**

Öneri gönderildikten sonra ön değerlendirme yapacak kişinin “Bekleyen İşlerim” sayfasında **“Ön Değerlendirme Yapılacak Öneriler”** olarak görev düşmektedir. Öneri koduna tıklanıp ön değerlendirilme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6df0ec3b-d7d1-4458-a037-dc39d2add27a)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3e4c3f54-fb6c-4661-8bd6-aa67e106da4d)

Ön değerlendirmeci tarafından verilen öneri değerlendirilerek öneri olup olmadığına karar verilir. Değerlendirme sonucunda “Öneri Değil” seçilirse altyapıda tanımlanan red nedenlerinden seçim yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb45531b1-4812-4006-8171-63906fc9ec63)

Değerlendirme sonucunda “Öneri” seçilirse, tanımlı uzman listesinden “Değerlendirecek Uzman” seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8427f05d-b973-4561-bb58-3314c7cb4db5)

“Kampanya Önerisi” check box’ı işaretlenirse puanlama aşamasında kullanılacak puan cetveli kampanya puanı üzerinden değerlendirilir. Sadece puan cetveli yönteminde geçerlidir. Eğer firmada kampanya önerisi kullanılmayacaksa öneri parametrelerinden “67. Ön değerlendirme aşamasında kampanya durumu belirlenecek mi?” parametresi “Hayır” olarak ayarlanarak ön değerlendirme ekranındaki görünürlüğü kaldırılır.

Açıklama alanında varsa bir açıklama bilgisi girilebilir.

Ek dosyalar sekmesinden varsa kanıt dosyalar eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload60871ae4-b67f-4368-8701-e61ad0bd0d62)

**“Öneri Detayları” sekmesinde** verilen öneriyle ilgili sisteme girilen tüm bilgiler görüntülenir. Detaylar altında öneriye ait detay bilgilere ulaşılır. Ek dosyalar sekmesinden öneriyle ilgili yüklenen ek dosyalara ulaşılır. Tarihçe sekmesinden öneri ile ilgili yapılan işlemlerin tarihçesine ulaşılır. (Öneri parametrelerinden “137. Öneri görüntülemede tarihçe gözüksün mü?” parametresi ile tarihçe sekmesi aktif hale getirilir.)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf2c20ed5-c4c3-444b-86ad-52664e2358f6) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf16ea51d-4a36-4a6a-b171-93055175b291)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada7723f59-360d-4642-9896-d41bb862c63c)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc1500b24-1f86-4682-bc25-a5a22f42c63b)

Öneriyi kabul etmek ve uzmana değerlendirmeye göndermek için ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8ac158ac-ca4a-44b2-bb6b-c56b9738ebdf) (Onaya Gönder) butonuna tıklanır. Öneri, uzman değerlendirme aşamasında seçilen uzmana onaya gider

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb7e48b55-0f95-461a-a769-8f9ad2dd41e5)

Ön değerlendirme işlemi Entegre Yönetim Sistemi/ Öneri Sistemi/ Ön Değerlendirme Yapacağım Öneriler menüsünden de gerçekleştirebilir. Kullanıcının “Ön Değerlendirme Bekleyen Öneriler” listesinde ilgili öneri seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3019642f-ee36-4a0e-9a91-c28255def6d1) (Değerlendir) butonu ile ön değerlendirme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3db92ad4-cd92-47ff-97b4-abfbb58ec5d6)

#### **Uzman Değerlendirme Süreci**

Öneri ön değerlendirme aşamasından geçtikten sonra, uzman değerlendirmecinin “Bekleyen İşlerim” sayfasında “Uzman Değerlendirme Yapılacak Öneriler” olarak görüntülenmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6eb24160-2a9c-43e4-a439-f53203b12eb6)

Uzman tarafından öneri numarası tıklanarak uzman değerlendirme ekranı görüntülenir. “Uzman Bölümüyle İlgili” alanında “Bölümümle İlgili Değil” seçilirse başka bir uzmana atama yapabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcbc984ca-718a-43e8-a24f-f4605253db18)

“Öneri Uygunluğu” alanında “Öneri Değil” seçilirse, öneri ret nedeni listeden seçilerek öeneri reddedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4fe304cd-aecb-4b97-9d3e-acc318eff8dc)

“Öneri Değerlendirme Sonucu” alanında “Aksiyona Gerek Yok” seçeneği seçilirse aksiyon aşamasını atlayıp kazanç/ maliyet süreci ile sistem devam eder. “Bölüm İçi Öneri” veya “Bölüm Dışı Öneri” seçilirse öneri, aksiyon planlamaya gider. “Bölüm İçi Öneri” seçilirse uzmanın kendi bölümü içerisinde aksiyon uygulanacak demektir. “Bölüm Dışı Öneri” seçilirse uzmanın kendi bölümü dışındaki başka bir bölüm tarafından aksiyon uygulanacak demektir. Özetle; aksiyonun gerçekleşmesi için farklı bir departmana ihtiyaç varsa (Örneğin; bakım gibi) bölüm dışı öneri seçilir. Aralarındaki fark uygulanma süresidir. Öneri parametrelerinden “11. Bölüm içi önerinin uygulanma süresi (gün)”, “12. Bölüm dışı önerinin uygulanma süresi (gün)” ayarlanan değerlere göre aksiyon uygulanma süreleri ayarlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload05af62a9-974b-4091-b4e6-85bdf63133f1)

“Ek Dosya” sekmesinden varsa kanıt dosya eklenebilir. “Öneri Detayları” sekmesinden verilen öneriye ait tüm bilgiler görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadda2ab078-9541-4b24-b14e-b7a10a30133d)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd62ea037-ee58-4e7a-b2f9-ef915c3eb7d6)

Uzman değerlendirme gerçekleştirildikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8ac158ac-ca4a-44b2-bb6b-c56b9738ebdf) (Onay Gönder) butonuna tıklanır. Önerinin hayata geçirilmesi için aksiyon planlaması yapılmak üzere uzman değerlendirmeci tarafından “aksiyon planlaması yapacak kişi” rolünde belirlenen kişiye aksiyon planlanma sürecine gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddf084b39-49e4-4159-8dc2-6d8068abaf88)

Uzman değerlendirme işlemi Entegre Yönetim Sistemi/Öneri Sistemi/ Uzman Değerlendirme Yapacağım Öneriler menüsünden de gerçekleştirebilir. Kullanıcının “Uzman Değerlendirme Bekleyen Öneriler” listesinde ilgili öneri seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3019642f-ee36-4a0e-9a91-c28255def6d1) (Onaya Gönder) butonu ile uzman değerlendirme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload55d67db7-cda2-4d42-aff7-5424f6960ecc)

#### **Aksiyon Planlama Süreci**

Aksiyon planlaması yapacak kişinin “Bekleyen İşlerim” sayfasında **“Aksiyon Planlaması Bekleyen Öneriler”** olarak görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1d5f2b80-f679-4f3f-88a0-08583c007b88)

Öneri numarasına tıklanarak aksiyon planlama ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddd124186-0ab9-4524-bd12-5acdd1329a0e)

“Dikkate Alınacak Tarih” alanı öneri parametresinde tanımlanan değere göre otomatik tanımlı gelmektedir. “31. Bildirim tarihinin kaç gün sonrasına kadar aksiyon açabilir?” parametresi kaç gün tanımlandıysa “dikkate alınacak tarih alanı”o değere göre gelmektedir. “Aksiyon Sorumlusu” sistemde tanımlı personel listesinden seçilir. “Aksiyonu Yapacak” alanından aksiyonu gerçekleştirecek kişi seçilir. “Sorumlu Departman” alanı aksiyon sorumlusunun departmanı olarak otomatik tanımlı gelmektedir, bu alan değiştirilebilir. Yapılacak aksiyon bilgisi “Aksiyon Tanımı” alanında girilir. Aksiyonla ilgili bilgilendirilmesi istenilen kullanıcı ya da kullanıcı grupları varsa “Bilgilenecekler” alanından seçilir. Varsa planlanan aksiyona ait bütçe bilgisi girilir. Aksiyonun başlangıç ve bitiş tarihleri seçilir. Aksiyonun gerçekleştirilmesi için atanacak aksiyon görev tipi seçilir. Ek Dosyalar sekmesinden ek dosya varsa sisteme yüklenir. Kayıt işlemi gerçekleştirilerek aksiyon görevi işi yapacak kullanıcıya atanır (Eğer aksiyon kalemi açma onayı varsa önce onaya gider.Onaylanan aksiyon görev olarak aksiyon işini yapacak kişiye atanır.)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddd1822db-575f-40bc-b723-bcffe25eab1a)

Eğer öneri kapsamında birden çok aksiyon tanımlanmak isteniyorsa; Entegre Yönetim Sistemi/ Öneri Sistemi/ Öneri Uzman İşlemleri menüsünden uzman ait öneri seçilir. Aksiyon işlemleri butonu ile yeni aksiyonlar tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload335a1ddb-da42-4fe1-a67d-8abafe30b8dd)

Bu aşamadan sonra aksiyonu gerçekleştirecek kişinin “Bekleyen İşlerim” sayfasında “Gerçekleştirilecek Aksiyonlar Listesi” görevi düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddd59b214-7bf4-4baa-bfae-abfc48aadf90)

Aksiyon numarasına tıklanarak gerçekleştirilecek aksiyon görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5cbf9503-abaa-44c2-8ed3-1c91e610e576)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb7f19688-c5a0-4a66-b199-678d8172ce69) (Gerçekleştir) butonu ile açılan ekranda gerçekleştirilen aksiyon bilgisinin girileceği “Yapılan İş” alanı tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaba442a4-f93e-4f71-8f1c-de2db9ac2a0a) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload392a149f-67ba-4262-9db9-99908e06a5d8) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload18b99682-8d23-4497-943f-b6184fb49729)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbe89ebb8-9c1a-49d9-a5a2-fa13135d58fb) (Kaydet) butonuna tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade0894459-9bfc-43cc-a810-7487e2b3f62b)

Bu aşamadan sonra aksiyon kapatma onayına gider. Kapatma onaycısının “Bekleyen İşlerim” sayfasında “Kapatma Onayı Bekleyen Aksiyonlar Listesi” görevİ düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload902551e5-fff0-4ea7-9020-92afbce9cd0a)

Aksiyon numarasına tıklanarak aksiyon onaylama ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3f571ac1-b570-4424-b737-1e4edc115b2a)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbdde10fe-1fcd-4f6b-a2c3-ddd0f6a9ab72) (Onayla butonuna tıklanarak aksiyon onaylama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada6a809dc-d5d5-428d-979a-17ee0ae7732e)

Öneriye ait aksiyonların tamamı gerçekleştirildikten kaç gün sonra kazanç/ maliyet analiz sürecine gideceği öneri parametresinden belirlenmelidir. “83. Uzman değerlendirme yapıldıktan sonraki işleme (aksiyon planlama, kazanç/ maliyet analizi) otomatik yönlendirme kullanılacak mı?” parametresi “”Evet” olarak tanımlanmalıdır. “127. Öneri Aksiyonları tamamlandıktan kaç gün sonra bir sonraki statüye geçilsin?” parametresi “0” olarak tanımlanırsa aksiyonlar tamamlandıktan sonra, hemen kazanç/ maliyet analiz sürecine geçer, “1” tanımlanırsa aksiyonlar tamamlandıktan 1 gün sonra kazanç/ maliyet analiz sürecine geçer.

Eğer önerinin kazanç/ maliyet analiz sürecine manual olarak geçmesi sağlanacaksa Entegre Yönetim Sistemi/ Öneri Sistemi/ Öneri Sistemi İşlemleri menüsünden işlem yapılır. “Durum” bilgisi “Aksiyon (Kapalı)” olan öneri seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc363fa5f-ecfc-46d5-b77e-003e376fd46b) (Kazanç Maliyete Geçsin) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf9abca78-4ce0-4859-9127-ab3212e5ac8f)

Kazanç maliyet analizini yapacak role görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload85b25fcd-1565-4fa1-8043-8b5339c455c5)

#### **Kazanç/ Maliyet Analizi Süreci**

Aksiyonlar tamamlandıktan sonra, öneri için uzman tarafından kazanç/ maliyet analizi yapılmaktır. Önerinin ne getirisi olacak, masraflar çıktıktan sonra net kazancı ne olacak gibi işlemler gerçekleştirilir.

Uzmanın “Bekleyen İşlerim” sayfasında “Kazanç/ Maliyet Analizi Bekleyen Öneriler” olarak görev düşer. Önerinin numarası tıklanarak kazanç/ maliyet analiz süreci başlatılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadccac10eb-f270-4f79-83bd-f1ef258a04f0)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload97d375bb-0d6d-4dc6-bac5-9ec438f9051e)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Yıllık Kazanç/ Katkı Hesabı Açıklama Bilgileri:** Önerinin hayata geçirilmesinin firmaya kattığı maddi/ manevi değerler tanımlanır.

**Öneri Brüt Kazancı:** Önerinin hayata geçirilmesinden sonra firmanın maddi kazancının olup olmadığı bilgisi tanımlanır. Maddi kazancı olmayan önerilerde “0” girilir. Maddi kazanç söz konusuysa önerinin firmaya ne kadar kazanç sağladığı bilgisi tanımlanır.

**Önerinin Uygulama Maliyet Açıklama Bilgiler:** Önerinin hayata geçirilmesi sürecinde ne gibi uygulama maliyetlerinin olduğu bilgisi tanımlanır.

**Önerinin Maliyeti:** Önerinin maliyet bilgisi TL olarak tanımlanır.

**Önerinin Net Kazancı:** “Öneri Brüt Kazancı”ndan “Önerinin Maliyeti”nin çıkarılmasıyla oluşan fark önerinin net kazancı olarak otomatik görüntülenir.

**Öneri Kazançları:** Kazanç kategorilerinden seçilen değerler görüntülenir. Bu alanda ekleme, çıkarm gibi değişiklikler yapılabilir.

**Başka İş Yerinde Uygulanabilir mi? :** Hayata geçen önerinin başka iş yerlerinde uygulanıp uygulanamayacağı seçilir. “Evet” seçeneği işaretlenirse sistemde kayıtlı olan işyerlerinden hangilerinde uygulanabileceği bilgisi seçilir.

**Başka Departmanda Uygulanabilir mi? :** Hayata geçen önerinin başka departmanlarda uygulanıp uygulanamayacağı seçilir. “Evet” seçeneği işaretlenirse sistemde kayıtlı olan departmanlardan hangilerinde uygulanabileceği bilgisi seçilir.

**Diğer Alanlar sekmesi:** Kazanç /Maliyet ile ilgili parametrik alanların bulunduğu sekmedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfbbc2aed-33e3-4e2a-86b9-6ff1c3312af4)

**Ek Dosyalar sekmesi:** Bu aşamada Öneri ile ilgili varsa Ek Dosya eklenebildiği sekmedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload13447c19-54db-47bd-a3dc-c052111a71c8)

**Öneri Detayları sekmesi:** Öneriye ait tüm bilgiler görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload46ef06d3-a5f7-4bad-b9b7-81ef5dfe9eb8) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb4e00140-3c00-4e41-80e2-d02ca3646e78) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb4e99ca3-dfc1-4643-8fbb-053014ed22a0)

Gerekli alanlar girildikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbe89ebb8-9c1a-49d9-a5a2-fa13135d58fb) (Kaydet) butonuna tıklanarak kazanç/ maliyet analizi aşaması tamamlanır, puanlama aşamasına geçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload44103392-c970-4df6-98a4-8f38054a193e)

#### **Puanlama Süreci**

Kazanç/ Maliyet analizinden sonraki süreç puanlama sürecidir. Akışta tanımlanan rolün “Bekleyen İşlerim” sayfasında “Puanlama Bekleyen Öneriler” olarak görev düşer. Öneri numarasına tıklanarak puanlama süreci başlatılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade903009c-ced4-4c21-8de3-a3865ddbaaaa)

Belirlenen puanlama yöntemine göre (Puan Cetveli, Formül Kullanma, Anket) puanlama işlemi gerçekleştirilir ve kayıt işlemi ile öneri kapatılır.

Puan cetvelinin kullanılıyorsa “Puan Kriteri” alanından hangi puan cetveli kullanılacaksa o seçilir. Öneri; ön değerlendirme aşamasında “Kampanya Önerisi” olarak seçilirse kampanyanın bireysel puanı puan olarak görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade2121acd-62c9-411d-bdc0-cd445cd3357b)

#### **Sonuçlanmış Öneriler**

Öneri kapatıldıktan sonra öneri verene sistem tarafından geri bildirim yapılır. Öneri veren kullanıcının “Bekleyen İşlerim” sayfasında **“Sonuçlanmış Önerilerim”** olarak bilgi düşmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1601ab59-5871-4c77-a694-0da66206d8f4)

Öneri numarasına tıklanarak açılan ekranda öneri ile ilgili gerçekleşen işlem bilgileri görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3dc638d8-5569-439f-9073-fbf2883ee5b1)

### **Değerlendirdiklerim**

**Menü Adı**: Entegre Yönetim Sistemi/ Öneri Sistemi/ Değerlendirdiklerim

Kullanıcının değerlendirdiği önerilerin durumunu gösteren menüdür. Hangi durumda, kimde bekliyor gibi bilgiler görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload373ddc9d-b562-46f6-8135-ecd36c4e5194)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf155cb87-0afb-41eb-8cac-57dc91784932): Öneri detayları görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddfd13c28-f80c-4e17-b716-6b8cca095c95): Aksiyon (Planlanacak) statüsünde olan öneriler için aksiyon planlanması yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload452f725f-82bd-4df7-a857-d58bd4080d6d): Öneri puan statüsünde ise bu buton yardımıyla puanlama süreci gerçekleştirilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0528721-1762-43e8-8a2c-44b8cf6a80f7): Puanlama işlemi yapılıp kapatılan öneriler için geri bildirimler bu buton yardımıyla yapılabilir. Sadece geri bildirim durumundaki öneriler için bu işlem yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbdb494b8-c881-4a6f-8d79-700b51ee6646): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload999bac6b-8859-4c6b-a211-d062c22d6785): Veriler Excel’ e aktarılabilir.

### **Puan Harcama**

**Menü Adı**: Entegre Yönetim Sistemi/ Öneri Sistemi/ Puan Harcama

Firmada öneriler için ödül sistemi varsa bu menü kullanılır. Önerilerden kazanılan puanların kullanıcılar tarafından harcandığı menüdür. Ek ödeme, hediye, alışveriş çeki gibi ödüller için puan harcama işlemleri gerçekleştirirler. Puan harcama işlemi ödülleri veren kullanıcılar tarafından yapılmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7d1c19c3-222c-40e1-b69e-8d51676ceffa)

Puan listesi ekranında kullanıcılara ait puanlar görüntülenmektedir. Puan harcaması yapılacak kişinin üzerinde iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload60a5407f-c507-42b8-adf2-1712d26b77a3) (Puan Harca) butonuna tıklanarak puan harcaması gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb39eb9c8-b07b-4dcf-a2ce-02200eee85eb)

Kaç puan harcandığı bilgisi girilir. Harcanan puanın açıklamasını yapılır ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbe89ebb8-9c1a-49d9-a5a2-fa13135d58fb) (Kaydet) butonu ile işlem kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6a17d79c-3c21-41aa-af64-a5af6a4ca384)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade9fc2151-ed8e-4d9f-8841-dec17d9837bc)

### **Geri Bildirim Onayı**

**Menü Adı**: Entegre Yönetim Sistemi/Öneri Sistemi/ Geri Bildirim Onayı

QDMS sisteminde kayıtlı olan ancak QDMS sistemi kullanıcısı olmayan bir personel adına, sistemde verilen öneriye ait önerinin durumu ile ilgili manuel olarak geri bildirim yapmak için kullanılır. Öneriyi veren personelin bilgisayarı olmadığı durumlarda, öneri sonucunun kişiye iletilmesi için kullanılan mekanizmadır. Öneri sonucunu, öneriyi verene iletme görevi, öneri uzman değerlendirmesi yapan kişidedir. Geri bildirim parametresi aktif ise uzman değerlendirme aşamasında öneri ret edilirse uzman değerlendirmeciye geri bildirim görevi düşmektedir. Uzman, öneriyi verene bunu ilettikten sonra QDMS’e gelerek bu görevi kapatabilir. Aynı şekilde Öneri kabul edildiğinde, Öneri Uzmanına geri bildirim görevi düşer. Öneri uzmanı, öneriyi verene önerinin kabul edildiğini ilettikten sonra QDMS’de bu görevi kapatabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0b95db1a-ea4f-41db-93cb-2eb85ee16430)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb4fc377d-4a20-4c7e-90e5-9e2e90cbe9d4)**:** Önceki ekrana dönülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbdb494b8-c881-4a6f-8d79-700b51ee6646): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddfc7150d-6ac8-4da3-8086-86794e0e486c): Onay işlemleri yapar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload726cc090-7b82-4d28-bc31-19cf80aa759f)

### **Öneri İtiraz**

**Menü Adı**: Entegre Yönetim Sistemi/ Öneri Sistemi/ Öneri İtiraz

Kullanıcıya ait herhangi bir aşamada reddedilen öneriler listelenip görüntülenir. Kullanıcı verdiği öneriye dair yapılan redde itiraz etmek için, bu menüyü kullanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload706172ba-a6df-4dd1-bf14-6420584ef80f)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbfc57102-91b9-4894-a3fd-d5ab5f3d73a2) (İtiraz Formu Doldur) butonuna tıklanarak “Reddedilen Öneriler-İtiraz Formu Doldurma” ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade94f7f7f-d8e2-4cf7-a06b-51301f4a560c)

Açıklama alanı yazılıp kayıt işlemi gerçekleştirildiğinde, ilgili değerlendirme rolüne itiraz değerlendirmesi için görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1f0c94bc-5881-4818-a9ac-0ce06635e09d)

### **Komisyon Değerlendirme**

**Menü Adı**: Entegre Yönetim Sistemi/ Öneri Sistemi/ Komisyon Değerlendirme

Öneriye yapılan 2. itirazdan sonra, önerinin bir öneri komisyonu tarafından değerlendirilmesi isteniyorsa komisyon değerlendirme süreci başlatılır. Belirlenen komisyon tarafından öneri değerlendirilir. Komisyon verilen öneriyi onaylar ise akış devam eder, reddederse öneri reddedilir. Komisyon tarafından reddedilen öneriye bir daha itiraz etme edilemez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb7a86590-1edf-42d2-b302-1e57e3bb206e)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadae0d9eba-c1b9-4348-9935-80f30b718aa3) (Onay İşlemleri) butonuna tıklanarak “İtiraz Edilen Öneriler-Komisyon Değerlendirme” ekranı görüntülenir.

Onay/ Ret İşlemleri sekmesinde önerinin onay ya da red işlemleri gerçekleştirilerek açıklama bilgisi girilir. girilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbe89ebb8-9c1a-49d9-a5a2-fa13135d58fb) (Kaydet) butonuna tıklanarak komisyon değerlendirme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb06cfbc4-cf0c-4373-9549-3c6909afdcc8)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload933c3d79-20e7-4c6b-b78b-f540cb32fbc7)

### **Aksiyon Takibi**

**Menü Adı**: Entegre Yönetim Sistemi/ Öneri Sistemi/ Aksiyon Takibi

Kullanıcının vermiş olduğu önerilere ait aksiyonların takibi ve raporlaması yapılır. Aksiyon modülüne ait kalemler raporu ekranıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5cf93d12-972f-4603-b496-864a79c0b4e5)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbdb494b8-c881-4a6f-8d79-700b51ee6646): Kayıtlar filtrelenerek arama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload999bac6b-8859-4c6b-a211-d062c22d6785) : Veriler Excel’ e aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload38753644-3265-4d3a-8dfa-fb2aa3c69670) : Özet Rapor alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade895a2cb-3057-4cd9-9e76-a0724f6f47a9): Log görüntüleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5e6374e1-4856-4612-9794-f15ed9ea7480): Aksiyon Çizelge Raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada651ff90-0d0a-4b24-b470-ccd4b30ccaa6) Excel’e aktar butonu ile excel formatında “Aksiyon Özet Raporu” görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload01121bc9-2c21-4976-867e-49492b874d1a)

### **Öneri Takip**

**Menü Adı**: Entegre Yönetim Sistemi/ Öneri Sistemi/ Öneri Takip

Kullanıcının vermiş olduğu tüm önerilerin durumlarının takip edildiği menüdür. Kullanıcının vermiş olduğu öneri hangi statüde kimde bekliyor gibi bilgiler görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload877ea329-6e24-4cae-8382-369f6d322c40)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload01163cb7-0c8c-416e-ab54-7f7ca2e5ffaf) (Görüntüle) butonuna tıklanarak öneriye dair bilgileri görüntülendiği “Öneri Detayları” ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload29e0ba31-8aab-4ff6-9eae-cc260bd75e83)

### **Raporlar**

**Menü Adı**: Entegre Yönetim Sistemi/ Öneri Sistemi/ Raporlar

Öneri modülünde gerçekleşen işlemler sonucunda oluşan öneri raporların görüntülendiği menüdür.

#### **Öneri Durum Raporu**

**Menü Adı**: Entegre Yönetim Sistemi/ Öneri Sistemi/ Raporlar/ Öneri Durum Raporu

Önerilerin en son durumları hakkında bilgi veren rapordur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5cfb300a-bb26-4253-8b59-184e7b28ba89)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload01163cb7-0c8c-416e-ab54-7f7ca2e5ffaf) (Görüntüle) butonu ile “Öneri Detayları” görüntülenir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2cdafcef-b2db-4b09-89fe-7bb209b13e7f) (Excel’e Aktar) butonuna ile “Öneri Durum Raporu” excel olarak sistemden alınabilmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadae7b2227-bafe-410d-95d0-9f497fd4b470)

#### **Değerlendirme Durum Raporu**

**Menü Adı**: Entegre Yönetim Sistemi/ Öneri Sistemi/ Raporlar/ Değerlendirme Durum Raporu

Öneri değerlendirme aşamalarını gösteren rapordur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload56bfd4cb-5b02-4d14-8704-ae1722e1dc73)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload01163cb7-0c8c-416e-ab54-7f7ca2e5ffaf) (Görüntüle) butonu ile “Öneri Detayları” görüntülenir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2cdafcef-b2db-4b09-89fe-7bb209b13e7f) (Excel’e Aktar) butonuna ile “Değerlendirme Durum Raporu” excel olarak sistemden alınabilmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload18a3494f-b15f-4dd5-b8e7-69c80dbcc90d)

#### **Değerlendirme Bekleyen Öneriler Raporu**

**Menü Adı**: Entegre Yönetim Sistemi/ Öneri Sistemi/ Raporlar/ Değerlendirme Bekleyen Öneriler Raporu

Sistemde değerlendirmede aşamasında bekleyen önerileri gösteren rapordur

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5226c7a9-3573-4ed4-b0b8-f5e44109c5c6)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload01163cb7-0c8c-416e-ab54-7f7ca2e5ffaf) (Görüntüle) butonu ile “Öneri Detayları” görüntülenir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2cdafcef-b2db-4b09-89fe-7bb209b13e7f) (Excel’e Aktar) butonuna ile ilgili rapor excel olarak sistemden alınabilmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb395d8a0-378d-45e5-8cff-03977fd4b048)

#### **Yıllık Öneri Takip Listesi**

**Menü Adı**: Entegre Yönetim Sistemi/ Öneri Sistemi/ Raporlar/ Yıllık Öneri Takip Listesi

Hangi yıla ait öneriler takip edilmek isteniyorsa, o yıl bilgisi sistemden seçilir. bu rapor ile seçilen yıl için hangi departmandaki hangi personellerin kaçar öneri verdiği ve bu önerilerden kaçının onaylandığı bilgisine erişilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6ba1b9bb-f1ea-4c6b-b9b2-957333bd8d7a)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2cdafcef-b2db-4b09-89fe-7bb209b13e7f) (Excel’e aktar) butonuna basılırsa, sistem otomatik olarak Yıllık Öneri Takip Listesi Raporu oluşturup kullanıcıya excel formatında sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7ac31493-89c3-45b2-823f-12e67c96d51f)

#### **Puan Alan Öneriler**

**Menü Adı**: Entegre Yönetim Sistemi/ Öneri Sistemi/ Raporlar/ Puan Alan Öneriler

Sistemde puanlama sürecinden geçen önerilerin kaçar puan aldığını gösteren rapordur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade479a2b4-3fd9-4dde-b38c-a56e96c92973)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2cdafcef-b2db-4b09-89fe-7bb209b13e7f) (Excel’e aktar ) butonuna basılırsa, sistem otomatik olarak Puan Alan Öneriler raporunu oluşturup kullanıcıya Excel formatında sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c7a108c-0fc4-4858-b6f9-efa85c532a6e)

#### **Kişi Puan Listesi**

**Menü Adı**: Entegre Yönetim Sistemi/ Öneri Sistemi/ Raporlar/ Kişi Puan Listesi

Kişilerin verdikleri öneriler kapsamında toplamda kaç puan aldıklarını gösteren rapordur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8f7f47ba-51c6-4dc1-9b99-227eade39e7c)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadabe33b78-1f1b-4374-85af-6ff9bd149341) (Puan Detayı) butonuna tıklanarak Kişi Puan Detayı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade8382965-5c30-4723-abd2-31f4aedf0fb6)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2cdafcef-b2db-4b09-89fe-7bb209b13e7f)(Excel’e aktar) butonuna basılırsa, sistem otomatik olarak Kişi Puan Listesi raporunu oluşturup kullanıcıya Excel formatında sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2a170ce1-ebc3-4ce7-b3e2-99068017086d)

#### **Kaynak Bazında Durum Raporu**

**Menü Adı**: Entegre Yönetim Sistemi/ Öneri Sistemi/ Raporlar/ Kaynak Bazında Durum Raporu

Öneri kaynağı bazında önerilerin durumunu gösteren rapordur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadccb3f318-cd76-4363-bbae-602d8a52ed54)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2cdafcef-b2db-4b09-89fe-7bb209b13e7f) (Excel’e aktar) butonuna basılırsa, sistem otomatik olarak Kaynak Bazında Durum Raporu oluşturup kullanıcıya Excel formatında sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload15ba6f25-381e-433f-b6e0-55b0f44388ca)

#### **Bölüm Bazında Durum Raporu**

**Menü Adı**: Entegre Yönetim Sistemi/ Öneri Sistemi/ Raporlar/ Bölüm Bazında Durum Raporu

Bölüm bazında öneri durumunu gösteren rapordur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2618f8fd-3623-4424-a2f5-78569be57dee)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2cdafcef-b2db-4b09-89fe-7bb209b13e7f) (Excel’e aktar) butonuna basılırsa, sistem otomatik olarak Bölüm Bazında Durum Raporu oluşturup kullanıcıya Excel formatında sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade2413a23-2ed4-4581-b49f-9318836d831a)

#### **En Çoklar Raporu**

**Menü Adı**: Entegre Yönetim Sistemi/ Öneri Sistemi/ Raporlar/ En Çoklar Raporu

En çoklar raporunda şu ana kadar verilen tüm öneriler baz alındığında kimin en çok öneri verdiğinin görülmesini sağlayan bir rapordur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4b4ee96b-0995-49cb-b8bc-d73c8c76cf37)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2cdafcef-b2db-4b09-89fe-7bb209b13e7f) (Excel’e aktar) butonuna basılırsa, sistem otomatik olarak En Çoklar Raporu oluşturup kullanıcıya Excel formatında sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadabaccce1-ceaa-4c32-8ba4-43d803a8de26)

#### **Öneri İzleme Raporu**

**Menü Adı**: Entegre Yönetim Sistemi/ Öneri Sistemi/ Raporlar/ Öneri İzleme Raporu

Hangi aşamada kaç tane öneri olduğunu ve bu önerilerin kaç tanesinin beklemede, kaç tanesini değerlendirilmiş olduğunu gösteren rapordur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload56a26cd1-59f5-4e05-9fb9-6f164e7ec28e)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2cdafcef-b2db-4b09-89fe-7bb209b13e7f) (Excel’e aktar) butonuna basılırsa, sistem otomatik olarak Öneri İzleme Raporu oluşturup kullanıcıya Excel formatında sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadef7225c7-40ce-4e70-b876-45befe1c9022)

#### **Öneri Havuzu**

**Menü Adı**: Entegre Yönetim Sistemi/ Öneri Sistemi/ Raporlar/ Öneri Havuzu

Sistemdeki tüm önerilerin gösterildiği rapordur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9acace7a-4e1f-41f4-ab69-5a49c8e3ca87)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2cdafcef-b2db-4b09-89fe-7bb209b13e7f) (Excel’e aktar) butonuna basılırsa, sistem otomatik olarak Öneri Havuzu raporunu oluşturup kullanıcıya Excel formatında sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf763ccaf-ea64-46d3-add1-ab793706a880)

#### **Öneri Aksiyon Raporu**

**Menü Adı**: Entegre Yönetim Sistemi/ Öneri Sistemi/ Raporlar/ Öneri Aksiyon Raporu

Sistemdeki önerilere ait aksiyonları gösteren rapordur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0e1a55a0-0536-41fd-89cf-79c67ed47799)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2cdafcef-b2db-4b09-89fe-7bb209b13e7f) (Excel’e aktar) butonuna basılırsa, sistem otomatik olarak Öneri Aksiyon Raporu oluşturup kullanıcıya Excel formatında sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f48e45e-2dd3-4738-aafb-f5c5fbb2a49d)

#### **Öneri Rapor**

**Menü Adı**: Entegre Yönetim Sistemi/ Öneri Sistemi/ Raporlar/ Öneri Rapor

Önerinin hangi statüde olduğunu gösteren rapordur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7780e23b-2891-4bb7-ba0e-4d777fbcb552)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2cdafcef-b2db-4b09-89fe-7bb209b13e7f) (Excel’e aktar) butonuna basılırsa, sistem otomatik olarak Öneri Raporu raporunu oluşturup kullanıcıya Excel formatında sunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfa3699b7-d643-4402-bbf3-9c8753919fc6)

### **Grafikler**

**Menü Adı**: Entegre Yönetim Sistemi/ Öneri Sistemi/ Grafikler

Öneri modülüne ait grafiklerin görüntülendiği menüdür.

#### **Öneri Sayıları Grafiği**

**Menü Adı**: Entegre Yönetim Sistemi/ Öneri Sistemi/ Grafikler/ Öneri Sayıları Grafiği

Belirtilen tarih aralığına ait aylık veya haftalık olarak öneri sayılarının grafiğini almak için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4ce3bc8-e9d2-493a-ad07-d2a44d7864bd)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload549c42bc-c150-48ba-9d46-bede09f6042b) (Grafik Çiz) butonuna tıklanarak yapılan filtrelere göre öneri sayıları grafiği oluşturulur. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3ce1fd9c-e585-412f-9d19-4de03064153c) (Dışa Aktar) butonu ile oluşturulan grafik istenilen formatta (excel, jpg, pdf vb ) dış ortama aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6edba7dc-9d01-4690-8bff-4de6b0fb2be4)

## **Sistem Altyapı Tanımları/ Öneri – 2.Kısım**

### **Puan Ekleme**

**Menü Adı**: Sistem Altyapı Tanımları/ Öneri/ Puan Ekleme

Öneri modül adminleri tarafından önerilere ek puan eklenmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload55cf7fc0-9d87-403d-9e1e-3fe5729c0317)

Puan eklenmek istenilen öneri seçilerek, ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload399ecbf5-7906-4716-9baa-1af002769be6) (Puan Ekleme) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload363ea606-6c6f-40c3-a835-b1290c51bd4e)

“Eklenecek Kişi Başı Puan” ve “Açıklama” bilgisi girilir ve kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadee923110-ba44-4153-94b7-bf4c16067a36)

### **Öneri Kayıt Bakım**

#### **Öneri Bilgileri Güncelleme**

**Menü Adı**: Sistem Altyapı Tanımları /Öneri/ Öneri Kayıt Bakım/ Öneri Bilgileri Güncelleme

Herhangi bir öneri kaydının öneriye ait bilgilerinin admin kullanıcı tarafından düzenlendiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20509b4d-a66a-4a8b-a4b1-60a013320f42)

Öneri kaydı seçilerek iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade5294232-4e38-4e0e-8bfd-c2228ab1b52b) (Güncelle) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4a94773f-c009-4cfd-85f8-bc578546a65a)

Açılan ekranda öneriye ait bilgiler düzenlenerek kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd4e5e030-1bea-4807-ae20-67693f798ee9)

#### **Statü Değiştirme**

**Menü Adı**: Sistem Altyapı Tanımları/ Öneri/ Öneri Kayıt Bakım/ Statü Değiştirme

Herhangi bir öneri kaydının durumunun admin kullanıcı tarafından değiştirildiği menüdür. Öneriyi ön değerlendirmeye ve bir önceki statüye çekmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd7c2315b-4280-4848-afd9-35f519ebf923)

Öneri kaydının seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5296ad12-b211-43a7-adcb-2ef9859e9898) (Ön Değerlendirmeye Getir) butonuna tıklanır. Öneri ön değerlendirmeye veya bir önceki statüye döndürülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd6ed72ac-d170-4d4c-a79d-3c409e316058)

Öneri ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload692f6c55-730b-4e2a-be53-278a36f0bf32)(Ön Değerlendirmeye Getir) butonuna tıklanarak ön değerlendirme statüsüne getirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload77df3611-5194-4349-8b26-44f7bceeffea)

Statü değiştirme nedeni yazılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload931ab8f0-e228-488c-8ce0-7b7aa2b60470) (Onayla) butonu ile işlem onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload15cce810-b809-4660-9ace-c6922ed3d4a8)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade1e5a3a5-31d2-4f77-a8d0-67aa7b58dd07)

Öneri ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade408648e-e7b2-4bfe-a875-53baee840216) (Önceki Statüye Geçir) butonuna tıklanarak bir önceki statüye geçiş sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb1265a9-70b3-4d58-8e7e-5b81b4a076a6)

### **Öneri Silici**

**Menü Adı**: Sistem Altyapı Tanımları/ Öneri/ Öneri Silici

Admin kullanıcı tarafından öneri silme işleminin gerçekleştirildiği menüdür. Silinen öneriler veri tabanından kaldırılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf2490aba-8428-4831-a5e7-3cfed78a15d2)

Öneri kaydı seçili iken ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadab620467-0827-4e14-9555-980ebbfd3e8a) (Sil) butonuna tıklanarak öneri kaydı silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5d4cbbb4-c253-493f-a4f3-284abae98ea7)
