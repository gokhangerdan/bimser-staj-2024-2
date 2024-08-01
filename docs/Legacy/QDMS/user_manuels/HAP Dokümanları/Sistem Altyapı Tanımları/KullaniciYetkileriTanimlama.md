---
title: Kullanıcı Yetkileri Tanımlama
description: Kullanıcı Yetkileri Tanımlama Yardım Dokümanı
sidebar_position: 2
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::



**Sistem Altyapı Tanımları Modülünde Kullanıcı Yetkileri Tanımlama Kullanıcı Yardım Dokümanı**

# **Kullanıcı Yetkileri**

Qdms’te Sistem Altyapı Tanımları modülünde 3 önemli menü bulunmaktadır. Bu menüler Kullanıcı Grupları Tanımlama, Yetki Grupları Tanımlama ve Kullanıcı Yetkileri Tanımlama menüleridir. Qdms ‘te Sistem Altyapı Tanımları Modülünde bu üç menünün kurgusu ne kadar iyi yapılırsa sistem o kadar aktif bir şekilde çalışır. İlk olarak Sistem Altyapı Tanımları modülünde Kullanıcı Grupların Tanımlama menüsünde kullanıcı grupları oluşturulur. Daha sonra Yetki Grupları menüsünde kullanıcıların Qdms üzerinde hangi menüleri göreceklerinin ayarlanır. Son olarakta Kullanıcı Yetkileri Tanımlama menüsünde kullanıcı grupları ile yetki gruplarının eşleştirilmesi yapılarak böylece toplu bir şekilde kullanıcılar için menü görme yetkilendirilmesi yapılmış olur.

# **1.Sistem Altyapı Tanımları**

## **1.1. BSAT (Bimser Sistem Altyapı Tanımları)/ Tanımlar**

**Menü Adı:** Sistem Altyapı Tanımlamaları/ BSAT/ Tanımlar

Qdms altyapı tanımlamalarının sistemde oluşturulduğu kısımdır. QDMS sisteminin kullanımı için gerekli olan personel bilgileri, müşteri bilgileri, ürün bilgiler, Kullanıcı grupları, Yetki grupları ve Kullanıcı yetkileri gibi bilgiler sistemde tanımlanır.

### **1.1.1.Kullanıcı Grupları Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Tanımlar/ Kullanıcı Grupları Tanımlama

Sistemde kullanılacak kullanıcı gruplarının tanımlama işleminin yapıldığı menüdür. Kullanıcı grupları; menü yetkilendirme işlemlerinde, bilgilendirme alanlarını daha kolay ve etkin kullanabilmede, müdür/ uzman/ mühendis gibi eş değer yetkinliklere sahip personelleri gruplamakta, aynı işyerinde/ departmanda bulunan kullanıcıları gruplamakta, modül bazlı kullanıcı grupları tanımlamada ve akış tanımlamalarında kullanım kolaylığı sağlamaktadır. Bir kişi birden fazla gruba dahil edilebilir. Sistem ilk kurulumunda “Sistem Yöneticileri” ve “Standart Kullanıcılar” diye tanımlı kullanıcı grubu tanımlı olarak gelmektedir. QDMS yöneticileri “Sistem Yöneticileri” grubuna dahil edilirken, diğer tüm kullanıcılar “Standart Kullanıcı” grubuna dahil edilmektedir. Doküman Modülünde doküman yönetimi ilgili yetkileri vereceğiniz bir özel kullanıcı grubu ya da İsg Modüllerinde İsg yöneticileri olduğu bir kullanıcı grubu oluşturabilirsiniz. Departman bazlı kullanıcı grupları oluşturulabilir. Örneğin Doküman Yönetimde Modülünde hazırlanan dokümanlarının doğru yerlere dağıtılması önemlidir. Kalite departmanı için hazırlanan bir dokümanın kişi sayısı 20 olan departmanda tek tek personellere gönderilme işlemi yerine Kalite departmanı kullanıcı grubu oluşturarak dağıtım matrisinde okuma görevi gönderilsin şeklinde kullanıcı grubu tanımlanarak doküman doğru yerlere dağıtım işlemi tek seferde otomatik bir şekilde yapılma işlemi gerçekleştirilir. Herhangi bir konu da bilgilendirme maillerin tek tek kişilere gönderilmesi yerine tanımlanan kullanıcı grupları sayesinde çoğunluğa tek seferde otomatik olarak gönderilmesi sağlanılır. Kullanıcı Grupları Qdms kullanım alanlarının çoğaltabilirsiniz. Qdms Modüllerde Kullanıcı Grupları kullanım alanlarında önemli bir şekilde kullanım kolaylığı sağlamaktadır. Ayrıca Özel kullanıcı grupları Modüllere göre ihtiyaç doğrultusunda tanımlanıyor.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload695b93d4-3f7d-4f1a-a70e-8512600c3e0e)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload770d0cc1-affd-4a2f-88f9-c6f656f130da): Yeni bir kullanıcı grubu tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload29d51d72-5377-41e7-abd7-f123d99afc89): Listede seçili olan kullanıcı grubu için düzeltme/ değişiklik/ güncelleme yapılır. Kod bilgisi değiştirilemez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada10a3474-34a3-488f-a6c2-56267a8ac3fc): Listede seçili olan kullanıcı grubu kopyalanarak çoğaltılır. Mevcut bir grubun içindeki kişiler, başka bir grup adı ile tekrar kullanılacak ise kopyalama butonuna ile grup kopyalama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20507b23-874d-4e95-806c-9ba76efd2c8c): Çeşitli kategorilerde grup kuralları oluşturulur. (HR Entegrasyonu mevcutsa)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6afcff7b-3117-42a6-a958-5ca5002ba1f2): Listede seçili olan kullanıcı grubu silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf9f6e992-7741-4272-85da-bc8b9f58f698): Kayıtlar filtrelenerek arama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload270ca4c8-fccc-4950-984f-0752d2115769) : Veriler Excel’e aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfebdae2b-d395-4699-a2ac-6572dd8083b0): Kullanıcı Grubu içerisindeki personel bilgileri Excel’e aktarılır.

Kullanıcı Grubu Tanımlama ekranına yeni bir Kullanıcı Grubu eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2290d54a-7129-44fa-8e10-172bae29787f) (yeni) butonuna tıklanarak Kullanıcı Grubu Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9addbb84-780a-4cc0-93d1-0af91f5f5b30)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Kullanıcı Grup Kodu:** Kulanıcı grup kodunun tanımlandığı alandır. Bu kod herhangi bir harf, sayı bilgisi içerebilir. Kullanıcı grup kodu manuel olarak tanımlanabileceği gibi otomatik olarak gelmesi de sağlanabilir. Bunun için; Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Parametreler menüsünden filtre sekmesinden modül olarak “Sistem Altyapı” seçilir ve arama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2ab41ac9-7aaa-43fb-a71e-3e3af2f12eeb)

Sistem Altyapı Tanımları parametrelerinden 113.parametre olan “kullanıcı grubu oto kod şablonu” parametresi “değiştir” butonuna ile açılarak parametre değeri olarak istenilen kod bilgisi girilir. Ör:Parametre değeri Bimser Çözüm için BC.\#\#\# şeklinde kod şablonu tanımlanmıştır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbd94ff4a-791f-4f8e-b813-fc408e4668f6)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6ff97c7d-a5b7-47ea-adfe-a5d0e87e97ba)

114.parametre olan “kullanıcı grubu oto kod sayacının da parametre değeri kod sayacının hangi sayaçtan başlaması isteniliyorsa o değer tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadebc9fe66-d658-4694-9960-341cb94fecf7)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload088abba4-cd13-481d-9cf3-dd14033b8067)

114\. numaralı parametrede parametre değeri 0 olarak tanımlandığı için Yeni tanımlanacak kullanıcı grupları ekran görüntüsünden görüldüğü gibi BC.001 kod şablonu olarak tanımlı gelecektir. Diğer tanımlanacak Kullanıcı grupları kod şablonu 1 artarak bundan sonra otomatik olarak gelecektir. BC.001, BC.002, BC.003 şeklinde sıralı olarak kullanıcı kodu otomatik olarak kullanıcı grubu tanımlanır.

**Açıklama:** Tanımlanacak kullanıcı grubunu adı bilgisinin girildiği alandır.

**Grup Üyeler:**Tanımlanacak kullanıcı grubu oluşturacak sistemde tanımlı kullanıcı/kullanıcı grubundan personelerin eklendiği alandır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcef4907a-525e-4b55-a41f-60618f38021c): Tanımlanacak Kullanıcı grubuna sistemde tanımlı Personel Listesinde personel seçilerek ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6fccd6de-4ccf-4ae5-940c-678f05779632):Tanımlanacak Kullanıcı grubuna sistemde tanımlı Kullanıcı Grubu listesinde kullanıcı grubu seçilerek kullanıcı grubunun personelleri eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload950e0fa0-3cfd-45d8-b6fb-2410f9a9ff44):Eklenen satırda bulanan kullanıcı silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9c8b0294-a657-4a3b-adc5-7cfb4e1b26cf):Eklenen tüm grup üyeleri silinir.

**Tüm Personelleri Gruba Ekle:** ilgili check box işaretlenirse tanımlanacak Kullanıcı grubuna Tüm personeller eklendiği alandır.

**E Posta:** Tanımlancak kullanıcı grubu ile ilgili E-posta bilgisinin girildiği alandır.

Tanımlanacak Kullanıcı Grubun Grup Üyeleri ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcef4907a-525e-4b55-a41f-60618f38021c)(Ekle ) butonu tıklanarak sistemde tanımlı Personel listesinde eklenecek personeller seçilerek eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4225d4c6-0105-42f0-bc8a-b7939cacafab)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload33799f1a-9696-463c-be05-54ea2a14c9a3)

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddf06c908-3679-40cf-a534-1e41a10e200b) (kaydet) butonuna tıklanarak Kullanıcı Grubu tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload08e8d398-67c7-42fd-90e8-d2034561157e)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload29d51d72-5377-41e7-abd7-f123d99afc89)(Değiştir) butonu tıklanarak Kullanıcı Tanımlama-Kayıt Güncelleme ekranı açılarak listede seçili olan kullanıcı grubu için düzeltme/ değişiklik/ güncelleme yapılır. Kod bilgisi değiştirilemez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc312b7e5-aa08-497a-b139-4e3aae78379c)

Örneğin Açıklama alanı ilgili kullanıcı grubun adı değiştirilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddf06c908-3679-40cf-a534-1e41a10e200b)(kaydet) butonu tıklnarak kayıt güncellleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb3cd98e-7327-425a-b97a-478d59d7c30f)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada10a3474-34a3-488f-a6c2-56267a8ac3fc)(Grubu Kopyala) butonu tıklanarak listede seçili kullanıcı grubu kopyalanır. Aynı grup üyelerine sahip bir kullanıcı grubu oluşturulmak istendiğinde Kopyalanan Kullanıcı grubu açıklama kısmı yeni kullanıcı grubunun adı bilgisi yazılarak kullanıcı grubu oluşturulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfa1f513b-f6da-4858-a318-0c83fbd19d71)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0d9f1812-72c1-46dd-b2a2-9470d3d4287c)

Kullanıcı Grubu kopyalama işleminde açıklama alanı kullanıcı grubunun ad bilgisi yazılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddf06c908-3679-40cf-a534-1e41a10e200b)(kaydet) butonu tıklarak Kullanıcı Grubu kopyalama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb2d5f896-cafc-4435-a27d-5fc542dcb6c3)

Kullanıcı grubu tanımlama ekranında sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload67824e02-e714-4f1e-bb40-6dfdabbad603) (grup kuralı oluştur) butonuna ile kullanıcı grubuna kural tanımlanabilir. Bu kural, HR Entegrasyonu olduğu durumlarda çalışır. Entegrasyon çalıştığı zamanlarda, bu ekranda oluşturulan kurallara göre personeller ilgili kullanıcı grubuna aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade4edd8d6-8b3a-420b-ab0b-1674302d6232)

Örnek üzerinden gidersek: Departman kodu 0001, D001 olan departmanlarda bulunan personellerin veya ünvanı 013 olan personellerin bu gruba otomatik olarak eklenmesi kuralı tanımlanmış vaziyettedir. Sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddf06c908-3679-40cf-a534-1e41a10e200b)(kaydet) butonuna tıklayarak Kullanıcı Grup Kuralı Oluştur kayıt işlem gerçekleştirilir. Kullanıcı grup kuralı oluştur kayıt işlemi gerçekleştirildikten sonra Kullanıcı Grubu seçili iken değiştir butonu tıklanıldığında “Kullanıcı grubu için tanımlanmış bir kural bulunmaktadır, grup üyelerinde yapmış olduğunuz değişiklikler transfer program çalıştığında iptal olacaktır” mesajı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20f58764-ad1e-4eb1-8b8e-27be9f11268b)

Personel entegrasyonu gerçekleştiği zamanlarda uygulanan grup kuralına göre personeller ilgili kullanıcı gruplarına aktarılmaktadır.

Kuralın belirlendiği seçenekte eğer “Benzeyen” kullanıyor ise karşısına gelen kodun sonuna % işareti konulmalıdır. Örneğin 50000498-01, 50000498-02 gibi pozisyonlardan 50000498 benzeyenler kuralı koyulacaksa 50000498% şeklinde yazılmalıdır. Eğer Tüm Kullanıcılar Grubuna sisteme dahil olan herkesin eklenmesi isteniyorsa bu durumda Kategori alanından Eşittir seçili olan ilgili alana 0 (sıfır) yazılıp kaydedilmelidir.

Burada Operatör dediğimiz “ve – veya” bağlacı çok önemlidir. Ve bağlacı kullanıldığında; kuralların hepsinin sağlanması durumunda kullanıcı grubuna personeller eklenir. Veya bağlacı kullanıldığında kuralların sadece birinin sağlanması durumunda kullanıcı grubuna personeller eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6afcff7b-3117-42a6-a958-5ca5002ba1f2)(Sil) butonu tıklanrak listede seçili olan kullanıcı grubu silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload61b2a28d-70b3-458d-8c4a-f532ac37993d)

“Seçili kaydı silmek istediğinizden emin misiniz?” mesajına tamam butonu tıklanarak kullanıcı grubu silme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadafbc1ea9-7792-438d-8c84-8dabf60593d3)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf9f6e992-7741-4272-85da-bc8b9f58f698)Ara butonu tıklanarak Kullanıcı grup kodu ve Açıklama alanlarına göre kayıtlar filtrelenerek arama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload030f90b1-7752-49ff-840c-72b51b8dffd9)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload157ed7ff-b741-4724-b5c5-f4dbb8eb3c1c)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload270ca4c8-fccc-4950-984f-0752d2115769) Excel Aktar butonu tıklanarak seçili kullanıcı grup excel formatında görüntülenir. Grup kodu, kullanıcı grubunun adı bulunduğu açıklama alanı ve kullanıcı sayısı alanları ilgili bilgilere Excel formatında rapor şeklinde ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9abec7a7-7c94-467d-afea-e6a3f38f2aa8)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfebdae2b-d395-4699-a2ac-6572dd8083b0)(Grubu Excel’e aktar) butonu tıklanarak listede seçili Kullanıcı Grubu içerisindeki personel bilgileri Excel’e aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc7504c68-c59d-4824-b992-efa4d04d7380)

Grubu Excel’e aktar butonu yardımıyla alınan raporda Grup kodu, Grup Adı, Grup üyelerini sicil no , ad ve soyad alanları ilgili bilgilere ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5de37000-1434-400c-b193-e12ecc0b0757)

### **1.1.2. Yetki Grupları Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Tanımlar/ Yetki Grupları Tanımlama

Kullanıcıların QDMS üzerinde hangi menüleri göreceklerinin ayarlandığı menüdür. Kullanıcı gruplarına göre menü yetkilendirilmesi yapılmaktadır. Örneğin sistem yöneticileri kullanıcı grupları her menüyü görebilir şeklinde seçilirken, standart kullanıcılar için sadece Entegre Yönetim Sistemleri menüsünün altındaki hangi modülün hangi ekranını görebileceklerse o şekilde menüler seçilir. İş Güvenliği Risk değerlendirme ekibinin QDMS üzerinde İsg Risk Değerlendirme alt yapı kurgusunu da yapması isteniyorsa, İsg Risk Değerlendirme Ekibi diye bir yetki grubu oluşturulup Sistem Altyapı tanımlarının altındaki İsg Risk Değerlendirme Modülüne ait tüm menüler ve Entegre Yönetim Sistemi menüsünün altındaki tüm İsg Risk Değerlendirme menü yetkileri seçilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload127de4b1-60fc-45a2-b6da-9361532449be)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade4f8d7be-0d9a-4a28-884d-2480c242adf6): Yeni bir yetki grubu tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload10119857-0459-4536-8a18-6192a2a9f5fc): Listede seçili olan yetki grubu için düzeltme/ değişiklik/ güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload38eefee2-e02c-4abd-bd5a-33c4c9bff00b): Listede seçili olan yetki grubu silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload270ca4c8-fccc-4950-984f-0752d2115769): Veriler Excel’ e aktarılır.

Yetki Grubu Tanımlama ekranına yeni bir yetki grubu eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2290d54a-7129-44fa-8e10-172bae29787f)(Yeni) butonuna tıklanarak Yetki Grupları Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload525efc94-e2b2-46c2-994f-b0046cabdbf9)

Açılan ekranda grup adı kısmına yetki grubunun tanımı yazılır. Görselin sol tarafında QDMS üzerinde yer alan tüm menüler olup, sağ tarafa tek okla seçilen menü görme yetkileri taşınır. Çift ok tüm menü yetkilerini taşır. Sağa taşınılan menüler, yetki grubuna ait olacak menüler anlamına gelir. Ardından kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb50f975-f381-40cf-9a26-4a844be0987e)

Sistem yöneticilerine yetki grubu tanımlamak için çift ok butonuna tıklanıp tüm yetkilerin ekranın sağ tarafına aktarılması yeterlidir. Diğer modül yetkileri için; ilgili kullanıcı grubunun görebileceği menü yetkilerinin işaretlenip tek ok butonuna ile ekranın sağ tarafına aktarılması yeterlidir. Yetki devri için işaretleme yapılırken ana başlıkların da işaretli olmasına dikkat edilmelidir.

Eğer kullanıcı gruplarına ait yetkilerden geri alınacak menü yetkileri varsa ters işlem yapılarak geri alınacak yetkiler ekranın sağ tarafında işaretlenerek ortada 3.sırada yer alan tek ok butonuna ile yetkiler geri alınır. Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddf06c908-3679-40cf-a534-1e41a10e200b) (kaydet) butonuna tıklanarak Yetki Grupları Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload249a089a-7661-40f9-9172-0b0624fd6ab3)

### **1.1.3. Kullanıcı Yetkileri Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Tanımlar/ Kullanıcı Yetkileri Tanımlama

Kullanıcı grupları ile yetki gruplarının eşleştiği menüdür. Oluşturulan kullanıcı gruplarının, yetki grubu tanımlama menüsünde belirlenen yetkilerden hangisine sahip olmasını isteniyorsa, ilgili kullanıcı grubu ile yetki grubunun ilişkilendirmesi gerekir. Böylece toplu bir şekilde kullanıcılar için menü görme yetkilendirilmesi yapılmış olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3fdd6a27-bba7-4e4c-8a71-1209b3715aa4)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade4f8d7be-0d9a-4a28-884d-2480c242adf6): Yeni bir kullanıcı yetki tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload38eefee2-e02c-4abd-bd5a-33c4c9bff00b): Listede seçili olan kullanıcı yetki eşleştirmesi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload270ca4c8-fccc-4950-984f-0752d2115769): Veriler Excel’ e aktarılır.

Kullanıcı Yetki Tanımlama ekranında yeni bir kullanıcı yetki eşleştirmesi yapmak için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2290d54a-7129-44fa-8e10-172bae29787f)(Yeni) butonuna tıklanarak Kullanıcı Yetki Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd4bf301d-136e-4254-bd8f-6f4fc5afd51a)

Kullanıcı grubu alanından sistemde tanımlı kullanıcı Grubu listesinden Kullancı Grubu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd0db7d41-ca76-4d8b-a1fc-f7c7a04f6e98)

Yetki Grubu alanında sistemde tanımlı yetki gruplarından ilgili yetki grubu seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cec00e8-d8e6-443f-8fc8-88feb44a759d)

Açılan ekranda kullanıcı grupları ve yetki grupları eşleştirilerek hangi kullanıcı grubunun hangi yetkiye sahip olacağı belirlenir. Gerekli alanlar seçildikten sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddf06c908-3679-40cf-a534-1e41a10e200b) (kaydet) butonuna tıklanarak Kullanıcı Yetki Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload089a121c-2aa0-42b1-aa48-a9b61464caf1)

Kullanıcı grubu ve yetki grupları eşleştirilme işleminde sonra grup üyelerinde bir personelin Qdms ana giriş sayfasından kullanıcı adı ve şifresi ile giriş yapılarak örnekteki Doküman Yönetimi Modülündeki verilen menu görme yetkisine sahip olduğu görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf8f97374-dd15-46ab-ba51-74a220323c8d)
