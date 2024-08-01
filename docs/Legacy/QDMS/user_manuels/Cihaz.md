---
title: Cihaz Yönetim Sistemi
description: Cihaz Yönetim Sistemi Yardım Dokümanı
sidebar_position: 11
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::


**Cihaz Yönetim Sistemi Modülü(v.5.24) Kullanıcı Yardım Dokümanı**

Modül Versiyonu: 5.24



**1.GİRİŞ: “QDMS Cihaz Yönetimi Modülü”**, bir firmadaki cihazların kalibrasyon, bakım, doğrulama gibi faaliyetlerinin takibinin sağlanması; periyodik olarak sürdürülmesi ve bu işlemler sonucunda oluşan verilerin saklanması ve raporlanması işlemlerini kapsar. Ayrıca cihaz envanterinin saklanması ve güncel tutulması da cihaz yönetiminin kapsamı dahilindedir.

**2.AMAÇ:** Bu yardım kılavuzunun amacı, QDMS üzerindeki Cihaz Yönetimi modülünün yardımıyla cihaz envanterinin sürekli güncel olarak tutulması, işlem tiplerinin belirlenmesi ve her bir cihaz ya da cihaz kategorisi için işlem periyotlarının tayin edilerek bu periyotlar geldikçe cihaz faaliyetlerinin gerçekleştirilip ilgili verilerin saklanması sırasında izlenecek yolu belirlemektir.

**3.SORUMLULUKLAR:** Cihaz Sorumlusu, İşlem Sorumlusu

**4.KISALTMALAR:**

QDMS: Kalite Dokümanları Yönetim Sistemi “ Quality Document Management System”

KAL: Kalibrasyon

BKM: Bakım

DOG: Doğrulama

# **5.İŞ AKIŞI:**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbcf6d8d7-6fc7-4114-82b8-13f7756bcb8a)



# **6.Cihaz Yönetim Sistemi Modülü**

Kalibrasyon, doğrulama gibi cihaza yönelik işlemlerin takibi, cihaz envanterlerini izleme, kalibrasyon rapor ve tarihçesine anlık olarak erişim, cihaz ve işlem sorumlularını e-mail ile bilgilendirme, işlem maliyetlerinin takibini yapan modüldür. Cihazın Hurda ve kullanımda olma durumlarının da takibinin yapıldığı modüldür.

## **6.1.Sistem Altyapı Tanımları/ Cihaz Yönetim Sistemi**

Cihaz Yönetim Sistemi Modülünün alt yapısının oluşturulacak tanımlamaların yapıldığı kısımdır. Yapılan tanımlamalara göre veriler karşımıza çıkmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload66d6be00-80b9-478e-aec8-571ce6a06586)

### **6.1.1.Cihaz Kategorileri**

**Menü Adı:** Sistem Altyapı Tanımları/ Cihaz Yönetim Sistemi/ Cihaz Kategorileri

Cihaz Kategorileri, Cihaz Yönetim Sistemi’nde kullanılacak olan cihazların kategori oluşturma işleminin gerçekleştiği menüdür. Bu menüde cihazları genel olarak ağırlık ölçerler nelerdir, basınç ölçerler nelerdir ve uzunluk ölçerler nelerdir belirleyerek kategorize ediyoruz. Örneğin ağırlık ölçülerin altında kantarlar ve teraziler olabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload85fa8f32-fd38-46f1-bfd6-3194691658f8)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload14183877-7514-400f-938b-0eefc8cbc9e7): Yeni bir cihaz kategorisi tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload07a65bd7-29e3-41b4-90f5-a6d035d4c2a7): Listede seçili cihaz kategorisi bilgisi ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9792a200-bc23-4661-8e45-acca30a6b593): Listede seçili cihaz kategorisi bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3ee199c5-efb6-4669-8515-fa599a878e7f): Listede seçili cihaz kategorisi için ölçüm sabitleri belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2815e85d-0f6e-40d0-81b8-d187b8e97c3f): Listede seçili cihaz kategorisi için işlem tiplerini belirler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5347290e-ea27-4cef-9e23-eb81fac0223f) : Veriler Excel’ e aktarılabilir.

Listeye yeni bir cihaz kategorisi eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4bed12f5-5517-4ef2-b2b1-ee881cfd6d30) (yeni) butonu tıklanarak Cihaz Kategorisi Tanımlama/ Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada7835d5b-de8f-4da3-878a-d6b760ec942a)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Üst Kategori Kodu:** Oluşturulma aşamasında olan üst kategori kodu, bir kategori kodu tanımı olarak önceden sisteme kaydedilir. Bu üst kategoriye bağlı alt kırılımı olması halinde bu alan otomatik dolu gelir. Dolu olarak gelen alanda bağlı olduğu üst kategori kodu tanımının adı yazar. Bağlı olduğu üst kırılım silinmek istenildiğinde sağ yanda bulunan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbe1c090e-8f68-43e3-bdde-e6c7e358f50d) (sil) butonu veya değiştirilmek istenildiğinde sağ yanda bulunan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2ab9f829-5d8f-48a8-9fba-021cff6e7956) (seç) butonu kullanılır. Bağlı olduğu bir üst kategori yok ise bu alan boş gelir.

**Kategori Tanımı:** Cihaz kategorisi adının bilgisi girilir.

**Kategori Kodu**: Cihaz kategorisi kod bilgisi girilir.

**Durum:** Cihaz Kategorisi pasif ya da aktif durumunun bilgisi seçilebilir.

**Tolerans Değer(%) :** Cihaz kategorisi tolerans değerinin (%) bilgisi girilir. Yüzdelik sapmayı ne kadar kabul edeceğini gösteren yerdir. Kabul alt ve üst aralıkları kullanıcı tarafından manuel girildiğinde tolerans değere göre kabul alt ve kabul üst aralıklarını otomatik hesaplar.

**Rapor Şablonu Dosya Adı:** Rapor şablonu dosya adı ve uzantısı eklenir. Cihaz kategorisi bazında rapor eklenir. Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Rapor Formatları menüsünde eklenen raporu bu alana adı yazılır.

**Otomatik Kod Şablonu Kullanımı:** Otomatik kod şablonu kullanılsın bilgisinin evet ya da hayır seçenekleri seçilebilir.

**Otomatik Kod Şablonu:** Otomatik kod Şablonu bilgisi girilir. Cihaz kategorilerini tanımlarken otomatik kod şablonun kullanılması sağlar. Örneğin: AO.\#\#\#

**Sayaç:** Kod sayacının kaçtan başlanması isteniyorsa o sayının yazıldığı kısımdır. Örneğin: 0 vb. kod sayacı cihaz kategorilerinin, otomatik kod şablonundaki \#\#\# ifadelerini baz alarak otomatik olarak saydırma işlemini yapan kısımdır. Örneğin: AO.\#\#\# otomatik kod şablonuna göre sayaç değeri 0 girildiğinde sistem tanımlanan cihaz kategorilerini sırayla AO.001 den AO.999 değerine kadar otomatik olarak kod verilmesini sağlar.

Üst Kategori kodu bilgisi sistemde tanımlı kategori listesinden seçilir. Cihaz kategorisi tanımı ve kod bilgisi girilir. Durum bilgisi "aktif" ve "pasif" olarak ikiye ayrılmaktadır. Aktif olarak tanımlı cihaz kategorisi sistemde kullanılan cihaz kategorileri ifade etmektedir. Eğer bir cihaz kategorisi tanımı sistemde artık kullanılmayacaksa, durumu “pasif” olarak değiştirilmelidir. Böylece hem geçmişteki mevcut kayıtlar etkilenmez, hem de yeni cihaz kategorisi seçim ekranlarında pasife alınan cihaz kategorisi bilgisi görüntülenmez. Cihaz kategorisinin durum kısmı aktif olarak seçilir. Tolerans değer (%) bilgisi girilir. Otomatik kod şablon bilgisi evet seçeneği tıklanır. Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload822250b9-55f0-468b-8e26-8524e5297bd3) (kaydet) butonu tıklanarak cihaz kategorisi tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload83d3e11e-867c-4731-bb9a-078b2825757a)

Var olan bir cihaz kategorisine yeni alt kategori eklemek için, alt kategori eklenecek cihaz kategorisi seçili haldeyken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8b58db1f-b557-4435-a825-e0c5c2e22102) (yeni) butonu yardımıyla cihaz kategorisi tanımlama ekranına gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada4ea37d0-442f-4a48-87b6-f33993a6e2a1)

Burada üst kategori kodu otomatik olarak gelir. Alt kategori oluşturulduktan sonra kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload44d71c70-ec7e-4f89-bf72-44bb7e81fce1)

Burada “Tolerans Değer” alanı cihaz kategorisine göre, ölçüm sabitleri alanında alt ve üst aralıklara % değer vererek limitleri belirleyebildiğiniz kısayol alanıdır. “Rapor Şablonu Dosya Adı” alanına rapor formatlarında bulunan, cihaz kategorilerine göre belirlenmiş rapor formatlarının adı yazılır. Bu sayede cihaz kategorilerine göre kalibrasyon raporu değişiklik gösterecektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc1e86c84-2b87-4ab9-b831-8ca5aade9100)

Cihaz Kategorisi Tanımlama ekranında listede herhangi bir kategori seçili durumdayken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc5d2d82f-61f7-41d4-8526-f71444d41c5b) (ölçüm sabitleri) butonuna basılırsa, Ölçüm Sabitleri ekranına ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaaf53a4e-088b-4a30-9990-ac64ac37f957)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1a15c935-e661-4293-a5fe-8206a387a296) : Yeni bir ölçüm sabiti tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload995e38cb-b0e3-44e6-b7fb-34204b6ab4ae) : Listede seçili ölçüm sabiti bilgisi ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5e900fda-57a4-46c7-bcdc-77828767aac4) : Listede seçili ölçüm sabiti bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5632f7cd-2a84-462f-90e7-5c7c3807a8ff) : Bir önceki ekrana dönülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5347290e-ea27-4cef-9e23-eb81fac0223f) : Veriler Excel’ e aktarılabilir.

Listeye yeni ölçüm sabitleri eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4bed12f5-5517-4ef2-b2b1-ee881cfd6d30) (yeni) butonu tıklanarak Ölçüm Sabitleri/ Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4bd747a3-e52d-4625-bbd8-7c799ec876e1)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Tanım:** Ölçüm sabitinin tanım bilgisi girilir.

**Ölçüm Birimi:** Ölçüm birimi bilgisinin BSAT/ Tanımlar/ Ölçü Birimi Tanımlama menüsüne gelinir. Bu menüdeki tanımlı olan ölçü birimleri karşımıza çıkmaktadır. Yeni bir ölçüm birimi tanımlanmak istenirse bu menüden tanımlanmalıdır. Örneğin Adet, Kilogram gibi

**Referans Değer:** Ölçüm sabitinin referans değer bilgisi girilir.

**Standart Değer:** Ölçüm sabitinin standart değer bilgisi girilir.

**Kabul Aralığı Alt:** Ölçüm sabitinin kabul aralığı alt bilgisi girilir.

**Kabul Aralığı Üst:** Ölçüm sabitinin kabul aralığı üst bilgisi girilir.

Ölçüm sabitinin tanım bilgisi girilir. Ölçüm sabitinin ölçüm birimi bilgisi sistemde tanımlı seçeneklerde seçilir. Referans ve standart değer bilgileri girilir. Kabul aralığı alt ve kabul aralığı üst bilgileri girilir. Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload822250b9-55f0-468b-8e26-8524e5297bd3) (kaydet) butonu tıklanarak ölçüm sabitleri tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6d996dda-5556-458b-9c67-2247a225b1ed)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcae375c0-8a2c-4d18-836b-fd8f82740829)

Cihaz Kategorisi Tanımlama ekranındaki![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload96ef6c28-cd6b-4ca8-a750-b6911854e8af) (işlem tipleri) butonu ile önceden belirlenmiş işlem tipleri ilgili kategoriye atanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1be7d69f-9a8b-438d-8f5e-dce0bef4a131)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1a15c935-e661-4293-a5fe-8206a387a296): Yeni bir kategoriye alt İşlem tipleri tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload995e38cb-b0e3-44e6-b7fb-34204b6ab4ae): Listede seçili kategoriye alt İşlem tipleri bilgisi ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload720d62b6-5e64-410b-bbd3-9815167e3a96): Listede seçili kategoriye alt İşlem tipi bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5632f7cd-2a84-462f-90e7-5c7c3807a8ff): Bir önceki ekrana dönülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5347290e-ea27-4cef-9e23-eb81fac0223f) : Veriler Excel’ e aktarılabilir.

Listeye yeni bir kategoriye alt işlem tipi eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4bed12f5-5517-4ef2-b2b1-ee881cfd6d30) (yeni) butonu tıklanarak Kategoriye Alt İşlem Tipileri/ Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload08d1ec24-1ad1-4f44-99bf-014f3fa40475)

**Açılan ekranda ilgili alanlar tanımlanır:**

**İşlem Tipi:** İşlem tipi Sistem altyapı Tanımları/ Cihaz Yönetimi/ İşlem Tipleri Tanımlama menüsündeki tanımlanmış olan işlem tipi seç listesinden seçilir.

**Periyod:** Kategoriye ait işlem tipleri periyod bilgisi girilir.

**Ön Bildirim Süresi (gün):** Kategoriye ait işlem tipleri ön bildirim süresi bilgisi gün olarak girilir.

**Durum:** Kategoriye ait işlem tipleri pasif ya da aktif durumunun bilgisi seçilebilir.

Kategoriye ait işlem tiplerinin işlem tipi bilgisi sistemde tanımlı işlem tipi listesinden seçilir. Kategoriye ait işlem tipinin periyot bilgisi girilir. Ön bildirim süresi gün olarak bilgisi girilir. Durum kısmı aktif seçilir. Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload822250b9-55f0-468b-8e26-8524e5297bd3) (kaydet) butonu tıklanarak kategoriye alt işlem tipleri tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfdc03329-9f2e-4a7c-ba9e-386bb64033ce)

### **6.1.2.İşlem Yerleri**

**Menü Adı:** Sistem Altyapı Tanımları/ Cihaz Yönetim Sistemi/ İşlem Yerleri

Sistemde cihazların dışarıda işleme tabi tutulduğu yerler tanımlama işleminin gerçekleştiği menüdür. Firmada kullanılan cihazlar kalibrasyon işlemleri için akredite olmuş laboratuvarlara gönderilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb6412f62-e7eb-4e0f-a962-1562822ca61d)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada6297bc8-77bf-4cb5-b0cd-911dac9289d0) : Yeni bir İşlem Yeri tanımlanır

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7f13c7de-793b-4928-af2e-5e380513372e): Listede seçili İşlem Yeri bilgisi ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8c67a226-429d-4832-bd18-4c5df89e2018) : Listede seçili İşlem Yeri bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5347290e-ea27-4cef-9e23-eb81fac0223f) : Veriler Excel’ e aktarılabilir.

Listeye yeni bir işlem yeri eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4bed12f5-5517-4ef2-b2b1-ee881cfd6d30) (yeni) butonu tıklanarak İşlem Yerleri/ Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload86db948e-809e-497d-8d80-f920b88bae06)

**Açılan ekranda ilgili alanlar tanımlanır:**

**İşlem Yeri Kodu:** İşlem yeri kod bilgisi girilir.

**İşlem Yeri Adı:** İşlem yeri adının bilgisi girilir.

**İşlem Sorumlusu:** İşlem yerinin işlem sorumlusunun bilgisi girilir.

**E-Posta:** İşlem sorumlusunun E-Posta bilgisi girilir.

**Telefon:** İşlem yerinin telefon bilgisi girilir.

**Adres:** İşlem yerinin adres bilgileri girilir.

**Fax:** İşlem yerinin fax bilgisi girilir.

**Açıklama:** İşlem yerinin detayı ve açıklama bilgisi girilir.

**Durum:** İşlem yerinin pasif ya da aktif durumunun bilgisi seçilebilir.

İşlem yeri kod, adı, sorumlusu, E-Posta ve adres gibi bilgileri girilerek durum kısmı aktif seçilir. Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload822250b9-55f0-468b-8e26-8524e5297bd3) (kaydet) butonu tıklanarak işlem yeri tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade8026ad7-fd56-4613-a9ca-3ebbe38b24c5)

İşlem yeri tanımlama kısmında kaydedilen yerler, dışarıda işlem gören cihazlar için geçerli olacaktır. Eğer cihazı içerde kalibre edilirse veya doğrulaması yapılırsa;

Sistem Altyapı Tanımları/ BSAT/ Tanımlar/ Şirket Profili Tanımlama menüsünden cihazda işlem yapılan yer seçebilir ve cihazın yerini seçebilme işlemlerini bu menüde gerçekleştirilir. Cihazın şirkette nerede olduğunu belirleme işlemi gerçekleştirilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfdf8b6a9-a563-4bd7-b8b6-36e2944fdfcf)

Listeye yeni bir Şirket Profili eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4bed12f5-5517-4ef2-b2b1-ee881cfd6d30) (yeni) butonu tıklanarak Şirket Profili/ Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc16d6503-2269-44fd-95ba-b56d5eeae742)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Üst Kod:** Şirket profilinin üst kod bilgisi şirket profili seç listesinden seçilebilir.

**Birim Kodu:** Şirket profili kod bilgisi girilir.

**Birim Adı:** Şirket profilinin adı bilgisi girilir.

**Birim Sorumlusu:** Şirket profili sorumlusu personel listesinden seçilebilir.

**Şirket Profili Sorumlu Kullanıcı Grubu:** Şirket profili sorumlu kullanıcı grubu bilgisi kullanıcı grubu seç listesinden seçilebilir. Sistem Altyapı Tanımları/BSAT/Tanımlar/Kullanıcı Grubu Tanımlama menüsünde tanımlı Kullanıcı Grubu listesinde seçim yapılır.

**Durum:** Şirket profilinin durumunun aktif veya pasif seçeneklerinden biri seçilebilir.

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload822250b9-55f0-468b-8e26-8524e5297bd3) (kaydet) butonu tıklanarak işlem yeri tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6da91e54-e05d-45ac-b9b9-acc73166bb1f)

Tanımlanan şirket profilleri, şirket profilinde tanımlanan lokasyonlarda cihazların yerleri veya cihazlara işlem yapılan yerler olabilir.

### **6.1.3.İşlem Tipleri Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ Cihaz Yönetim Sistemi/ İşlem Tipleri Tanımlama

Cihaz yönetimi kapsamındaki tüm işlem türleri tanımlanır. Bu işlem tipleri kalibrasyon, doğrulama, bakım olabilir. Kalibrasyon firma dışında yetkili bir firma tarafından işlem yeri tanıtılarak gerçekleştirilirken, doğrulama ise firmanın kendi bünyesinde şirket profili tanımlanarak gerçekleştirilir. Kalibrasyon, Doğrulama ve bakım genelde kullanılan işlemlerdir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada84e04c1-4b72-42e4-95ca-87ec865e3cfe)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada6297bc8-77bf-4cb5-b0cd-911dac9289d0): Yeni bir İşlem Tipi tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7f13c7de-793b-4928-af2e-5e380513372e): Listede seçili İşlem Tipi bilgisi ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8c67a226-429d-4832-bd18-4c5df89e2018): Listede seçili İşlem Tipi bilgisi siler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload46547470-fd55-473a-b074-8929ae5524cd) : Listede seçili İşlem Tipi bilgisi için özel alanlar tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload347dd012-3fdc-4a08-af0b-c760ad8f7918) : Listede seçili İşlem Tipi bilgisi ile ilgili sonuçlar tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5347290e-ea27-4cef-9e23-eb81fac0223f) : Veriler Excel’ e aktarılabilir.

Listeye yeni işlem tipi eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4bed12f5-5517-4ef2-b2b1-ee881cfd6d30) (yeni) butonu tıklanarak İşlem tipi tanımlama/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadff97ff85-8779-4375-93ba-23c45c4b0360)

**Açılan ekranda ilgili alanlar tanımlanır:**

**İşlem Tipi Grup Kodu:** İşlem tipi grup kodu bilgisi sistemden seçilebilir.

**İşlem Tip Kodu:** İşlem tipi kod bilgisi girilir. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’.

**İşlem Tipi Tanımı:** İşlem tipi tanım bilgisi girilir.

**Sertifika Bilgisi Kullanılacak:** Sertifika bilgisi kullanılacaksa ilgili check box işaretlenir. İşlem tipine göre sertifika ekleme opsiyonu açar.

**Durum:** Pasif ya da aktif durumunun bilgisi seçilebilir. Durum bilgisi "aktif" ve "pasif" olarak ikiye ayrılmaktadır. Aktif olarak tanımlı işlem tipi sistemde kullanılan işlem tipi ifade etmektedir. Eğer bir işlem tipi tanımı sistemde artık kullanılmayacaksa, durumu bilgisi “pasif” olarak değiştirilmelidir. Böylece hem geçmişteki mevcut kayıtlar etkilenmez, hem de yeni İşlem Tipi seçim ekranlarında pasife alınan işlem tipi bilgisi görüntülenmez.

Açılan ekranda işlem tipi kodu ve tanım bilgisi girilir. İşlem tipinin durum kısmı aktif olarak seçilir. Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload822250b9-55f0-468b-8e26-8524e5297bd3) (kaydet) butonu tıklanarak işlem tipi tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc65cb91e-7ba6-44b9-a7d0-c56231211859)

İlk kez işlem tipi oluşturulacaksa işlem tipi grup kodu kutucuğu boş gelir, ancak listeden bir işlem tipi seçili durumdayken yeni işlem tipi oluşturma ekranına gelinirse, seçili işlem tipinin kodu, grup kodu olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7a70806d-3133-4a79-8ba9-6e4d0d145d79)

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload822250b9-55f0-468b-8e26-8524e5297bd3) (kaydet) butonu tıklanarak İşlem Tipi Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload78719bc7-e4be-4434-a6e6-a5542c6bfd35)

Listede bir işlem tipi seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb9b7c354-3838-45ca-bcf4-08ad63ef6d54) ( alan tanımlama ) butonuna tıklanırsa, sadece o işlem türüne özgü parametrik alanlar tanımlanabilir. Bu özel alanlar kalibrasyon raporuna da eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload245320d9-e16f-4402-aff6-54a4e5edb019)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1a15c935-e661-4293-a5fe-8206a387a296): Yeni bir Alan eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload79914dab-c463-4b76-a0c4-c0c960f196a2): Var olan alanda değişiklik yapılmak istenirse kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5e900fda-57a4-46c7-bcdc-77828767aac4): İlgili alanı silmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload355cb70c-aa10-4780-a7cf-4ade42a0da2e): Eğer liste şeklinde Alan eklenmişse liste elemanı ekler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5632f7cd-2a84-462f-90e7-5c7c3807a8ff): Bir önceki ekrana geri dönülür.

Listeye yeni bir alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4bed12f5-5517-4ef2-b2b1-ee881cfd6d30) (yeni) butonu tıklanarak Alan Tanımlama/ Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd1225cb4-5f0d-4981-861e-dcaf7266ad0d)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Alan Kodu:** Alan Kodu bilgisi girilir. Daha önce tanımlamış kod bilgisi aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’.

**Alan Tanımı:** Alan tanım bilgisi girilir.

**Başlık Notu:** Alanın başlık notu bilgisi girilir.

**Kısa Kod:** Kısa Kod bilgisi girilir.

**Veri Tipi:** Veri Tipi seçilir. Veri Tipleri Metin, Çoklu Metin, Nümerik, Personel gibi.

Açılan ekranında, Alan Kodu, Alan Tanımı ve Kısa Kod bilgileri girilip Veri Tipi seçilerek, ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload04bdc119-ac3a-4206-9caa-70bf37d2516a) (kaydet) butonu tıklanarak İşlem Tipine özel parametrik alan oluşturulur. Buradaki kısa kod bilgisi alana yazılan veya alanda seçilen bilginin Kalibrasyon raporuna yansıması için kullanılacak olan kısaltmadır. Veri tipi alanında yapılan seçime göre, metin, numerik, tarih, personel, pozisyon, departman ve liste tipli parametrik alanlar oluşturulabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddbc6fcf6-65e0-4cdf-b1ee-b9846d770d19)

İşlem tiplerinden herhangi bir işlem tipi seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4e9a047e-86ec-40dd-93c2-27bffb2a93ab) ( sonuçlar ) butonu tıklanırsa, o işlem tipinin sonucunda ortaya çıkacak durumlar tanımlanır. Bu durumlara örnek olarak; kullanıma devam edilecek, kalibrasyon sonucu kullanıma uygun değildir, hurdaya ayrılacak vb. durumlar tanımlanır. Bu sonuçlar da kalibrasyon raporu oluştururken kullanılacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfe4562e7-7a01-4583-b202-187df3d15159)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1a15c935-e661-4293-a5fe-8206a387a296): Yeni bir işlem tipine ait sonuçlar tanımlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload79914dab-c463-4b76-a0c4-c0c960f196a2): Listede seçili işlem tipine ait sonuçları bilgisini ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5e900fda-57a4-46c7-bcdc-77828767aac4): Listede seçili işlem tipine ait sonuçları bilgisini siler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5632f7cd-2a84-462f-90e7-5c7c3807a8ff): Bir önceki ekrana geri dönülür.

Listeye yeni bir işlem tipine ait sonuçları eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4bed12f5-5517-4ef2-b2b1-ee881cfd6d30) (yeni) butonu tıklanarak Sonuç Tanımlama/ Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7a904b3b-88e9-42cc-89ad-47b7cca73e95)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Sonuç Kodu:** Sonuç kodu bilgisi girilir. Daha önce tanımlamış kod bilgisi aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’.

**Sonuç Tanımı:** Sonuç tanımı bilgisi girilir.

**Bölümü Değiştirilecek:** Sonucun bölümü değiştirilecekse ilgili check box işaretlenir. Bölümü değiştirilecek aktif edilirse cihazın yeni bölümü seçilebilir.

**Durumu Değiştirilecek:** Durumu değiştirilecekse ilgili check box işaretlenir. Durumu değiştirilecek aktif edilerse yeni durumu seçilir.

**Yeni Durum:** Önceden tanımlanmış olan durum tanımlamadan, sonucun yeni durumu hurda ve kullanımda gibi seçenekler seçilebilir.

**Durum:** Sonucun pasif ya da aktif durumunun bilgisi seçilebilir.

Açılan ekranda sonuç kodu ve sonuç tanımı bilgisi girilerek durum kısmı aktif seçilir. Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload822250b9-55f0-468b-8e26-8524e5297bd3) (kaydet) butonu tıklanarak sonuç tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadddd3b103-41f9-4d40-bc46-ea8a603fb4c1)

### **6.1.4.Durum Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ Cihaz Yönetim Sistemi/ Durum Tanımlama

Durum tanımlama sonuç tipi oluştururken seçilmesi gereken durumlar (hurda, kullanımda, kullanım dışı vb.) tanımlanır. Cihazın durum bilgisi ifade edilmiş olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload86d44c66-0f48-4765-aa37-c2ff0a4b6cac)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1a15c935-e661-4293-a5fe-8206a387a296): Yeni bir durum tanımlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload79914dab-c463-4b76-a0c4-c0c960f196a2): Listede seçili durum bilgisi ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5e900fda-57a4-46c7-bcdc-77828767aac4): Listede seçili durum bilgisi siler.

Listeye yeni bir Durum eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4bed12f5-5517-4ef2-b2b1-ee881cfd6d30)(yeni) butonu tıklanarak Durum Tanımlama/ Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3622f7f0-cb31-4757-be27-012d0090bb2b)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Durum Kodu:** Durumun kod bilgisi girilir. Daha önce tanımlamış kod bilgisi aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’.

**Durum Tanımı:** Durumun tanım bilgisi girilir.

**Varsayılan:** Durumun varsayılan bilgisi seçilecekse ilgili check box işaretlenir. Durum direkt tanımlanan durum olarak default gelir.

**İşleme Devam Edilmeyecek:** Cihaz işleme devam Edilmeyecek seçilecekse ilgili check box işaretlenir. İşleme devam edilmeyecek check box’ı seçilirse, kalibrasyon vb. işlemlerine devam edilmez, kullanım dışı olur.

**Renk:** Durumun renk seçeneklerinden seçilebilebilir. Cihazlar durumlarına göre renklendirilir. Örneğin durumu kullanımda olan cihazları yeşil renk, hurda cihazları kırmızı ve arıza cihazlar kahverengi olarak görüntülenebilir.

**Durum:** Durumun pasif ya da aktif durumunun bilgisi seçilebilir.

Açılan ekranda durum kodu ve durum tanımı bilgisi girilir. İşleme devam edilmeyecek check box işaretlenir. Durumun renk kısmı ilgili seçeneklerden seçilir. Durumun durum kısmı aktif seçilir. Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload822250b9-55f0-468b-8e26-8524e5297bd3) (kaydet) butonu tıklanarak durum tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc197b23b-f349-4196-bded-bb5cf65ff4c3)

### **6.1.5.E-Posta Ayarları**

**Menü Adı:** Sistem Altyapı Tanımları / Cihaz Yönetim Sistemi/ E-Posta Ayarları

E-Posta ayarları ekranında, cihaz modülü süreçlerinin hangi aşamasında kimlere mail ve sms gönderimi yapılacağı belirlenir. E-posta ayarlarından cihaz modülünde yer alan ‘İşlem Yapılacak Cihazlar’’ kimlere gönderilmesi gerektiği seçilerek, güncellenebilir. Bu işlem için![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb8d8e8b7-1f04-4426-bd6c-20f7d044377a)(değiştir) butonu kullanılmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaded63a467-713b-4f02-b9f2-26f34e53a51b)

İlgili roller seçilmek için E-Posta Gitsin mi? check box’ ı işaretlenir. Giden e-postada yazan mail içeriği Kullanılacak Mesaj Gövdesi alanından ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload55d9c608-5513-4b17-a797-ad91235912f2)(seç) butonuyla seçilir, yanlış eklenen bir mesaj gövdesini silmek içinse ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload93a0e62c-0bab-40d2-9696-52e6a65ea09f)(sil) butonu kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload49642256-f568-415d-b0d4-8a8f74a44c62)

Değişiklikler yapıldıktan sonra E-posta ayarlarını kaydetmek için sağ üstte yer alan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload97a8968d-2f41-4211-a2d9-26611a61f3b9)(kaydet) butonu kullanılır. Hiçbir değişiklik yapmadan çıkmak için ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0e4665e7-a76e-4a4a-a93e-ed7682a4388b)(geri) butonu kullanılır.

Ayrıca gecikme mailleri gönderilmesi ile ilgili parametrelere Sistem Altyapı Tanımları/ Cihaz Yönetim Sistemi/ Cihaz Yönetimi Parametreleri menüsünden ulaşılabilir. Örneğin; **20 nolu parametre:** Gecikme mailleri gönderilsin mi? (E/H) E: evet, H: hayır anlamında kullanılır.

**21 nolu parametre:** Gecikme mailleri gönderilmeyecek üstler (birden fazla kullanıcı ise sicil numaralarını virgül ile ayırarak yazınız) vb. örnek verilebilir.

**6.1.6.Cihaz Kodu Değiştirme**

**Menü Adı:** Sistem Altyapı Tanımları / Cihaz Yönetim Sistemi/ Cihaz Kodu Değiştirme

Sistemde bulunan cihazların kodunu değiştirme işleminin gerçekleştiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5e678ea2-1ffc-48dc-8701-8e3abf3f99d5)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Cihaz kodu:** Eski cihaz kodu bilgisi girilir.

**Yeni Kod:** Yeni cihaz kodu bilgisi girilir.

Açılan ekranda cihazın eski kod bilgisi ve cihazın yeni kod bilgisi girilir.

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload822250b9-55f0-468b-8e26-8524e5297bd3) (kaydet) butonu tıklanarak cihaz kodu değiştirme kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc0ebd94b-ba1e-42bc-a835-0001ea414ad9)

### **6.1.7.Cihaz Bakım**

**Menü Adı:** Sistem Altyapı Tanımları/ Cihaz Yönetim Sistemi/ Cihaz Bakım

Cihazların belirli bilgilerinin toplu olarak değiştirilmesi işleminin gerçekleştirildiği menüdür.

Bu menü ile tüm cihazların bilgileri istenildiğinde kolay olarak değiştirilebilir.

**Cihaz Bilgileri Güncelle:** Cihaz bilgileri güncelleme işlemi gerçekleştirilir. Cihaz bakım ekranı açıldıktan sonra filtre ekranında istenen filtreleme yapıldıktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadea5baa53-ac9c-4e26-83e7-ccf04ba88a5f) (Ara) butonuna basılarak cihazlar listelenir. Değişiklik yapılması istenen cihazlar seçildikten sonra (Tümünü seç ile ilgili check box’ı işaretlenerek listelenen tüm cihazlar da seçilebilir.). Cihaz bilgileri güncellemede cihaz sorumlusu, cihaz kategorisi, cihazın yeri, durum ve cihazın adı alanlar sistemde tanımlı listeden seçilerek değişiklik ve güncelleme işlemi yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6de16187-0a40-4b37-8bde-2740712feedc)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Cihazın Sorumlusu:** Cihazın sorumlusunun sistemde tanımlı pozisyon listesinden seçilir.

**Cihazın Kategorisi:** Cihazın kategorisinin sistemde tanımlı kategori listesinden seçilir.

**Cihazın Yeri:** Cihazın yeri sistemde tanımlı şirket profili listesinden seçilir.

**Durum:** Cihazın durumu hurda veya kullanımda seçilebilir.

**Cihazın Adı:** Cihazın adı bilgisi girilir.

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload822250b9-55f0-468b-8e26-8524e5297bd3) (kaydet) butonu tıklanarak cihaz bakım kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9a290d9a-1783-46f9-929e-bc29a3a25eea)

**İşlem Tipi bilgilerini güncelleme:** İşlem tipi bilgileri güncelleme işlemi gerçekleştirilir. Var olan işlem tipini günceller. Cihaz bakım ekranı açıldıktan sonra filtre ekranında istenen filtreleme yapıldıktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadea5baa53-ac9c-4e26-83e7-ccf04ba88a5f) (Ara) butonuna basılarak cihazlar listelenir. Değişiklik yapılması istenilen cihazlar seçildikten sonra (Tümünü seç ile ilgili check box’ı işaretlenerek listelenen tüm cihazlar da seçilebilir.) işlem tipi bilgilerini güncellemede periyot, işlem sorumlusu ve işlem politikası alanlar sistemde tanımlı listeden seçilerek değişiklik ve güncelleme işlemi yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada450fdd7-5109-46dd-8fa2-aa53675af39f)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Periyod:** Periyod bilgisinin girilir.

**İşlem Sorumlusu:** İşlem sorumlusu sistemde tanımlı pozisyon seçme listesinden seçilebilir.

**İşlem Politikası:** İşlem politikasının; işlem içerde yapılır, işlem dışarda yapılır, işlem hem içerde hem dışarda yapılır ve işlem periyodik olarak takip edilmez seçenekleri seçilebilir.

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload822250b9-55f0-468b-8e26-8524e5297bd3) (kaydet) butonu tıklanarak cihaz bakım kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc5f28f3e-bdd2-4c9c-8f1c-374eac91e5c9)

**İşlem Tipi bilgilerini güncelleme/ekle:** Yeni bir işlem tipi eklemek için kullanılır. İşlem Tipi, periyod, İşlem Sorumlusu, İşlem Politikası, Son işlem Tarihi ve Gelecek işlem Tarihi alanlarını bilgisi eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7b5a2f05-3856-4890-8db5-93b78903a234)

**Açılan ekranda ilgili alanlar tanımlanır:**

**İşlem Tipi:** İşlem tipi sistemde tanımlı işlem listesinden seçilebilir.

**Periyod:** Periyod bilgisi girilir.

**İşlem Sorumlusu:** İşlem sorumlusu sistemde tanımlı pozisyon listesinden seçilebilir.

**İşlem Politikası:** İşlem politikasının; işlem içerde yapılır, işlem dışarda yapılır, işlem hem içerde hem dışarda yapılır ve işlem periyodik olarak takip edilmez seçenekleri seçilebilir.

**Son İşlem Tarihi:** Son işlem tarihi seçilebilir.

**Gelecek İşlem Tarihi:** Gelecek işlem tarihi bilgisi seçilebilir.

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload822250b9-55f0-468b-8e26-8524e5297bd3) (kaydet) butonu tıklanarak cihaz bakım kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf69ee8e2-07e6-4aee-b8c7-27876d2b58c3)

### **6.1.8.Çoklu Cihaz Kodu Değiştirme**

**Menü Adı:** Sistem Altyapı Tanımları/ Cihaz Yönetim Sistemi/ Çoklu Cihaz Kodu Değiştirme

Cihaz kodlarının çoklu bir şekilde değiştirme işleminin gerçekleştiği menüdür. Cihaz Kodlarının çoklu bir şekilde değiştirme işlemi Bimser Destek Sistemi tarafından yapılmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd084334a-f8aa-4b20-b1b1-6aa6ee83d3e2)

### **6.1.9.Cihaz Yönetimi Parametreleri**

**Menü Adı:** Sistem Altyapı Tanımları/ Cihaz Yönetim Sistemi/ Cihaz Yönetimi Parametreleri

Cihaz Yönetimi Modülünün kullanıcının istek ve ihtiyaçlarına göre sistemsel ayarlarının yapıldığı ve bunlara göre parametreleri belirlendiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3e06f9d-ce05-45fe-9925-94821cdf78ce)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7f13c7de-793b-4928-af2e-5e380513372e) :Listede seçili parametre güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3078baed-d974-4206-af19-eb7daa035bcf) : Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5347290e-ea27-4cef-9e23-eb81fac0223f) : Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload11d32490-e0be-4b80-8d41-59e9927ccdcc)

Parametreler ekranında listede seçili parametrenin parametre değeri “Evet” seçilerek Aktif edilme işlemi veya parametre değeri “Hayır” seçilerek pasif edilme işlemi yapılır. Ayrıca listede seçili parametre değeri bilgisi girilir veya parametre değeri tanımlı olan parametrenin değeri değiştirme işlemleri yapılır. Bu işlemlerin yapılması için parametreler ekranında parametre seçili iken ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7f13c7de-793b-4928-af2e-5e380513372e)(Değiştir) butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddbaa6ddc-a805-4679-ab83-d3ca5fe2a8dd)

Açılan parametreler ekranında parametrenin değeri “Evet” seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload10c52682-f215-4a5b-b500-70de5a0ca4fa)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload822250b9-55f0-468b-8e26-8524e5297bd3)(Kaydet) butonu tıklanarak parametre aktif edilme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f32770b-cf3e-45a5-8e92-2d526a16b757)

Diğer işlemler içinde parametre seçili iken ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7f13c7de-793b-4928-af2e-5e380513372e)(Değiştir) butonu tıklanarak yapılır.

### **6.1.10.Cihaz Silici**

**Menü Adı:** Sistem Altyapı Tanımları/ Cihaz Yönetim Sistemi/ Cihaz Silici

Sistemden cihaz silme işleminin gerçekleştiği menüdür. Cihazların kullanılmamak üzere sistemden silinmesini sağlamaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload069fda23-84e5-4bd8-b152-0beb99e0bfc7)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8c67a226-429d-4832-bd18-4c5df89e2018): Listede seçili cihazı siler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3078baed-d974-4206-af19-eb7daa035bcf) : Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f2efd50-c4fe-483b-8f56-4bfcd3599e3b)

Silinmek istenen cihaz seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5e900fda-57a4-46c7-bcdc-77828767aac4) (Sil) butonu tıklanarak Cihaz Silme işlemi gerçekleştirilir.

## **6.2.Entegre Yönetim Sistemi/ Cihaz Yönetim Sistemi**

Cihaz Sistemi Yönetimi Modülün Cihaz tanımlama, İşlem Gerçekleştirme, İşlem Tarihçesi menüleri gerçekleştirme ve raporlarının görüntülendiği kısımdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload738d1ac8-de4f-4fdf-a381-7b26ad150dd2)

### **6.2.1.Cihaz Tanımlama**

**Menü Adı:** Entegre Yönetim Sistemi/ Cihaz Yönetim Sistemi/ Cihaz Tanımlama

Bu ekranda tanımlanan cihazların listesi bulunmaktadır. Cihaz tanımlama menüsünde listelenen cihazlarının durumu kullanımda olanlar mavi renk olarak görüntülenir. Sistem Altyapı Tanımları/Cihaz Yönetim Sistemi/Durum Tanımlama menüsünde Cihazların durumların tanımlama işlemin yapıldığı ekranda Renk alanında Kullanımda, hurda gibi durumlarda Cihazların renkleri bu menüde belirlenir. Sistemde “kullanımda” durumundaki cihazın rengi Mavi olarak DurumTanımlama menüsünde tanımlanmış ve Cihaz listesinde mavi renkte görüntülenmesi sağlanmıştır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd991b749-29fb-48d0-a9ea-30ab6b17789d)

Filtre sekmesinde durum alanı hurda olarak seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadea5baa53-ac9c-4e26-83e7-ccf04ba88a5f) ara butonu tıklanarak hurda olan cihazlar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc6017e42-77c8-49ed-a729-5deed347dffc)

Cihaz Tanımlama menüsünde listelenen Cihazlarının Durumu “Hurda” olanlar kırmızı renk olarak görüntülenir. Sistemde “Hurda” durumundaki cihazın rengi Kırmızı olarak Durum Tanımlama menüsünde tanımlanmış ve Cihaz listesinde Kırmızı renkte görüntülenmesi sağlanmıştır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload277b67a5-7f93-4cf8-83df-63028d93d5b2)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca15a7d2-1419-4522-914a-7801ed2f5de5) : Yeni cihaz ekler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload79914dab-c463-4b76-a0c4-c0c960f196a2) : Listede seçili cihaz bilgilerini güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5e900fda-57a4-46c7-bcdc-77828767aac4): Listede seçili cihazı listeden siler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload569fbec7-d061-4676-9685-1d8b855bedd6): Seçili cihazın kopyalanarak yeni bir cihaz oluşturmak için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9eafdb16-afcc-4c90-9ac8-040eb33a33c6): Seçili cihazın ölçüm sabitleri ekranını gösterir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload91f1e56b-654b-4ddf-94f6-7596f8c461a9): Seçili cihaz için tanımlanmış işlem tiplerinin bulunduğu ekranı açar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload932e6e9b-29ed-476b-8fd1-7e76a952e5ae) : Seçili cihaz üzerinde yapılmış işlemlerin tarihçesini gösterir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadea5baa53-ac9c-4e26-83e7-ccf04ba88a5f) : Belirlenen filtreleme kriterlerine göre cihaz listesi içinde arama yapar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadccb5c492-6079-4825-9253-59b5f659ce35) : Cihaz listesini Excel’e aktarır.

**Cihazların toplu bir şekilde sisteme aktarımı istenilirse;**

**Menü Adı:** Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Aktarımlar/ Cihaz Aktarma

Cihaz aktarım işleminin gerçekleştiği menüdür. Cihaz Yönetimi modülünde işlem yapılan cihazların toplu olarak sisteme aktarımının gerçekleştirilmesi isteniyorsa “Cihaz Aktarma” menüsü kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5b5cd054-1355-45eb-8068-4fbe94050ac2)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload19d3cb60-1f64-4e5d-96d5-85fd99cb8798) : İlgili şablon bilgisayara indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf3743a20-28a6-4d87-be1d-f950ca450dc1) : Doldurulan şablon sisteme yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload820750d6-8117-4061-b0e0-736c0c4ec196): Oluşturulan ve sisteme yüklenen şablonun hata verip vermediğine dair kontrol amacıyla kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload03b05495-6e12-44d5-89fb-323a42cdf171): Aktarım işlemi gerçekleştirilir.

Ekran üzerinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload19d3cb60-1f64-4e5d-96d5-85fd99cb8798) (şablon indir) butonu ile şablon indirilir, gerekli bilgiler doldurulduktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf3743a20-28a6-4d87-be1d-f950ca450dc1) (şablon yükle) butonu ile sisteme yüklenir. Girilen bilgilerin kontrolünün sağlanması için, ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload820750d6-8117-4061-b0e0-736c0c4ec196) (kontrol et) butonu kullanılır. Aktarılan veriler aktarım için uygunsa ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload03b05495-6e12-44d5-89fb-323a42cdf171) (aktar) butonu aracılığıyla aktarım gerçekleşmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload368e291d-695a-414b-9601-12c3f08ca993)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload19d3cb60-1f64-4e5d-96d5-85fd99cb8798) Şablon indir butonu ile İlgili şablon bilgisayara indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbd71ab43-9de1-4358-99cf-1e6973f56b04)

**Cihaz aktarma açılan şablonda ilgili alanlar tanımlanır;**

**Cihaz Kodu:** Aktarım yapılacak Cihazın sistemde tanımlı olmayan kod bilgisinin Cihaz aktarma şablonuna yazıldığı zorunlu alandır. Numerik ve alphanumerik kod bilgisi girilir.

**Cihaz Adı:**Aktarım yapılacak Cihazın adı bilgisinin cihaz aktarma şablonuna yazıldığı alandır.

**Cihaz Kategorisi:** Aktarım yapılacak Cihazın cihaz kategorisi Sistem Altyapı Tanımları/Cihaz Yönetimi Sistemi\>Cihaz Kategori Tanımlama menüsünde tanımlı kod bilgisinin Cihaz aktarma şablonuna yazıldığı alandır.

**Sertifika No:** Aktarım yapılacak Cihazın varsa son işlem yapılmış sertifika bilgisinin Cihaz aktarma şablonuna yazıldığı alandır.

**Modeli:** Aktarım yapılacak Cihazın model bilgisinin Cihaz aktarma şablonuna yazıldığı alandır.

**Seri No:** Aktarım yapılacak Cihazın seri no bilgisinin Cihaz aktarma şablonuna yazıldığı alandır.

**Markası:** Aktarım yapılacak Cihazın marka bilgisinin Cihaz aktarma şablonuna yazıldığı alandır.

**Cihazın Yeri:** Aktarım yapılacak Cihazın cihaz yeri Sistem Altyapı Tanımları/BSAT/Tanımlar/Şirket Profili Tanımlama menüsünde tanımlı cihazın yerinin kod bilgisinin Cihaz aktarma şablonuna yazıldığı alandır.

**Cihaz Sorumlusu:** Aktarım yapılacak Cihazın sorumlusu Sistem Altyapı Tanımları/BSAT/Tanımalar/Pozisyon Tanımlama menüsünde tanımlı cihazın sorumlusunu kod bilgisinin Cihaz aktarma şablonuna yazıldığı alandır.

**Durum:** Aktarım yapılacak Cihazın durumu Sistem Altyapı Tanımları/Cihaz Yönetimi Sistemi\>Durum Tanımlama menüsünde tanımlı Durum kod bilgisinin Cihaz aktarma şablonuna yazıldığı alandır.

**Cihaz Yeri Açıklaması:** Aktarım yapılacak Cihazın cihaz yeri bilgisinin Cihaz aktarma şablonuna yazıldığı alandır.

**Tolerans Değer:** Aktarım yapılacak Cihazın tolerans değer bilgisinin Cihaz aktarma şablonuna yazıldığı alandır.

**Cihaz Maliyeti:** Aktarım yapılacak Cihazın cihazın maliyet bilgisinin Cihaz aktarma şablonuna yazıldığı alandır.

Periyot-Son İşlem Tarihi ve Ölçüm Sabitleri sekmelerinde alanların şablondaki açıklamalar dikkate alınarak doldurulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada19f85bf-bbea-48d1-8c8b-ba5aa2bd51eb)

Cihaz Aktarım Şablonu doldurularak kaydedilir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf3743a20-28a6-4d87-be1d-f950ca450dc1) Şablon yükle butonu ile doldurulan şablon sisteme yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f98e6a0-2099-4ad9-8199-876d05549558)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload287cd91a-ed5b-4801-a5b4-5f3b013d14e2)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada3855d98-1c25-4c12-be38-061f9d9195bc)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada8ed43a4-f29e-48b3-b496-9c7390c2e60a) Kontrol et butonu tıklanarak Oluşturulan ve sisteme yüklenen şablonun hata verip vermediğine kontrol edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8a648732-9366-46fc-9b6f-e1ecda77f39c)

Sistemde “Veriler aktarım işlemine uygun” mesajı alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload101c725d-4dc6-4d68-886c-45a242977132)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload03b05495-6e12-44d5-89fb-323a42cdf171) (Aktar) butonu tıklanarak Cihaz Aktarma işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4a1c775c-aa02-4b5e-92f5-7ae9402911f8)

Cihaz aktarma işleminin başarıyla aktarıldığı ve aktarılan Cihaz sayısının bilgisinin sistemde tarafında verildiği görülür. Aktarılma işlemi yapılan Cihazlar Entegre Yönetim Sistemi\> Cihaz Yönetim Sistemi\>Cihaz Tanımlama menüsünde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload45fda0e8-0962-48a7-940a-f9419136a9f5)

Listeye yeni bir cihaz eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4bed12f5-5517-4ef2-b2b1-ee881cfd6d30) (yeni) butonu tıklanarak Cihaz Tanımlama/ Yeni Kayıt ekranı görüntülenir.

**Cihaz Bilgileri Sekmesi:** Cihaz hakkında genel bilgilerin yer aldığı sekmedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8a9f0cfa-84a0-42ed-902c-234eb59c154c)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Cihaz Kodu:** Cihaz kod bilgisi sistem tarafından otomatik verilir. Cihaz kodunun sistem tarafından otomatik verilmesi için Sistem Altyapı Tanımları/Cihaz Yönetim Sistemi/Cihaz Yönetim Sistemi Parametrelerinde 7 numaralı “Cihaz Kodu otomatik verilsin mı?(E/H)” parametre seçili iken ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7f13c7de-793b-4928-af2e-5e380513372e)(Değiştir) botunu tıklanarak parametre değeri “Evet” seçilerek parametre aktif edilir. Parametre aktif edildikten sonra sistem tarafından Cihaz Tanımlama ekranında cihaz kodları otomatik verilir. Parametre değeri “Hayır” seçilerek parametre pasif edildiğinde cihaz tanımlama ekranında kodlar manuel olarak bilgisi girilir.

**Cihazın Kategorisi:** Cihazın kategorisi; Sistem Alt Yapı Tanımları/ Cihaz Yönetimi/ Cihaz Kategorileri menüsünde tanımlanmış olan cihazların listesi gelmektedir. Kategori listesinden seçilir.

**Adı:** Cihazın adının bilgisi girilir.

**Model:** Cihazın model bilgisi girilir.

**Seri No:** Cihazın seri no bilgisi girilir.

**Cihazın Sorumlusu:** Cihazın sorumlusu sistemde tanımlı olan pozisyon listesinden seçilebilir. Pozisyon belirleyerek cihaz üzerinde değişiklik yapacak kişiyi belirliyoruz.

**Cihaz Yeri:** Cihazın yeri sistemde tanımlı olan şirket profilinden seçilir.

**Cihaz Yeri Açıklaması:** Cihaz yeri açıklaması bilgisi girilir.

**Durum:** Sistem Alt Yapı Tanımları/ Cihaz Yönetimi/ Durum Tanımlama menüsünden tanımlanmış olan durumların listeden seçildiği alandır. Cihazın hurda veya kullanımda olması durumu seçilebilir.

**Durumun Gerçekleştiği Tarih:** Cihazın durumunun gerçekleştiği tarih belirlenir.

**Tolerans Değer:** Cihazın tolerans değerinin bilgisi girilir.

Cihaz bilgileri sekmesinde cihaz kategorisi, adı, marka, model, cihaz sorumlusu gibi alanlar bulunmaktadır. Cihaz Kodu alanı boş bırakılır, sistem otomatik olarak kendisi kod üretir. Cihaz Kategorisi açılır menüsünden önceden tanımlanan kategorilerden biri seçilir. Cihaz Sorumlusu olarak da açılan listeden sorumlu seçilir.

Burada belirlenen Tolerans Değer yüzdesine göre, Ölçüm sabitlerinde kabul alt ve kabul üst aralıkları otomatik olarak atanır. Standart Değer 100 ve Tolerans değer %3 olduğu varsayılırsa, Kabul Üst Aralığı 103, Kabul Alt Aralığı ise 97 olarak atanır.

**Diğer Bilgiler sekmesi:** Cihaza özel tanımlanmış parametrik alanlar varsa bunların yer aldığı sekmedir. Ayrıca cihazın maliyet bilgisi ve cihaz ile ilgili eklenmek istenen notlar gibi bilgiler girilebilir. Parametrik alanlar; Sistem Altyapı Tanımları/BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsünden oluşturulabilir.Açılan Dil Ayarların menüsünde Modül olarak CihaYönetim Sistemi modülü seçilir. Modülü Cihaz Yönetim Sistemi seçildikten sonra Cihaz Yönetim Sisteminde tanımlanacak Pasif parametrik alan tipleri görüntülenir. Bu pasif parametrik alanlardan metin, metin(çoklu satır), liste, gibi parametrik tipli alanların tanımlanıp Diğer bilgiler sekmesinde görüntülenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload539f3f41-d8a4-4b35-a987-b3d96ef388fa)

**Açılan ekranda otomatik gelen ilgili alanlar tanımlanır:**

**Cihazın Maliyeti:** Cihazın maliyet bilgisi girilir.

**Notlar:** Cihaz ile ilgili bilgilerin not olarak bilgisi girilir.

**Ek Dosyalar sekmesi:** Cihaz ile ilgili eklenmek istenen doküman, resim vb. dosya varsa eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9c835b16-134c-4639-b429-e83d8a8cc2be)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6402f0e3-25b8-4051-86a1-47312daa0a5a): Ek dosya yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade98def70-437d-492c-b95b-b6776bda96c2):Listeye eklenen Ek dosyayı görüntüler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8a03e010-962a-48d9-b14f-29a089011a41):Listeye eklenen Ek dosya silebilir.

Gerekli tüm alan bilgileri girildikten sonra, ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf092494a-736e-404a-b4ff-1e03b4264a9b) (Kaydet) butonu tıklanarak Cihaz Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload709b6aae-c7ad-4aa6-950e-f450f77ab32b)

Tanımlanan cihaz satırı seçili iken, ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f7e6c7d-11b6-4dea-a1d2-1760ff1e3f5b) ( ölçüm sabitleri ) butonu tıklanırsa, seçili cihazın ölçüm sabitlerinin girileceği ekran görüntülenir. Açılan yeni ekranda cihaz için önceden tanımlanan ölçüm sabitleri görülebilir, güncellenebilir, silinebilir, istenirse yeni ölçüm sabitleri tanımlanabilir ve ölçü birimi belirlenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb0cb4e1c-161b-419e-aba8-32a31efba97e)

Listeye yeni bir Ölçüm Sabiti eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4bed12f5-5517-4ef2-b2b1-ee881cfd6d30)(yeni) butonu tıklanarak Ölçüm Sabitleri/ Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7d7f6f33-10c2-4671-a756-f2f71b940569)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Tanım:** Ölçüm sabitlerinin tanım bilgisinin girilir.

**Ölçüm Birimi:** Ölçüm sabitlerinin ölçüm birimi bilgisi seçilebilir.

**Referans Değer:** Ölçüm sabitlerinin referans değer bilgisi girilir.

**Standart Değer:** Ölçüm sabitlerinin standart değer bilgisi girilir.

**Kabul Aralığı Alt:** Ölçüm sabitlerinin kabul aralığı alt bilgisi girilir.

**Kabul Aralığı Üst:** Ölçüm sabitlerinin kabul aralığı üst bilgisi girilir.

Referans, standart değerler ile kabul alt ve üst aralıkları bilgileri girilebilir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7ee40c20-97ca-4393-ae70-5c4398881caa) Kaydet butonuyla girilen değerler kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload88d39028-65ac-428b-89e2-8131d5983d2f)

Bir cihaza istenildiği kadar ölçüm sabiti tanımlanabilir. Ölçüm sabitleri ekranındaki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8f0d3320-9508-4b17-9de4-f9d577d1f33c) (ölçüm birimi tanımlama) butonu ile ölçü birimi tanımlanabilir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9534736d-ade6-40e0-9856-d091624c161b) (Ölçüm birimi tanımlama) butonu tıklanıp yeni ölçüm birimi tanımlama ekranına gelindiğinde, ölçüm sabitleri için birimler tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada3fb0a86-dca8-469d-9869-557b7ec63128)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Referans Değer Birimi:** Ölçü Birimi Referans Değer Birimi bilgisi girilir.

**Standart Değer Birimi:** Ölçü Birimi Standart Değer Birimi bilgisi girilir.

Bu ekranda referans ve standart ölçüm sabitleri için, referans ve standart ölçüm birimleri girilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload822250b9-55f0-468b-8e26-8524e5297bd3) ( kaydet) butonu ile birimler kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload578fd377-f5e3-4f22-b4e8-f1532a560328)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload92c3cf35-2b9e-4a1b-965a-562af1c4ce81)

Cihaz listesi ekranındaki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada7f3512e-a196-4124-8c2a-9c5653c20f94) (işlem tipleri) butonuyla tanımlanmış işlem tiplerinden biri ya da birkaçı seçilen cihaza atanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8838078a-11c8-4476-8bb9-69b634847004)

Açılan ekranda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca15a7d2-1419-4522-914a-7801ed2f5de5) (Yeni) butonuna basılarak cihaza yeni işlem tipi tanımlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload358656fe-8e99-4834-8d89-1de95e3c6ff1)

**Açılan ekranda ilgili alanlar tanımlanır:**

**İşlem Tipi:** Cihaza ait işlem tipleri Sistem Alt Yapı Tanımları/ Cihaz Yönetimi/ İşlem Tipleri Tanımlama menüsünden tanımlanan listeden seçilebilir.

**Periyod:** Cihaza ait işlem tiplerinin periyod bilgisi girilir. Cihaz yönetimi sistemi modülü 10.Parametrede kalibrasyon periyodu(G)ün, (A)y parametre değerine G harfi yazılırsa Gün olarak, A harfi yazılırsa Ay olarak kalibrasyon periyodu belirlenir. Örnekte 12 günde bir kalibrasyon yapabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload93bd5dc0-6efb-48db-ac20-db0de27d486e)

**Ön Bildirim Süresi(Gün):** Cihaza ait işlem tiplerinin ön bildirim süresi Gün olarak bilgisi girilir.

**İşlem Sorumlusu:** Cihaza ait işlem tiplerinin İşlem sorumlusu sistemde tanımlı olan pozisyon listesinden seçilebilir.

**İşlem Politikası:** Cihaza ait işlem tipleri işlem politikasının seçilebildiği alandır. Seçilebilen İşlem Politikaları;

İşlem içerde yapılır, İşlem dışarda yapılır, İşlem hem içerde hem dışarda yapılır ve İşlem periyodik olarak takip edilmez seçeneklerinden seçilir.

**İşlem Yeri:** Cihaza ait işlem tiplerinin işlem yeri sistemde tanımlı olan şirket profili seç listesinde seçilebilir.

**Son İşlem Tarihi:** Cihaza ait işlem tiplerinin son işlem tarihi bilgisi girilir.

**Gelecek İşlem Tarihi:** Cihaza ait işlem tiplerinin gelecek işlem tarihi bilgisinin sistem periyod bilgisine göre otomatik olarak hesaplayarak belirtir.

**Sertifika No:** Cihaza ait işlem tiplerinin sertifika no bilgisi girilir.

**Sertifika Dosyası:** Cihaza ait işlem tiplerinin Sertifika dosyası sistemden eklenebilir ve görüntülenebilir .

**Durum:** Cihaza ait işlem tiplerinin durum bilgisi aktif veya pasif seçilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload60b19ac6-bb9c-4c9c-b295-e0fd82a56b6b)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload37bde464-e1e4-4c7e-9df0-82697e86ff65)

İşlem tipi menüsünden daha önceden tanımlı işlemlerden biri seçilir. İşlem tipinin periyodu, ön bildirim süresi, işlem sorumlusu, işlem yeri, işlem politikası, son işlem tarihi bilgileri girilir. Sistem periyod bilgisine göre gelecek işlem tarihini otomatik olarak hesaplar. Bir sonraki iş emrini de parametreden aktif hale getirilmişse bu tarihte otomatik olarak açabilir. Bir cihaza istenilen farklı türlerde işlem tipleri eklenebilir. Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload822250b9-55f0-468b-8e26-8524e5297bd3) (kaydet) butonu tıklanarak Cihaza Ait İşlem Tipleri Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload817df091-90c4-423b-bc0a-2319ffcb0d99)

Cihaz listesi ekranında iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaf653d0e-e172-445b-b4d0-d9e2cd1ebc5b) (tarihçe) butonuyla seçili cihazın işlem tarihçesi görüntülenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload16b0429a-89d0-4dac-85ac-38f93e408190)

### **6.2.2.İşlem Gerçekleştirme**

**Menü Adı:** Entegre Yönetim Sistemi/ Cihaz Yönetim Sistemi/ İşlem Gerçekleştirme

Cihaz Yönetimi Modülünde 26 numaralı “iş emirleri günü geldiğinde otomatik olarak açılsın mı” parametresi “evet” olarak seçilirse tüm iş emirleri zamanı geldiğinde otomatik olarak açılacaktır. Parametreyi aktif hale getirmek için, Sistem Altyapı Tanımları/ Konfigürasyon Ayarları/ Parametreler menüsü izlenerek Cihaz Yönetimi parametreleri sayfasına gelinir. Burada ilgili parametre “evet” olarak seçilirse tüm iş emirleri zamanı geldiğinde otomatik olarak açılmaya başlayacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload30192695-457d-4b56-b98c-98b9b5cdb943) Ancak zamanından önce işlem yapmak için manuel olarak da iş emri açmak mümkündür. Manuel olarak iş emri açmak ve otomatik olarak açılan iş emirlerini gerçekleştirmek için Cihaz Yönetimi Modülünün Entegre Yönetim Sistemi menüsü altındaki İşlem Gerçekleştirme menüsüne gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload381bdd0c-91ed-478a-bc39-5213ae021e14)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca15a7d2-1419-4522-914a-7801ed2f5de5) : Yeni iş emri oluşturulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload995e38cb-b0e3-44e6-b7fb-34204b6ab4ae) : Listede seçili iş emri bilgileri güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5e900fda-57a4-46c7-bcdc-77828767aac4) : Listede seçili iş emri bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadedcfee4a-c883-4ced-9b2d-197e2f1cefdd): Cihaz bilgileri ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload51efc583-f1a5-43db-9ee3-36b5001f577d) : Kalibrasyon Raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaf3dd6cb-1910-4efb-8e06-6b96f0bc434a): Belirlenen filtrelere göre iş emirleri arasında filtreleme yapılır.

Listeye yeni iş emri eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4bed12f5-5517-4ef2-b2b1-ee881cfd6d30) (yeni) butonu tıklanarak İş emri Listesi/ Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6222db99-9809-425f-bc10-09dc043026bd)

**Açılan ekranda ilgili alanlar tanımlanır:**

**İşlem Tipi:** İşlem tipi sistemde tanımlı olan işlem tipi listesinden seçilir.

**İşlem Yapılacak Cihazlar:** İşlem yapılacak cihazlar, işlem yapılacak cihazların listesinden seçilir.

**İşlem Sorumlusu:** İşlem sorumlusu sistemde tanımlı olan pozisyon listesinden seçilir. İşlem sorumlusu cihazın kalibrasyonunu, doğrulamasını ya da bakım işlemlerini gerçekleştirmekle sorumlu olan personeldir.

**Planlanan İşlem Tarihi:** Planlanan işlem tarihi belirlenir.

**İşlem Yeri Tipi:** İşlem yeri tipi iç veya dış olarak seçilir.

**İşlem Yeri:** İşlem yeri BSAT/ Tanımlar/ Şirket Profili Tanımlama menüsünde tanımlanmış olan şirket profili listesinden seçilir. İstenirse 47. parametreye göre; İşlem gerçekleştirme listesinde işlem yeri yerine cihaz yeri gösterilsin? Parametresiyle cihaz yerinin gösterilmesi sağlanır.

**İş Yeri Açıklaması:** İş yeri açıklaması bilgisi girilir.

**Notlar:** İş emri listesinin not bilgisinin girilir.

İşlem tipi, İşlem yapılacak cihazlar, İşlem sorumlusu gibi alanlar bulunur. İşlem tipi alanı seçildiğinde, önceden tanımlanan işlem tipleri ağacı ekrana gelir, buradan istenen işlem tipi seçilir. İşlem yapılacak cihazlar alanı tıklandığında ise o an o işleme uygun olan cihazların listesi ekrana gelir, uygun olan cihaz seçilir. İşlem sorumlusu, işlem tarihi, işlemin yapıldığı yer (iç/dış), işlem yeri açıklaması gibi bilgiler girilir. Bu bilgiler girildikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5eb5737f-1712-4c71-92a3-13e6bba3fc2d) (kaydet) butonuyla iş emri kaydedilmiş ve işlem sorumlusu olan kişiye atanmış olur. Ayrıca 16. parametreye göre; İş emirlerinde İşlem Yapma Yetkisi Olanlar (I) İşlem Sorumlusu, (C) Cihaz Sorumlusu (Virgül ile ayırarak yazınız) istenirse cihaz sorumlusuna da verilebilir..

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada70131ab-2f8d-4523-8e28-66626618fe6a)

İşlem zamanı yaklaştığı zaman parametrelerde belirlenen gün sayısı kadar önce (25. parametre: İş emirleri kaç gün önce haber verilsin (İçerde yapılan), 27. Parametre: İş emirleri kaç gün önce haber verilsin (Dışarda yapılan) ayarlanarak) cihaz sorumlusuna ve işlem sorumlusuna hatırlatma maili gidecektir ve işlem sorumlusunun **Bekleyen İşlerim** ekranında **İşlem Yapılacak Cihazlar** şeklinde bir sekme belirecektir. Planlanan İşlem tarihine dek bu iş emri gerçekleştirilmelidir, aksi takdirde gecikme mailleri gönderilmeye başlanır. Bekleyen işlerim ekranında gecikmiş işler kırmızı renkte, planlanan bitiş tarihi henüz gelmemiş olan işler ise sarı renkte görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload434e8ea3-3c71-4f19-b743-95d8f775ea69)

İşlem Sorumlusu, cihaz koduna tıklayarak iş emri listesi ekranına yönlenecektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9042cc37-8873-4930-a97a-03d8da2fc444)

Listede iş emri seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9292b772-f93b-4959-af39-0eee3c62b0b4) (kalibrasyon raporu) butonuna basılarak iş emri raporunun yazılacağı ekrana gelinir. Bu sayfa 3 sekmeden oluşur;

**Ölçüm Değerleri Sekmesi;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload12d2b0f3-8a56-494b-9a49-8727a1cca082)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload93721e47-11cf-4e41-9d62-61afeb5e9f99) Yeni botunu tıklanıp yeni ölçüm değerleri tanımlama ekranına görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload90c91a20-d50c-452f-9964-574a5d6ae6dd)

Daha önceden belirlenmiş ölçüm sabitleri varsa, ölçüm değeri tanımı, ölçü birimi, referans değer, standart değer, kabul alt aralığı ve kabul üst aralığı dolu olarak gelir. Yalnızca ölçülen değer yazılarak, sistem sapma ve hata oranını hesapladıktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload822250b9-55f0-468b-8e26-8524e5297bd3) (kaydet) butonu ile değerler kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec24e861-4541-4486-98a6-adbeb7fd51e7)

Ölçüm değerleri sekmesinde Standart değer Kabul aralığı alt ve Kabul aralığı üst aralığında değilse sapma gösterir. Ölçüm Değerleri ekranda renk olarak kırmızı renkte görünür. Ölçüm değerleri sekmesinde Standart değer Kabul aralığı alt ve Kabul aralığı üst aralığında ise sapma göstermez. Ölçüm Değerleri ekranında renk olarak yeşil renkte görünür. Örnekte olduğu gibi.

**İşlemler Sekmesi;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8f01363a-6bc9-4a9f-9c1f-d5f635ba0059)

**Açılan ekranda ilgili alanlar tanımlanır:**

**İşlem Tarihi:** Cihazın işlem tarihi bilgisi belirlenir.

**Sertifika No:** Cihazın sertifika no’su bilgisi girilir.

**İşlem Maliyeti:** Cihazın işlem maliyeti ve biriminin bilgisi girilir.

**Cihaza Yönelik İşlem:** Cihaza yönelik işlem bilgisi seçilir.

**Cihaza Yönelik İşlem Açıklaması:** Cihaza yönelik işlem açıklaması bilgisi girilir.

**Kalibrasyon Nedeni:** Kalibrasyon nedeni bilgisi girilir.

Cihaza yönelik yapılan işlemlerle ilgili işlem tarihi, sertifika numarası, işlem maliyeti, cihaza yönelik işlemler, cihaza yönelik işlem açıklamaları belirtilir.

**Ek Dosyalar Sekmesi;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5057e4f3-dc22-429c-8f0f-50bc85a44b04)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6402f0e3-25b8-4051-86a1-47312daa0a5a): Ek dosya yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade98def70-437d-492c-b95b-b6776bda96c2):Listeye eklenen Ek dosyayı görüntüler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8a03e010-962a-48d9-b14f-29a089011a41):Listeye eklenen Ek dosyayı silebilir.

Açılan ekranda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6402f0e3-25b8-4051-86a1-47312daa0a5a)Dosya yükle butonu tıklanarak cihaza yapılan işlemlere ait ölçüm raporları, sertifika gibi varsa ek dosyalar sisteme yüklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadef7fccff-d629-4200-b376-eac169cd0c33)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfd4cd146-8222-438d-8af4-f8a719ef2d5c) : Var olan şekliyle raporları kaydeder.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb0fc00bf-d9e0-44a2-a2fb-05c3b9fb44a7) : Kalibrasyon Raporu hazırlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcf718522-66a7-4907-ad96-096c31d9ce92) : Manuel olarak işlem raporu yükler. ( İsteğe bağlı )

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2eb3f87b-f168-4ad3-9301-c172d6b28e3f) : İş emrini kapatır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload01841fb5-b9a4-4655-8c45-8c2ccafc3b2f) : İş emrini yayınlar ve kapatır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6428e013-eff3-4864-9262-a3e6a17a28ec) : Bir önceki sayfaya döndürür.

İşlem Raporu ekranında, ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade2e15c05-d674-4b30-9b50-440c172a7e6f) (Kalibrasyon raporu hazırla) butonu tıklanarak Kalibrasyon Raporu hazırlanır. İşlem Raporu’nun oluşturulduğuna dair mesaj ekranı çıktıktan sonra, İşlem Raporu görüntülenebilir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7fbdb89d-3490-4190-8033-11fb68b2beaf)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8eb655fc-c0c2-4ab6-b956-b8d15dc5ce54)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfd4cd146-8222-438d-8af4-f8a719ef2d5c):Kaydet.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload91891dcc-e605-48d3-a119-2acac6544b5f):Rapor hazırlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload154d7ed8-ae95-490a-9365-b29034942f34):Raporu hazırladıktan sonra güncellenen bilgilere göre eski raporu silip tekrar rapor oluşturur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload65ab0c37-cda3-4932-91a2-fbc4d4178d46):Dışardan sisteme Rapor yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb0c2483f-22dc-45b9-a822-0001d2161803):Rapor görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadde103605-c3b1-4291-a17e-97f2163d4927):Kapat ve bir sonraki iş emrine geçme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2eb3f87b-f168-4ad3-9301-c172d6b28e3f) : İş emrini kapatır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload01841fb5-b9a4-4655-8c45-8c2ccafc3b2f) : İş emrini yayınlar ve kapatır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb0c2483f-22dc-45b9-a822-0001d2161803)Raporu görüntüle butonu tıklanarak Excel Formatında Rapor görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7e9dcf07-df1c-439b-8b15-49b520a9abbf)![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload41071125-c320-4853-8a44-6658af275004)

Rapor oluşturulduktan/yüklendikten sonra ise iş emrini kapatmak için iki buton bulunmaktadır. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload01d834fe-5c40-4399-99be-f80ee14c0ac7) (İş emri kapat) butonuyla iş emrini yayınlanmadan kapatır, bu esnada kimseye mail gitmez. Ancak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7ff4ddc7-7c6a-451a-9e19-64c058f3ae09) (iş emri kapat ve yayınla) butonu tıklanırsa iş emri kapatılır ve ilgili kişilere mail gönderimi yapılır.

BSAT/ Konfigürasyon Ayarları/ Akış Tanımlama menüsünden iş emri kapatma onayı tanımına gelip, ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload995e38cb-b0e3-44e6-b7fb-34204b6ab4ae) (düzenle) butonu yardımı ile akış için rol ataması yapılır. ![http://localhost/QDMS/common/images/kullaniciGrubuEkle.png](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9f178d6b-6c3c-49ac-a942-95bdbfd4eb6f)(ekle) butonu ile ilgili rol tanımlı olan listeden seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5ca7eedf-1494-42c4-a59e-756eb88e6f80)

**Bekleyen İşlerim** ekranında **Kapatma Onayı Bekleyen İşlemler** şeklinde düşer. İlgili cihaz Kodu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadee464ddd-37c1-4410-bc24-2faa8225f565)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc94e980-a709-4ef8-9fc7-fe2133963f12)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb0c2483f-22dc-45b9-a822-0001d2161803):Rapor görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9e6a9b32-d4a3-4535-8316-b96543b5af96):İş emri onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0226e53c-54d4-41b6-a23f-e26dccdd2e64):İş emri ret edilir.

İş emri ret edilecek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0226e53c-54d4-41b6-a23f-e26dccdd2e64) (ret) butonu tıklanarak ret nedeni yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc1670671-9594-4e8d-863e-73b5c0bf02e1)

İş emri ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9e6a9b32-d4a3-4535-8316-b96543b5af96) (onay) butonu tıklanarak iş emri onay verilerek kapatılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddbf24a30-a7ce-40d2-a59a-052665d8d1b1)

### **6.2.3.İşlem Tarihçesi**

**Menü Adı:** Entegre Yönetim Sistemi/ Cihaz Yönetimi/ İşlem Tarihçesi

Cihaz yönetimi modülü içerisindeki cihazların işlem tarihçelerine göz atmak için kullanılabilir.

İşlem tarihçesi menüsü tıklanır ve cihaz listesi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0e486c40-e85d-4df7-ae52-491d3980d701)

Listeden bir cihaz seçilir ve sağ üstteki butonlardan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7981086d-0270-42e1-bb1f-e6635308f606) (cihaz bilgileri) butonu tıklanırsa cihaz bilgileri ekranı açılır. Bu ekrandan cihaz ile ilgili temel bilgilere ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload386d9a41-fb02-4b98-a00f-cf8911fcd986)

Ek dosyalar sekmesinde ekranda cihaza yapılan işlemlere ait ölçüm raporları, sertifika gibi varsa ek dosyalar sistemde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload14271e2c-f266-4393-a447-abacaed4d032)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload203e4d64-f15f-4f7a-927b-b594e46c44f1) (Tarihçe) butonu tıklanırsa seçili cihazın işlem tarihçesi görüntülenir. Bu ekranda hangi işlemin hangi cihazlara kaç kere uygulandığı görülebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4ef50570-beb6-48bc-8dfe-19c75a79aee3)

İşlem tarihçesi ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8c21a1da-3107-4127-8f4f-20fbb175220e) (raporu görüntüle) butonu tıklanırsa seçili işlem için kalibrasyon raporu/sertifika dosyası bilgisayara indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload58d724fa-fcda-4ccd-94ae-6f9dec941ea5)

Ek dosyalar sekmesinde ekranda cihaza yapılan işlemlere ait ölçüm raporları, sertifika gibi varsa ek dosyalar sistemde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload830e35a2-9056-415f-b4b1-77161ab4cb4e)

### **6.2.4.Raporlar**

**Menü Adı:** Entegre Yönetim Sistemi/ Cihaz Yönetimi/ Raporlar

Cihaz Yönetimi Sistemi Modülü ile ilgili Raporların görüntülendiği menüdür.

#### **6.2.4.1.Planlanan İşlemler Raporu**

**Menü Adı:** Entegre Yönetim Sistemi/ Cihaz Yönetimi/ Raporlar/ Planlanan İşlemler Raporu

Planlanan İşlemler Raporu’nda gelecek işlem tarihleri kısmından filtreleme yapılarak gelecek işlem tarihleri görüntülenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2a6f34f9-7e6b-41ef-83d5-cd337831267e)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3078baed-d974-4206-af19-eb7daa035bcf): Kayıtlar filtrelenerek arama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5347290e-ea27-4cef-9e23-eb81fac0223f): Veriler Excel’ e aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload55243636-dc8e-4877-b745-6fcb0a5745be) (Excel’e aktar) butonu ile Excel formatında Planlanan İşlemler Raporu görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4ee25ded-6c49-4250-9987-205c85144d0b)

#### **6.2.4.2.İş Emirleri Raporu**

**Menü Adı:** Entegre Yönetim Sistemi/ Cihaz Yönetimi/ Raporlar/ İş Emirleri Raporu

İş Emirleri Raporu en genel rapordur. Sistemde o ana dek açılmış ve kapatılmış tüm iş emirlerinin görüntülenip istenilen filtrelere göre listelenebileceği rapordur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload856649aa-b301-405c-ae00-acbdecd7bec8)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3078baed-d974-4206-af19-eb7daa035bcf): Kayıtlar filtrelenerek arama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5347290e-ea27-4cef-9e23-eb81fac0223f): Veriler Excel’ e aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload55243636-dc8e-4877-b745-6fcb0a5745be) (Excel’e aktar) butonu ile Excel formatında İş Emirleri Raporu görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadea22c35e-ad33-4a9c-a91e-f88190210b54)

#### **6.2.4.3.İş Emirleri Detay Raporu**

**Menü Adı:** Entegre Yönetim Sistemi/ Cihaz Yönetimi/ Raporlar/ İş Emirleri Detay Raporu

İş Emirleri Detay Raporu ise İş Emirleri Raporu’nun benzeridir. Ek olarak ölçüm değerleri yer almaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6dbcdd2d-e4f8-417d-9e03-5ae97b8a82c4)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3078baed-d974-4206-af19-eb7daa035bcf): Kayıtlar filtrelenerek arama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5347290e-ea27-4cef-9e23-eb81fac0223f): Veriler Excel’ e aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload55243636-dc8e-4877-b745-6fcb0a5745be) (Excel’e aktar) butonu ile Excel formatında İş Emirleri Detay Raporu görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload667cc76a-c1c8-44f6-853c-34d2fbee30da)

#### **6.2.4.4.Maliyet Raporu**

**Menü Adı:** Entegre Yönetim Sistemi/ Cihaz Yönetimi/ Raporlar/ Maliyet Raporu

Maliyet Raporu, cihaz ve işlem maliyetleri bilgilerini içeren rapordur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2c8b5cf6-43a0-4a48-9741-651f381b6acd)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3078baed-d974-4206-af19-eb7daa035bcf): Kayıtlar filtrelenerek arama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5347290e-ea27-4cef-9e23-eb81fac0223f): Veriler Excel’ e aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload55243636-dc8e-4877-b745-6fcb0a5745be) (Excel’e aktar) butonu ile Excel formatında Maliyet Raporu görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3cbbd15-7549-402f-b6fa-c265be59e01d)

#### **6.2.4.5.Onay Durum Raporu**

**Menü Adı:** Entegre Yönetim Sistemi/ Cihaz Yönetimi/ Raporlar/ Onay Durum Raporu

Onay Durum Raporu, onayda bekleyen cihaz ve işlemlerin durum bilgilerini içeren rapordur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf659c891-3d53-438b-9d4a-fcb7cbd2e887)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3078baed-d974-4206-af19-eb7daa035bcf): Kayıtlar filtrelenerek arama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5347290e-ea27-4cef-9e23-eb81fac0223f): Veriler Excel’ e aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload55243636-dc8e-4877-b745-6fcb0a5745be) (Excel’e aktar) butonu ile Excel formatında Onay Durum Raporu görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload17f82e8c-be64-43ef-87ba-cb8487b9a356)

#### **6.2.4.6.Onay Kontrol**

**Menü Adı:** Entegre Yönetim Sistemi/ Cihaz Yönetimi/ Raporlar/ Onay Kontrol

Onay kontrol kodu ile cihazın kim tarafından, ne zaman onayının verildiğini kontrol eden rapordur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcd65e9e6-046d-4c8e-9773-33bbba06c7e6)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3078baed-d974-4206-af19-eb7daa035bcf): Kayıtlar filtrelenerek arama yapılabilir.

Onay kontrol ekranında onay kodu bilgisi girilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3078baed-d974-4206-af19-eb7daa035bcf) filtrele butonu tıklanır. Sistemin ürettiği Onay kodu bilgisi ile cihazın kaç no’lu iş emri ile hangi tarihte saat kaçta kim tarafından onaylandığı bilgisi verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload890dd757-6648-45a6-a05a-c18e49dd7e63)

#### **6.2.4.7.Zaman Çizelgesi Raporu**

**Menü Adı:** Entegre Yönetim Sistemi/ Cihaz Yönetimi/ Raporlar/ Zaman Çizelgesi Raporu

Zaman Çizelgesi Raporu’nda ise işlem sorumluların ay bazında yapması gereken işlemlerin bilgisi görsel olarak ifade edilir. Hangi gün hangi iş emrinin hangi sorumluda olduğu görülebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadef6d4961-6723-45d5-9e4c-a0e258557db2)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3078baed-d974-4206-af19-eb7daa035bcf): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5347290e-ea27-4cef-9e23-eb81fac0223f): Veriler Excel’ e aktarılabilir.

Bu ekrana gelindiği takdirde Kalibrasyon Listesi kulakçığında bir takvim görüntülenecektir. Üst kısımda ay-yıl seçilebilmektedir. Takvimin alt kısmında ise günler ve takvimin sol tarafında ise işlem sorumlusu olarak atanan kişiler bulunmaktadır. Planlanan İşlem Tarihi’nin olduğu günlerde işaret bulunur.

Kalibrasyon Arama kulakçığına gelindiği takdirde ise işlem tipi ve arama tipine göre filtreleme yapılabilir. Alanlar uygun şekilde doldurulur ve filtreleme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload94f65602-0835-4231-82d9-153e3d074ea5)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload55243636-dc8e-4877-b745-6fcb0a5745be) (Excel’e aktar) butonu ile Excel formatında Zaman Çizelgesi Raporu görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload451f03b7-38ef-44fa-adab-e99317e8409a)
