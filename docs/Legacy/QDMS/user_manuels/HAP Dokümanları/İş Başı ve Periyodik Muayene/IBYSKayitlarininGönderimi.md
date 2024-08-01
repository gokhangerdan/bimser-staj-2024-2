---
title: IBYS Kapsamında Sağlık Kayıtlarının Gönderimi
description: IBYS Kapsamında Sağlık Kayıtlarının Gönderimi Yardım Dokümanı
sidebar_position: 2
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::


**IBYS Kapsamında Sağlık Kayıtlarının Gönderimi**


# **1.IBYS KAPSAMINDA SAĞLIK KAYITLARININ GÖNDERİMİ**

Sağlık kayıtlarının bakanlığa gönderilebilmesi için, muayene olan personelin TC Kimlik numarası, personel tanımında işyeri bilgisi, ilgili iş yerinin iş yeri tanımlama sayfasında iş yeri sgk numarası bilgisinin dolu olması gerekmektedir. Hekim muayene tarihinde, SGK kayıtlarında sorumlu olduğu işyerinin çalışan kaydını gönderebilir.

## 1.1.Sistem Altyapı Tanımları/ İş Başı ve Periyodik Muayene

IBYS kapsamında sağlık kayıtlarının gönderimi için “İşbaşı ve Periyodik Muayene Modülü”nün altyapısını oluşturmak amacıyla gerekli tanımlamalar yapılır. Yapılan tanımlamalara göre giriş ekranında veriler kullanılmaktadır.

### **1.1.1.Muayene Türü Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ İşbaşı ve Periyodik Muayene/ Muayene Türü Tanımlama

“İşe Giriş Muayenesi, Periyodik Muayene, Poliklinik, İşe Dönüş Muayenesi, Kurumdışı Muayene, Gebe Takibi, Engelli Takibi” gibi muayene türlerinin tanımlandığı menüdür. Tanımlanan muayene türleri “Fonksiyon Dizayner” menüsünde “Statü” olarak görüntülenmektedir. Böylece sistemde kullanılmak üzere tanımlanan alanların, hangi statüde (muayene türünde) görüntüleneceği belirlenir. Tanımlanan bu muayene türleri muayene takibi ekranında listelenerek, hangi muayene gerçekleştirilecekse o muayene türünün görüntülenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9575c2fa-ef19-4c48-a8d3-3e74ba7c3ad9)


**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadff3825b7-6750-4409-868f-4daa9746ea20):Yeni bir muayene türü tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0c6b6d08-e4a4-4c74-af7d-d2fc0d3d10ba): Listede seçili olan muayene türü bilgisi güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload02bc4c38-193f-4b6c-a610-ca37753fc139): Listede seçili olan muayene türü bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4eb56777-a3b1-4560-b38e-4e638f4ae5d2): Listede seçili olan muayene türü bilgisi için rapor formatı tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2c7d68b1-ea52-4387-beb4-7db4c1fca781): Kayıtlar filtrelenerek arama yapılır.

Yeni bir muayene türü eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada60154ad-336d-444d-ac5a-e1eb9f1e02d5) (Yeni) butonuna tıklanarak “Muayene Türü Tanımlama/ Yeni Kayıt” ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb5f37ac-b03c-4375-b5d1-d72a000a115f)

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

Muayene Türü Tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload813856b3-24f5-49b9-a37e-b7fbf3aea278) (Kaydet) butonuna tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5c980a75-b491-478f-b0d4-8fb119c1f454)

Sistem Altyapı Tanımları/ İşbaşı ve Periyodik Muayene**/ İş Başı periyodik Muayene Parametreleri menüsü tıklanarak** Muayene tanımlama ekranında tanımlanan Muayene Türlerine ait ID bilgileri İş başı Periyodik Mauyene Parametrelerinden uygun parametrelerin parametre değerlerine yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload296f47f2-7ba7-41b7-9b33-e40714fb9e05)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d7f450d-f8aa-4191-8427-64c87d86154b) :Listede seçili parametre güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2c7d68b1-ea52-4387-beb4-7db4c1fca781) : Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload261c3eda-ba06-4a6d-a600-0db01d946d1d) : Veriler Excel’ e aktarılabilir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d7f450d-f8aa-4191-8427-64c87d86154b)Güncelle butonu tıklanarak parametrenin değer bilgisinin girilmesi işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload77d426e5-4d68-4d21-8b4b-93b4af9259ca)

43 numaralı Periyodik Muayene Türü ID parametresine göre tanımlanan Periyodik Muayene türünün ID’sinin numarası parametre değerine yazılır ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload813856b3-24f5-49b9-a37e-b7fbf3aea278) (kaydet) butonu tıklanarak parametre güncelleme kayıt işlemi gerçekleştirilir. Sisteminde bu muayene türlerinden birden fazla olabilir.Her birinin ID numarasını istenirse parametreye virgül ile ayrılarak parametre değerine yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd0ea704e-4b42-4458-8eeb-1bfe5502410d)

Muayene türü ID bilgilerini İş Başı ve Periyodik Muayene Modülü parametrelerinde uygun parametrelere değer olarak yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload77bcb337-f0de-4233-9910-1d92ba39d2b4)

### **1.1.2.Test Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ İşbaşı ve Periyodik Muayene/ Test Tanımlama

İşbaşı ve periyodik muayenesi gibi muayene türleri için yapılması gereken testlerin tanımlandığı menüdür. Tanımlanan bu testler seçilen muayene türlerine göre testler sekmesinde görüntülenmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadac43e56f-6083-47fa-9b5e-be027863d085)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadff3825b7-6750-4409-868f-4daa9746ea20): Yeni bir test tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0c6b6d08-e4a4-4c74-af7d-d2fc0d3d10ba): Listede seçili olan test bilgisi güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload02bc4c38-193f-4b6c-a610-ca37753fc139) : Listede seçili olan test bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2c7d68b1-ea52-4387-beb4-7db4c1fca781): Kayıtlar filtrelenerek arama yapılır.

Yeni bir test eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada60154ad-336d-444d-ac5a-e1eb9f1e02d5) (Yeni) butonuna tıklanarak “Test Tanımlama/ Yeni Kayıt” ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4bc70d0-a2af-4401-a97b-7f0510ce9346)

**Açılan ekranda ilgili alanlar tanımlanır;**

**Adı:** Testin adının tanımlanır.

**Zorunlu Departmanlar:** Tanımlanan test bilgisini hangi departmanlar için zorunlu olduğu bilgisi sistemde tanımlı olan departman listesinden seçilir.

**Default Açıklama:** Muayene işlemlerini gerçekleştirirken ilgili testin açıklama alanında gelmesi istenilen sabit bir açıklama varsa bu alanda tanımlanır. Örneğin; “normal sınırlar içerisinde” açıklaması.

**Şablon Kullanılsın:** Yapılan testle ilgili detaylı olarak sonuçların girilmesi ve bir excel formatında görüntülenmesi isteniyorsa “Şablon Kullanılsın” check box’ı işaretlenir.

**Rapor Şablonu:** Tanımlanan teste ait detay değerlerin girileceği şablon adının tanımlaması yapılır. Rapor formatı düzenleme menüsünden ilgili test şablonunun sisteme yüklenmiş olması gerekir.

**Alt Testler:** Tanımlana teste ait incelenecek detay değerlerin neler olduğu tanımlanır.

“Test Tanımlama” ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload813856b3-24f5-49b9-a37e-b7fbf3aea278) (Kaydet) butonuna tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload33f7fa0d-548b-42b3-92ae-3a7910abfa8a)

Sistem Altyapı Tanımları/ İşbaşı ve Periyodik Muayene**/ İş Başı periyodik Muayene Parametreleri menüsü tıklanarak** Test tanımlama ekranında tanımlanan Testlere ait ID bilgileri İş Başı Periyodik Mauyene Parametrelerinden uygun parametrelerin parametre değerlerine yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfef82429-c8e0-40a0-93ac-8b8873b85f72)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d7f450d-f8aa-4191-8427-64c87d86154b) :Listede seçili parametre güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2c7d68b1-ea52-4387-beb4-7db4c1fca781) : Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload261c3eda-ba06-4a6d-a600-0db01d946d1d) : Veriler Excel’ e aktarılabilir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d7f450d-f8aa-4191-8427-64c87d86154b)Güncelle butonu tıklanarak parametrenin değer bilgisinin girilmesi işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload24fcce9b-19fd-495d-83eb-209457f22821)

49 numaralı Kan testi ID veya alt testi parametresine göre Tanımlanan Testin ID’sinin numarası parametre değerine yazılır ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload813856b3-24f5-49b9-a37e-b7fbf3aea278)(kaydet) butonu tıklanarak parametre güncelleme kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc78ffb06-c08a-4143-b896-413328cda1d6)

### **1.1.3.Personel Durumunu Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ İşbaşı ve Periyodik Muayene/ Personel Durumunu Tanımlama

Personelin engel/ kısıt gibi işe etki edebilecek özel durumlarının tanımlandığı menüdür. Örneğin; gece çalışamaz, yüksekte çalışamaz, hamile, maluliyet, tehlikeli işlerde çalışamaz gibi. Bu menüde tanımlanan durumlar muayene takibi ekranında sonuç sekmesinde personel durumu alanında kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb17957a7-c19b-4c5c-9abc-60d97d164e67)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadff3825b7-6750-4409-868f-4daa9746ea20): Yeni bir personel durumu tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0c6b6d08-e4a4-4c74-af7d-d2fc0d3d10ba): Listede seçili olan personel durumu bilgisi güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload02bc4c38-193f-4b6c-a610-ca37753fc139): Listede seçili olan personel durumu bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2c7d68b1-ea52-4387-beb4-7db4c1fca781):Kayıtlar filtrelenerek arama yapılır.

Yeni bir personel durumu eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada60154ad-336d-444d-ac5a-e1eb9f1e02d5)(Yeni) butonuna tıklanarak “Personel Durumu Tanımlama/ Yeni Kayıt” ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadff3ce25c-0e1e-48f5-bbad-ceb8a70b1a12)

“Adı” alanında personel durumunun ne olduğu tanımlanır. Eğer “Risk Durumu” check box’ı işaretlenirse personelin risk grubunda olduğu belirtilir. O personele QDMS üzerinden herhangi bir görev atamak istenildiği zaman sistem tarafından uyarı verilerek, işyeri hekiminden bilgi alınması gerektiği belirtilmektedir.

“Personel Durumu Tanımlama” ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload813856b3-24f5-49b9-a37e-b7fbf3aea278) (Kaydet) butonuna tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload530c5a62-2a26-4df4-9311-2eb83438fe1e)

Tanımlanan Personel durumları ID bilgilerini İşbaşı ve periyodik muayene modülü parametrelerinde uygun parametrelerin parametre değerlerine yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc8e5629c-a3e6-45a0-aedd-b49ab8127f98)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d7f450d-f8aa-4191-8427-64c87d86154b) :Listede seçili parametre güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2c7d68b1-ea52-4387-beb4-7db4c1fca781) : Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload261c3eda-ba06-4a6d-a600-0db01d946d1d) : Veriler Excel’ e aktarılabilir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d7f450d-f8aa-4191-8427-64c87d86154b)Güncelle butonu tıklanarak parametrenin değer bilgisinin girilmesi işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload751e4c4f-ea34-44de-a6b8-7039a20ca703)

55 numaralı Personel durumu çalışamaz ID parametresine tanımlanan Personel Durumu tanımlama menüsündeki Personel Durumu ID numarası parametre değerine yazılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload813856b3-24f5-49b9-a37e-b7fbf3aea278)(kaydet) butonu tıklanarak parametre güncelleme kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2f31af70-a4ac-4773-bb03-92b8d58a4d92)

Bu şekilde Alt Yapı Tanımları IBYS kapsamında sağlık kayıtların gönderimi için tanımlanmıştır.

## 1.2.Entegre Yönetim Sistemi/ İş Başı ve Periyodik Muayene

IBYS kapsamında sağlık kayıtların gönderim için İş Başı ve Periyodik Muayene modülünde Muayene Takibi işlemlerinin yapıldığı kısımdır.

### **1.2.1.Muayene Takibi**

**Menü Adı:** Entegre Yönetim Sistemi/ İş Başı ve Periyodik Muayene/ Muayene Takibi

Personellerin seçilen muayene türüne göre muayenelerinin takip edildiği ekrandır. Açılan ekranda personeller tanımlı olarak gelmektedir. İşyeri hekimleri ve işyeri hemşireleri sadece bağlı oldukları işyerlerindeki çalışan personelleri ekranlarında görüntüleyebilmektedirler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f4e16aa-b9fa-4295-85b6-f73d58a841c6)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade25161a1-2475-496e-8cf9-96f47cbb3747): Listede seçili olan personel için yeni muayene takibi gerçekleştirilir

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload975fd36b-dee9-4b8e-b53f-fb943f91b591): Listede seçili olan personel için tansiyon takibi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload861fd507-e136-40a8-8715-eca0dcb1f1d9): Listede seçili olan personel için sağlık özgeçmişi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2c7d68b1-ea52-4387-beb4-7db4c1fca781): Kayıtlar filtrelenerek arama yapılır.

Bir personelin muayenesini gerçekleştirmek için ekranda ilgili personel seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcb12fc77-45a4-455b-83c6-70e40176f237)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd2be3f19-2f6b-49e1-980e-62e126795b09) (Yeni) butonu ile muayene tanım ekranına gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload79c3bbb0-6866-4b7d-b61e-7c1d2dcfb1c2)

Hangi muayene gerçekleştirilecekse ilgili muayene türü seçilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf08dda8c-6e7f-4312-b9d2-0fcbc67761a2) (İleri) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4c823515-3075-4d8e-92d2-a22c97cb3491)

Açılan ekran muayene türüne göre altyapıda kurgulanan ekrandır.

**Ana sekmede** tanımlanan alanlara göre ilgili bilgiler doldurulur. Alan tanımlamada tanımlanan alanlara göre ilgili tüm alanlar doldurulur. Varsa testler, fiziki/ psikolojik muayene gibi sekmeler doldurulur. (Bu alanların ekrana gelip gelmeyeceğine altyapılarda muayene türü tanımlarken karar verilir.)

Sonrasında başlatacağınız muayene işlemi için muayene takibi kişi bilgileri sekmesinde bulunan aşağıdaki bilgilerin doldurulması zorunludur. Bu bilgiler tamamlandıktan sonra işaretli olan kaydet butonu ile sisteme kaydedilmelidir.Bilgileri hekim tarafından doldurulabileceği gibi İnsan Kaynakları departmanı tarafından ilgili kişi de doldurabilmektedir. Bilgilerde değişiklik olduğu takdirde ise Hekim muayene sırasında bilgileri günceleyebilmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2b11b4bc-b352-4ae0-bdf7-21631a4fe431)

**Özgeçmiş sekmesinde**; personelin hastalık özgeçmişi ile ilgili bilgilere ulaşılmaktadır. Bu sekmede çalışanların daha önce almış oldukları hekim ve hemşirelik hizmetleri, tansiyon takibi bilgileri yer almaktadır. Bu sekmede yeni işlemler yapılabilir, varolan kayıtlar görüntülenebilir, güncellenebilir, ilgili ek2 formu yazdırılabilir, muayene türlerine göre tanımlı olan rapor formatları sistemden alınabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc68b6ede-83ee-494f-9cc8-f34165163a31)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc46f7c2d-645a-4386-bcc4-b4c92741d90f) (Göster) butonuyla seçilen muayene için muayene özgeçmişi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3018d962-b830-49d3-bb5f-6a37d7498e19)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload192b0e48-add7-4973-b118-b134af85f402) (Düzenle) butonuna tıklanarak “Muayene Takibi/ Kayıt Güncelleme” ekranı açılır. Açılan ekranda herhangi bir değişiklik yapılarak “Kaydet” butonu tıklanarak kayıt güncelleme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc4205216-c9a0-4592-962e-b27e691e6ea2)

**Fiziki/ psikolojik muayene sekmesinde;** sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd2be3f19-2f6b-49e1-980e-62e126795b09) (Ekle) butonuyla hangi muayenelerin yapılacağı seçilir. Eğer muayene türü tanımlama menüsünde zorunlu fiziki muayeneler tanımlandıysa bu sayfada görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9c2d4293-6f44-4118-827e-8c6071404f3d)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5afcd2f0-1ddb-498d-93b7-dabfd187c8c1)

Açıklama kısmına muayene ilgili açıklama yazılabilir. Fiziki/ psikolojik muayene tanımlama menüsünde tanımlanan default açıklamalar varsa açıklama kısmında görüntülenir, bu tanımlar ihtiyaç halinde hekim tarafından bu ekrandan değiştirilebilir. Varsa ek dosya eklenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload47f96990-7e78-4abc-a3a5-7e3b7d414337)

**Testler sekmesinde;** sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd2be3f19-2f6b-49e1-980e-62e126795b09) (Ekle) butonuyla hangi testlerin yapılacağı seçilir. Eğer muayene türü tanımlama menüsünde zorunlu testler tanımlandıysa bu sayfada görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload272ef20c-a69e-4357-9306-98515a2d556a)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcc51c206-c4c9-4e6b-9ae2-28a118dff0f4)

Açıklama kısmına muayene ilgili açıklama yazılabilir. Test tanımlama menüsünde tanımlanan default açıklamalar varsa açıklama kısmında görüntülenir, bu tanımlar ihtiyaç halinde hekim tarafından bu ekrandan değiştirilebilir. Varsa ek dosya eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1b873e8d-1b43-42d8-b772-6c758eff0465)

Testler kapsamında eğer şablon kullanılıyorsa tanımlanan test adına göre ayrı bir sekmede görüntülenir. Teste ait ilgili değerler Excel üzerinde tanımlanır.

**Sonuç sekmesinde;** altyapıda kurulan muayene türü ayarlarına göre çıkan muayene sonuç yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade56f2de3-7182-42f1-a39e-4fed9a061cf8)

Açılan ekranda ilgili alanlar tanımlanır;

**Hekim Kanaati:** Muayene sonucuna göre işyeri hekimi hasta ile ilgili kanaatlerini tanımlar.

**Personel Durumu:** Muayene sonucuna göre eğer personelde özel bir durum/ engel söz konusu ise ilgili alandan seçim yapılır. Örneğin; yüksekte çalışamaz, vardiyalı işlerde çalışamaz, gebe gibi. Eğer personelin geçmiş muayenelerinde seçilen bir durumu varsa, bu alan otomatik dolu olarak gelir. QDMS’in herhangi bir modülünde görev atamak için, durumu tanımlanan bir personel seçildiği zaman, isminin yanında sarı ünlem işaretiyle birlikte, “doktorla/ amirinle görüşünüz” uyarısı görüntülenir. Böylece personele yapamayacağı bir işin atanmaması için uyarı verilir. Örneğin; yüksekte çalışma izni olmayan bir personele yüksekte çalışmayla ilgili bir görev atandığı zaman personel seçildiği anda adının yanında uyarı çıkmaktadır ve amirinden/ doktordan onay alınmadan personelin çalıştırılamayacağı bilgisi iletilmiş olmaktadır.

**Personel Durum Bitiş Tarihi:** Personelin seçilen durum bilgisi için bir bitiş tarihi varsa sistemden seçilir.

**Kontrol:** Eğer muayene sonucuna göre belirlenen süre sonunda bir kontrol yapılması gerekiyorsa “evet” olarak seçilir. Bu veri, genelde poliklinik muayenelerinde, işe dönüş kapsamında çalışanın yeniden muayene edilerek kontrol edilmesi amacıyla kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6228432e-05a2-43db-a473-6fea3cdf2df3)(Sonuç Bildirim) butonuna tıklanarak e-posta ayarlarında belirtilen ilgili rollere sonuç bildirim mail gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4ce35c5e-3abe-4c80-9396-b2a034f61049)

## 1.3.Sağlık Kayıtları

**Menü Adı:** Sistem Altyapı Tanımları/ BSAT /Konfigürasyon Ayarları/ Sağlık Kayıtları

İş sağlığı kapsamındaki periyodik muayeneleri EK-2 formatında bakanlığa iletmek için kullanılan menüdür.Tamamlanmış olan muayene kaydı, Sistem Altyapı Tanımları/BSAT/ Konfigürasyon Ayarları/Sağlık Kayıtları sayfasına düşmektedir. İlgili kaydı seçerek gönder butonu ile açılan e imza ekranında şifre bilgisi girilerek kayıt gönderilebilir. Sağlık kayıtları ekranında bulunan yenile butonu sağlık kaydının güncel durumunu (Hatalı kayıt-başarılı işlem gibi.) güncellemek için kullanılmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3b331e25-a5e6-499b-8658-3be15ce537ea)

Ekranda bulunan butonlar yardımıyla;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc375c580-ebe5-42cb-8071-a1bed678fe77): Seçilen kayıtlar elektronik imza ile imzalanarak bakanlığa gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20d4a8ae-7a70-452c-aaf2-333d854d0cc2): Kayıtlar filtrelenerek arama yapılır.

Bakanlığa iletilmek istenilen periyodik muayeneler seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc375c580-ebe5-42cb-8071-a1bed678fe77) “gönder” butonuna tıklanır. Sistemde tanımlı olan işyeri hekimi tarafında elektronik olarak imzalanarak seçilen kayıtlar bakanlığa iletilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload779bd206-6c57-4cfe-a616-85aef8e9f6a3)
