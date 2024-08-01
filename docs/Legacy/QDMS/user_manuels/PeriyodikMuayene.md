---
title: İş Başı ve Periyodik Muayene
description: İş Başı ve Periyodik Muayene Yardım Dokümanı
sidebar_position: 45
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::



**İş Başı ve Periyodik Muayene Modülü(v.5.24) Kullanıcı Yardım Dokümanı**

Modül Versiyonu: 5.24



**1. GİRİŞ**: 4857 sayılı İş Kanunu kapsamda işe giriş muayeneleri veya çalışanların periyodik muayenelerini gerçekleştirilmelidir. İşyeri Hekimi ve Diğer Sağlık Personelinin Görev, Yetki, Sorumluluk ve Eğitimleri Hakkında Yönetmeliği kapsamında işyeri tehlike sınıfına göre belirlenen periyotlarda periyodik muayenelerin tekrarlanması zorunludur (Madde 4). 6331 sayılı Kanununun 6 ncı maddesine göre iş sağlığı ve güvenliği hizmetlerinin elektronik ortamda yönetilebilmesi kapsamında “elektronik işyeri hekim uygulaması” başlatılmış olup, reçeteler elektronik ortamda yazılmaktadır.

**2. AMAÇ:** Bu yardım kılavuzunun amacı, QDMS kullanan kuruluşların İşbaşı ve Periyodik Muayene Modülünün implementasyonu sırasında ve sonrasında izleyeceği yolu belirlemektir.

**3. SORUMLULUKLAR**: İşyeri Hekimi, İşyeri Hemşiresi, İnsan Kaynakları, İş Güvenliği Uzmanı

**4. KISALTMALAR**: -

**5. İŞ AKIŞI**:

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade2fa2b03-ddf5-4ca7-8ecc-8d03ba651e49)



# **6. İŞ BAŞI VE PERİYODİK MUAYENE**

İşbaşı, periyodik ve poliklinik muayene kayıtlarının takibi ve raporlanması; reçetelerin elektronik ortamda yazılması; istirahat rapor takibi; personel durum takibi; iş yerleri bazında hekim yetkilendirmesi; periyodik muayenelerde yönetici, hekim ve çalışana ön bildirim; işyeri ve departman bazında hastalık dağılımının gösterilmesini sağlayan modüldür.

## Sistem Altyapı Tanımları/ İşbaşı ve Periyodik Muayene

“İşbaşı ve Periyodik Muayene Modülü”nün altyapısını oluşturmak amacıyla gerekli tanımlamalar yapılır. Yapılan tanımlamalara göre giriş ekranında veriler kullanılmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9b5f5fbc-c976-4a69-850f-cf3d292d960b)

İşbaşı ve Periyodik Muayene Modülünün etkin bir şekilde kullanılabilmesi için personellere ait verilerin sistemde tanımlı olması gerekir. Sistem Altyapı Tanımları/ BSAT/ Tanımlar/ Personel Tanımlama menüsünde “Ek Alanlar” butonuyla personele ait verilerin sisteme girilmesi gerekir. Böylece personele ait genel sağlık bilgileri ve özgeçmiş bilgileri oluşturulmuş olur.

“İşbaşı ve Periyodik Muayene” modülündeki bilgiler kişisel veri gizliliği kapsamında gizli bilgiler olup menü yetkilendirme yapılması gerekmektedir. Menü görme yetkisi sadece işyeri hekimi ve varsa işyeri hemşiresine verilmelidir.

### **Hastalık Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ İşbaşı ve Periyodik Muayene/ **Hastalık Tanımla**

Muayene takibi/ ana sekmesinde bulunan, “Hastalık Teşhisi” alanında görüntülenen, tüm hastalık tanımlarının bulunduğu menüdür. Bu tanımlar sistemden default olarak gelmektedir. Hastalık tanımları poliklinik muayene türünde kullanılmaktadır. İhtiyaç halinde diğer muayene türlerinde de kullanılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c54104a-c2e6-4e71-8616-eb7221b0fda3)

Ekranda sağ üst köşede bulunan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload94a13b02-ace7-4ffd-bd57-642cc448a2e2)(Arama) butonu ile hastalığın kodu, tanımı ya da açıklama bilgisine göre kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade33bdf05-cad3-46b8-a0e6-a5ae0f8d3fe9)

### **Personel Durumu Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ İşbaşı ve Periyodik Muayene/ Personel Durumunu Tanımlama

Personelin engel/ kısıt gibi işe etki edebilecek özel durumlarının tanımlandığı menüdür. Örneğin; gece çalışamaz, yüksekte çalışamaz, hamile, maluliyet, tehlikeli işlerde çalışamaz gibi. Bu menüde tanımlanan durumlar muayene takibi ekranında sonuç sekmesinde personel durumu alanında kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1e81f111-b944-4c8d-a812-763e6dc71e8e)

Ekranda bulunan butonlar yardımıyla;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d874145-1d55-44f4-ac00-b3563cac5798): Yeni bir personel durumu tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload213a0b25-e5b1-4a9f-97e8-6ed87050af1d): Listede seçili olan personel durumu bilgisi güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3f5aded4-6338-4f35-91a1-8be7ad69df25): Listede seçili olan personel durumu silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload94a13b02-ace7-4ffd-bd57-642cc448a2e2):Kayıtlar filtrelenerek arama yapılır.

Yeni bir personel durumu eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada65b5694-919b-45e5-a3fd-a5d0e31ce13f)(Yeni) butonuna tıklanarak “Personel Durumu Tanımlama/ Yeni Kayıt” ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload81dbdbf2-2b40-483a-9e46-7a5ea146f999)

“Adı” alanında personel durumunun ne olduğu tanımlanır. Eğer “Risk Durumu” kutucuğu işaretlenirse personelin risk grubunda olduğu belirtilir. O personele QDMS üzerinden herhangi bir görev atamak istenildiği zaman sistem tarafından uyarı verilerek, işyeri hekiminden bilgi alınması gerektiği belirtilmektedir.

“Personel Durumu Tanımlama” ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload86f5315a-463b-4e6e-9910-ed2dd62b39d7) (Kaydet) butonuna tıklanarak kayıt işlemi gerçekleştirilir.

### **Kontrol Tipi Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ İşbaşı ve Periyodik Muayene/ **Kontrol Tipi Tanımlama**

Kontrol takibi yapılacak hastalar için hangi kontrol tipinin yapılacağı bu menüden tanımlanır. Örneğin; işe dönüş kontrolü, hastalık takibi gibi. Bu menüde tanımlanan kontrol tipleri muayene takibi menüsünde sonuç sekmesinde “Kontrol” olarak görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfd6efefd-843a-4789-8606-2f5779c24143)

Ekranda bulunan butonlar yardımıyla;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d874145-1d55-44f4-ac00-b3563cac5798): Yeni bir kontrol tipi tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload213a0b25-e5b1-4a9f-97e8-6ed87050af1d): Listede seçili olan kontrol tipi bilgisi güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3f5aded4-6338-4f35-91a1-8be7ad69df25): Listede seçili olan kontrol tipi bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload94a13b02-ace7-4ffd-bd57-642cc448a2e2): Kayıtlar filtrelenerek arama yapılır.

Yeni bir kontrol tipi eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada65b5694-919b-45e5-a3fd-a5d0e31ce13f) (Yeni) butonuna tıklanarak “ Kontrol Tipi Tanımlama/ Yeni Kayıt” ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8fe62003-9059-4227-9d69-8455fd73d6dd)

“Adı” alanında kontrol tipinin ne olduğu tanımlanır. Eğer “İşe Başlama” kutucuğu işaretlenirse hastalık/ kaza sonucu personelin işe başlama kontrolünün yapıldığı belirtilmiş olur.

“Kontrol Tipi Tanımlama” ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload86f5315a-463b-4e6e-9910-ed2dd62b39d7) (Kaydet) butonuna tıklanarak kayıt işlemi gerçekleştirilir.

### **İşyeri Hemşiresi Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ İşbaşı ve Periyodik Muayene/ İşyeri Hemşiresi Tanımlama

İşyeri hemşiresi tanımlama işleminin gerçekleştiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd6e304fb-95d4-4905-a858-a130f0697b57)

Ekranda bulunan butonlar yardımıyla;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d874145-1d55-44f4-ac00-b3563cac5798): Yeni bir işyeri hemşiresi tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload213a0b25-e5b1-4a9f-97e8-6ed87050af1d): Listede seçili olan işyeri hemşire bilgisi güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3f5aded4-6338-4f35-91a1-8be7ad69df25): Listede seçili olan işyeri hemşiresi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload94a13b02-ace7-4ffd-bd57-642cc448a2e2): Kayıtlar filtrelenerek arama yapılır.

Yeni bir işyeri hemşiresi tanımlamak için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada65b5694-919b-45e5-a3fd-a5d0e31ce13f) (Yeni) butonuna tıklanarak “İşyeri Hemşiresi Tanımlama/ Yeni Kayıt” ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbbb04ff9-8537-4245-a614-86f0438cfde1)

Açılan ekranda ilgili alanlar tanımlanır;

**Sicil No:** Sistemde tanımlı olan personel listesinden işyeri hemşiresi seçilir.

**Diploma No:** Hemşirenin “Diploma No” bilgisi tanımlanır.

**Diploma Tarihi:** Hemşirenin “Diploma Tarihi” seçilir.

**İş Yeri Hemşireliği Belge Tarihi:** Eğer hemşirenin, “İşyeri Hemşireliği Belgesi” varsa, o belgeye ait “İş Yeri Hemşireliği Belge Tarihi” seçilir.

**İş Yeri Hemşireliği Belge No:** Eğer hemşirenin, “İşyeri Hemşireliği Belgesi” varsa, o belgeye ait “Belge No” bilgisi tanımlanır.

**İşyeri:** Sisteme tanımlanan işyeri hemşiresinin hangi işyerlerinde çalıştığı bilgisi sistemde tanımlı olan işyeri listesinden seçilir. Böyle işyeri hemşiresi sadece bağlı bulunduğu işyerlerindeki personelleri görebilir.

Gerekli alanlar tanımlandıktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload86f5315a-463b-4e6e-9910-ed2dd62b39d7) (Kaydet) butonuna tıklanarak kayıt işlemi gerçekleştirilir. İş yeri Hemşiresinin Bekleyen işlerimde “Onay Bekleyen Atama Listesi” olarak iş düşer. Onaylama işleminde İşyeri Hemşiresinin ataması yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6fb8099d-d0cb-432e-84f9-311df0f57fa3)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload381355ae-d8cc-401d-bc0c-fafc7cdab795)

### **Test Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ İşbaşı ve Periyodik Muayene/ Test Tanımlama

İşbaşı ve periyodik muayenesi gibi muayene türleri için yapılması gereken testlerin tanımlandığı menüdür. Tanımlanan bu testler seçilen muayene türlerine göre testler sekmesinde görüntülenmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload72785c34-c470-426e-8f93-627d51d8d8f9)

Ekranda bulunan butonlar yardımıyla;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d874145-1d55-44f4-ac00-b3563cac5798): Yeni bir test tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload213a0b25-e5b1-4a9f-97e8-6ed87050af1d): Listede seçili olan test bilgisi güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3f5aded4-6338-4f35-91a1-8be7ad69df25) : Listede seçili olan test bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload94a13b02-ace7-4ffd-bd57-642cc448a2e2): Kayıtlar filtrelenerek arama yapılır.

Yeni bir test eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada65b5694-919b-45e5-a3fd-a5d0e31ce13f) (Yeni) butonuna tıklanarak “Test Tanımlama/ Yeni Kayıt” ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload205c26cf-6ae1-4772-9ddb-b3f7f8b843cf)![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload030759eb-3fb9-4989-acc3-b3feebfe8546)

Açılan ekranda ilgili alanlar tanımlanır;

**Adı:** Testin adının tanımlanır.

**Zorunlu Departmanlar:** Tanımlanan test bilgisini hangi departmanlar için zorunlu olduğu bilgisi sistemde tanımlı olan departman listesinden seçilir.

**Default Açıklama:** Muayene işlemlerini gerçekleştirirken ilgili testin açıklama alanında gelmesi istenilen sabit bir açıklama varsa bu alanda tanımlanır. Örneğin; “normal sınırlar içerisinde” açıklaması.

**Şablon Kullanılsın:** Yapılan testle ilgili detaylı olarak sonuçların girilmesi ve bir excel formatında görüntülenmesi isteniyorsa “Şablon Kullanılsın” kutucuğu işaretlenir.

**Rapor Şablonu:** Tanımlanan teste ait detay değerlerin girileceği şablon adının tanımlaması yapılır. Rapor formatı düzenleme menüsünden ilgili test şablonunun sisteme yüklenmiş olması gerekir.

**Alt Testler:** Tanımlana teste ait incelenecek detay değerlerin neler olduğu tanımlanır.

**ÖNEMLİ NOT-1:** Örneğin; kan testi adı altında tanımlanan teste ait WBC, HGB, RBC gibi kan testi içerisinde kontrol edilen alt değerler “alt Testler” alanında tanımlanır. Testlere ait veri girişi yapılacak excel formatı, girilen alt değerlere göre düzenlenerek “Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Rapor Formatları Düzenleme” menüsünden sisteme tanımlanır. Tanımlanan ilgili rapor formatının listedeki görüntülenen adı, “rapor şablonu” alanında tanımlanır. “Şablon Kullanılsın” kutucuğu işaretlenir. Yapılan bu işlemler neticesinde şablon kullanılması istenilen testler ayrı birer sekme halinde görüntülenir. Şablon kullanılmayan testler ise “Testler” sekmesinin altında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade0b59adf-e2ff-4f7b-8eaa-f11aabd059ce)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8a08de37-8584-4c4d-8fe4-54437e43bc74)

**ÖNEMLİ NOT-2:** Şablon olarak görüntülenecek tüm testlerin ayrı ayrı tanımlamasının yapılarak ayrı sekmeler altında görüntülenmesine gerek yoktur. Tüm testler yukarıdaki ekran görüntüsünde olduğu gibi sisteme “Tüm Testler” adı altında tanımlanır. “Test Tanımlama” ekranında aşağıdaki ekran görüntüsünde görüntülendiği gibi tanımlama işlemi gerçekleştirilir. “Alt Testler” kısmında kan, sft, odio gibi tüm testlere ait detay değerler tanımlanır. Sisteme yüklenecek olan excel formatı tek bir formatta her teste ait ayrı sheet olarak hazırlanır ve sisteme yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada2d2dec1-5d5f-4840-a6c1-c3c7c8001f6b)

“Test Tanımlama” ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload86f5315a-463b-4e6e-9910-ed2dd62b39d7) (Kaydet) butonuna tıklanarak kayıt işlemi gerçekleştirilir.

### **Fiziki/ Psikolojik Muayene Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ İşbaşı ve Periyodik Muayene/ Fiziki/ Psikolojik Muayene Tanımlama

İşbaşı ve periyodik muayenesi gibi muayene türleri için yapılması gereken fiziki/ psikolojik muayenelerin tanımlandığı menüdür. Tanımlanan bu fiziki/ psikolojik muayeneler seçilen muayene türlerine göre görüntülenmektedir

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd5774a00-7cb9-4b86-ae16-5e03ffd98b7b)

Ekranda bulunan butonlar yardımıyla;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d874145-1d55-44f4-ac00-b3563cac5798): Yeni bir fiziki/ psikolojik muayene tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload213a0b25-e5b1-4a9f-97e8-6ed87050af1d): Listede seçili olan fiziki/ psikolojik muayene bilgisi güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3f5aded4-6338-4f35-91a1-8be7ad69df25): Listede seçili olan fiziki/ psikolojik muayene silinir.

Yeni bir fiziki/ psikolojik muayene tanımlamak için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada65b5694-919b-45e5-a3fd-a5d0e31ce13f) (Yeni) butonuna tıklanarak “Fiziki/ Psikolojik Muayene Tanımlama/ Yeni Kayıt” ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8c9ab1dc-58c7-4478-97d5-630bee8145d0)

Açılan ekranda ilgili alanlar tanımlanır:

**Adı:** Fiziki/ psikolojik muayenenin adı tanımlanır.

**Default Açıklama:** Muayene işlemlerini gerçekleştirirken ilgili fiziki/ psikolojim muayene açıklama alanında gelmesi istenilen sabit bir açıklama varsa bu alanda tanımlanır. Örneğin; “Değerler Normal” açıklaması.

Fiziki/ psikolojik muayene tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload86f5315a-463b-4e6e-9910-ed2dd62b39d7) (Kaydet) butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4ee07200-dfca-4c1f-8bda-3eb0b20b3530)

### **Muayene Türü Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ İşbaşı ve Periyodik Muayene/ Muayene Türü Tanımlama

“İşe Giriş Muayenesi, Periyodik Muayene, Poliklinik, İşe Dönüş Muayenesi, Kurumdışı Muayene, Gebe Takibi, Engelli Takibi” gibi muayene türlerinin tanımlandığı menüdür. Tanımlanan muayene türleri “Fonksiyon Dizayner” menüsünde “Statü” olarak görüntülenmektedir. Böylece sistemde kullanılmak üzere tanımlanan alanların, hangi statüde (muayene türünde) görüntüleneceği belirlenir. Tanımlanan bu muayene türleri muayene takibi ekranında listelenerek, hangi muayene gerçekleştirilecekse o muayene türünün görüntülenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf3dd57e0-5c03-417b-b362-fadd4f6bf8d5)

Ekranda bulunan butonlar yardımıyla;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d874145-1d55-44f4-ac00-b3563cac5798):Yeni bir muayene türü tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload213a0b25-e5b1-4a9f-97e8-6ed87050af1d): Listede seçili olan muayene türü güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3f5aded4-6338-4f35-91a1-8be7ad69df25): Listede seçili olan muayene türü silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc56ed7c3-7e6f-4c1b-8f45-ece103cb626d): Listede seçili olan muayene türü için rapor formatı tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload94a13b02-ace7-4ffd-bd57-642cc448a2e2): Kayıtlar filtrelenerek arama yapılır.

Yeni bir muayene türü eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada65b5694-919b-45e5-a3fd-a5d0e31ce13f) (Yeni) butonuna tıklanarak “Muayene Türü Tanımlama/ Yeni Kayıt” ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload73ceee2b-c8d4-4327-b4ef-c75a8618aa38)![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd70d681f-4318-4573-9090-2477d241f28d)

Açılan ekranda ilgili alanlar tanımlanır;

**Tanım:** Muayene türünün adı tanımlanır. Örneğin; Periyodik Muayene.

**Zorunlu Testler:** Tanımlanan muayene türü için yapılması gereken zorunlu testler varsa test listesinden seçim yapılır. Örneğin; Tüm Testler

**Zorunlu Fiziki Muayene:** Tanımlanan muayene türü için yapılması gereken zorunlu fiziki muayeneler varsa fiziki muayene listesinden seçim yapılır. Örneğin; Kardiyovasküler Muayene

**Periyodik mi?:** Tanımlanan muayene türünün periyodiklik bilgisi seçilir.

**Periyot (Ay):** “Periyodik mi?” alanında “Evet” seçeneği seçilirse kaç ayda bir periyodik muayene işleminin gerçekleştirileceği bilgisi tanımlanır.

**İlişkili Kullanıcı Grupları:** “Periyodik mi?” alanında “Evet” seçeneği seçilirse hangi kullanıcı grubu için periyodik muayene görevinin oluşacağı belirlenir.

**Gösterilecek Sonuçlar:** Tanımlanan muayene türü sonucunda “İşe Devam, Sevk, İstirahat” seçeneklerinden hangilerinin gösterileceği işaretlenir.

**Anamnez Formu sekmesi kullanılsın:** Tanımlanan muayene türü için muayene gerçekleştirme ekranında “Anamnez Formu” sekmesinin görüntülenmesi isteniyorsa kutucuk işaretlenir. Alan tanımlama menüsünde tanımlanıp, fonksiyon dizayner menüsü ile anamnez formu için eşleştirilen alanlar bu sekmenin altında görüntülenir.

**Test sekmesi kullanılsın:** Tanımlanan muayene türü için muayene gerçekleştirme ekranında test sekmesinin görüntülenmesi isteniyorsa kutucuk işaretlenir.

**Fiziki muayene sekmesi kullanılsın:** Tanımlanan muayene türü için muayene gerçekleştirme ekranında fiziki muayene sekmesinin görüntülenmesi isteniyorsa kutucuk işaretlenir.

**Reçete sekmesi kullanılsın:** Tanımlanan muayene türü için muayene gerçekleştirme ekranında e-reçete yazma sekmesinin görüntülenmesi isteniyorsa kutucuk işaretlenir. Poliklinik muayenelerde kullanılır.

**Kişi bilgileri sekmesi kullanılsın:** Tanımlanan muayene türü için muayene gerçekleştirme ekranında kişi bilgileri sekmesinin görüntülenmesi isteniyorsa kutucuk işaretlenir. Personel tanımlama ekranında ek bilgiler butonu ile tanımlanan kişisel bilgiler görüntülenir.

**Ana sekmede teşhis kullanılmasın:** Tanımlanan muayene türü için muayene gerçekleştirme ekranında ana sekmede hastalık teşhisi alanının görüntülenmesi istenmiyorsa kutucuk işaretlenir. “Hatalık Teşhisi” alanı poliklinik muayenelerde kullanılırken, periyodik muayene gibi diğer muayene türlerinde kullanılmayabilir.

**Sonuç sekmesi kullanılmasın:** Tanımlanan muayene türü için muayene gerçekleştirme ekranında sonuç sekmesinin görüntülenmesi istenmiyorsa kutucuk işaretlenir.

**Ana sekmede kişi ek bilgileri gösterilmesin:** Tanımlanan muayene türü için muayene gerçekleştirme ekranında ana sekmede boy, kilo, kitle indeksi gibi kişi ek bilgilerinin görüntülenmesi istenmiyorsa kutucuk işaretlenir.

**Sonuç sekmesinde de hekim kanaati gösterilmesin:** Tanımlanan muayene türü için muayene gerçekleştirme ekranında sonuç sekmesinde metin tipli veri girişi yapılan hekim kanaati alanının görüntülenmesi istenmiyorsa kutucuk işaretlenir.

**Sonuç sekmesinde de personel durumu gösterilmesin**: Tanımlanan muayene türü için muayene gerçekleştirme ekranında sonuç sekmesinde personel durumu seçim alanının görüntülenmesi istenmiyorsa kutucuk işaretlenir. “Personel Durumu” alanı periyodik muayene, işe giriş muayenesi gibi muayenelerde kullanılırken, poliklinik muayene türünde kullanılmayabilir.

**Sonuç sekmesinde de kontrol gösterilmesin:** Tanımlanan muayene türü için muayene gerçekleştirme ekranında sonuç sekmesinde kontrol tipi seçim alanının görüntülenmesi istenmiyorsa kutucuk işaretlenir. “Kontrol” alanı poliklinik muayenelerde kullanılırken, periyodik muayene gibi diğer muayene türlerinde kullanılmayabilir.

**Maksimum Rapor Süresi (Gün):** Tanımlanan muayene türü için muayene gerçekleştirme ekranında hekim tarafından kaç gün rapor verilebileceği bilgisi tanımlanır. Poliklinik muayenelerde işyeri hekiminin verebileceği yasal istirahat süresi 2 gün olarak gelmektedir. Kurumdışı muayene gibi işyeri hekiminin yapmadığı hastane muayenelerine ait raporlar için kullanılır. Sisteme tanımlanan maksimum rapor süresinden fazla rapor girişine izin verilmez.

Muayene Türü Tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload86f5315a-463b-4e6e-9910-ed2dd62b39d7) (Kaydet) butonuna tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddd108d93-d927-4d81-bfd0-d2a4f998983a)

Sisteme tanımlanan muayene türü için kullanılması istenilen bir rapor formatı varsa sisteme uygun olarak ilgili kısa kodlarla düzenlenir. Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Rapor Formatları Düzenleme menüsünden sisteme yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcad3edde-19f0-47dc-a334-1a90f97a2888)**Muayene türü** tanımlama ekranında ilgili muayene türü seçiliyken sağ üst köşede bulunan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc56ed7c3-7e6f-4c1b-8f45-ece103cb626d) (Rapor Formatları) butununa tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf39ab3d8-c1b9-494a-869a-cc18519d0e0e)

Seçile muayene türünde kullanmak üzere yeni bir rapor formatı tanımlamak için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada65b5694-919b-45e5-a3fd-a5d0e31ce13f) (Yeni) butonuna tıklanarak “Rapor Formatları Tanımlama/ Yeni Kayıt” ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload55e8ab8f-2346-4bde-ade2-9a63a4aa7700)

Açılan ekranda rapor adı bilgisi girilir. “Rapor Formatı” alanına rapor formatları düzenleme menüsünde yüklenen raporun adı (uzantısı) tanımlanır ve kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7b3a76f2-ef6f-4441-b8a5-625a4912a684)

### **Alan Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ İşbaşı ve Periyodik Muayene/ Alan Tanımlama

İşyeri Hekimi Tanımlama, İşyeri Hemşiresi Tanımlama, Muayene Türü Tanımlama, Muayene Takibi, Muayene Takibi Sonuçlar, Test Tanımlama, Fiziki/ Psikoloji Muayene Tanımlama, Muayene Takibi Ana Sekme menilerinde kullanılması istenilen firmaya özel alanların tanımlandığı yerdir. Burada oluşturulan alanlar, alan havuzuna kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1880ca26-2552-4c8d-b151-12c9a294d301)

Ekrandaki bulunan butonlar yardımıyla;

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload81dad6f1-5aa6-4e1e-8faa-1b49a86d2dcd): Yeni bir alan eklenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload32b5ddb9-32f0-403c-8971-25063c432c47): Var olan alanda değişiklik yapılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8373a01f-4411-49ca-a3f9-e66e4359a6c6): Seçili olan alan silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload15e4ae10-646c-4f30-97c1-0d14e456035a): Liste tipli alanın değerleri (liste elemanları) tanımlanır.

Yeni bir Alan tanımlamak için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada65b5694-919b-45e5-a3fd-a5d0e31ce13f) (Yeni) butonuna tıklanarak “Alan Tanımlama/ Yeni Kayıt” ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc16fda15-5bd1-47c3-bbff-71adbf2e8742) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc1765b42-b454-4368-8b12-b2839c195dd2)

Açılan ekranda ilgili alanlar tanımlanır;

**Alan Kodu:** Alan kodu bilgisi tanımlanır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’

**Alan Adı:** Alan adı bilgisi tanımlanır.

**Başlık Notu:** Alanın başlık notu bilgisi tanımlanır.

**Giriş Tipi:** Oluşturulan alanda kullanıcı tarafından veri girişi/seçim mi yapacağı ya da hesaplama yöntemi ile otomatik olarak sistem tarafından mı atanacağı belirlenir.

**Alan Tipi:** Oluşturulan alanın metin, numerik, tarih, liste vb. alan tiplerinden hangisi olacağı belirlenir.

**Görünme Şartı:** Tanımlama işlemi devam eden alanın daha önceden tanımlanan başka bir alanın değerine göre görünüp görünmeyeceği belirlenir. Kullanımı [ALANKODU]=ALAN_DEĞERİ vb. şekildedir.

**Durum:** Alan durumu aktif veya pasif olarak seçilir.

**Termin Alanı:** Termin alanı aktif edilecekse ilgili kutucuk işaretlenir. Aksiyon ve DF’ lerin terminleri burdaki süre göz önüne alınarak belirlenir.

**Güncellemeden değer yükselmesin:** Güncellemeden değer yükselmesin bilgisi aktif edilecekse ilgili kutucuk işaretlenir. Bu bilginin işaretli olduğu alanlarda puan değeri güncelleme sırasında mevcut değerden daha yüksek olarak girilemez.

**İlişkili Alan:** İlişkili alan özelliği ile seçenek tipli iki alan arasında ilişki kurulabilmektedir. Referans alanın elemanlarının tanımlandığı ekranda ilişkili alandan hangi değerler ile ilişkili olduğu seçilebilmektedir. Böylece referans alanın form üzerinde değeri değiştiğinde ilişkili alan seçimli olarak otomatik dolabilmekte ya da seçim ekranından sadece ilişkilendirilen değerler arasından seçim yapılabilmektedir.

**İlişkili Alan Otomatik Doldurulsun:** ilişkili alan otomatik doldurulsun seçeneği aktif edilecekse ilgili kutucuk işaretlenir. Liste tipli iki alanın değerleri arasında kurulan ilişkiye göre alanlardan birinin otomatik doldurulmasını sağlar.

**Genişlik:** Alanın kolon genişliği bilgisi tanımlanır.

Alan tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf34b3f72-6c58-4f55-a2ec-72636b3e4f0a) (Kaydet) butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8c33ab57-54b0-45f8-a7c5-7b76bf59f350)

Bu alan seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload59bbc679-7741-481b-afea-370ee04ff785) (değerler) butonu tıklanırsa, “İlaç alerjiniz var mı” alanının liste elemanlarının tanımlanacağı ekrana ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf3f36b09-3859-461e-b453-f2fb8fa04fdc)

Ekrandaki bulunan butonlar yardımıyla;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1e8c97ab-81bc-454a-9d84-086647d4940a): Yeni bir liste değeri tanımlanır

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8e7b1e88-eb18-4f15-9c18-5a31d0221355): Listede seçili olan liste değeri güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload04f096f7-b165-45ba-a095-0afa225037c7): Listede seçili olan liste değeri silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload94a13b02-ace7-4ffd-bd57-642cc448a2e2): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcfca8cca-820a-4b15-8b1e-0bb74b1df676): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada3f32114-ecde-48db-8316-f89c7926da30): Şablon indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadccd13818-2fe3-4550-ab7f-00991e72613c): Şablon yüklenilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5e1f92aa-9d22-4bf9-938d-85f59501d68d) Yeni butonuna tıklanarak yeni değer tanımlama işlemine başlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadab81d0e8-472f-477e-8b73-bc3bd6f6b82f)![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade1d76e47-91ab-4f98-aef6-dd964a6bcf74)

Açılan ekranda ilgili alanlar tanımlanır;

**Tanım:** Tanım bilgisi girilir.

**Açıklama:** Açıklama bilgisi yazılır.

**Değer:** Değerin puan karşılığı girilir.

**Durum:** Değerin durumu aktif veya pasif olarak seçilir.

**Varsayılan:** İlgili liste değerinin varsayılan olarak alanda görünmesini sağlar.

**Önlem zorunlu mu?:** Bu değer seçili olduğunda önlemler sekmesinden en az bir önlem girilmesi zorunlu olur.

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf34b3f72-6c58-4f55-a2ec-72636b3e4f0a) (Kaydet) butonuna tıklanarak değer tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadadbade3f-1b86-4760-967d-143ad2ed8696)

Sistemde mevcut bulunan alan tiplerinin tam listesi aşağıda belirtilmiştir;

**Metin:** Elle yazım imkanı veren metin kutucuğu ekler.

**Metin Çok Satırlı:** Elle yazım imkanı veren karakter sınırı olmayan çok satırlı metin kutucuğu ekler.

**Nümerik:** Sayısal olarak veri girişi yaptırır.

**Nümerik-Parasal**: Parasal değer olarak nümerik giriş yaptırır.

**Nümerik-Birim:** Birim olarak nümerik giriş yaptırır.

**Tarih:** Takvim alanı ekler.

**Liste:** Birden fazla element arasından tek seçim yaptırır.

**Puanlı Liste:** Açılır menüden seçim yaptırır, liste elementlerinin puan değerleri mevcuttur.

**Arama Özellikli Liste:** Birden fazla element arasından geniş arama fonksiyonuyla arama yapabilecek şekilde, tekli ve/veya çoklu seçim yapılmasını sağlar.

**Ağaç Liste:** Ağaç kırılımına sahip birden fazla element arasından geniş arama fonksiyonuyla arama yapabilecek şekilde seçim yapılmasını sağlar.

**Personel:** QDMS personel veri tabanından kişi seçilebilmesini sağlar.

**Departman:** QDMS departman veri tabanından departman bilgisi seçilebilmesini sağlar.

**Ünvan:** QDMS unvan veri tabanından unvan bilgisi seçilebilmesini sağlar.

**Doküman:** QDMS doküman veri tabanından doküman seçilebilmesini sağlar.

**Süreç:** QDMS süreç veri tabanından süreç seçilebilmesini sağlar.

**Yönetim Sistemi:** QDMS yönetim Sistemi veri tabanından yönetim sistemi bilgisi seçilebilmesini sağlar.

**Müşteri:** QDMS müşteri veri tabanından müşteri bilgisi seçilebilmesini sağlar.

**Tedarikçi:** QDMS tedarikçi veri tabanından tedarikçi bilgisi seçilebilmesini sağlar.

**Ürün Grubu:** QDMS ürün grubu veri tabanından ürün grubu bilgisinin seçilebilmesini sağlar.

**Ürün:** QDMS ürün veri tabanından ürün bilgisinin seçilebilmesini sağlar.

**Şirket Profili:** QDMS şirket profili veri tabanından şirket profili bilgisi seçilebilmesini sağlar.

**Başlık:** Formlara koyu harflerle yazılacak başlık alanı ekler.

**Dosya:** Dosya ekler.

**Resim:** Resim ekler.

**Resim Liste:** Resim listesinden seçim sağlar.

**Çoklu Resim:** Çoklu resim seçilmesini sağlar.

**Tablo:** Tablo tipli alan oluşturulmasını sağlar. (Bu tip bir alan eklendikten sonra alan değerleri olarak yeni alan tanımlamalarının yapılması gereklidir.)

**Sorgu:** QDMS/Ensemble veritabanları içerisindeki ana verilerden seçim yapılabilmesi için tanımlanabilen alan türüdür. (Sadece Bimser Destek Ekibi tarafından tanımlanmalıdır) Tekli ve çoklu seçim yapılabilir.

**Sorgu Ağaç:** QDMS/Ensemble veritabanları içerisindeki ağaç kırılımlı ana verilerden seçim yapılabilmesi için tanımlanabilen alan türüdür. (Sadece Bimser Destek Ekibi tarafından tanımlanmalıdır) Tekli ve çoklu seçim yapılabilir.

**Sekme:** Aktif sekme haricinde alanların ilişki kurularak içerisinde görülebileceği yeni bir sekme oluşturur.

**Onay Kutusu Liste:** Tekli veya çoklu seçim yaptırılacak tipte bir liste tipli alandır.

**Risk:** Risk tabanlı modüllerden değerlerin seçilebilmesini sağlar. Bu tip bir alan eklendikten sonra hangi modülden değerlerin geleceği alan tanımlama ekranında seçilmesi gereklidir.

**Açıklamalı Liste:** Seçilen liste değerinin yanına açıklama yazabilme imkanı sağlayan alan tipidir. Alan Tanımlama menüsünde alan değerleri tanımlanırken her değer için açıklama kutucuğunun aktif olup olmayacağının seçilmesi gerekir. Burada yapılan seçime göre Entegre Yönetim Sistemi menüsü altında bu alanın görüleceği menüde ilgili seçim yapıldığında alan değerinin yanına kullanıcının açıklama yazabilmesi için kutucuk açılmış olur.

**Pozisyon:** QDMS pozisyon veri tabanından pozisyon bilgisi seçilebilmesini sağlar.

**Saat:** Saat tipli alan ekler.

### **Fonksiyon Dizayner**

**Menü Adı:** Sistem Altyapı Tanımları/ İşbaşı ve Periyodik Muayene/ Fonksiyon Dizayner

Fonksiyon Dizayner özelliği ile alan havuzuna eklenen alanlar “İşbaşı ve Periyodik Muayene” modülünün ilgili fonksiyonları ile ilişkilendirilebilir. Alanların görüntülenebileceği muayene türlerinin, Sistem Altyapı Tanımları/ İşbaşı ve Periyodik Muayene/ Muayene Türü Tanımlama menüsünde tanımlanmış olması gerekmektedir. “İşbaşı ve Periyodik Muayene” modülünün sistem altyapı tanımları altından “Fonksiyon Dizayner” menüsüne gelinir. Açılan ekranda “İşbaşı ve Periyodik Muayene” modülünün alan eklenebilecek fonksiyonları sıralanacaktır. Bu ekranda “İş Yeri Hekimi Tanımlama, İş Yeri Hemşiresi Tanımlama, Muayene Türü Tanımlama, Muayene Takibi, Muayene Takibi Sonuçlar, Test Tanımlama, Fiziki/ Psikolojik Muayene Tanımlama ve Muayene Takibi Ana Sekme Tanımlama” fonksiyonlarında kullanılacak alanlar ve bunların sıralaması ile onay işlemlerindeki hiyerarşi detayı tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload66104545-0c61-4aef-8d04-0ce3322deddc)

Tanımlı alanın hangi fonksiyonda görüntülenmesi isteniyorsa, ekranın sağ üst köşesinde bulunan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload605be876-a357-4ad1-8440-84f036ba18a0) (Alanlar) butonu ile görüntülenmesi sağlanır. Örneğin sisteme tanımlanan bütün alanların muayene takibi ekranında açılması ve bu alanda işlem yapılması isteniliyorsa “Muayene Takibi Ana Sekme” fonksiyonu seçilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload605be876-a357-4ad1-8440-84f036ba18a0) (Alanlar) butonu ile açılması sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload89542e0b-9d0b-4be8-9b9e-19e71bbdbe11)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload53d8a6dd-d250-45e1-9c14-d0a9ca0faf7c) (Alanlar) butonu ile açılan ekranda seçili fonksiyonda kullanılacak alanlar ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada65b5694-919b-45e5-a3fd-a5d0e31ce13f)(Yeni) butonuna tıklanarak belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9b307094-393e-4b61-abb4-8cfadca4c136) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload451ef79b-d76a-472c-b84c-1bc5ac8bbe93)

Açılan ekranda ilgili alanlar tanımlanır;

**Alan Adı:** Alan tanımlama ekranında tanımlanmış alanlardan alan seçimi yapılır.

**Zorunlu Mu?:** Alanın zorunlu olup olmadığı seçilir.

**Zorunluluk Mesajı:** Zorunlu alan doldurulmadığında verilecek uyarı mesajı bilgisi bu alana yazılır.

**Sıra No:** Alanın sıra no belirlenir.

**Varsayılan Rol:** İlgili alanın değeri daha önce tanımlanmış bir üst formdan ya da kaydı giren kişinin adı soyadı, pozisyonu, unvanı, departmanı, iş yeri gibi verileri ise bunlar için tanımlanmış rol seçilebilir.

**Varsayılan Değer Değiştirilmesin:** Seçilen alan varsayılan olarak bir değer getiriyorsa getirdiği değerin değiştirmemesini sağlar.

**Gridde göster:** Alanın gridde gösterilmesi gerekiyorsa ilgili kutucuk işaretlenir.

**Seçimde göster:** Alanın seçimde gösterilmesi gerekiyorsa ilgili kutucuk işaretlenir.

**Satır Sayısı:** İlgili alan çoklu satır ise, veri girişi ekranında kaç satır gözükmesi gerektiği belirlenir.

**Kolon Genişliği:** İlgili modülde girilen kayıtların listesinde (gridde) alanın kolon genişliği bilgisinin belirlenir. Verinin uzun olduğu alanlar için ort. 250, sadece rakam girilen alanlar için ise 75 kullanılması idealdir. Alana girilecek veriler düşünülerek bu aralıklarda bir değer kullanmak uygun olacaktır.

**Aktif Statü:** Alanın sisteme tanımlanan statülerin hangilerinde aktif olacağını belirler. Bu alanda işaretlenen statülerde ilgili alanın tipine göre işlem gerçekleştirilebilir. “Muayene Türü Tanımlama” menüsünde tanımlanan muayene türleri için işlem yapılır.

**Zorunlu Statü:** Alanın sisteme tanımlanan statülerin hangilerinde zorunlu olacağını belirler. İlişkili Sekme: Seçilen alanın, sistemde sekme tipli tanımlanan bir alanında altında gözükmesi isteniyorsa hangi sekmenin altında gözükeceği bilgisi seçilir. “Muayene Türü Tanımlama” menüsünde tanımlanan muayene türleri için işlem yapılır.

Gerekli tüm alanlar doldurulduktan sonra ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf0d45b5f-fca1-48da-aa9c-a45675a0db51) (Kaydet) butonuyla, ilgili alan için ilgili fonksiyon tanımlama işlemi gerçekleştirilir. Bu şekilde işbaşı ve periyodik muayene modülünde hangi alanların hangi fonksiyonda yer alacağı belirlenmiş olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload001d71fb-1b3f-404d-9f58-fb6f785b97df)

### **İlaç Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ İşbaşı ve Periyodik Muayene/ İlaç Tanımlama

Bakanlık sisteminde bulunan, e-reçete ile yazılabilen tüm ilaçlar sistemde tanımlı olarak gelmektedir. Genel sağlık sigortasının karşılamadığı, özel sigortaların karşıladığı ilaçların da sistemde kullanılması ve hekimler tarafından reçeteye yazılması isteniyorsa bu menüden tanımlaması gerekir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2110b1c9-0006-477b-a4a6-eefaf35437a6)

Ekranda bulunan butonlar yardımıyla;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d874145-1d55-44f4-ac00-b3563cac5798): Yeni bir ilaç eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload11e9e8e6-c78d-45fa-b7bf-7ee4a9ae9b80): Listede seçili olan ilaç güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload04f096f7-b165-45ba-a095-0afa225037c7): Listede seçili olan ilaç silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0f85514-289a-41ac-a554-b2ce810c82c8): Tanımlı olan tüm ilaç listesi excel’e aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload94a13b02-ace7-4ffd-bd57-642cc448a2e2): Kayıtlar filtrelenerek arama yapılır.

Sistemde yeni bir ilaç tanımlamak için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada65b5694-919b-45e5-a3fd-a5d0e31ce13f) (Yeni) butonuna tıklanarak “İlaç Tanımlama/ Yeni Kayıt” ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8c1000d2-cfd3-42fe-be89-59161ba13bb4)

Açılan ekranda ilgili alanlar tanımlanır;

**Barkod:** İlacın barkod bilgisi tanımlanır.

**İlaç:** İlacın adı tanımlanır.

**İlaç Medula Sistemine Gönderilmesin:** Medula adı verilen online sistem kısaca "reçete onay sistemi / reçete provizyon sistemi" şeklinde tanımlanmaktadır. GSS (Genel Sağlık Sigortası) kapsamındaki tüm ilaçların e-reçete onayı medula sisteminde gerçekleştirilir. Bir ilaç GSS kapsamında değilse medula sistemi tarafından ilaç onayı verilmez. GSS tarafından karşılanmayıp, özel sağlık sigortası tarafından karşılanabilecek ilaçların reçeteye yazılması durumunda o ilacın medula sistemine iletilmemesi için kullanılır.

Gerekli alanlar doldurulduktan sonra kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadde5e2ac3-a8a9-446f-80e6-0279f0027d74)

### **Aşı Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ İşbaşı ve Periyodik Muayene/ Aşı Tanımlama

Firma bünyesinde gerçekleştirilen ve takip edilen aşı işlemlerinin tanımlandığı menüdür

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeeb83089-551e-4926-ab0e-1a76f35d077d)

Ekranda bulunan butonlar yardımıyla;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d874145-1d55-44f4-ac00-b3563cac5798): Yeni bir aşı tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload11e9e8e6-c78d-45fa-b7bf-7ee4a9ae9b80): Listede seçili olan aşı güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload04f096f7-b165-45ba-a095-0afa225037c7): Listede seçili olan aşı silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0f85514-289a-41ac-a554-b2ce810c82c8): Mevcut aşı listesi excel’e aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload94a13b02-ace7-4ffd-bd57-642cc448a2e2): Kayıtlar filtrelenerek arama yapılır.

Sistemde yeni bir aşı tanımlamak için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada65b5694-919b-45e5-a3fd-a5d0e31ce13f) (Yeni) butonuna tıklanarak “**Aşı** Tanımlama/ Yeni Kayıt” ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload60b53904-d6f8-4719-84df-29a3a7a66d20)

Açılan ekranda ilgili alanlar tanımlanır;

**Adı:** Tanımlanan aşının adı bilgisi yazılır.

**Aşı Dozları:** Tanımlanan aşının doz miktarları ay bazında sisteme girilir. Doz zamanı geldiği zaman sistem tarafından uyarı verilir.

Doz alanında doz miktarı ve dozun hangi ay aralıklarla gerçekleştirileceği seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload18700b82-cf1f-41e1-99a8-398081495ff3) (Ekle) butonuna tıklanır. Örneğin: 2.Doz 6 Ay Sonra

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2b16b756-d657-4aaf-bd40-d7844ce4aea0)

**İlişkili Kullanıcı Grubu:** Sistemde tanımlanan aşının hangi kullanıcı gruplarına uygulanacağı seçilir.

Gerekli alanlar doldurulduktan sonra kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload17cb513c-1dc7-4b78-b01c-394a9b67303b)

Tanımlanan aşılar “Entegre Yönetim Sistemi/ Muayene Takibi/ Hemşirelik Hizmetleri” alanında “Enjeksiyon İşlemleri” kısmında listelenir.

Tanımlanan aşılar sistemde tanımlı olan hekimlerin ve hemşirelerin bekleyen işlerinde “Yapılacak Aşılar” olarak görüntülenir.

### **E-Posta Ayarları**

**Menü Adı:** Sistem Altyapı Tanımları/ İşbaşı ve Periyodik Muayene/ E-Posta Ayarları

İşbaşı ve Periyodik Muayene sürecinin hangi aşamasında kimlere mail gönderimi yapılacağı belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc597edab-79b2-4143-8487-5d0eed631739)

Muayene işleminin hangi basamağında mail gitmesi isteniyorsa, o basamak seçilerek ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf88cd549-ecc4-4826-b27e-32d93191a1ba)(Değiştir) butonuna tıklandığında roller ekranı gelir. İlgili aşamayla ilgili hangi rollere mail gideceği belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2398d459-acd9-47d4-ac6c-32bc58228f35)

Sistemde roller boş gelmektedir. Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Rol Tanımlama menüsünden roller tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada1496fc4-bb91-4096-8172-76a032c25b1e)

Yeni bir rol tanımlamak için ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb4be3f7a-50cb-4203-94f5-b1ada96f6122) (Yeni) butonuyla ekran açılır. Açılan ekranda ilgili modül seçilir, rol tanımı yazılır ve bulma yöntemi alanına rolün sorgusu yazılarak kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload15982547-a39e-4b98-b057-5084a1f79e52)

Roller tanımlandıktan sonra ilgili mesaj gövdelerinin tanımlanması gerekmektedir. Bunun için Sistem Altyapı Tanımları/ BSAT/ Tanımlar/ Mesaj Gövdesi Tanımlama ekranından yeni butonuyla mesaj gövdesi tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c783026-787d-43dd-b9e3-c59e1f1da0a3)

Örneğin, sevk bildirimi yapıldığı zaman mesaj gitmesi isteniliyorsa e-posta ayarlarından sevk bildirimi seçilir,![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf88cd549-ecc4-4826-b27e-32d93191a1ba) butonuna basılarak sevk bildirimi için E-Posta ayarlarının yapılacağı ekrana gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadefd349bb-c3fd-4f22-b317-d3490ea67cb9)

Açılan ekranda, sol tarafta roller sütunu bulunur. Bu, e-posta bildirimimin gideceği rolü yani kişiyi göstermektedir. Kime E-Posta gitmesi isteniyorsa, o rolle ilgili “E-Posta Gitsin Mi?” kutucuğu işaretlenir. Daha sonra gönderilecek e-posta’daki kullanılacak mesaj gövdesi seçilir. Bütün bu işlemlerden sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfaf50233-6b38-43d1-ad0d-e464894b8e20) (Kaydet) butonu ile yapılan ayarlar kaydedilir.

### **İş Başı ve Periyodik Muayene Parametreleri**

**Menü Adı:** Sistem Altyapı Tanımları/ İşbaşı ve Periyodik Muayene/ **İş Başı periyodik Muayene Parametreleri**

“İşbaşı ve Periyodik Muayene” Modülünde kullanıcının istek ve ihtiyaçlarına göre sistemsel ayarların yapıldığı ve bunlara göre parametrelerin belirlendiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6ebc9618-a65a-463f-b257-d6a6f627b089)

### **İş Yeri Hekimi Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Tanımlar/ İş Yeri Hekimi Tanımlama

Firma bünyesindeki iş yeri hekiminin sisteme tanımlandığı menüdür. “Eğitim Planlama” ve “İşbaşı ve Periyodik Muayene” modüllerinde kullanılmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0fe03893-e50d-4a48-8dc7-0bbfa84b2ab4)

Ekranda bulunan butonlar yardımıyla;

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload81dad6f1-5aa6-4e1e-8faa-1b49a86d2dcd): Yeni bir iş yeri hekimi tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload32b5ddb9-32f0-403c-8971-25063c432c47): Listede seçili olan iş yeri hekimi için değişiklik yapılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8373a01f-4411-49ca-a3f9-e66e4359a6c6): Listede seçili olan iş yeri hekimi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload94a13b02-ace7-4ffd-bd57-642cc448a2e2): Kayıtlar filtrelenerek arama yapılır.

Yeni bir iş yeri hekimi tanımlamak için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada65b5694-919b-45e5-a3fd-a5d0e31ce13f)(Yeni) butonuna tıklanarak “İş Yeri Hekimi Tanımlama/ Yeni Kayıt” ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload18bae62e-88ab-4a50-9907-181faf83f366)

Açılan ekranda “Personel” bilgisi sistemde tanımlı personel listesinden seçilir. Diploma No, Diploma Tarihi, İş yeri Hekimliği Belge Tarihi, İş yeri Hekimliği Belge No, E-Reçete Kullanıcı Adı ve Şifre bilgisi girilir. E-Reçete Kullanıcı Adı ve Şifre bilgisi olarak, hekimin medula sistemi (Medula Sistemi=Doktorların reçeteleri onaylatmak için kullandıkları reçete onay sistemi / reçete provizyon sistemi) kullanıcı adı ve şifre bilgisini tanımlaması gerekmektedir. İşyeri hekiminin bağlı bulunduğu iş yeri sistemde tanımlı iş yeri listesinden seçilir. Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf34b3f72-6c58-4f55-a2ec-72636b3e4f0a) (Kaydet) butonuna tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaf253d5a-fbaa-40d5-9a7d-9055e9bc7a1e)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2e44bd56-62c0-4767-aac5-09ad622fc645)

### **Muayene Aktarma**

**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Aktarımlar/ Muayene Aktarma

Firmada geçmişte gerçekleştirilen işbaşı ve periyodik muayene, poliklinik muayene, kurumdışı muayenesi, işe dönüş muayenesi gibi muayene türlerine ait tüm kayıtların QDMS sistemine toplu olarak aktarım işlemlerinin gerçekleştiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload006e7fda-81e6-4b7a-a6a6-6ff88f6c97d9)

Hangi muayene türü için aktarım yapılmak isteniyorsa o muayene türü seçilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload83ff7dff-1ae9-4768-8c52-48e74eb81713) (Şablon İndir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload21f36b3d-fe78-4c64-9955-6d673a8792b1)Aktarım şablonundaki gerekli bilgiler formata uygun olarak doldurulduktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbca7ff43-d944-4776-a67c-b5eeb4db8bf3) (Şablon Yükle) butonu ile sisteme yüklenir. Girilen bilgilerin kontrolünün sağlanması için ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf9951c6e-48d1-44db-9e23-283d8d54f086) (Kontrol Et) butonuna tıklanarak oluşturulan ve sisteme yüklenen şablonun hata verip vermediği kontrol edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f2f7a59-1b3e-4c41-985c-1ebd095054c4)

Aktarılan veriler aktarım için uygunsa ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload918c87db-44dd-4498-9c31-813279a324fa) (Aktar) butonu aracılığıyla aktarım işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5abda814-afdc-4960-8bcc-167be02f2b81)

### **Muayene Test Aktarma**

**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Aktarımlar/ Muayene Test Aktarma

Firmada geçmişte gerçekleştirilen işbaşı ve periyodik muayene kapsamında gerçekleştirilen detay testlere ait tüm kayıtların QDMS sistemine toplu olarak aktarım işlemlerinin gerçekleştiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload277b343d-b5f9-425e-a22c-951b118034e8)

Hangi muayene türü için test aktarımı yapılmak isteniyorsa o muayene türü seçilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload83ff7dff-1ae9-4768-8c52-48e74eb81713) (Şablon İndir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc2ba8ce6-5483-4a72-8a18-750171cc0426)

Test Aktarım Şablonu doldurularak kaydedilir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbca7ff43-d944-4776-a67c-b5eeb4db8bf3) (Şablon Yükle) butonu ile doldurulan şablon sisteme yüklenir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbf4bc1ac-951c-4303-a941-4635d893ccbc) (Kontrol Et) butonuna tıklanarak oluşturulan ve sisteme yüklenen şablonun hata verip vermediği kontrol edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf934af7b-8e7e-4bed-a1a1-e72e814587d0)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload918c87db-44dd-4498-9c31-813279a324fa) (Aktar) butonuna tıklanarak “Test Aktarma” işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada76f06e0-8dde-40dd-aac0-1ff19505059f)

## Entegre Yönetim Sistemi/ İşbaşı ve Periyodik Muayene

Tüm muayene işlemlerinin gerçekleştirildiği, hemşirelik hizmetlerinin gerçekleştirildiği, raporların görüntülendiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbe265465-60f2-4686-bf39-d778239a5209)

### **Muayene Takibi**

**Menü Adı:** Entegre Yönetim Sistemi/ İş Başı ve Periyodik Muayene/ Muayene Takibi

Personellerin seçilen muayene türüne göre muayenelerinin takip edildiği ekrandır. Açılan ekranda personeller tanımlı olarak gelmektedir. İşyeri hekimleri ve işyeri hemşireleri sadece bağlı oldukları işyerlerindeki çalışan personelleri ekranlarında görüntüleyebilmektedirler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload27c923ac-cb81-4911-b92a-e5df98ac21e5)

Ekranda bulunan butonlar yardımıyla;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0bb0c1c-721e-4dc3-9e2d-0461eaa97238): Listede seçili olan personel için yeni muayene takibi gerçekleştirilir

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf57618c7-4ad4-4829-a117-0d01ba71948d): Listede seçili olan personel için tansiyon takibi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd4aa3fca-712b-44af-b710-ed38310bf037): Listede seçili olan personel için hemşirelik hizmetleri gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload44124db4-2091-4b4e-8dd7-a61367e7e115): Listede seçili olan personel için sağlık özgeçmişi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload94a13b02-ace7-4ffd-bd57-642cc448a2e2): Kayıtlar filtrelenerek arama yapılır.

Bir personelin muayenesini gerçekleştirmek için ekranda ilgili personel seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload626a06a7-ee16-4820-912f-79c02ab68970)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload47539fff-07e5-40c0-a088-a220c0bb131a) (Yeni) butonu ile muayene tanım ekranına gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload362aa833-ad66-4b99-82ba-ed9d38a43225)

Hangi muayene gerçekleştirilecekse ilgili muayene türü seçilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload09a62b52-5551-4784-bf27-e7c1e7affd34) (İleri) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade96b3d0a-74b7-4dc9-97b9-76e622d4b86a)

Açılan ekran muayene türüne göre altyapıda kurgulanan ekrandır.

**Ana sekmede** tanımlanan alanlara göre ilgili bilgiler doldurulur. Alan tanımlamada tanımlanan alanlara göre ilgili tüm alanlar doldurulur. Varsa testler, fiziki/ psikolojik muayene gibi sekmeler doldurulur. (Bu alanların ekrana gelip gelmeyeceğine altyapılarda muayene türü tanımlarken karar verilir.)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1f4d61db-fbd4-4332-aaf6-e52abac4daf1)

**Özgeçmiş sekmesinde**; personelin hastalık özgeçmişi ile ilgili bilgilere ulaşılmaktadır. Bu sekmede çalışanların daha önce almış oldukları hekim ve hemşirelik hizmetleri, tansiyon takibi bilgileri yer almaktadır. Bu sekmede yeni işlemler yapılabilir, varolan kayıtlar görüntülenebilir, güncellenebilir, ilgili ek2 formu yazdırılabilir, muayene türlerine göre tanımlı olan rapor formatları sistemden alınabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload26a28640-f20e-4adf-b691-cc355f472184)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1f5849a0-c432-4082-ad08-2fbf28ab1a01) (Göster) butonuyla seçilen muayene için muayene özgeçmişi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3ee2aa3a-e2de-4206-ab1a-709da6147c57)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload80f30421-4357-404a-b56b-51df83fe3104) (Düzenle) butonuna tıklanarak “Muayene Takibi/ Kayıt Güncelleme” ekranı açılır. Açılan ekranda herhangi bir değişiklik yapılarak “Kaydet” butonu tıklanarak kayıt güncelleme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbd1b98a7-daa1-46a1-89d2-446ba979295f)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload36d726cd-915d-4f90-85a3-740c607eabc9) (Toplu Rapor) butonuna tıklanarak “Muayene Toplu Özgeçmiş Raporu” excel olarak görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload098573b6-49d8-450b-a48f-a44ce781f8cb)

**Fiziki/ psikolojik muayene sekmesinde;** sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload47539fff-07e5-40c0-a088-a220c0bb131a) (Ekle) butonuyla hangi muayenelerin yapılacağı seçilir. Eğer muayene türü tanımlama menüsünde zorunlu fiziki muayeneler tanımlandıysa bu sayfada görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5866b0e8-f116-4f38-8a60-ff9584e93674)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload11d6b425-940f-4caa-93eb-789d97029df2)

Açıklama kısmına muayene ilgili açıklama yazılabilir. Fiziki/ psikolojik muayene tanımlama menüsünde tanımlanan default açıklamalar varsa açıklama kısmında görüntülenir, bu tanımlar ihtiyaç halinde hekim tarafından bu ekrandan değiştirilebilir. Varsa ek dosya eklenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1cfc1806-528f-48c6-825a-5f1f4fd2b653)

**Testler sekmesinde;** sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload47539fff-07e5-40c0-a088-a220c0bb131a) (Ekle) butonuyla hangi testlerin yapılacağı seçilir. Eğer muayene türü tanımlama menüsünde zorunlu testler tanımlandıysa bu sayfada görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload873600fb-ada7-4482-a178-6a113fedc99e)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload784749a4-17f9-4a45-a01f-77822f657853)

Açıklama kısmına muayene ilgili açıklama yazılabilir. Test tanımlama menüsünde tanımlanan default açıklamalar varsa açıklama kısmında görüntülenir, bu tanımlar ihtiyaç halinde hekim tarafından bu ekrandan değiştirilebilir. Varsa ek dosya eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcae3bacf-3512-4579-bc9f-f41e775bfdea)

Testler kapsamında eğer şablon kullanılıyorsa tanımlanan test adına göre ayrı bir sekmede görüntülenir. Teste ait ilgili değerler excel üzerinde tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9b896743-8646-4564-b2b0-90dd481058fc)

**Sonuç sekmesinde;** altyapıda kurulan muayene türü ayarlarına göre çıkan muayene sonuç yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1679f7e0-79e8-42ed-a15b-3f1255ec7e36)

Açılan ekranda ilgili alanlar tanımlanır;

**Hekim Kanaati:** Muayene sonucuna göre işyeri hekimi hasta ile ilgili kanaatlerini tanımlar.

**Personel Durumu:** Muayene sonucuna göre eğer personelde özel bir durum/ engel söz konusu ise ilgili alandan seçim yapılır. Örneğin; yüksekte çalışamaz, vardiyalı işlerde çalışamaz, gebe gibi. Eğer personelin geçmiş muayenelerinde seçilen bir durumu varsa, bu alan otomatik dolu olarak gelir. QDMS’in herhangi bir modülünde görev atamak için, durumu tanımlanan bir personel seçildiği zaman, isminin yanında sarı ünlem işaretiyle birlikte, “doktorla/ amirinle görüşünüz” uyarısı görüntülenir. Böylece personele yapamayacağı bir işin atanmaması için uyarı verilir. Örneğin; yüksekte çalışma izni olmayan bir personele yüksekte çalışmayla ilgili bir görev atandığı zaman personel seçildiği anda adının yanında uyarı çıkmaktadır ve amirinden/ doktordan onay alınmadan personelin çalıştırılamayacağı bilgisi iletilmiş olmaktadır.

**Personel Durum Bitiş Tarihi:** Personelin seçilen durum bilgisi için bir bitiş tarihi varsa sistemden seçilir.

**Kontrol:** Eğer muayene sonucuna göre belirlenen süre sonunda bir kontrol yapılması gerekiyorsa “evet” olarak seçilir. Bu veri, genelde poliklinik muayenelerinde, işe dönüş kapsamında çalışanın yeniden muayene edilerek kontrol edilmesi amacıyla kullanılır.

Kontrol Tarihi: Kontrol bilgisinin “Evet” seçildiği durumlarda kontrolün hangi tarihte yapılacağını belirlemek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf09d4a1a-0d14-4429-812f-b6406f5ba0e8)(Sonuç Bildirim) butonuna tıklanarak e-posta ayarlarında belirtilen ilgili rollere sonuç bildirim mail gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4f8b9e77-85d2-4068-9f54-e75a281838db)

#### **Bekleyen İşlerim**

**Bekleyen Sağlık Kontrolleri;** Kontrol süresi gelen personelin muayene kontrolleri hekimin bekleyen işlerim sayfasında “Bekleyen Sağlık Kontrolleri” olarak görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4c5cb1d1-5931-427f-8951-7277a2227b8b)

**Bekleyen Sağlık Kontrolleriniz;** Hastaya kontrol zamanını hatırlatmak amacıyla çalışanın bekleyen işlerim sayfasında “Bekleyen Sağlık Kontrolleriniz” olarak görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade3da4bd5-4d41-40be-a98c-9b9ca4ac25ac)

**Bekleyen Sağlık Muayeneleri;** Muayene türü tanımlama menüsünde periyodik olarak belirlenen muayene türleri için periyot süresi geldiğinde hekimin bekleyen işlerim sayfasında “Bekleyen Sağlık Muayeneleri” olarak görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload204f0d6d-afe3-42b3-b6a2-fde5c7588ae8)

### **E-Reçete**

**Menü Adı:** Entegre Yönetim Sistemi/ İş Başı ve Periyodik Muayene/ Muayene Takibi

Muayene takibi menüsünde poliklinik muayenesi yapılacak personel listeden seçilir. Bir personele reçete yazılabilmesi için personelin “TC Kimlik No” ve “Cinsiyet” bilgileri sistemde tanımlı olmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload25977d84-ca5e-4ced-88a8-9205033b4732)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload47539fff-07e5-40c0-a088-a220c0bb131a) (Yeni) butonu ile muayene türü seçim ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload69e09fe7-e327-4670-a35c-c6e991340ddf)

Poliklinik muayene seçilerek, ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload09a62b52-5551-4784-bf27-e7c1e7affd34) (İleri) butonuna tıklanır.

**Ana sekmede** ilgili bilgiler tanımlanır, hastalık teşhisi seçilir. Muayene türünde testler ve fiziki/ psikolojik muayene sekmeleri kullanılacaksa ilgili veri girişleri yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadba4038ae-acc9-429b-adaa-80dcda6648f6)

“Hastalık Teşhisi” alanında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcec2b0c6-8854-4bb0-9abe-6bdf39c33640)(Ekle) butonu ile sistemde tanımlı olan hastalık listesinden hastalık seçim yapılabileceği gibi, ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcec2b0c6-8854-4bb0-9abe-6bdf39c33640)butonunun yanındaki alanda da manual olarak veri girişi yapılıp hastalık seçilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload72673115-8068-490c-bc11-3409ba89178f)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload70054459-eb4e-4472-82b2-4fc98011db2a)

Hastalık ismi yazılarak getirilmek istenirse; hastalığın ismi yazılarak aratılır ve hastalık teşhisi alanına eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9560aefe-36d1-4fd8-a828-c725b65a93da)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d89a9c8-cc7d-479a-ba93-9c15903e7e48)

**Sonuç sekmesi** tıklanarak Hekim Kanaati yazılır ve ilgili alanlar doldurulur. Eğer istirahat verilecekse sonuç alanından istirahat seçilerek rapor süresi tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload49e5b643-c697-4f0a-b75b-a267a8139a84)

Hastaya reçete yazmak için **Reçete sekmesi** tıklanır. Burada E-Reçete sistemi ile entegre reçete oluşturulabilmektedir. Reçete yazılması için hastalık teşhisi bilgisinin girilmesi zorunludur. Yazılan ilaç hangi reçete türünü kapsıyorsa Reçete Türü alanından ilacın reçete türü seçilir. Örneğin Normal, Kırmızı, Turuncu, Mor, Yeşil gibi.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload37398a07-9f4b-4afe-8746-f68740ebe2cc)

Reçete türü seçeneği ekranda normal seçilmiş olarak gelecektir. Hekim kırmızı, turuncu, mor, yeşil reçete kapsamında bir ilaç yazacaksa reçete türü olarak ilgili reçeteyi seçmesi gerekmektedir. Reçete türü normal seçildiği halde diğer reçete türlerinde bir ilaç yazılırsa sistem tarafından uyarı verilerek buna izin verilmemektedir. Ancak kırmızı, turuncu, mor ya da yeşil reçete türü seçilirse bu reçete içerisine bu kapsamdaki ilaçlar ile birlikte normal reçete türündeki ilaçlarda yazılabilmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5186609f-664a-4fb0-bca7-b129124357aa)

Ekranda bulunan butonlar yardımıyla;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cb33d7d-dc77-44a7-8811-cbf1c1c8e146): Reçete gönderilir. (imzasız).

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload254980c8-c804-49dc-972c-95f7bceb35db): İmzalı reçete gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbc27e4b6-0943-457e-835b-c0b6e4d711c7): Reçete yazdırılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbfdbfe29-9f67-4c27-9ea6-483f68ae5262): Reçete mail gönderilir.

Reçeteye ilaç yazmak için “Yeni Kayıt” linki tıklanarak açılan ekranda “İlaç Adı” yazan yerdeki “...” işaretli butona tıklanarak SGK veri tabanındaki ilaç listesi görüntülenir. Buradan reçeteye eklenecek ilaç seçilir. İlaç adına ve barkoda göre arama yapılabilir. Aynı işlem tekrarlanarak reçeteye istenildiği kadar ilaç eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload13e0ef51-d677-48b6-a47b-f6ff4d87f294)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9cfe9c39-35ab-4678-965e-bf55b8ac7760)

İlaç seçimi yapıldıktan sonra ilacın kullanım şekli, periyodu, periyot birimi, kaç kere, kaç kutu kullanılacağı bilgisi ve (varsa) açıklama alanları doldurulur. Güncelle linki tıklanarak ilacın reçete kaydedilmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1f2ba64c-3a2e-45e8-a7c1-825af4f0fd1d)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload254980c8-c804-49dc-972c-95f7bceb35db) (İmzalı Reçete Gönder) butonuna tıklanarak, işyeri hekiminin kendi E-İmza doğrulaması ile SGK onaylı gerçek E-REÇETE üretilir. E-Reçete No alanında da reçete numarası görüntülenir.

### **İş Başvurusu Muayenesi**

**Menü Adı:** Entegre Yönetim Sistemi/ İş Başı ve Periyodik Muayene/ İş Başvurusu Muayenesi

Henüz işe girişi yapılmamış, sistemde personel olarak tanımlı olmayan kişinin işe giriş muayenesini yapmak için kullanılan menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3cc18895-c527-4864-9884-dac68b8adf25)

Açılan ekranda ilgili alanlar tanımlanır;

**Sicil No:** Kayıtsız Hasta Giriş İşe Giriş Muayenesi ekranında Sicil No bilgisinin sistem tarafından verildiği alandır.

**Adı:** Kayıtsız Hasta Giriş İşe Giriş Muayenesi ekranında işe giriş muayenesi yapılan kişinin “Adı” bilgisinin girildiği alandır.

**Soyadı:** Kayıtsız Hasta Giriş İşe Giriş Muayenesi ekranında işe giriş muayenesi yapılan kişinin “Soyadı” bilgisinin girildiği alandır.

**TC Kimlik No:** Kayıtsız Hasta Giriş İşe Giriş Muayenesi ekranında işe giriş muayenesi yapılan kişinin “TC Kimlik No” bilgisinin girildiği alandır. Sistem tarafından geçici olarak sicil numarası verilir. Bu numara kişinin işe girişi onaylandıktan sonra sistemde düzeltilir.

**Cinsiyet:** Kayıtsız Hasta Giriş İşe Giriş Muayenesi ekranında işe giriş muayenesi yapılan kişinin “Cinsiyet” bilgisinin seçilebildiği alandır.

**Doğum Tarihi:** Kayıtsız Hasta Giriş İşe Giriş Muayenesi ekranında işe giriş muayenesi yapılan kişinin “Doğum Tarihi” bilgisinin seçilebildiği alandır.

**İş Yeri:** Kayıtsız Hasta Giriş İşe Giriş Muayenesi ekranında işe giriş muayenesi yapılan kişinin çalışması planlanan “İş Yeri” bilgisinin seçilebildiği alandır.

Açılan ekranda sicil no alanına geçici sicil nosu, adı, soyadı ve diğer bilgiler girilerek kaydedilir. Açılan ekranda “İşe Giriş Muayenesi” seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3a68e534-11a0-4edf-995a-246daf30f32c) (İleri) butonuna tıklanır ve muayene işlemi gerçekleştirilerek tamamlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload972ecf94-67e5-4551-ada0-c5fbc8ffca08)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5548ac64-3637-4d51-82f8-520a726f1d68)

Muayenesi yapılan kişi için ilgili birimler tarafından işe giriş onayı verildikten sonra, kişinin personel listesine tanımlanması gerçekleştirilir ve kişiye gerçek sicil numarası verilir. İş başvurusu muayenesi ekranında kişiye verilen geçici sicil numarasının, işe girişten sonra verilen gerçek sicil numarası ile değiştirilmesi gerekir. Bunun için; Sistem Altyapı Tanımları/ BSAT/ Tanımlar/ İşe Giriş Muayenesi Sonuçlandırma menüsü açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada67a4577-e5a2-4eb6-a0a5-5684831029c5)

İşe girişi gerçekleştirilen kişi listeden seçilerek, ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcf06e74b-5533-4f3e-b860-7ee2c1fd3f55) (Değiştir) butonu ile “Personel Tanımlama-Kayıt Güncelleme” ekranı açılır. “Kayıtlı Personelden Seç” alanından ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5bf60753-e671-4dab-93af-d822dab45323) (Seç) butonu ile tanımlı personel listesi görüntülenir. Muayenesi gerçekleştirilen, personel listesine tanımlanmış olan kişi, personel listeden seçilir. Değiştirilmek istenilen bilgiler varsa düzenlenir ve kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade6b9353b-fdf9-4a2d-8cd9-033757bf0230)![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc5bd0334-c295-49ba-bd3c-d92d5fbfc31c)![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload895b4d94-deca-4208-9bb3-04ae00356e19)

Böylece geçici sicildeki muayene bilgileri asıl sicile aktarılmış olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload174b5b94-1b6e-4e5e-a9b9-78365ef78de8)

### **Kurum Dışı Muayene**

**Menü Adı:** Entegre Yönetim Sistemi/ İş Başı ve Periyodik Muayene/ Kurum Dışı Muayene

Dışarda yapılan muayenelerin, hastalık işlemlerinin, hastalık raporlarının işyeri hekimi veya işyeri hemşiresi tarafından sisteme girilmesinin sağlandığı menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb8ca6166-3d59-44d2-8f4d-02086eb960c9)

Kurumdışı muayenesi bilgi girişi yapılacak personel muayene takibi ekranından seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload748f5789-2e18-47c4-8060-5cf5c2ebb2a6)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload47539fff-07e5-40c0-a088-a220c0bb131a) (Yeni) butonuna tıklanarak açılan sayfada muayene türü olarak “Kurum Dışı Muayene” seçilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload09a62b52-5551-4784-bf27-e7c1e7affd34) (İleri) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload53a7b82d-e007-429b-aecf-c21b5e5b099f)

Açılan ekranda muayene türü seçildikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload09a62b52-5551-4784-bf27-e7c1e7affd34) (ileri) butonuna basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload55a352e6-0252-4245-b6a9-932a24eb0a40)

Muayene türüne göre altyapıda kurgulanan görüntülenir. Kurumdışı muayene ekranında görüntülenmesi istenilen, veri girişi yapılacak bilgiler altyapıda tanımlanmış olmalıdır. Ana sekmede tanımlanan alanlara göre ilgili bilgiler doldurulur ve kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload512d08ab-89a3-4eec-82cf-1115cc584ca1)

### **Misafir Hasta Kayıt**

**Menü Adı:** Entegre Yönetim Sistemi/ İş Başı ve Periyodik Muayene/ Misafir Hasta Kayıt

Firmanın çalışanı olmayan ziyaretçi, danışman gibi kişilerin, işyeri hekimi tarafından muayenesinin yapıldığı menüdür. Kayıtsız hasta işe giriş muayenesini yapılır. Sistem tarafından otomatik bir sicil numarası verilir. Misafir kişiye ait adı, soyadı, T.C. kimlik no, cinsiyeti, doğum tarihi ve hangi işyerinde bulunduğu bilgisi sistemde tanılanır ve kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc2e7fa75-2d84-47f9-9001-8ee8d45a6680)

Açılan ekranda muayene türü olarak “Poliklinik” seçilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload09a62b52-5551-4784-bf27-e7c1e7affd34) (İleri) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc69a41a5-a6cd-43a2-8b23-e82fecfb0be5)

Muayene Takibi menüsünde yapılan işlemler aşama aşama aynı şekilde gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload36cf742f-ad5e-4a2c-a169-610224ebbbe6)

### **Tansiyon Takibi**

**Menü Adı:** Entegre Yönetim Sistemi/ İş Başı ve Periyodik Muayene/ Muayene Takibi

Muayene takibi listesinde seçili olan personel için tansiyon bilgilerinin sisteme tanımlanması ve takip işleminin gerçekleştirilmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload27c923ac-cb81-4911-b92a-e5df98ac21e5)

Muayene Takibi ekranında listeden seçilen personel için ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5757265b-78b9-4054-b919-03c3e88bec34) (Tansiyon Takibi) butonu ile tansiyon takibi ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload71be37f3-104a-4392-96e8-6fb1f62dc174)

Ekranda bulunan butonlar yardımıyla;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d874145-1d55-44f4-ac00-b3563cac5798)**:** Yeni bir hasta tansiyon bilgisi eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload11e9e8e6-c78d-45fa-b7bf-7ee4a9ae9b80): Listede seçili olan hasta tansiyon bilgisi güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload04f096f7-b165-45ba-a095-0afa225037c7): Listede seçili olan hasta tansiyon bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0f85514-289a-41ac-a554-b2ce810c82c8): Mevcut hasta tansiyon listesi excel’e aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload94a13b02-ace7-4ffd-bd57-642cc448a2e2): Kayıtlar filtrelenerek arama yapılır.

Sistemde seçilen personele ait yeni bir tansiyon bilgisi eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada65b5694-919b-45e5-a3fd-a5d0e31ce13f) (Yeni) butonuna tıklanarak “Tansiyon Takibi - Yeni Kayıt” ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9cf7417f-2529-4538-a8cf-63088c309b32)

Büyük tansiyon, küçük tansiyon ve hasta durumu hakkında açıklama bilgisi tanımlandıktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf34b3f72-6c58-4f55-a2ec-72636b3e4f0a) (Kaydet) butonuna tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadef54bdb3-da6a-4741-964a-4fe0727c872a)

### **Hemşirelik Hizmetleri**

**Menü Adı:** Entegre Yönetim Sistemi/ İş Başı ve Periyodik Muayene/ Muayene Takibi

Muayene takibi listesinde seçili olan personel için enjeksiyon, pansuman, ilaç verme gibi hemşirelik hizmetlerinin gerçekleştirilmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload27c923ac-cb81-4911-b92a-e5df98ac21e5)

Muayene Takibi ekranında listeden seçilen personel için ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0ec4b133-b1f3-47b6-989b-0f57efbc1fa2) (Hemşirelik Hizmetleri) butonu ile enjeksiyon, pansuman, ilaç verme işlemleri gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3a3d66b7-1714-41ad-bfbf-e8400c203229)

Ekranda bulunan butonlar yardımıyla;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d874145-1d55-44f4-ac00-b3563cac5798)**:** Yeni bir hemşirelik hizmetleri bilgisi eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload11e9e8e6-c78d-45fa-b7bf-7ee4a9ae9b80):Listede seçili olan hemşirelik hizmetleri bilgisi güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload04f096f7-b165-45ba-a095-0afa225037c7):Listede seçili olan hemşirelik hizmetleri bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0f85514-289a-41ac-a554-b2ce810c82c8): Mevcut hemşirelik hizmetleri listesi excel’e aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload94a13b02-ace7-4ffd-bd57-642cc448a2e2): Kayıtlar filtrelenerek arama yapılır.

Sistemde seçilen personele ait gerçekleştirilen yeni bir hemşirelik hizmeti bilgisi eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada65b5694-919b-45e5-a3fd-a5d0e31ce13f) (Yeni) butonuna tıklanarak “Hemşirelik Hizmetleri Takibi - Yeni Kayıt” ekranı görüntülenir. “Yapılan İşlem” alanında hastaya gerçekleştirilen işlem “Enjeksiyon, İlaç verme, Pansuman” seçeneklerinden seçilir.

Eğer ilaç verme veya pansuman seçilirse, sadece açıklama bilgisinin girilebileceği alan görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfa57ee0a-1f97-4353-973f-564ea3ae1517)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload622cd322-15d1-40ba-aa57-f34f23f4a47b)

Yapılan işlem enjeksiyon seçilirse, sistem altyapı tanımları kısmında aşı tanımlama menüsünde sisteme tanımlanan aşı listesi ve ilişkili doz bilgisi görüntülenir. “Açıklama” alanında yapılan işlem açıklamasına ait bilgi girişi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadebc434fa-a555-4524-9f9d-8260d02bde76)

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf34b3f72-6c58-4f55-a2ec-72636b3e4f0a) (Kaydet) butonuna kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3c0f6bca-2c2a-436d-99ec-0a2d2ed3949d)

### **Muayelerim**

**Menü Adı:** Entegre Yönetim Sistemi/ İş Başı ve Periyodik Muayene/ Muayenelerim

İşbaşı ve Periyodik Muayene/ E-Reçete Modülünde Muayane olan persolenin kendi muyane kaydının görüntülendiği menüdür. Bu menü tıklandığında personele özel Muayane Özgeçmiş ekranı gelir ve açılan Muayene Özgeçmişi ekranında login olan personel kendine ait Muayene özgeçmişi ile ilgili hastalık kayıtlarını bu menüde görüntülenir. Bu menü ile personellerin kendine ait hastalık özgeçmişi ile ilgili tüm ayrıntılı bilgilere ulaşılması ve görüntülenmesi sağlandı.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4e53eb1e-b036-41aa-ac69-fadb76898c6f)

Açılan Muayelerim menüsünde Muayene Özgeçmişi ekranında Muayene Listesi, Hemşirelik Hizmetleri, Tansiyon Takibi ve Filtre sekmeleri bulunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadce9415d6-2274-42e1-a718-9609dd8f2c38)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1f5849a0-c432-4082-ad08-2fbf28ab1a01) :Listede seçili muayene için muayene özgeçmişi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload94a13b02-ace7-4ffd-bd57-642cc448a2e2): Kayıtlar filtrelenerek arama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1f5849a0-c432-4082-ad08-2fbf28ab1a01) (Göster) butonu tıklanarak seçilen muayene için muayene özgeçmişi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload647d70f4-abdc-42cd-937e-e575ce537fa8)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload31e27e16-47c5-4cee-bd0e-a38ead0550fc) Geri butonu ile ana ekrana geri dönülür.

**Muayene Listesi Sekmesi;**

Muayelerin menüsünde açılan Muayene Özgeçmişi ekranında login olan personel kendine ait Muayene özgeçimişi ile ilgili hastalık kayıtlarının listelendiği sekmedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload66726b7a-824b-42c6-adf5-6ffdb65348b3)

**Hemşirelik Hizmetleri Sekmesi;**

Muayelerim menüsünde Muayene özgeçmişi ekranında seçili olan personel için sistemde tanımlı enjeksiyon, pansuman, ilaç verme gibi hemşirelik hizmetlerinin listesinde işlemleri görüntülendiği sekmedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload234b0e89-b4b3-4185-864e-d54a533efa0c)

**Tansiyon Takibi Sekmesi;**

Muayelerim menüsünde Muayene özgeçmişi ekranında seçili olan personelin tansiyon takibi listesinde sisteme tanımlı tansiyon işlemlerinin görüntülendiği sekmedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9a7dd1d4-7d02-4d8d-b5ad-bf266207d4f2)

**Filtre Sekmesi;**

Muayelerim menüsünde Muayene özgeçmişi ekranında Filtre sekmesinde arama kriterlerine göre filtreleme yapıldığı sekmedir. Filtre sekmesinde Muayene Tarihi, Hastalık Teşhisi, Hekim Kanaati, Sonuç ve Kontrol alanlarına göre ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload94a13b02-ace7-4ffd-bd57-642cc448a2e2)(Ara) butonu tıklanarak filtreleme işlemleri yapılır. Örnekte Muayene Tarihi alanında Takvim alanında tarih seçimi yapılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload94a13b02-ace7-4ffd-bd57-642cc448a2e2)(Ara) butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd8091eea-881d-407a-95ba-c5ebfe5b058d)

Seçilen tarih aralığında personelin Muayene Özgeçmiş ekranında Muayene listesinde sekmesinda hastalık kayıt geçmişi listelenir ve isterse ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1f5849a0-c432-4082-ad08-2fbf28ab1a01)(göster) butonu tıklanarak hastalık kaydı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada80299ea-2d3f-4224-bfb0-9716ba54dbd9)

Aynı şekilde belirlenen tarih aralığında Personelin Hemşirelik Hizmetleri sekmesinde Hemşerilikle ilgili yapılan işlemlerin ve Tansiyon Takibi sekmesinde Tansiyon işlemlerin kayıt bilgilerine ulaşılır.

### **Revir Başvuru Formu**

Personellerin rahatsızlıkları nedeni ile revir gitmek için başvuru yapıldığı menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd86e687c-3f0e-4df0-8bfe-1d7e0b973bf6)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Hasta:**Revir Başvuru Formu- Yeni Kayıt ekranında hastanın adı ve soyadı bilgisinin sistemde tanımlı personel listesinde seçildiği alandır.

**İş yeri:** Revir Başvuru Formu- Yeni Kayıt ekranında hastanın işyeri bilgisinin sistem tarafında otomatik olarak bilgisinin girildiği alandır. Hastanın iş yeri bilgisi SAT/BSAT/Tanımlar/Personel Tanımlama menüsünde tanımlı ise sistem otomatik olarak iş yeri bilgisi otomatik olarak işyeri alanına verir. Personel Tanımlama menüsünde tanımlı olmadığında iş yeri alanında sistemde tanımlı işyeri listesinde seçim yapılır.

**Başvuru Tarihi:** Revir Başvuru Formu- Yeni Kayıt ekranında revir başvuru tarihi ve saat bilgisinin açılan Takvim alanında seçildiği alandır.

**Başvuru Sebebi:** Revir Başvuru Formu- Yeni Kayıt ekranında hastanın revire başvurma sebebinin bilgisinin girildiği alandır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload738ec2b3-68dd-4dd6-9a85-9e21c78413a5)

Sistem tarafından “Revir başvurusunu onaya göndermek istediğinizden emin misiniz?” uyarı mesajı tamam butonu tıklanarak revir başvurusunu işlemi tamamlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5fdfb6e3-84fa-4553-9bcc-88889b56aaf8)

### **Raporlar**

**Menü Adı:** Entegre Yönetim Sistemi/ İş Başı ve Periyodik Muayene/ Raporlar

“İş Başı ve Periyodik Muayene Modülü” kapsamında sistemde yapılan muayene işlemlerine göre sistem tarafından oluşturulan takip raporların görüntülendiği menüdür.

#### **Aylık Muayene Sayısı Raporu**

**Menü Adı:** Entegre Yönetim Sistemi/İş Başı ve Periyodik Muayene/ Raporlar/ Aylık Muayene Sayısı Raporu

Sistemde gerçekleştirilen muayeneler için aylık olarak raporların alındığı menüdür. Hangi muayene türünde hangi ay/ yılda kaç tane muayene gerçekleştirildiği görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6658e754-4c3a-4a0d-9abb-d5bf383cba89)

Hangi yıla ait rapor oluşturulmak isteniyorsa, yıl bilgisi listeden seçilir. İşyeri ve/ veya departman seçimi yapılarak işyeri bazlı, departman bazlı sistemde aylık raporlar oluşturulabilir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload60e3cd14-d755-4c3e-95de-58668a342a2f) (Excel’e Aktar) butonuna tıklanarak “Aylık Muayene Sayısı Raporu” görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3a2f2a79-ddd6-4532-a8ef-f354385c5a34)

#### **Yapılacak Periyodik Muayene Raporu**

**Menü Adı:** Entegre Yönetim Sistemi/ İş Başı ve Periyodik Muayene/ Raporlar/ Yapılacak Periyodik Muayene Raporu

Yapılacak periyodik muayenelere ait raporun alındığı menüdür. Yapılması gereken tüm periyodik muayeneler bu listede görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4f70f593-3f76-463a-ac77-4989fbc0d174)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload60e3cd14-d755-4c3e-95de-58668a342a2f) (Excel’e Aktar) butonuna tıklanarak “Yapılacak Periyodik Muayene Raporu” oluşturulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload71d7e65a-f855-41a5-bd97-d4b4846cb8d1)

#### **Muayene Log Raporu**

**Menü Adı:** Entegre Yönetim Sistemi/ İş Başı ve Periyodik Muayene/ Raporlar/ Muayene Log Raporu

Sistemde gerçekleştirilen tüm muayene işlemlerine ait yapılan tüm kayıtları gösteren rapordur. Kim, hangi hasta için, hangi tarihte, hangi işlemi gerçekleştirmiş (muayene kayıt, Ek-2 formu yazdırma, muayene detayı görüntüleme, muayene güncelleme, vb.) olduğuna dair tüm kayıtlar sistemde kayıt altına alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3e072bb5-11ce-4362-965a-01174c444f72)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload60e3cd14-d755-4c3e-95de-58668a342a2f) (Excel’e Aktar) butonuna tıklanarak “Muayene Log Raporu” oluşturulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload897710c1-5539-462f-9410-9d09a66de065)

#### **En Çoklar Analizi**

**Menü Adı:** Entegre Yönetim Sistemi/ İş Başı ve Periyodik Muayene/ Raporlar/ En Çoklar Analizi

Sistemde “hastalık, ilaç, muayene sonucu” kapsamında X ekseninde seçilen değere göre, en çok hangi hastalığın olduğu/ ilacın kullanıldığı/ muayene sonucunun olduğu verisi grafik şeklinde raporlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload197cf471-d838-42a0-81f6-d7dfa7caf38d)

En Çoklar Analizi ekranında, grafik seçenekleri bölümünde gerekli seçimler gerçekleştirilir. Grafikte olması istenen veri sayısı “en çok” alanında belirlenir. Grafik Seçeneklerinden X ekseninde yer alması istenen nitelik seçilir. Ana tema, renk paleti özelliklerinden grafik özelleştirilebilir. Grafik başlığı belirtilerek grafik oluşturmak için ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbce8b9c4-066c-4571-91fa-22f30c735e3a) (Grafik Çiz) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1a0a4844-faca-4abc-bbff-1c93e86fdd91) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8bc970fa-04ff-4301-bdb1-59f69a85c195)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload60e3cd14-d755-4c3e-95de-58668a342a2f) (Excel’e Aktar) butonuna tıklanarak “Muayene Listesi Raporu” oluşturulur.

#### **Muayene Listesi Raporu**

**Menü Adı:** Entegre Yönetim Sistemi/ İş Başı ve Periyodik Muayene/ Raporlar/ Muayene Listesi Raporu

Yapılan tüm muayeneleri türlerini gösteren rapordur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc8ddf405-131f-4649-bd27-412c3d8f7abf)

Filtre sekmesinden muayene türü, sonuç (istirahat, sevk, işe devam) gibi farklı filtrelere göre arama yapılarak istenile muayene listesi raporu görüntülenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3d2de640-6044-4079-8c67-a30c5e16bee2)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload60e3cd14-d755-4c3e-95de-58668a342a2f) (Excel’e Aktar) butonuna tıklanarak “Muayene Listesi Raporu” oluşturulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5e473b1b-8a32-4765-a968-b2b98d05dc44)

#### **Personel Raporu**

**Menü Adı:** Entegre Yönetim Sistemi/İş Başı ve Periyodik Muayene/ Raporlar/ Personel Raporu

QDMS’te tanımlı personel listesine ait kan grubu, medeni durumu, kronik hastalık bilgisi gibi ek alanların görüntülendiği rapordur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9ce9a9be-5301-4d0d-96be-c44978571464)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload60e3cd14-d755-4c3e-95de-58668a342a2f) (Excel’e Aktar) butonuna tıklanarak “Personel Raporu” görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadde331813-a158-4f24-81f5-69f6e2f0b380)

#### **Muayene Test Raporu**

**Menü Adı:** Entegre Yönetim Sistemi/ İş Başı ve Periyodik Muayene/ Raporlar/ Muayene Test Raporu

Muayene sırasında girilen test değerlerinin gösterildiği rapordur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd867ee1f-9b88-4c55-9be0-3a787cd80ceb)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload60e3cd14-d755-4c3e-95de-58668a342a2f) (Excel’e Aktar) butonuna tıklanarak “Muayene Listesi Raporu” oluşturulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6805a51e-8231-4dca-9bf5-ff1e66a8cef2)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3f812ddb-5542-42e3-b1f2-a21cf4e79843) (Test Raporu) butonuna tıklanarak “Muayene Test Raporu” oluşturulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1916a822-b83c-4c55-8e17-ae230ecd3fb8)

#### **Tansiyon Takip Raporu**

**Menü Adı:** Entegre Yönetim Sistemi/ İş Başı ve Periyodik Muayene/ Raporlar/ Tansiyon Takip Raporu

Hastaların tansiyon takibini gösteren rapordur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfcb16e52-e157-4f82-80f9-6ee816521edb)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload60e3cd14-d755-4c3e-95de-58668a342a2f) (Excel’e Aktar) butonuna tıklanarak “Tansiyon Takip Raporu” görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3a372570-184b-4bc9-a28f-457b6d10879e)

#### **Hemşirelik Hizmetleri Raporu**

**Menü Adı:** Entegre Yönetim Sistemi/ İş Başı ve Periyodik Muayene/ Raporlar/ Hemşirelik Hizmetleri Raporu

Gerçekleştirilmiş olan enjeksiyon, pansuman, ilaç verme işlemleri kapsamındaki hemşirelik hizmetlerin görüntülendiği rapordur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9f5f98c0-e06f-46cd-9e14-dcc20bce9131)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload60e3cd14-d755-4c3e-95de-58668a342a2f) (Excel’e Aktar) butonuna tıklanarak “Hemşirelik Hizmetleri Raporu” görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8bcedba2-adf3-4ece-b68d-8a0076c70d59)

#### **İstirahat Raporu**

**Menü Adı:** Entegre Yönetim Sistemi/ İş Başı ve Periyodik Muayene/ Raporlar/ İstirahat Raporu

İstirahat verilmiş hastaların listesinin görüntülendiği rapordur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9f7c5473-ff0c-4b99-ab77-bbda78e5822a)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload60e3cd14-d755-4c3e-95de-58668a342a2f) (Excel’e Aktar) butonuna tıklanarak “İstirahat Raporu” görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9c1053b1-8f41-40dc-95d9-334b61f7cedb)
