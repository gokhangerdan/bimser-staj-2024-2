---
title: Onay Akışı Tanımlama 
description: Onay Akışı Tanımlama  Yardım Dokümanı
sidebar_position: 6
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::


**Onay Akışı Tanımlama Kullanıcı Yardım Dokümanı**


# **1.Onay Akışı Tanımlama İşlemi**

Qdms bulanan tüm Modülerinde Onay Akışı Tanımlama işlemi aynı şekilde yapılmaktadır. Onay işleminde Rol tanımlama menüsünde ilgili modül için Rol Tanımlama işlemi yapılır. Rol tanımlamada menüsünde bir kullanıcı grubuna yada bir personel bağlı SQL sorgular bulma yöntemi alanı yazılarak tanımlı kullanıcı grubuna yada personele akışta onay işleminin yapılması sağlanılır. Yada Bimser Destek Ekibinde yardım alınarak istenilen özel rolün SQL Sorgusu Bulma yöntemi alanı yazılarak, SQL sorguda yazılan Role akışta onaya gitmesi sağlanabilir. Rol tanımlama işleminde sonra Akış Tanımlama işleminde ilgili Modül için Akış tanımlama işlemi yapılarak aynı menüde akışta kullanılacak Rol tanımlama menüsünde tanımlı Rolü atama işlemi yapılır. Akış Tanımlama işleminde ilgili Modülün Alt Modülde Akış eşleştirilmesi yapılarak onay politikasi belirlenirek akış aşamasının işleyişinin çalışması sağlanılır. Örnek olarak DÖF Modülünde “DÖF Açma Onayı” akışının bir roldeki personel ve “DÖF Aksiyon Açma Onayı”akışının bir kullanıcı Grubuna atama işlem basamakları ve akışın işleyişi çalışması gösterilecektir.

## **1.1.DÖF Modülü Onay Akışı Tanımlama**

Onay Akışı tanımlama işleminde Modülllerde DÖF modülü kullanılır. DÖF Modülünde onay akışı tanımlama işleminde öncelikle onay akışında kullanıcak Rol, Rol tanımlama menüsüde tanımlanır. Rol tanımlama menüsünde onay akışı olarak kullanılacak Rol kullanıcı veya kullanıcı grubu olarak ataması yapılarak hangi role gideceği bilgisi tanımlanır. Rol tanımlama atanacak Rol bir personele olarak seçilecek SQL sorgusuna persolenin sicil numarası bilgisi tırnak içerisinde yazılır. Örnek olarak sicil numarası=bguner olan bir personel için SQL sorgusu aşağıdaki şekilde yazılır.

Personel için SQL Sorgusu:

**SELECT SICIL_NO FROM BSAT001 WHERE SICIL_NO='bguner'**

Bir kullanıcı grubu olarak bir Rol ataması yapılacaksa SQL sorgusuna Kullanıcı grubunun kodu tırnak içerisinde yazılarak Rol tanımlama işlemi yapılır. Kullanıcı Grubu Sistem Yöneticiler için Grup Kodu=001 olan bir kullanıcı grubu için SQL sorgusu aşağıdaki şekilde yazılır.

Kullanıcı Grup için SQL Sorgu:

**SELECT SICIL_NO FROM BSAT009A WHERE GRUP_KODU='001'**

Rol Tanımlama işleminde sonra Modülde kullanıcak akış için Akış tanımlama menüsünde Akış Tanımlama işlemi yapılır. Akış tanımlamada kullanıcak rol ataması yapılır. Akış tanımlama işlemi yapıldıktan sonra Alt Modül Tanımlama menüsünde akışların eşleştirme işlemi yapılarak onay politikası belirlenerek Modülün onay akışı tasarlanarak onay işlemi yapılır.

### **1.1.1.DÖF Modülünde SQL Sorgusunda Personel Seçilen Rol İçin Onay Akışı Basamakları**

DÖF modülünde onay akışı işlem basamaklarının yapılması için “DÖF Açma Onayı ” akışını örnek olarak uygulaması yapılır. DÖF modülünde akışın hangi Role gideceğinin atamasının yapılması için öncelikle Rol tanımlama menüsünde akış için ilgili Rol tanımlama işlemi yapılır. Rol tanımlama işleminde SQL sorgusunda bir personel kullanılacak şekilde yapılır. Personel için SQL sorgusunu yazmak için Personel Tanımlama menüsünde tanımlı olan Personelin sicil numarası DÖF modülü için tanımlanan akış için bir SQL sorguda tırnak içeresinde yazarak onay akışın o Personele gitmesini sağlanılır.

### **1.1.1.1.Rol Tanımlama**

**Menü:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Rol Tanımlama

DÖF Modülü onay akışı “DÖF Açma Onayı” akışının bir personel gitmesi için modüllerde kullanılan onay akışları için onaycı olarak hangi role gideceği bilgisinin tanımlandığı menü olan rol tanımlama menüsüne gidilir. Bu menüde her modül için Rol tanımlama işlemi mümkündür. Roller değiştirilmek istenildiğinde ya da yeni bir rol tanımlanmak istenildiğinde Bimser Çözüm Ekibinden destek alınabilir. Onay akışında Rol atanmak için tanımladığımız Personel için “DÖF Açan” tanımı bir rol tanımlaması için Rol tanımlama menüsünde yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload84b46f37-85d4-4cb8-a41c-df33165fa423)


**Ekranda bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20a95e30-c500-4590-baf4-f2968cbce3bb): Yeni bir rol tanımı yapılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadce7a102b-027b-4213-88ab-19b81d4c54bf): Listede seçili olan rol tanımı için düzeltme/ değişiklik/ güncelleme yapılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload67f4bcc9-fdf2-44ec-a24a-6ce7a04d4651): Listede seçili olan rol tanımı silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade666859e-5dd8-4d3f-8a00-1b287d4f5c90): Kayıtlar filtrelenerek arama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcda3659d-fc0d-4426-9a09-d2fb96f95e70): Veriler Excel’ e aktarılır.

“DÖF Açan” tanımı olan Rol tanımlamak için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0eae799f-169c-49ff-8e6d-0e301495f9f7) (yeni) butonuna tıklanarak Rol Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6906cfac-a907-4f52-82aa-e058de0f438b)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Modül:** Tanımlanan Rolü hangi modül için seçileceğinin belirlendiği alandır.

**Rol No:** Tanımlanan Rolün Rol nosunun sistem tarafından otomatik verildiği alandır.

**Bulma Yöntemi:** Tanımlanan Rolün SQL sorgusunun yazıldığı alandır.

**Rol Tipi:** Rol tipi seçeneklerinde Personel, Kurumsal Müşteri, Bireysel Müsşteri, Tedarikçi ve Diğer gibi seçeneklerinde seçildiği alandır.

Rol Tanımlama-Yeni Kayıt ekranında Modül kısmında Modül olarak Düzeltici ve Önleyici Faaliyetler Modülü seçilir. Rol No sistem tarafında otomatik verilir. Rol tanımı bilgisi “DÖF Açan” olarak bilgisi yazılır. Bulma yöntemi alanında SQL sorgusu yazılır. Personel tanımlama menüsünde tanımlı Personelin sicil numarası bilgisinin SQL sorguda tırnak içeresinde yazarak Rol tanımlaması Personel için yapılır. Personel için bir SQL sorgu bilgisi Rol Tanımlamada yapılmıştır.

Tanımlanan Personel: DÖF Açan

Personel Sicil numarası: fbas

Personel için tanımlanan SQL Sorgu aşağıdaki şekilde yazılır.

**SELECT SICIL_NO FROM BSAT001 WHERE SICIL_NO='fbas'**

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8f72a020-7c45-4cee-b47b-ff8b4f45a0f7) (kaydet) butonuna tıklanarak Rol tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadac0aad6f-b944-4b6f-b32e-108b2c899bc0)

Rol Tanımlama işleminden sonra Akışların Tanımlama işlemi yapılacak Akış Tanımlama menüsüne gidilir.

### **1.1.1.2. Akış Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Akış Tanımlama

Modüllerde kullanılan onay akışlarının tanımlamaları yer aldığı menüdür. Yeni bir Akış tanımlamak için Akış tanımlama menüsüne gidilir. Sistemde her Modül için akış tanımı mevcut olan menüdür

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadded6ec18-81e6-411f-ae27-666c2fd859d5)

**Ekranda bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20a95e30-c500-4590-baf4-f2968cbce3bb): Yeni bir akış tanımlaması yapılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadce7a102b-027b-4213-88ab-19b81d4c54bf): Listede seçili olan akış tanımlaması için düzeltme/ değişiklik/ güncelleme yapılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload67f4bcc9-fdf2-44ec-a24a-6ce7a04d4651): Listede seçili olan akış tanımlaması silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcda3659d-fc0d-4426-9a09-d2fb96f95e70): Veriler Excel’ e aktarılır.

“DÖF Açma Onayı ” adında Akış tanımlamak için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0eae799f-169c-49ff-8e6d-0e301495f9f7) (yeni) butonuna tıklanarak Akış Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload59fb58e8-0711-46d6-a682-1b45dae39114)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Modül:** Tanımlanan akışın hangi modül için tanımlandığının seçildiği alandır.

**Akış No:** Tanımlanan akışın Akış No’sunun sistem tarafından otomatik verildiği alandır.

**Onaycı No:** Onaycının kaçıncı sırada onay vereceğinin sıra numarasının verildiği alandır.

**Onaylaması Gereken:** Onaylaması gerekenin belirtildiği alandır. Bir kullanıcı grubu olarak Rol ataması yapıldığında onaylaması gereken alana “0” olarak bilgisi girildiğinde Kullanıcı grubunda herkesin onaylaması gerekir. Kullanıcı grubunda onaylaması gereken alana “1” olarak bilgisi girildiğinde Kullanıcı grubunda 1 kişinin onaylama işlemi yapmasının yeterli olur. Personel için onaylayan bir kişi olduğu için “1” yazılır.

**Sıra No:** Onaycı sıra no bilgisinin yazıldığı alandır. Birden fazla onaycı atama işlemi yapılır. Sıra No bilgisi tersten işler. Hiyerarşide 0,1,2 şeklinde olan bir onaylamada ilk olarak 2,1, 0 şeklinde onay sıralaması devam eder. Sıfır son onaycı olacak şekilde onaylama işlemi yapılır.

**Ekranda butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload10a1ce83-59f1-40ce-ae3b-145d14418dae) : Rol eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5fb2c8bf-e55f-437c-a875-4c63fc97cc61): Listede seçili olan kayıt silinir.

Modül kısmında Modül olarak Düzeltici ve Önleyici Faaliyetler Modülü seçilir. Akış No bilgisi sistem tarafında otomatik verilir. Akış Tanımı “DÖF Açma Onayı” olarak bilgisi yazılır.

Ekle butonuna tıklandığında rol tanımlamada yer alan roller açılmaktadır. Uygun olan rol seçilip kaydedilir. Örnek olarak Rol Tanımlamada tanımlanan “DÖF Açan” seçilerek “DÖF Açma Onayını” akışında o Role atama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload57d10e70-67c1-4d35-9f25-91386f2e8a4d)

Birden çok Akış onaycısı tanımlanabilir. Ekranda sıra numarası onaycının kaçıncı sırada onay vereceğini belirtir. Hiyerarşi yapılır. 0, 1, 2 gibi sıra numaraları ile en son sıfırıncı onaycıya gelmesi sağlanabilir. Örnekte Personel olarak tanımlanan SQL sorgudaki bir kişinin onay vermesi yeterli olacak şekilde belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3b7c06d6-fe84-4c58-b15e-61e0123b4bb0)

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8f72a020-7c45-4cee-b47b-ff8b4f45a0f7) (kaydet) butonuna tıklanarak Akış tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload53c22777-1ce6-4401-a129-a381da0a282c)

Akış tanımlama için uygun rol seçildikten sonra alt modüle tanımlama menüsü de kontrol edilmelidir. Aksi takdirde alt modülde tanımlama uygun değilse akış uygun bir şekilde sağlanmayabilir veya istenilen akış çalışmayabilir. Akış Tanımlama dan sonra Alt modülde Tanımlama menüsünde akışın eşleştirme işlemi onay politikasının belirlenmesi yapılır.

### **1.1.1.3.Alt Modül Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Alt Modül Tanımlama

Modüllerde var olan açma, gerçekleştirme, geciktirme, kapatma onayları için kullanılan akışların modüllere tanıtıldığı; onay talep, bildirim ve red mesajlarının ilişkilendirildiği menüdür. Tanımlanan akışın Alt Modülde onay politikasının tanımlama işlemi için Alt Modül tanımlama menüsüne gidilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1da42a0c-846f-4698-b7a8-f35553b1993b)

**Ekranda bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadce7a102b-027b-4213-88ab-19b81d4c54bf): Listede seçili olan alt modül tanımlama için düzeltme/ değişiklik/ güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcda3659d-fc0d-4426-9a09-d2fb96f95e70): Veriler Excel’ e aktarılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadce7a102b-027b-4213-88ab-19b81d4c54bf)(Değiştir) butonu tıklanrak alt modül tanımlama için değişiklik yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload98830eba-d0e9-47cd-aac3-13af2a543e91)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Alt Modül No:** Alt Modül No’sunun sistem tarafında otomatik verildiği alandır.

**Alt Modül Tanımı:** Alt Modül Tanımının sistem tarafından otomatik verildiği alandır.

**Akış Tanımı:**Sistemde tanımlı akışın seçilebildiği alandır.

**Onay Talep Mesajı**:Sistemde tanımlı mesaj seçeneklerinde olan Onay Talep Mesajının seçilebildiği alandır. Sistem Altyapı Tanımları/BSAT/Tanımlar/Mesaj Gövdesi Tanımlama menüsünde Onay Talep Mesajı tanımlanır.

**Onay Tamam Mesajı:** Sistemde tanımlı mesaj seçeneklerinde olan Onay Tamam Mesajının seçilebildiği alandır. Sistem Altyapı Tanımları/BSAT/Tanımlar/Mesaj Gövdesi Tanımlama menüsünde Onay Taman Mesajı tanımlanır.

**Onay Ret Mesajı:** Sistemde tanımlı mesaj seçeneklerinde olan Onay Ret Mesajının seçilebildiği alandır. Sistem Altyapı Tanımları/BSAT/Tanımlar/Mesaj Gövdesi Tanımlama menüsünde Onay Ret Mesajı tanımlanır.

**Onaycı Başlatan İse Onay Geçilmesin:** İlgili check box işaretlendiğinde sisteme veri girişi yapıp onaya gönderen personel onaycının kendisi ise onay sürecini atlayarak akış sürecini bir sonraki basamağa geçmesini sağlar.

Alt Modül tanımlama menüsüne geldikten sonra ilgili modül tanımı üzerinde ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadce7a102b-027b-4213-88ab-19b81d4c54bf) (Değiştir) butonuna tıklanarak akış tanımı olarak” DÖF Açma Onayı” seçilerek , onay talep mesajı, onay tamam mesajı, onay red mesajı ilişkilendirmeleri yapılmaktadır. “Onaycı Başlatan İse Akış Geçilmesin” check box işaretlendiği takdirde, eğer sisteme veri girişi yapıp onaya gönderen personel onaycının kendisi ise onay sürecini atlayarak akış sürecini bir sonraki basamağa geçmesini sağlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload799626bf-da37-4f8e-801a-eddd0063f6e4)

### **1.1.2.DÖF Modülünde SQL Sorgusunda Kullanıcı Grubu Seçilen Rol İçin Onay Akışı Basamakları**

DÖF modülünde Kullanıcı Grubu seçilen Rol için onay akışı işlem basamaklarının yapılması için “DÖF Aksiyon Açma Onayı” akışını örnek olarak uygulaması yapılır. DÖF modülünde akışın hangi Role gideceğinin atamasının yapılması için öncelikle Rol tanımlama menüsünde akış için ilgili Rol tanımlama işlemi yapılır. Rol tanımlama işleminde SQL sorgusunda bir kullanıcı grubu kullanılacak şekilde yapılır. Kullanıcı Grup için SQL sorgusunu yazmak için Kullanıcı Grubu menüsünde DÖF modülü için tanımlanan akış için bir kullacı grubu tanımlayıp, tanımlanan bu kullanıcı grubunun kodu SQL sorguda tırnak içeresinde yazarak onay akışın o kullanıcı grubuna

gitmesini sağlanılır.

### **1.1.2.1. Kullanı Grubu Tanımlama**

Sistemde kullanılacak kullanıcı gruplarının tanımlandığı menüdür. Akış tanımlamalarında kullanım kolaylığı sağlamaktadır. “DÖF Aksiyon Açma Onayı” akışı için bir kullanıcı grubu tanımlama işlemi Kullanıcı Grubu Tanımlama menüsü tıklanılır .

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d4c5fcd-eca4-4b2c-a68a-0cfed0475b91)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload98553ac2-0119-4238-9c73-b2b2138891ee): Yeni bir kullanıcı grubu tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada067a871-22df-4044-b3da-c08c8e3fc488): Listede seçili olan kullanıcı grubu için düzeltme/ değişiklik/ güncelleme yapılır. Kod bilgisi değiştirilemez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload01250a4a-bd56-4454-a4b0-acffed1d04a5): Listede seçili olan kullanıcı grubu kopyalanarak çoğaltılır. Mevcut bir grubun içindeki kişiler, başka bir grup adı ile tekrar kullanılacak ise kopyalama butonuna ile grup kopyalama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload708d4bc5-add3-46e3-a710-01fee6897799): Çeşitli kategorilerde grup kuralları oluşturulur. (HR Entegrasyonu mevcutsa)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9143191f-ecb3-43ff-8bff-d12806408a31): Listede seçili olan kullanıcı grubu silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade666859e-5dd8-4d3f-8a00-1b287d4f5c90): Kayıtlar filtrelenerek arama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcda3659d-fc0d-4426-9a09-d2fb96f95e70) : Veriler Excel’e aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7f8b9a2b-3993-44c3-810d-cf77b7c2ba87): Kullanıcı Grubu içerisindeki personel bilgileri Excel’e aktarılır.

“DÖF Ekip Üyeleri” kullanıcı grubu tanımlamak için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0eae799f-169c-49ff-8e6d-0e301495f9f7) (yeni) butonuna tıklanarak Kullanıcı Grubu Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload88e73517-a09b-4f37-bae6-8638bb6ed7a6)

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8f72a020-7c45-4cee-b47b-ff8b4f45a0f7) (kaydet) butonuna tıklanarak kullanıcı grubu tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade8286807-f79c-4849-b0b8-ae10b6ecfbcf)

Kullanıcı Grubu tanımlama işleminde sonra “DÖF Aksiyon Açma Onayı ” akış için Rol Tanımlama işlemi yapılır.

### **1.1.2.2.Rol Tanımlama**

DÖF Modülü için kullanıcı grubu tanımlama işleminde sonra modüllerde kullanılan onay akışları için onaycı olarak hangi role gideceği bilgisinin tanımlandığı menü olan rol tanımlama menüsüne gitmek için Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Rol Tanımlama menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1bbc0f5c-b293-4f62-bb03-f810622bee21)

Açılan ekranda “DÖF Ekip Üyeleri” adında Rolü tanımlamak için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0eae799f-169c-49ff-8e6d-0e301495f9f7) (yeni) butonuna tıklanarak Rol Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload22a555a5-d865-4275-b4d1-87554b2d115b)

Rol Tanımlama-Yeni Kayıt ekranında Modül kısmında Modül olarak Düzeltici ve Önleyici Faaliyetler Modülü seçilir. Rol No sistem tarafında otomatik verilir. Rol tanımı bilgisi “DÖF Ekip Üyeleri” olarak bilgisi yazılır. Bulma yöntemi alanında SQL sorgusu yazılır. Kullanıcı Grupları tanımlama menüsünde tanımlanan kullanıcı grubun grup kod bilgisinin SQL sorguda tırnak içeresinde yazarak Rol tanımlaması kullanıcı grubu için yapılır. Grup için bir SQL sorgu bilgisi Rol Tanımlamada yapılmıştır.

Tanımlanan Kullacı Grubu: DÖF Ekip Üyeleri

Kullanıcı Grup Kodu:DF.001

**SELECT SICIL_NO FROM BSAT009A WHERE GRUP_KODU='DF.001'**

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8f72a020-7c45-4cee-b47b-ff8b4f45a0f7) (kaydet) butonuna tıklanarak Rol tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb095f8c0-8779-42e2-a334-d8994ad48d45)

Rol Tanımlama işleminden sonra Akışların Tanımlama işlemi yapılacak Akış Tanımlama menüsüne gidilir.

### **1.1.2.3. Akış Tanımlama**

“DÖF Aksiyon Açma Onayı” Akışının tanımlamak için Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Akış Tanımlama menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadad9bd9fb-48a1-4d9b-9797-30921a4cf1fb)

Açılan ekranda “DÖF Aksiyon Açma Onayı” adında Akış tanımlamak için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0eae799f-169c-49ff-8e6d-0e301495f9f7) (yeni) butonuna tıklanarak Akış Tanımlama/ Yeni Kayıt ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload89f8ee81-1ccf-4ad3-bb1e-137c9d688d70)

Ekranda butonlar yardımıyla;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload10a1ce83-59f1-40ce-ae3b-145d14418dae) : Rol eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5fb2c8bf-e55f-437c-a875-4c63fc97cc61): Listede seçili olan kayıt silinir.

Modül kısmında Modül olarak Düzeltici ve Önleyici Faaliyetler Modülü seçilir. Akış No bilgisi sistem tarafında otomatik verilir. Akış Tanımı “DÖF Aksiyon Açma Onayı” olarak bilgisi yazılır.

Ekle butonuna tıklandığında rol tanımlamada yer alan roller açılmaktadır. Uygun olan rol seçilip kaydedilir. Örnek olarak Rol Tanımlamada tanımlanan “DÖF Ekip Üyeleri” seçilerek “DÖF Aksiyon Açma Onayı” akışa rol atama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8442e574-c0db-4264-bc97-cab8aab79046)

Örnekte kullanıcı grubu olarak gruptaki bir kişinin onay vermesi yeterli olacak şekilde Onaylaması gereken alanında “1” olarak belirlendi. Kullanıcı grubu olarak onaylaması gereken alanda “0” yazıldığı takdirde tüm gruptaki kişilerinin onaylaması gerekmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbdb94c1f-b347-4bd1-84ae-1936ce22ffeb)

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8f72a020-7c45-4cee-b47b-ff8b4f45a0f7) (kaydet) butonuna tıklanarak Akış tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc2015cc2-91f4-41f0-8e68-d59503f67ace)

Akış tanımlama için uygun rol seçildikten sonra alt modüle tanımlama menüsü de kontrol edilmelidir. Aksi takdirde alt modülde tanımlama uygun değilse akış uygun bir şekilde sağlanmayabilir veya istenilen akış çalışmayabilir. Akış Tanımlamadan sonra Alt Modülde Tanımlama menüsünde akışın eşleştirme işlemi olan onay politikasının tanımlama işlemi yapılır.

### **1.1.2.4.Alt Modül Tanımlama**

“DÖF Aksiyon Açma Onayı” akışının onay politikasını belirlemek için Alt Modül tanımlama menüsüne gitmek için Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Alt Modül Tanımlama menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1845d333-7c89-4a9e-bca0-acdeec8c538f)

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadce7a102b-027b-4213-88ab-19b81d4c54bf)(Değiştir) butonu tıklanrak alt modül tanımlama için değişiklik yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4a6f2b1c-94c0-4e0b-a0ca-448186aa4624)

Alt Modül tanımlama menüsüne geldikten sonra ilgili modül tanımı üzerinde ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadce7a102b-027b-4213-88ab-19b81d4c54bf) (Değiştir) butonuna tıklanarak akış tanımı, onay talep mesajı, onay tamam mesajı, onay red mesajı ilişkilendirmeleri yapılmaktadır. “Onaycı Başlatan İse Akış Geçilmesin” kutucuğu işaretlendiği takdirde, eğer sisteme veri girişi yapıp onaya gönderen personel onaycının kendisi ise onay sürecini atlayarak akış sürecini bir sonraki basamağa geçmesini sağlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload08dfde2e-9aad-4037-ba12-a885fa2b9a10)

DÖF Modülünde “DÖF Açma Onayı” ve “Döf Aksiyon Açma onayı” Akış kurgusunun işleyişi için DÖF Modülünde göstermek için altyapı tanımları olan DÖF Kök Neden, DÖF işlem Kaynağı ve Uygunsuzluk Kategorileri Tanımlama işlemleri DÖF Modülünde Sistem Altyapı Tanımları kısmında tanımlanır. Altyapı da bu tanımlamalar yapıldıktan sonra yeni bir DÖF kaydı açmak için Entegre Yönetim Sistemi kısmına gidilerek DÖF İşlemleri menüsünde Yeni bir DÖF kaydı açılır.

### **1.1.3. DÖF Modülünde Onay Akışlarının İşleyişi**

### **1.1.3.1.DÖF İşlemleri**

Yeni bir Döf kaydının açıldığı ve açılan Döf kayıtlarının listelendiği menüdür. DÖF İşlemleri menüsüne gitmek için Entegre Yönetim Sistemi/ Düzeltici ve Önleyici Faaliyetleri / DÖF İşlemleri menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc9d79fd1-7e45-4745-9477-f611a283efbc)

**Ekranda bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload416ce40b-17ac-4c19-8015-4e14b4f958fa) : Yeni bir DÖF’ ü sisteme girerken kullanılan butondur.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbf1d0e56-8d27-495f-bac3-32333252c85f) : Var olan kayıt üzerinde, yetki olması halinde değişiklik yapmak için kullanılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade4dc74b6-772c-4064-b5e2-886c32c469a6) : Herhangi bir DÖF’ ün tüm bilgilerini görüntülemek için kullanılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfbcf446d-0f96-4e2b-aad4-2076ee705bcb) : Seçilen DÖF’ e bağlı Müşteri Şikayeti varsa şayet ilgili kayda götürür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2c120034-30ba-4a80-8bfc-d53088681d6a) : DÖF detayında düzeltmeler için kullanılan kayıt bakım butonudur.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload28d8b8fb-bda9-4599-91e9-39fa2198d624) : DÖF Kaydını silmek istenirse kullanılacak butondur. Sistem Yöneticilerinde çıkar. Uç kullanıcılarda görünmez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload67975e17-352d-40cb-a2a2-95c557a51486) : Parametrik bir buton olmakla birlikte Sistem Yöneticilerin ekranında çıkar. DÖF’leri iptal etmek için kullanılır. Silmekten farklı bir işlemdir. DÖF İşleyişi durur fakat sistem de kayıtlı olmaya devam eder. Bir onay akış çerçevesinde çalışır. Bunun için alt yapıda Akışın tanımlanması gereklidir. (İptal edilmek istenen DÖF kayıtlarının hangi rol tarafından onaylanacak veya red edilecek olduğunu belirlemek için SAT/ BSAT/ Konfigürasyon Ayarları/ Akış Tanımlama menüsüne gelinir. DÖF İptal Onay Akışı ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d9d6582-b6ca-46fb-bba6-b35881900ab3) butonuyla role bağlanır.)

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb86ff274-94e9-4302-8eab-d0f0e4077c51) : DÖF’ün herhangi bir aşamasına göre çıktı almayı sağlayan butondur. Hangi aşamaya kadar rapor alınmak istenilirse seçim yapılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4a4449d0-1660-4d6e-8911-dc1b4d35e9a7) (Yazdır) butonuna tıklanır. Seçili kayıda ait rapor bilgisayara çekilmiş olur.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4e6c29eb-59a7-4809-b27c-c9db7aa7c131) : DÖF’ leri Excel olarak çıktısını almak istersek kullanılan butondur.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload355afde8-00f1-4ebe-aaf9-148882f93ade) : Arama sekmesinden seçimler yapıp filtreleme işlemi yapılmak istendiğinde kullanılır.

Yeni DÖF Kaydının Açılması için  ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0eae799f-169c-49ff-8e6d-0e301495f9f7) Yeni butonu tıklanarak DÖF İşlemleri / Yeni Kayıt ekranına gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload58740311-0441-45bd-9d42-cea1ae5db701)

DÖF sekmesinde DÖF Detay başlığı altında işlem kaynağı, uygunsuzluğun olduğu bölüm, işyeri, uygunsuzluk tanımı, uygunsuzluk detayı ve uygunsuzluk kategorisi belirlenir. İstenirse bilgilendirmeye eklenecek personeller, işyeri, süreç ve madde no seçildikten sonra yönetim sistemleri açılır menüsünden ilgili yönetim sistemi listeden seçilir.

Eğer DÖF Modülü için önceden parametrik alanlar oluşturulmuş ise Detay Bilgiler sekmesine geçilerek bu alanlar doldurulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8c6c22bb-d3dd-469e-8e8c-e4bf3618fe63)

Eğer oluşturulmamışsa Çözüm Ekibi sekmesi tıklanarak DÖF Çözüm Ekibi tanımlanır. DÖF Çözüm Ekibi ekranında çözüm ekibi lideri ve sorumlu departman seçilir. Ekip üyeleri, personel listesinden seçilir. Ayrıca Gelişme Raporu’nun yazılacağı son tarih belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload81a7349d-3cfd-4562-abd9-aecdfbe7c125)

Ek Dosyalar sekmesine geçilerek istenirse DÖF kaydına doküman, ses, görüntü vb. formatlarda istenen dosyaların eklenmesi gerçekleştirilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload33610a76-5838-40af-85b2-0e93196077de)

**![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd33e815e-062c-4907-aac8-446d2782bc68)**Kaydet butonu ile kaydedildiğinde eğer DÖF açma onayı için bir akış kurgulandıysa ilgili rolün onayına kurgulanmadıysa Ekip Liderine Gelişme Raporu yazılması için görev düşer. **Yeni DÖF girildikten sonra ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd33e815e-062c-4907-aac8-446d2782bc68) (kaydet) butonuna bastığınızda sistem yeni kaydı onaya gönderir.**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload04c9eee3-9026-4d73-92b2-3ca904a8b005)

Onaydaki kişi Rol tanımlamada “DÖF Açan” Rolü olarak tanımlamıştı. Bu Rol için Personel için tanımlanan SQL Sorgusu **SELECT SICIL_NO FROM BSAT001 WHERE SICIL_NO='fbas'** şeklinde yazılmıştı. Personel Tanımlama menüsündeki Furkan Baş olan personelin sicil numarası “fbas” olduğu için DÖF kaydı onay için bu kullanıcıya gönderilir. **Onaydaki kişiye sistem mail yollarken aynı zamanda bekleyen işlerine “Onay Bekleyen DÖF listesi” şeklinde iş düşürdüğü görüntülenir.**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5ed61b8d-2357-403d-aa73-38ad4d89e890)

#### **1.1.3.1.1.DÖF Onaylama**

DÖF, açma onayına gönderildikten sonra ilgili kişi, Bekleyen İşleri’ne gelerek “Onay Bekleyen DÖF’ ler “Listesi adı altında açma onayı vereceği DÖF’ü görür. DÖF no’sunun üzerine tıklayarak Onay Bekleyen DÖF’ler listesini görüntüler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadea4e681c-07d1-4daa-a76c-5403f5cfed75)

**Ekranda bulunan butonlar yardımıyla;**

**![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc16c4781-6c35-4eea-8cc7-85745518b448): İlgili DÖF kaydının görüntülemek istediğinizde kullanılır.**

**![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf9faa448-dcfc-483e-8608-a240722600e5) : İlgili DÖF kaydı ile değişik yapması istenirse kullanılır. Eğer talepten açılan DÖF ise zorunlu alanları doldurmadan onaylama işlemi yapmamıza sistem izin vermeyecektir.**

**![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcef4fcf0-b003-4ae4-8647-dbfa5fe1b833) : DÖF onaylama işlemini yapmak için kullanılır. Onay işleminden sonra ilgili DÖF kaydı Ekip Liderinin önüne düşer.**

**![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload61d72326-07c3-4029-91de-056689b196f6) : DÖF’ te girilen bilgiler uygun olmadığı durumda, DÖF’ ü reddetmek için kullanılır. Red edilen** açan kişiye ret etme nedeniyle birlikte gönderilebilir. Ret ederken detay bilgi için ret veya kaydın iptali için ret edilebilir, buna bağlı olarak ilgili seçeneği seçmelidir.

**![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcef4fcf0-b003-4ae4-8647-dbfa5fe1b833)** : Onayla butonu tıklanır. Onay notu yazılarak DÖF kaydı onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7df09c6e-542d-4680-a15f-0adb073f3973)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d0d0b71-3a5c-4374-b8cf-2d83ad9a9f49)

#### **1.1.3.1.2.Gelişme Raporu**

**Onaylama işleminden sonra gelişme raporu yazmak üzere Ekip Liderinin bekleyen işlerine düşer.** Ekip üyeleri/ ekip lideri, Bekleyen İşleri’ne gelerek “Gelişme Raporu Yazılacak DÖF’ler Listesi” sekmesinin altında ilgili DÖF no’su üzerine tıklayarak DÖF bilgilerinin olduğu ekrana gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadccfaa5e5-0d7b-4ffd-bcf9-987147f80504)

**Ekip lideri Acil aldığı önlemleri ve DÖF çalışmasının gidişatını Gelişme raporunda belirtir. DÖF Sonuçlandırma süresini, Ekibini varsa ek dosyasını ekleyerek kaydet butonunu tıklar ise bir sonra ki aşamaya geçilir**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload07ac734e-b2c3-4b7d-a939-585873c5e23e)

**![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload39e8471b-83db-474d-b24d-8806886305c9)** Kaydet butonuyla Gelişme Raporu kaydedilir.

#### **1.1.3.1.3.Kök Nedenler**

Gelişme raporu yazıldıktan sonra, Kök Nedenler sekmesi aktif olur. Kök Neden Analizi ekranına gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade7257d8b-cbb7-4469-847b-9d0b7ea4d8b0)

**Ekranda bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20a95e30-c500-4590-baf4-f2968cbce3bb) : Yeni bir kök neden eklemek için kullanılan butondur.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadce7a102b-027b-4213-88ab-19b81d4c54bf) : Girilen kök nedende değişiklik veya güncelleme yapmak istenirse kullanılan butondur.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload67f4bcc9-fdf2-44ec-a24a-6ce7a04d4651) : Yanlış girilen kök nedenleri silmek için kullanılan butondur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade6a94f63-4fe0-4407-b66f-f3e78a62a32e) Yeni butonu tıklanarak kök neden ekleme ekranına gelinir.

**![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc873a9f1-d49c-4703-be39-2f7f6f54c798) : Kök neden analiz raporu dosyasının sisteme eklenmesi için kullanılan butondur.**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf6dc6d4a-d87a-40b4-8090-8d81a8b84137)

Açılan ekranda daha önceden tanımlanan kök nedenlerden istenenler seçilir, açıklama bilgisi girilir. Daha sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada07245bb-c6c0-41a4-8f0c-5f200dedb8a7) kaydet butonu tıklanarak kök neden kaydedilerek DÖF ile ilişkisi kurulmuş olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6bd84b4e-0718-439f-a566-cf2d98d3836f)

#### **1.1.3.1.4.Aksiyonlar**

Kök Nedenler belirlendikten sonra süreç, DÖF Aksiyonlarının planlanması ile devam eder. Aksiyonlar sekmesine gelinir. Burada DÖF ile ilgili oluşturulacak aksiyonlar planlanır ve iş olarak atanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb9ba1a9-ec0a-409f-b09e-d6627a0c60af)

Ekranda bulunan butonlar yardımıyla;

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20a95e30-c500-4590-baf4-f2968cbce3bb) : Yeni bir aksiyon eklemek için kullanılan butondur.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload49609eb1-9549-443e-ba7f-65b5e8ae47b2) : Aksiyonun içeriğinin görmek için kullanılan butondur.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadce7a102b-027b-4213-88ab-19b81d4c54bf) : Girilen aksiyon ile ilgili değişiklik veya güncelleme yapmak istenirse kullanılan butondur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0a2d7b07-1853-4a6e-91b9-3c7824c8d221) : Aksiyonu kopyalamak için kullanılan butondur.

**![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload265967bc-b971-4196-ac90-ebd2dfb8cb65) : Aksiyon listesini Excel’e aktarmak için kullanılan butondur.**

**![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload58318ecd-9fdc-4663-91a7-7b7cf7637d34) : Planlanan aksiyonun termin süresini geciktirmek istediğimizde kullanılan butondur.**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload10efeb87-677a-4f3a-bd11-a780e9c33f0a) Yeni butonu tıklanarak Aksiyonlar-Yeni Kayıt ekranına gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade21423b9-367b-4ed7-86f9-ea5850d0f94b)

Açılan ekranda Aksiyondan sorumlu kişi ve aksiyonu yapacak kişi listeden seçilir, aksiyon bilgisi girilir, aksiyonun planlanan bitiş tarihi belirlenir, aksiyon ile ilgili standart madde numaraları eklenebilir, aksiyon ile ilgili varsa referans dokümanlar ve kök nedenler eklenir. Yine istenirse Ek Dosyalar kısmından, Aksiyon ile alakalı ek dosya, doküman vb. eklenebilir.

Aksiyon bilgileri girildikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload43e137ac-cbe4-43d1-8e99-fbe609c99bf1) (kaydet) butonuyla aksiyon planlanmış olur ve işi yapacak kişiye bilgilendirme olarak mail yoluyla gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload48e89014-4e9b-4a97-975f-637cc483383c)

Onaydaki kişi Rol tanımlamada “DÖF Ekip Üyeleri” Rolü olarak tanımlamıştı. Bu Rol için Kullanıcı Grubu için tanımlanan SQL Sorgusu **SELECT SICIL_NO FROM BSAT009A WHERE GRUP_KODU='DF.001'** şeklinde yazılmıştı. Kullanıcı Grubu Tanımlama menüsündeki “DÖF Ekip Üyeleri” olan kullanıcı grubun kodu “DF.001” olduğu için” DÖF Aksiyon Açma onayı”akışı onay için bu kullanıcı grubunda bulanan kişilere gönderilir. **Onaydaki kullanıcı grubundaki kişilere sistem mail yollarken aynı zamanda bekleyen işlerine “**Açma Onayı Bekleyen DÖF Aksiyonları Listesi**” şeklinde iş düşer. Akış tanımlamada kullanıcı grubunadaki 1 kişinin onaylaması yeterli olacak şekilde ayarlandığı için 1 kişi onayladığı zaman akış süreci diğer aşamada devam eder. Kullanıc grubu olan “DÖF Ekip Üyeleri” grubunda bulanan herhangi 1 kişinin seçilerek onaylama işlemi yapılır.**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload66f71437-2944-422f-b856-ba8c6972f390)

Aksiyon listesinde görüntülenir ve aksiyonu gerçekleştirecek kişilerin Bekleyen İşleri’nde **“Açma Onayı Bekleyen DÖF Aksiyonları Listesi”** görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8860d065-0aa4-41a7-ad8c-d6d9d2fe5416)

Bekleyen İşleri’nden Açma Onayı Bekleyen DÖF Aksiyonlar Listesi altına gelinerek DÖF-Aksiyon No üzerine tıklanır. Onay Bekleyen Döfler ekranına ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload81f40c31-d922-49ca-8c58-a6812b00469e)

**Ekranda bulunan butonlar yardımıyla;**

**![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc16c4781-6c35-4eea-8cc7-85745518b448): İlgili DÖF kaydının görüntülemek istediğinizde kullanılır.**

**![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcef4fcf0-b003-4ae4-8647-dbfa5fe1b833) : DÖF Aksiyon Açma onaylama işlemini yapmak için kullanılır. Onay işleminden sonra ilgili DÖF kaydı Ekip Liderinin önüne düşer.**

**![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload61d72326-07c3-4029-91de-056689b196f6) : DÖF’ te girilen bilgiler uygun olmadığı durumda, DÖF aksiyon Açma onayını reddetmek için kullanılır. Red edilen** açan kişiye ret etme nedeniyle birlikte gönderilebilir. Ret ederken detay bilgi için ret veya kaydın iptali için ret edilebilir, buna bağlı olarak ilgili seçeneği seçmelidir.

**![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcef4fcf0-b003-4ae4-8647-dbfa5fe1b833)** : Onayla butonu tıklanır. Onay notu yazılarak “DÖF Aksiyon Açma” kaydı onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadad20866c-ed00-44f6-ae1e-08968bdd3da3)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd58dbc71-9ab8-45ee-b7b8-9ddd6e070ea5)

Aksiyon listesinde görüntülenir ve aksiyonu gerçekleştirecek kişinin Bekleyen İşleri’nde “Gerçekleştirilecek DÖF Aksiyonları” listesi altında belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc81a3612-d06b-4b35-8469-7b28e2b20a93)

Bekleyen İşleri’nden Gerçekleştirilecek DöF Aksiyonlar Listesi altına gelinerek DöF-Aksiyon No üzerine tıklanır. DÖF bilgileri ekranına ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3f86c9be-e429-497d-b003-17affd8a2f7e)

Aksiyon sekmesine gelinir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7de118cd-3e60-4674-b370-6de62a05ada6)(Aksiyon gerçekleştir) butonu yardımıyla Aksiyon Gerçekleştirme Bilgisi girilecektir. Aksiyon Gerçekleştirme ekranında, aksiyonun gerçekleştirme bilgisi ve gerçekleştirme tarihi girilir. Ayrıca istenirse aksiyonun gerçekleştirme aşamasına ek dosya eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload51c8e174-d117-44a2-8024-b2215a2ba18e)

Aksiyon Gerçekleştirme ekranında, aksiyonun gerçekleştirme bilgisi ve gerçekleştirme tarihi girilir. Ayrıca istenirse aksiyonun gerçekleştirme aşamasına ek dosya eklenebilir. Yapılan iş ve varsa ek dosya eklendikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload43e137ac-cbe4-43d1-8e99-fbe609c99bf1)(kaydet) butonunu tıkladığımızda aksiyon gerçekleştirme onayı için kullanıcılara gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload55231816-9893-406b-a53e-b5695f591dbc)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadedabac1f-e62c-4aba-8561-bfb030456886)

İlgili kişileri Bekleyen İşlerinde “Gerçekleştirme Onayı Bekleyen DÖF Aksiyonlar Listesi” olarak iş düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload79049b8f-ac5a-429b-b786-3258c541fd58)

Bekleyen İşleri’nden “Gerçekleştirme Onayı Bekleyen DÖF Aksiyonlar Listesi” altına gelinerek DÖF-Aksiyon No üzerine tıklanır. Onay Bekleyen Döfler ekranına ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9c7cf8e5-4ba0-4a9d-84c0-f8a504fdab74)

**Ekranda bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc16c4781-6c35-4eea-8cc7-85745518b448)**: İlgili DÖF kaydının görüntülemek istediğinizde kullanılır.**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcef4fcf0-b003-4ae4-8647-dbfa5fe1b833) **:** Gerçekleştirme Onayı Bekleyen DÖF Aksiyonlar **işlemini yapmak için kullanılır. Onay işleminden sonra ilgili DÖF kaydı Ekip Liderinin önüne düşer.**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload61d72326-07c3-4029-91de-056689b196f6) **: DÖF’ te girilen bilgiler uygun olmadığı durumda,** Gerçekleştirme Onayı Bekleyen DÖF Aksiyonlar **onayını reddetmek için kullanılır. Red edilen** açan kişiye ret etme nedeniyle birlikte gönderilebilir. Ret ederken detay bilgi için ret veya kaydın iptali için ret edilebilir, buna bağlı olarak ilgili seçeneği seçmelidir.

**![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcef4fcf0-b003-4ae4-8647-dbfa5fe1b833)** Onayla butonu tıklanır. Onay notu yazılarak “Gerçekleştirme Onayı Bekleyen DÖF Aksiyonlar” kaydı onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadafd4e1fc-83c2-4dfb-a4e8-bf139fb66019)

#### **1.1.3.1.5.Sonuç Raporu**

Aksiyonlar planlanıp gerçekleştirildikten sonra süreç, sonuç raporunun yazılmasıyla devam eder. Ekip Lideri/ Üyesi, Bekleyen İşleri’ne gelerek “Sonuç Raporu Yazılacak DÖF’ler Listesi**”** sekmesinin altında ilgili DÖF’ü görür ve DÖF no’suna tıklayarak DÖF bilgilerinin olduğu ekrana gelir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1068b456-be99-4b11-ba0a-a14c9ebc4776)

Sonuç raporu, DÖF ile ilgili alınan nihai önlemleri, çözüm önerilerini içeren bir rapordur. DÖF İşlemleri sırasında yapılan tüm işlemlerin özeti niteliğinde, Kapatma onayı verecek kişi için hazırlanan sonuç raporudur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcee46053-4fb2-47b9-aa77-85aa2700c1b6)

Açılan ekranda Sonuç Raporu yazılır. Sonuç Raporu’na eklenmek istenen ek dosyalar, eklenebilir. Daha sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload43e137ac-cbe4-43d1-8e99-fbe609c99bf1) (kaydet) butonuyla Sonuç Raporu kaydedilir ve DÖF kapatma onayına gider.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4424e5a0-256e-4d87-ad7a-a83b16975ded)

Sonuç raporu yazılma işlemi kaydedildikten sonra, önceden belirlenen DÖF kapatma sorumlusuna **“**Kapatılacak DÖF’ler Listesi**”** olarak bekleyen işlerine düşecektir.

#### **1.1.3.1.6.Kapatma**

“Kapatılacak DÖF’ler Listesi**”** sekmesi altında ilgili DÖF’ü görüntüler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload99240cac-f8f3-4b58-9bd8-6e54c9d173ad)

DÖF no’su üzerine tıklayarak “Onay Bekleyen DÖF’ler**”** ekranına gelir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd3ccdd7a-d1b5-4c5a-b19a-bbaebd9d854f)

**Ekranda bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload49609eb1-9549-443e-ba7f-65b5e8ae47b2) : DÖF ile ilgili tüm bilgileri görüntülemek için kullanılan butondur.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadae193758-e1b7-4c1f-a598-cb5405c23bb5) : Kapatma onayı verecek kişi yapılan aksiyonların yeterli olmadığı kararı verdiğinde, eksik kalan aksiyonları tanımlamada kullandığı butondur.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9ec38415-1f7b-46d6-a0d7-8e55ff2a661c): Yapılan aksiyonların yeterliliğini, etkinliğini veya düzgün yapılıp yapılmadığını farklı bir kişi tarafından izlenerek rapor yazma görevi verilmek istendiğinde kullanılan butondur.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc6afc87b-799b-4a50-8b24-90cdcd11ffa6): Kapatma onayı verilecek DÖF’leri filtreleme işlemi için kullanılan butondur

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload99b88e00-0a27-4845-b176-f64c8bf65aff) Kapatma butonu tıklanarak DÖF’ü Kapatma ekranına gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc6bdc7e9-f8f3-4f88-b361-9141a02bf858)

Açılan ekranda yeterlilik bilgisi girilir. Ayrıca istenirse uygunsuzluk kategorisi alanına eklemeler yapılabilir. Yine istenirse kapatma aşamasına ek dosya eklenebilir. Gerekli alanlar doldurulduktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d99b5ab-6ce6-4d37-840c-324b8419a99b) (kaydet) butonu tıklanarak bilgiler kaydedilir ve DÖF kapatılmış olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddeee09a9-90bd-41bc-8c74-7436e4bd0883)
