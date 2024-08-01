---
title: Atık Yönetim
description: Atık Yönetim Yardım Dokümanı
sidebar_position: 31
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::


**Atık Yönetim Modülü(v.5.24) Kullanıcı Yardım Dokümanı**

Modül Versiyonu: 5.24



**1.GİRİŞ:** Çevre ve Şehircilik Bakanlığı’nın yayınlamış olduğu Atık Yönetimi Yönetmeliği’ne göre tehlikeli ve tehlikesiz atıkların taşınması, belirli kurallara bağlanmıştır. Bu yönetmeliğe göre tehlikeli atıklar lisanslı taşıyıcı tarafından taşınıp lisanslı bertaraf firmalarına teslim edilecektir. Bu süreçte Ulusal Atık Taşıma Formu adı verilen ve kısaca UATF olarak adlandırılan atığın bulunduğu yerden atık işleme tesisine kadar taşıma işlemlerinde kullanılan, kayıt ve beyanlarını içeren formlar kullanılmaktadır. Ulusal Atık Taşıma Formu (UATF), 14/03/2005 tarih ve 25755 sayılı Resmi Gazetede yayımlanan Tehlikeli Atıkların Kontrolü Yönetmeliğinin Ek-9 unda yer alan formu, ifade etmektedir.

**2.AMAÇ:** Bu yardım kılavuzunun amacı, atık üreticisi firmadaki QDMS kullanıcısının, Atık Yönetimi Modülünü kullanarak Ulusal Atık Taşıma Formu’nu ve Atık Yönetim Planı’nı oluştururken kullanacağı yolu belirlemektir.

**3.SORUMLULUKLAR:** Üretici firma sorumlusu, taşıyıcı firma sorumlusu, alıcı firma sorumlusu.

**4.KISALTMALAR:** UATF: Ulusal Atık Taşıma Formu

**5.İŞ AKIŞI:**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb1a39036-7aa0-4314-b3f8-aa19e490596f)



# **6. ATIK YÖNETİMİ MODÜLÜ**

Atığın kaynağında azaltılması, özelliğine göre ayrılması, toplanması, geçici depolanması, ara depolanması, geri kazanılması, taşınması, bertarafı ve bertaraf işlemleri sonrası kontrolü ve benzeri işlemleri içeren bir yönetim biçimidir.

Kurum içerisinde toplanmış tehlikeli ve tehlikesiz atıkların lisanslı taşıyıcılar tarafından sevk edilmesi sürecini yönetilmesi, Atık yönetim planları oluşturulması, Atık lisanslarını tanımlanması, takibini sistem üzerinden gerçekleştirilmesi, Tehlikeli ve tehlikesiz atık formları doldurulması, tüm işlemler için sistem tarafından otomatik bildirimler gönderilmesi, ihtiyaca yönelik faklı akışların tasarlanması ve farklı özel parametrik tipli alanların tanımlandığı modüldür.

## **6.1.Sistem Altyapı Tanımları/Atık Yönetimi**

Atık Yönetim Modülünün altyapısının oluşturulacak tanımlamaların yapıldığı kısımdır. Yapılan tanımlamalara göre giriş ekranında veriler karşımıza çıkmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload066b5fa1-4b3f-4230-86ed-3a4632b8e812)Atık Yönetimi Modülünün altyapı tanımları şu alt başlıklardan oluşur;

-   Atık Türü Tanımlama
-   H Kodu Tanımlama
-   Firma Tanımlama
-   Bertaraf Yöntemi Tanımlama
-   Geri Kazanım Yöntemi Tanımlama
-   Sabit İşlemleri
-   Alan Tanımlama
-   Fonksiyon Dizayner
-   Atık Yetki Matrisi

Bu tanımlamalardan sadece Firma Tanımlama menüsü, Modülü kullanacak kuruma özel bir alandır. Diğer bütün tanımlama alanları Modül kurulumunda tebliğin gerektirdiği varsayılan verilerle gelecektir.

### **6.1.1.Atık Türü Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/Atık Yönetimi/ Atık Türü Tanımlama

Hazır olarak gelen standart atık türleri listesi görüntülendiği menüdür. Bu listedeki atık türleri 6 basamaklı koda ulaşacak şekilde kırılımlandırılmıştır. Atık Yönetimi Modülü içerisinde kullanılacak tüm atık türleri bu listeden seçilecektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload608e0411-9aaa-4b6f-aead-8787d46f3ae8)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload71b6f966-3431-4824-8265-afae6abad8a9): Yeni bir Atık Türü eklenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec02cbd1-eacd-49cd-94fa-b6eed46112b6): Listede seçili Atık Türü ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada5a8c439-df5b-4dee-b6e6-1c77595159b3) : Kayıtlar filtrelenerek arama yapılabilir.

Atık Türleri ekranına yeni bir Atık Türü eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f57774d-d120-4475-8917-d6c73e233f15)(yeni) butonu tıklanarak Atık Türleri/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload374bbfb6-81f7-4d8a-9543-4e65947a80dd)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Üst Kategori Kodu:** Atık Türü Tanımlama ekranında Atık Türünün Üst Kategori Kodu seçilebildiği alandır.

**Atık Kodu:** Atık Türü Tanımlama ekranında Atık Türünün 6 basamaklı kod bilgisinin girildiği alandır.

**Atık Tanım:** Atık Türü Tanımlama ekranında Atık Türünün Atık Tanımı bilgisinin girildiği alandır.

**Durum:** Atık Türü Tanımlama ekranında Atık Türünün Aktif veya Pasif durum bilgisinin girildiği alandır.

Açılan ekranda Atık Türü Üst kategori kodu seçilir. 6 basamaklı Atık Türü kod bilgisi girilir. Atık tanımı bilgisi tanımlanır. Atık Türü Tehlikeli ise ilgili check box işaretlenir. Durum bilgisi "Aktif" ve "Pasif" olarak ikiye ayrılmaktadır. Aktif olarak tanımlı Atık Türleri sistemde kullanılan Atık Türlerini ifade etmektedir. Eğer bir Atık Türü tanımı sistemde artık kullanılmayacaksa, durumu bilgisi “Pasif” olarak değiştirilmelidir. Böylece hem geçmişteki mevcut kayıtlar etkilenmez, hem de yeni Atık Türü seçim ekranlarında pasife alınan Atık Türleri bilgisi görüntülenmez. Atık Türünün durum kısmı Aktif olarak seçilir. Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfc9fd407-ee4e-4fe1-9e58-b1e1c085f537) (kaydet) butonu tıklanarak Atık Türü Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload76d090dd-69fa-41c1-8a8a-49744742186d)

### **6.1.2.H Kodu Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/Atık Yönetimi/H Kodu Tanımlama

H kodlarının tanımlama işlemlerinin yapıldığı menüdür. H kodları tehlikeli kabul edilebilen atıkların özelliklerini gösterirler. Tehlikeli atığın sınıflandırma, ambalajlama ve etiketlemesinde kullanılırlar. Ayrıca Ulusal Atık Taşıma Formunda atığın tehlikeli kabul edilebilen özelliğini belirtmek için kullanılırlar. Modül kurulumu yapılırken bu kodlar otomatik olarak gelmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadce8f1d5d-7a2e-498c-afda-4e3ca78e85b9)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload71b6f966-3431-4824-8265-afae6abad8a9): Yeni bir H kodu tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec02cbd1-eacd-49cd-94fa-b6eed46112b6): Listede seçili H kodu bilgisi ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

H Kodu Tanımlama ekranına yeni bir H Kodu eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f57774d-d120-4475-8917-d6c73e233f15)(yeni) butonu tıklanarak H Kodu Tanımlama /Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade63602b5-0081-4789-ae05-e31f854a38dd)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Kod:** H Kodu Tanımlama ekranında H Kodunun Kod bilgisinin girildiği alandır.

**Tanım:** H Kodu Tanımlama ekranında H Kodunun Tanım bilgisinin girildiği alandır.

**Durum:** H Kodu Tanımlama ekranında H Kodunun Aktif ve Pasif durum bilgisinin seçilebildiği alandır.

Açılan ekranda H Kodu tanımlanırken H kodunın kod ve tanım bilgisi girilir. Durum bilgisi "Aktif" ve "Pasif" olarak ikiye ayrılmaktadır. Aktif olarak tanımlı H Kodu sistemde kullanılan H Kodularını ifade etmektedir. Eğer bir H Kodu tanımı sistemde artık kullanılmayacaksa, durumu bilgisi “Pasif” olarak değiştirilmelidir. Böylece hem geçmişteki mevcut kayıtlar etkilenmez, hem de yeni H Kodu seçim ekranlarında pasife alınan H Kodu bilgisi görüntülenmez. H kodunun durum kısmı Aktif olarak seçilir. Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfc9fd407-ee4e-4fe1-9e58-b1e1c085f537) (kaydet) butonu tıklanarak H Kodu Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload615e1196-3668-4a87-abf5-65c1e1717237)

### **6.1.3.Firma Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/Atık Yönetimi/ Firma Tanımlama

Atık üreticisi firma, taşıyıcı firma ve alıcı firmalar tanımlama işlemini gerçekleştiği menüdür. Bu menüde veriler hazır olarak gelmeyip, tamamen Modülü kullanan kuruma özel olarak oluşturulur. Bu listeye atığı üreten firmalar, atığı taşıyacak firmalar ve atığı bertaraf edecek alıcı firmalar ayrı ayrı tanımlanır. Taşıyıcı ve alıcı firmalar için atık türüne göre mevcut lisanslar belirlenir ve tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6d137501-09c1-4fbd-9563-d630bf77bc26)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload71b6f966-3431-4824-8265-afae6abad8a9):Yeni bir Firma tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec02cbd1-eacd-49cd-94fa-b6eed46112b6): Listede seçili Firma bilgisi ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeaaef181-9a2b-409f-8479-31ff4976070f): Listede seçili Firma bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada5a8c439-df5b-4dee-b6e6-1c77595159b3): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4607bdda-010e-4174-89c1-f44f6c699c1d): Veriler Excel’ e aktarılabilir.

Firma Tanımlama ekranına yeni bir Firma eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f57774d-d120-4475-8917-d6c73e233f15)(yeni) butonu tıklanarak Firma Tanımlama/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf35935fb-5725-4b95-a1a4-81ea611c0428)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Unvan:** Firma Bilgileri sekmesinde Firmanın adının bilgisinin girildiği alandır.

**Firma Sahibi:** Firma Bilgileri sekmesinde Firma Sahibi bilgisinin girildiği alandır.

**İl:** Firma Bilgileri sekmesinde Firmanın bulunduğu İl bilgisinin girildiği alandır.

**İlçe:** Firma Bilgileri sekmesinde Firmanın bulunduğu İlçe bilgisinin girildiği alandır.

**Mahalle/Semt:** Firma Bilgileri sekmesinde Firmanın bulunduğu Mahalle/Semt bilgisinin girildiği alandır.

**Cadde/Sokak:** Firma Bilgileri sekmesinde Firmanın bulunduğu Cadde/Sokak bilgisinin girildiği alandır.

**Kapı No:** Firma Bilgileri sekmesinde Firmanın Kapı No bilgisinin girildiği alandır.

**Vergi No:** Firma Bilgileri sekmesinde Firmanın Vergi No Bilgisinin girildiği alandır.

**Telefon:** Firma Bilgileri sekmesinde Firmanın Telefon Numarası bilgisinin girildiği alandır.

**Fax No:** Firma Bilgileri sekmesinde Firmanın Fax Numarası bilgisinin girildiği alandır.

**Sorumlu Kişinin Adı ve Soyadı:** Firma Bilgileri sekmesinde Firmanın Sorumlu Kişinin Adı ve Soyadı bilgisinin girildiği alandır.

**Firma Türü:** Firma Bilgileri sekmesinde Taşıyıcı, Üretici ve Alıcı Firma türü seçeneklerinin seçilebildiği alandır.

**Durum:** Firma Bilgileri sekmesinde Firmanın Aktif ve Pasif durum bilgilerinin seçilebildiği alandır.

**Lisans Sekmesi:**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4143ff31-9694-4ddb-a26d-3c0daa98a7c1)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload71b6f966-3431-4824-8265-afae6abad8a9): Yeni bir Lisans tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec02cbd1-eacd-49cd-94fa-b6eed46112b6): Listede seçili Lisans bilgisi ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeaaef181-9a2b-409f-8479-31ff4976070f): Listede seçili Lisans bilgisi silinebilir.

Lisans Tanımlama ekranına yeni bir Lisans eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f57774d-d120-4475-8917-d6c73e233f15)(yeni) butonu tıklanarak Lisans Tanımlama/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload436f188c-b192-4524-b417-a104d890a7fc) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada07a39e2-05cc-4ff6-810a-419d2626462a)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Lisans No:** Lisans Sekmesinde Lisans No Bilgisinin girildiği alandır.

**Firma Türü:** Lisans Sekmesinde Üretici, Taşıyıcı ve Alıcı Firma Türleri aktif edilecekse ilgili check box işaretlenir.

**Lisans Kodları:** Lisans Sekmesinde Lisans Kodları Atık Seç (Seçilen Atığın Kodu 6 Haneli olmalı) Listesinden seçilebildiği alandır.

**Lisans Türü:**  Lisans Sekmesinde Lisans Türü Lisans olarak seçilebilecekse ilgili check box işaretlenir. Lisans Türü Geçici Faaliyetler Belgesi seçilebilecekse ilgili check box işaretlenir.

**Bitiş Tarihi:** Lisans Sekmesinde Lisans Bitiş Tarihi bilgisinin girildiği alandır.

**Lisans Durumu**: Lisans Sekmesinde Lisans Durumun Aktif veya Pasif seçilebildiği alandır.

**Plaka:** Lisans Sekmesinde plaka bilgisinin girildiği alandır.

Açılan ekran taşıyıcı ve alıcı firmalar için doldurulur. Lisans bilgileri sekmesinde Firma lisans numarası, lisans kodları, lisans türü, lisans bitiş tarihi ve varsa plaka bilgileri sisteme girilir.

Firma lisans bitiş tarihine göre atık yönetimi parametrelerinden 2. parametrede belirlenen süre öncesi Modül yöneticisine ve 3.parametrede tanımlanan role uyarı mesajı gitmektedir.

Atık Yönetimi 2. Parametre

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbd9ea22a-0c7c-42d9-9dc2-a347d7a33772)

Atık Yönetiminde 3. Parametre.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c9608ab-37bb-4ab6-9976-51e7eaa717ff)

Eğer taşıt plakalarının Firma üzerinden otomatik gelmesi yerine manuel olarak sisteme giriş yapılması isteniliyorsa atık yönetimi parametrelerinden 5. Parametre aktif hale getirilir.

Atık Yönetimi 5.Parametre

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload77550418-38ca-4a70-a5c1-f29833d4d931)

Tüm bu işlemler gerçekleştirildikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0b383724-2383-4730-a639-cb69d3f86b32) ( kaydet) butonu ile lisans kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9089473e-9d3b-495a-9d86-febfa3716b77)

Lisanslar bu şekilde kaydedildikten sonra ekranın en üst sağ köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0b383724-2383-4730-a639-cb69d3f86b32) (kaydet) butonu ile Firma bilgisi kaydedilmiş olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload23960bce-309b-453a-8785-b657d63fca2c)

Firmalar ekranındaki Arama sekmesinden firma türüne, adına ve iline göre arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload203a721d-583e-4a47-ab39-a96e234f85e1)

### **6.1.4.Bertaraf Yöntemi Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/Atık Yönetimi/ Bertaraf Yöntemi Tanımlama

Atık Yönetim Modülünde ilgili atıklara ait bertaraf yöntemi tanımlama işleminin gerçekleştiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade2f670a2-9cd2-4149-a04f-9136f22b4235)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload71b6f966-3431-4824-8265-afae6abad8a9): Yeni bir Bertaraf Yöntemleri tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec02cbd1-eacd-49cd-94fa-b6eed46112b6): Listede seçili Bertaraf Yöntemleri bilgisi ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

Bertaraf Yöntemleri Tanımlama ekranına yeni bir Bertaraf Yöntemleri eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f57774d-d120-4475-8917-d6c73e233f15)(yeni) butonu tıklanarak Bertaraf Yöntemleri Tanımlama /Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddadae7bb-40c7-4b01-9037-2fbfdce634b1)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Kod:** Bertaraf Yöntemi Tanımlama ekranında Bertaraf Yöntemi kod bilgisinin girildiği alandır.

**Tanım:** Bertaraf Yöntemi Tanımlama ekranında Bertaraf Yöntemi Tanım bilgisinin girildiği alandır.

**Durum:** Bertaraf Yöntemi Tanımlama ekranında Bertaraf Yönteminin Aktif veya Pasif Durum bilgisinin seçilebildiği alandır.

Açılan ekranda Bertaraf yöntemin kod ve tanım bilgisi girilir. Durum bilgisi "Aktif" ve "Pasif" olarak ikiye ayrılmaktadır. Aktif olarak tanımlı Bertaraf Yöntemi sistemde kullanılan Bertaraf Yöntemlerini ifade etmektedir. Eğer bir Bertaraf Yöntemi tanımı sistemde artık kullanılmayacaksa, durumu bilgisi “Pasif” olarak değiştirilmelidir. Böylece hem geçmişteki mevcut kayıtlar etkilenmez, hem de yeni Bertaraf Yöntemi seçim ekranlarında pasife alınan Bertaraf Yöntemi bilgisi görüntülenmez. Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfc9fd407-ee4e-4fe1-9e58-b1e1c085f537) (kaydet) butonu tıklanarak Bertaraf Yöntemi Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d48ff8e-e2bd-43c3-8c1a-286785fb40e0)

### **6.1.5.Geri Kazanım Yöntemi Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/Atık Yönetimi/ Geri Kazanım Yöntemi Tanımlama

Atık yönetimi Modülüne ait geri kazanım yöntemi tanımlama işleminin gerçekleştiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload799f4b2e-2d8f-4ac5-9043-a9c45df15a0d)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload71b6f966-3431-4824-8265-afae6abad8a9):Yeni bir Geri Kazanım Yöntemleri tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec02cbd1-eacd-49cd-94fa-b6eed46112b6): Listede seçili Geri Kazanım Yöntemleri bilgisi ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

Geri Kazanım Yöntemleri Tanımlama ekranına yeni bir Geri Kazanım Yöntemleri eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f57774d-d120-4475-8917-d6c73e233f15)(yeni) butonu tıklanarak Geri Kazanım Yöntemleri Tanımlama /Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4eba58f7-8814-4d17-93fc-c98b70c4c0d8)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Kod:** Geri Kazanım Yöntemleri Tanımlama ekranında Geri Kazanım Yöntemleri kod bilgisinin girildiği alandır.

**Tanım:** Geri Kazanım Yöntemleri Tanımlama ekranında Geri Kazanım Yöntemleri Tanım bilgisinin girildiği alandır.

**Durum:** Geri Kazanım Yöntemleri Tanımlama ekranında Geri Kazanım Yöntemleri Aktif veya Pasif Durum bilgisinin seçilebildiği alandır.

Açılan ekranda Geri Kazanım Yöntemlerinin kod ve tanım bilgisi girilir. Durum bilgisi "Aktif" ve "Pasif" olarak ikiye ayrılmaktadır. Aktif olarak tanımlı Geri Kazanım Yöntemleri sistemde kullanılan Geri Kazanım Yöntemleri ifade etmektedir. Eğer bir Geri Kazanım Yöntemleri tanımı sistemde artık kullanılmayacaksa, durumu bilgisi “Pasif” olarak değiştirilmelidir. Böylece hem geçmişteki mevcut kayıtlar etkilenmez, hem de yeni Geri Kazanım Yöntemleri seçim ekranlarında pasife alınan Geri Kazanım Yöntemleri bilgisi görüntülenmez. Geri Kazanım Yöntemin durum kısmı Aktif seçilir. Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfc9fd407-ee4e-4fe1-9e58-b1e1c085f537) (kaydet) butonu tıklanarak Geri Kazanım Yöntemleri Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfc2c9f05-5d58-43b0-9da9-afeb512b690c)

### **6.1.6.Atık Yönetimi Parametreleri**

**Menü Adı:** Sistem Altyapı Tanımları/Atık Yönetimi/ Atık Yönetimi Parametreleri

Atık Yönetimi Modülünün kullanıcının istek ve ihtiyaçlarına göre sistemsel ayarlarının yapıldığı ve bunlara göre parametreleri belirlendiği (seçilebildiği) menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5ddece0c-6eb0-40c5-994c-e2c0e285a3c4)

**Ekranındaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec02cbd1-eacd-49cd-94fa-b6eed46112b6): Listede seçili parametre güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada5a8c439-df5b-4dee-b6e6-1c77595159b3): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4607bdda-010e-4174-89c1-f44f6c699c1d): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload46d23d7b-3046-4fbb-814b-42b8272b1f21)

### **6.1.7.Sabit İşlemleri**

**Menü Adı:** Sistem Altyapı Tanımları/Atık Yönetimi/ Sabit İşlemleri

Atık Yönetim Modülünde taşıma türleri, fiziksel Özellikler, renkler, ambalaj ve konteynır türleri gibi sabit işlemlerin tanımlama işlemlerinin gerçekleştiği menüdür.

### **6.1.7.1.Taşıma Türleri**

Sistem Altyapı Tanımları/Atık Yönetimi/ Sabit İşlemler/ Taşıma Türleri

Atık Yönetim Modülünde sabit işlemlerde atığın karayolu, hava ve deniz gibi taşıma türlerinin tanımlama işleminin gerçekleştiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadafa5ccf9-ef51-405e-93b9-e235b3b7878a)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload71b6f966-3431-4824-8265-afae6abad8a9):Yeni bir Taşıma Türü tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec02cbd1-eacd-49cd-94fa-b6eed46112b6): Listede seçili Taşıma Türü bilgisi ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeaaef181-9a2b-409f-8479-31ff4976070f): Listede seçili Taşıma Türü bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada5a8c439-df5b-4dee-b6e6-1c77595159b3):Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4607bdda-010e-4174-89c1-f44f6c699c1d) :Veriler Excel’ e aktarılabilir.

Sabitler/Taşıma Türü ekranına yeni bir Taşıma Türü eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f57774d-d120-4475-8917-d6c73e233f15)(yeni) butonu tıklanarak Sabitler-Taşıma Türü /Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfb10c737-9884-4081-843b-b06fc4175780)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Sabit Kodu:** Sabitler/Taşıma Türü ekranında Atığın Taşıma Türünün Sabit Kod bilgisinin girildiği alandır.

**Sabit Tanımı:** Sabitler/Taşıma Türü ekranında Atığın Taşıma Türünün Sabit Tanım bilgisinin girildiği alandır.

Açılan ekranda Atığın Taşıma Türü Sabit Kodu ve Sabit Tanımı bilgisi girilir. Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfc9fd407-ee4e-4fe1-9e58-b1e1c085f537) (kaydet) butonu tıklanarak Sabitler/Taşıma Türü kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload859ad45e-26a6-40df-9275-2089453de951)

### **6.1.7.2.Fiziksel Özellikler**

**Menü Adı:** Sistem Altyapı Tanımları/Atık Yönetimi/ Sabit İşlemler/ Fiziksel Özellikler

Atık Modülünde sabit işlemlerde atığın katı, toz ve sıvı gibi fiziksel özelliklerin tanımlama işleminin gerçekleştiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload13042324-69f5-4abb-9071-d892bf1d5e93)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload71b6f966-3431-4824-8265-afae6abad8a9): Yeni bir Fiziksel Özellik tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec02cbd1-eacd-49cd-94fa-b6eed46112b6): Listede seçili Fiziksel Özellik bilgisi ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeaaef181-9a2b-409f-8479-31ff4976070f): Listede seçili Fiziksel Özellik bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada5a8c439-df5b-4dee-b6e6-1c77595159b3): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4607bdda-010e-4174-89c1-f44f6c699c1d): Veriler Excel’ e aktarılabilir.

Sabitler/Fiziksel Özellik ekranına yeni bir Fiziksel Özellik eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f57774d-d120-4475-8917-d6c73e233f15)(yeni) butonu tıklanarak Sabitler/Fiziksel Özellik /Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadacd4c97f-dcf0-45b1-806b-216ea651c980)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Sabit Kodu:** Sabitler/Fiziksel Özellik ekranında Atığın Fiziksel Özelliğin Sabit Kod bilgisinin girildiği alandır.

**Sabit Tanımı:** Sabitler/Fiziksel Özellik ekranında Atığın Fiziksel Özelliğin Sabit Tanım bilgisinin girildiği alandır.

Açılan ekranda Atığın Fiziksel Özelliğin Sabit Kod ve Sabit Tanımı bilgisi girilir. Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfc9fd407-ee4e-4fe1-9e58-b1e1c085f537) (kaydet) butonu tıklanarak Sabitler/Fiziksel Özellik kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd94844fc-a97d-465c-9ad3-df0332c19717)

### **6.1.7.3.Renkler**

**Menü Adı:** Sistem Altyapı Tanımları/Atık Yönetimi/ Sabit İşlemler/ Renkler

Atık Yönetim Modülünde Sabit İşlemlerde atığın renginin tanımlama işleminin gerçekleştiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada85a41e4-b316-4650-8b79-ebea6276ea59)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload71b6f966-3431-4824-8265-afae6abad8a9): Yeni bir Renk tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec02cbd1-eacd-49cd-94fa-b6eed46112b6): Listede seçili Renk bilgisi ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeaaef181-9a2b-409f-8479-31ff4976070f): Listede seçili Renk bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada5a8c439-df5b-4dee-b6e6-1c77595159b3): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4607bdda-010e-4174-89c1-f44f6c699c1d):Veriler Excel’ e aktarılabilir.

Sabitler/Renk ekranına yeni bir Renk eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f57774d-d120-4475-8917-d6c73e233f15)(yeni) butonu tıklanarak Sabitler/Renk/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaecc7110-6d6a-45d9-8341-d598839bd052)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Sabit Kodu:** Sabitler/Renk ekranında Atığın Renginin Sabit Kod bilgisinin girildiği alandır.

**Sabit Tanımı:** Sabitler/Renk ekranında Atığın Renginin Sabit Tanım bilgisinin girildiği alandır.

Açılan ekranda Atığın Renginin Sabit Kod ve Sabit Tanım bilgisi girilir. Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfc9fd407-ee4e-4fe1-9e58-b1e1c085f537) (kaydet) butonu tıklanarak Sabitler/Renk kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload945b3e35-7732-4124-a6ec-f28737ae677b)

### **6.1.7.4.Ambalaj ve Konteynır Türleri**

**Menü Adı:** Sistem Altyapı Tanımları/Atık Yönetimi/ Sabit İşlemler/ Ambalaj ve Konteynır Türleri

Atık Yönetim Modülünde sabit işlemlerde atığın ambalaj ve konteynır türlerinin tanımlama işleminin gerçekleştiği menüdür. Örnek varil, ahşap fıçı, bidon gibi.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcc3e90d5-b66d-4bf0-a081-2f58cab4ee80)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload71b6f966-3431-4824-8265-afae6abad8a9):Yeni bir Ambalaj ve Konteynır Türü tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec02cbd1-eacd-49cd-94fa-b6eed46112b6):Listede seçili Ambalaj ve Konteynır Türü bilgisi ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeaaef181-9a2b-409f-8479-31ff4976070f):Listede seçili Ambalaj ve Konteynır Türü bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada5a8c439-df5b-4dee-b6e6-1c77595159b3):Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4607bdda-010e-4174-89c1-f44f6c699c1d):Veriler Excel’ e aktarılabilir.

Sabitler/Ambalaj ve Konteynır Türü ekranına yeni bir Ambalaj ve Konteynır Türü eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f57774d-d120-4475-8917-d6c73e233f15)(yeni) butonu tıklanarak Sabitler/Ambalaj ve Konteynır Türü /Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade017b614-0af4-4875-b839-20bca41e330a)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Sabit Kodu:** Sabitler/Ambalaj ve Konteynır Türü ekranında Atığın Ambalaj ve Konteynır Türünün Sabit Kod bilgisinin girildiği alandır.

**Sabit Tanımı:** Ambalaj ve Konteynır Türü ekranında Atığın Ambalaj ve Konteynır Türünün Sabit Tanım bilgisinin girildiği alandır.

Açılan ekranda Atığın Ambalaj ve Konteynır Türünün Sabit Kodu ve Sabit Tanım bilgisi girilir. Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfc9fd407-ee4e-4fe1-9e58-b1e1c085f537) (kaydet) butonu tıklanarak Sabitler/Ambalaj ve Konteynır Türü kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb384d75a-cc5e-4db1-9e4c-11e99205eae4)

### **6.1.8.Alan Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/Atık Yönetimi/ Alan Tanımlama

Atık Yönetim Modülünün yer alacak bütün alanların tanımlandığı menüdür. Burada oluşturulan alanlar, alan havuzuna kaydedilir. Buradaki alan tanımlama özelliği, QDMS’in risk Modüllerindeki alan tanımlama özellikleri ile aynıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc556deaa-3c7e-47b9-9c28-04096047e741)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload71b6f966-3431-4824-8265-afae6abad8a9):Yeni bir alan eklenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec02cbd1-eacd-49cd-94fa-b6eed46112b6):Var olan alanda değişiklik yapılmak istenirse kullanılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeaaef181-9a2b-409f-8479-31ff4976070f):İlgili alanı silmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload07485f77-3839-4545-af0b-9d624decf68f) :Alanın değerleri tanımlanır.

Alan Tanımlama ekranına yeni bir alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f57774d-d120-4475-8917-d6c73e233f15)(yeni) butonu tıklanarak Alan Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9af227f0-2668-4d4f-a279-c0244f85850f)![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb5c9d967-2fab-44d3-a977-0d3d21981478)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Alan Kodu:** Alan Tanımlama ekranında Alan Kodu bilgisinin girildiği alandır.

**Alan Adı:** Alan Tanımlama ekranında Alan Adı bilgisinin girildiği alandır.

**Başlık Notu:** Alan Tanımlama ekranında Alan Başlık Notu bilgisinin girildiği alandır.

**Giriş Tipi:** Alan Tanımlama ekranında Giriş tipinin hesaplanan veya veri girişi tipi bilgisinin seçilebildiği alandır. Giriş tipi seçeneği oluşturulan alanın manuel olarak veri girişi ile mi yoksa hesaplama yöntemi ile mi belirleneceğini gösterir.

**Alan Tipi**: Alan Tanımlama ekranında alan tipinin bilgisinin seçilebildiği alandır. Alan Tipi ise oluşturulan alanın metin, numerik, tarih, liste vb. tiplerinden hangisi olduğunu gösterir.

**Görünme Şartı:** Alan Tanımlama ekranında Görünme Şartı bilgisinin girildiği alandır. Liste tipli alanın değerlerine göre oluşturulan alanın görüntülenmesini sağlar.

**Durum:** Alan Tanımlama ekranında durumun Aktif veya Pasif olarak bilgisinin seçilebildiği alandır. Aktif olarak tanımlı alanlar sistemde kullanılan alanları ifade etmektedir. Eğer bir alan sistemde artık kullanılmayacaksa, durumu bilgisi “Pasif” olarak değiştirilmelidir. Böylece hem geçmişteki mevcut kayıtlar etkilenmez, hem de yeni alan seçim ekranlarında pasife alınan alan bilgisi olarak görüntülenir.

Açılan ekranda alan kodu ve alan tanımı bilgisi girilir. Giriş Tipi Veri Girişi olarak seçilir. Alan tipi sistemde tanımlı alan tiplerinden Metin tipli alan tipi seçilir. Tanımlanan alanın Durum kısmı Aktif seçilir. Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfc9fd407-ee4e-4fe1-9e58-b1e1c085f537) (kaydet) butonu tıklanarak Alan Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf7d11286-c750-42e2-a293-0abdc5d466d2)

**Sistemde mevcut bulunan alan tiplerinin tam listesi aşağıda belirtilmiştir;**

**Metin:** Text kutucuğu ekler.

**Metin Çok Satırlı:** Çok satırlı text kutucuğu ekler.

**Nümerik-Parasal:** Parasal değer olarak nümerik giriş yaptırır.

**Nümerik-Birim:** Birim olarak nümerik giriş yaptırır.

**Tarih:** Takvim alanı ekler.

**Liste:** Birden fazla element arasından tek seçim yaptırır.

**Puanlı Liste:** Açılır menüden tekli seçim yaptırır, liste elementlerinin puan değerleri mevcuttur.

**Arama Özellikli Liste:** Açılır menü altından birden fazla seçim yapılmasını sağlar.

**Ağaç Liste:** Ağaç dallanması şeklinde menü altından birden fazla seçim yapılmasını sağlar.

**Personel:** QDMS Personel veri tabanından kişi bilgisi seçilebilmesini sağlar.

**Departman:** QDMS Departman veri tabanından departman bilgisi seçilebilmesini sağlar.

**Unvan:** QDMS Unvan veri tabanından unvan bilgisi seçilebilmesini sağlar.

**Doküman:** QDMS Doküman veri tabanından doküman seçilebilmesini sağlar.

**Süreç:** QDMS Süreç veri tabanından süreç seçilebilmesini sağlar.

**Yönetim Sistemi:** QDMS Yönetim Sistemi veri tabanından yönetim sistemi bilgisi seçilebilmesini sağlar.

**Müşteri:** QDMS Müşteri veri tabanından müşteri bilgisi seçilebilmesini sağlar.

**Tedarikçi:** QDMS Tedarikçi veri tabanından tedarikçi bilgisi seçilebilmesini sağlar.

**Ürün Grubu:** QDMS Ürün Grubu veri tabanından ürün grubu bilgisinin seçilebilmesini sağlar.

**Ürün:** QDMS Ürün veri tabanından ürün bilgisinin seçilebilmesini sağlar.

**Şirket Profili:** QDMS Şirket Profili veri tabanından şirket profili bilgisi seçilebilmesini sağlar.

**Başlık:** Risk formuna ya da detay ekranına başlık ekler.

**Dosya:** Dosya ekler.

**Resim:** Resim ekler.

**Resim Liste:** Resim listesinden seçim sağlar.

**Çoklu Resim:** Çoklu resim seçilmesini sağlar.

**Tablo:** Tablo verilerinin kullanılmasını sağlar.

**Sorgu:** Sorgulama şeklinde seçim sağlar.

**Sorgu Ağaç:** Ağaç dallanması şeklinde sorgu yapılmasını sağlar.

### **6.1.9.E-Posta Ayarları**

**Menü Adı:** Sistem Altyapı Tanımları/Atık Yönetimi/E-Posta Ayarları

E-Posta ayarları ekranında, Atık Yönetim Modülü sürecinin hangi aşamasında kimlere mail gönderimi yapılacağı belirlenir. Bildirim ayarı yapılacak değerin üzerine gelinip ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd2310ebb-2a90-4760-8f4c-be147f48cf56) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6103434b-eff0-45ff-b9c0-5c3350fff2fb)

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcb3f2d1a-b379-4e29-9ce1-0179983e6005)Değiştir butonu ile değerin içine girdikten sonra, rollere göre uygun mesaj gövdesi seçilir ve E-posta gitsin mi check-box‘ ı işaretlenerek kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadac7cd9b1-e769-4632-b941-9b3ddecb212f)

### **6.1.10.Fonksiyon Dizayner**

**Menü Adı:** Sistem Altyapı Tanımları/Atık Yönetimi/ Fonksiyon Dizayner

Fonksiyon Dizayner özelliği ile alan havuzuna eklenen alanlar Atık Yönetim Modülünün istenilen sayfaları ile ilişkilendirilebilir. Bunun için Atık Yönetim Modülünün Sistem Altyapı Tanımları altından Fonksiyon Dizayner menüsüne gelinir. Açılan ekranda Atık Yönetim Modülünün alan eklenebilecek fonksiyonları sıralanacaktır. Bu fonksiyonlar Atık Talep Formu, Atık Formu, Atık Formu Alıcı, Atık Formu Üretici ve Atık Formu Taşıyıcı fonksiyonlarında kullanılacak alanlar ve bunların sıralaması ile onay işlemlerindeki hiyerarşi detayı tanımlanır.,

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload71189967-4c4f-480a-bd20-f1bac2b1c050)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload094c0e19-a83a-4f16-be1f-f4cc2a77db7e) Alanlar butonu ile formların detaylarında kullanılacak “Alanlar” belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddab4fb9b-9ea3-4449-a019-2968619f56e4)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload71b6f966-3431-4824-8265-afae6abad8a9):Yeni bir Fonksiyon tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec02cbd1-eacd-49cd-94fa-b6eed46112b6): Listede seçili Fonksiyon güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeaaef181-9a2b-409f-8479-31ff4976070f): Listede seçili Fonksiyon silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload74cebbdd-1d7e-42ff-9cce-9f51a435d156) : Önceki ekrana geri dönülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada5608ae2-ee2c-411d-ad38-afdbec7924da)Alanlar butonu ile açılan ekranda seçili fonksiyonda kullanılacak alanlar ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f57774d-d120-4475-8917-d6c73e233f15) yeni kayıt butonuna tıklanarak belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddfc7f405-6937-4e7b-83d5-d0cf19cf404c) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1da903c3-2f44-4017-8d37-0aa58b7bcec0)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Alan Adı:** Alan Tanımlama/Fonksiyonlar/Yeni kayıt ekranında Alan Adı Bilgisinin seçilebildiği alandır.

**Zorunlu Mu? :** Alan Tanımlama/Fonksiyonlar/Yeni kayıt ekranında seçilen Alanın Zorunlu Mu? bilgisinin Evet ya da Hayır seçeneklerinden seçilebildiği alandır. Seçilen Alanın zorunluğu sorgulatılıyor. Evet seçeneği seçildiğinde Alan zorunlu oluyor.

**Zorunluluk Mesajı:** Alan Tanımlama/Fonksiyonlar/Yeni kayıt ekranında Seçilen Alanın Zorunluluk Mesajı bilgisinin girildiği alandır. Zorunlu alanlar doldurulmadığında verilecek uyarı mesajı bilgisi yazılır.

**Sıra No:** Alan Tanımlama/Fonksiyonlar/Yeni kayıt ekranında Seçilen Alanın Sıra No bilgisinin girildiği alandır.

**Varsayılan Rol:** Alan Tanımlama/Fonksiyonlar/Yeni kayıt ekranında Seçilen Alanın Varsayılan Rol bilgisinin Onaycı Tanımları Listesinden seçilebildiği alandır. Alanların içeri rol ekranında daha önce tanımlanmış bir rol ile getirilecek varsayılan rol alanı doldurulur.

**Varsayılan Değer Değiştirilmesin:** Alan Tanımlama/Fonksiyonlar/Yeni kayıt ekranında Seçilen Alanın Varsayılan Değer Değiştirilmesin bilgisi aktif edilmek istenirse ilgili check box işaretlenir. Seçilen Alan varsayılan olarak bir değer getiriyorsa getirdiği değerin değiştirmemesini sağlar.

**Gridde göster:** Alan Tanımlama/Fonksiyonlar/Yeni kayıt ekranında Seçilen Alanın Gridde Gösterilmesi aktif edilmek istenirse ilgili check box işaretlenir

**Satır Sayısı:** Alan Tanımlama/Fonksiyonlar/Yeni kayıt ekranında Seçilen Alanın satır sayısının bilgisinin belirlendiği alandır.

**Kolon Genişliği:** Alan Tanımlama/Fonksiyonlar/Yeni kayıt ekranında Seçilen Alanın Kolon Genişliği bilgisinin belirlendiği alandır.

Gerekli tüm alanlar doldurulduktan sonra ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload39adaf14-ba6e-4e61-8c24-f05e96f57226) (kaydet) butonu tıklanarak, ilgili alan için ilgili Fonksiyon tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5fd7f3ea-eee6-41ea-a1e6-ecdbae6637c9)

### **6.1.11.Atık Yetki Matrisi**

**Menü Adı:** Sistem Altyapı Tanımları/Atık Yönetimi/ Atık Yetki Matrisi

Atık Yönetimi Modülünün kullanımı ile alakalı rol bazlı veya kullanıcı grubu bazlı yetkilendirmelerin yapıldığı menüdür. Rollere yetki vermek için ilgili check – box’lar işaretlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1ab2681b-df3b-473d-8042-6831142f9558)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload29b909af-0d63-4c92-a3f1-a299e3fb96fc):Kullanıcı grubu eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7fc4b47a-87bf-4c4f-900a-6815ca396b99):Kullanıcı grubu siler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload432afe92-b808-4c19-a909-2496c2e0ca87): Tüm Kullanıcı gruplarını siler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8c4d2169-457e-48f7-bba9-412c4e440de3):Kayıt işlemi yapar.

Grup eklemek için ise ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcac4bd6e-615a-4ccb-b5a3-4b4de7e32be9) (kullanıcı grubu ekle) butonuna tıklanarak sistemde tanımlı olan Kullanıcı Grubu seç Listesinde Kullanıcı grubu eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc7c78765-8d90-42ed-a561-50cf2be7002e)

Eklenen Kullanıcı grubuna yetkileri işaretlenerek verilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfc9fd407-ee4e-4fe1-9e58-b1e1c085f537) (kaydet) butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload02bcb132-22bc-48c7-b326-872ae46d42ca)

## **6.2.Entegre Yönetim Sistemi/Atık Yönetimi**

Tehlikeli Atık Formu, Tehlikesiz Atık Formu, Atık Talep Formu, Atık Yönetim Planı, Rapor Oluştur ve En Çoklar Analizi menülerin işlemlerinin gerçekleştirildiği kısımdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade395d3dd-1feb-476f-a275-811b4e663639)

### **6.2.1.Tehlikeli Atık Formu**

**Menü Adı:** Entegre Yönetim Sistemi/Atık Yönetimi/ Tehlikeli Atık Formu

Atık Yönetimi Modülünde Tehlikeli Atık Formu tanımlama işleminin gerçekleştiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4a359d7e-5855-43b0-920d-a5da5d8a1c27)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload71b6f966-3431-4824-8265-afae6abad8a9):Yeni bir Tehlikeli Atık Form tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec02cbd1-eacd-49cd-94fa-b6eed46112b6):Listede seçili Tehlikeli Atık Form bilgisi güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf094ebac-4d76-4e8f-bd8a-234ef7cef1f4):Listede seçili Tehlikeli Atık Form bilgisinin kayıt bakım modunda açar. Kayıt bakım ekranın açılması için Kullanıcının modül yönetici olması gerekir. Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/ Yönetici Tanımlama menüsünde Atık Yönetimin modülü için Modül Yöneticisi tanımlanması gerekir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada5a8c439-df5b-4dee-b6e6-1c77595159b3):Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6c002efd-fa17-409f-bc61-f587c99b049c): PDF formatında görüntüler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload70c1f4aa-5019-4f1c-8fb6-fcde88016211): Word olarak görüntüler.

Formlar ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7e9dcd24-2969-403f-9eaf-89a54c500b85) (yeni) butonu ile yeni Tehlikeli Atık Formu tanımlanmasına başlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload054c861b-e6ff-42bf-8202-09f8a52cee66)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Form Seri No:** Form sekmesinde Form Seri No bilgisinin girildiği alandır.

**Form Statü:** Form sekmesinde Form Statüsünün seçilebildiği alandır. Form Statüsü Üreticide, Taşıyıcıda, Alıcıda ve Tamamlandı seçeneklerinden oluşmaktadır.

**İş Yeri:** Form sekmesinde İş Yeri bilgisi sistemde tanımlı İş Yeri Listesinden seçilebildiği alandır.

Bu ekranda üç sekme bulunmaktadır. Form sekmesinde formun seri no’su ve o an ki statüsü ( Üreticide, Taşıyıcıda, Alıcıda) belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload436767ba-b500-4f6e-8716-c03af1b8d868)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Üretici Firma:** Üretici Firma sekmesinde Üretici Firma bilgisinin sistemde tanımlı Firma Listesinden seçilebildiği alandır.

**H Kodu:** Üretici Firma sekmesinde H Kodu bilgisinin sistemde tanımlı H Kodu Listesinden Seçilebildiği alandır.

**Atık Tanımı:** Üretici Firma sekmesinde Atık Tanımı bilgisinin Atık (Seçilen atığın kodu 6 haneli olmalıdır) Listesinden seçilebildiği alandır.

**Fiziksel Özellik:** Üretici Firma sekmesinde Atığın Fiziksel Özellik bilgisinin seçilebildiği alandır. Örneğin Katı, Toz/toz şeklinde, Çamurlu gibi.

**Renk:** Üretici Firma sekmesinde Atığın Renk bilgisinin seçilebildiği alandır.

**Ağırlık:** Üretici Firma sekmesinde Atığın Ağırlığın miktar ve birim olarak bilgisinin girildiği alandır.

**Ambalaj ve Konteyner Türü:** Üretici Firma sekmesinde Atığın Ambalaj ve Konteyner Türü bilgisinin seçilebildiği alandır.

**Ambalaj ve Konteyner Sayısı:** Üretici Firma sekmesinde Atığın Ambalaj ve Konteyner sayısı bilgisinin girildiği alandır.

**Atık Çıkış Tarihi:** Üretici Firma sekmesinde Atık Çıkış Tarihi bilgisinin girildiği alandır.

Açılan ekranda Üretici Firma bilgisi sistemde tanımlı Firma Listesinde, H kodu bilgisi sistemde tanımlı H Kodu Listesinden, Atık Tanımı bilgisi sistemde tanımlı Atık (Seçilen atığın kodu 6 haneli olmalıdır) Listesinden seçilir. Atığın Renk, Fiziksel Özellik, Ambalaj ve Konteyner bilgileri sistemde tanımlı seçeneklerden seçilir. Ambalaj ve Konteyner sayısı bilgisi girilir. Atık Çıkış Tarihi bilgisi belirlenir. Çıkan atığın üretici firma bilgileri girildikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0b383724-2383-4730-a639-cb69d3f86b32) (kaydet) butonu ile kaydedilir ve formlar ekranında aşağıdaki gibi görüntülenir

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload187897fd-93d5-48fc-b3a0-c06a4443278c)

Listeden de görülebileceği gibi atığın statüsü “Üreticide” olarak gözükmektedir, atık henüz taşıyıcıya verilmemiştir.

Atık, üreticiden çıkıp taşıyıcıya verildikten sonra aynı listeden ilgili çıkan atığın kaydı seçilip ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload339fdb85-34a1-47d6-951e-827f330a2fa4) (düzenle) butonu ile çıkan atığın kaydının Taşıyıcı bilgileri girilmeye başlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload428a3575-9ae6-4544-933a-9b9663de1956)

Atık formu tanımlama-kayıt güncelle ekranında form statü taşıyıcıda seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5d4dd271-42ec-451a-b593-7e106636cd74)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Taşıyıcı Firma:** Taşıyıcı sekmesinde Taşıyıcı Firma bilgisinin sistemde tanımlı Firma Listesinden seçilebildiği alandır.

**Lisans No:** Taşıyıcı sekmesinde Lisans No bilgisinin sistemde tanımlı Lisans Listesinden seçilebildiği alandır.

**Taşıt:** Taşıyıcı sekmesinde Taşıyıcı Taşıt plakasının sistemde tanımlı Plaka Listesinden seçilebildiği alandır.

**Taşıma Türü:** Taşıyıcı sekmesinde sistemde tanımlı olan Taşıyıcı Taşıma Türü listesinden Taşıyıcı Taşıma Türü bilgisinin seçilebildiği alandır. Örneğin: Karayolu, Deniz gibi.

**Teslim Tarihi:** Taşıyıcı sekmesinde Taşıyıcı Teslim Tarihi bilgisinin girildiği alandır.

**Taşıma Bedeli:** Taşıyıcı sekmesinde Taşıyıcı Taşıma Bedeli bilgisinin girildiği alandır.

**Alınan Ürün Ücreti:** Taşıyıcı sekmesinde Taşıyıcı Alınan Ürün Ücreti bilgisinin girildiği alandır.

Taşıyıcı firma kutucuğunda, altyapı kurgulaması sırasında oluşturulan ve taşıyıcı olarak belirlenen firmalardan birisi seçilir. Lisans no alanında ise, seçilen firmaya ait atık taşıma lisanslarından uygun olanı seçilir. Taşıt alanına taşıtın plakası girilir. Taşıma türü açılır menüsünde, sisteme önceden kaydedilmiş atık taşıma türlerinden birisi seçilir ve son olarak ise atığın alıcıya teslim edileceği tarih seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7f760b5c-3eba-4f59-b9f1-9d4edf1b0f0c)

Çıkan atığın taşıyıcı firma bilgileri yukarıdaki gibi girildikten sonra Alıcı sekmesi tıklanır ve bu kez alıcı firma bilgileri sisteme kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0e5d615-a243-43f4-abef-7d06ce66a9b2)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6eae1f03-14ab-4fdf-9743-5a080311285e)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Alıcı Firma:** Alıcı sekmesinde Alıcı Firma bilgisi sistemde tanımlı olan Firma Listesinden seçilebildiği alandır.

**Lisans No:** Alıcı sekmesinde Lisans No bilgisi sistemde tanımlı olan Lisans Listesinden seçilebildiği alandır.

**Ağırlık:** Alıcı sekmesinde Ağırlık bilgisinin girildiği alandır.

**Bertaraf/Geri Kazanım Yöntemi:** Alıcı sekmesinde Bertaraf/Geri Kazanım Yöntemi bilgisi sistemde tanımlı Bertaraf/Geri Kazanım Yöntemi Listesinden seçilebildiği alandır.

**Lisanslı Ara Depolama Tesisinden Atık Transferi:** Alıcı sekmesinde Lisanslı Ara Depolama Tesisinden Atık Transferi bilgisinin seçilebildiği alandır. İlgili seçenekler;

Arıtılmadan bertaraf/geri kazanım tesisine gönderilen atıklar seçeneği aktif edilecekse ilgili check box işaretlenir.

Arıtılarak bertaraf/geri kazanım tesisine gönderilen atıklar (başka atık üreterek) seçeneği aktif edilecekse ilgili check box işaretlenir.

Arıtılarak bertaraf/ geri kazanım tesisine gönderilen atıklar(başka atık üretmeden) seçeneği aktif edilecekse ilgili check box işaretlenir.

Diğer seçeneği aktif edilecekse ilgili check box işaretlenir.

**Kabul Tarihi:** Alıcı sekmesinde Kabul Tarihi bilgisinin girildiği alandır.

**Bertaraf Bedeli:** Alıcı sekmesinde Bertaraf Bedeli bilgisinin girildiği alandır.

**Toplam Bertaraf Bedeli:** Alıcı sekmesinde Toplam Bertaraf Bedeli sistem tarafından otomatik hesaplanır.

Bu ekrandaki alıcı firma alanında yine sistemin altyapı kurgulanırken kaydedilen ve alıcı olarak belirtilen firmalardan biri seçilir. Lisans no kısmında, alıcı firmanın uygun atık lisansları arasından seçim yapılır. Daha sonra ağırlık bilgisi girilir. Bir alttaki alanda ise sistemde mevcut bulunan bertaraf/ geri kazanım yöntemleri arasından seçim yapılır ya da bu alan daha sonra doldurulmak üzere boş bırakılabilir.

Bertaraf yöntemleri kutucuğunun altındaki alanda ise atık alıcıya ulaşmadan evvel arıtma işlemine tabi tutulmuşsa ya da tutulmamışsa bununla ilgili check box’lar işaretlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload89e25a2c-f9b6-45c9-9891-25f3d5985c94)

Atık alıcı tarafından bertaraf edildikten sonra yapılacak son işlem ise atık formunun içerisine girilerek formun statüsünün “Tamamlandı” olarak değiştirilmesi ve kaydedilmesidir. Bu aşamadan sonra çıkan atığın formunun son haliyle kaydedilmiş olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload928a55fd-df7c-461c-a75a-f43ed00a1b24)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2c6c3383-952c-492f-a1a0-3ace18355e34)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6c002efd-fa17-409f-bc61-f587c99b049c)Pdf görüntüle butonu tıklanarak Ulusal Tehlikeli Atık Taşıma Formu PDF formatında görüntüler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadba767d5d-fd43-4959-843d-42c650c82c83)![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd54333b1-0135-412f-813f-a28ad5803a52)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload70c1f4aa-5019-4f1c-8fb6-fcde88016211)Word görüntüle butonu tıklanarak Ulusal Tehlikeli Atık Taşıma Formu Word olarak görüntüler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload31983ec3-ed8f-4e87-9626-0e106cd04ea5)![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload426d6bbd-94f8-477b-a96d-3bec1610301f)

### **6.2.2.Tehlikesiz Atık Formu**

**Menü Adı:** Entegre Yönetim Sistemi/Atık Yönetimi/ Tehlikesiz Atık Formu

Atık Yönetimi Modülünde Tehlikesiz Atık Formu tanımlama işleminin gerçekleştiği menüdür.

Tehlikesiz atık formu tanımlama işleminin tehlikeli atık tanımlamadan tek farkı, taşıyıcı firma bilgisinin bu formda olmamasıdır. Sadece üretici ve alıcı firma bilgileri girilmesi yeterli olacaktır. Onun dışındaki bütün işlemler tehlikeli atık tanımlama süreciyle aynıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc5d6579e-4dda-49e8-9a6c-baf209a2271f)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload71b6f966-3431-4824-8265-afae6abad8a9):Yeni bir Tehlikesiz Atık Form tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec02cbd1-eacd-49cd-94fa-b6eed46112b6):Listede seçili Tehlikesiz Atık Form bilgisi güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada5a8c439-df5b-4dee-b6e6-1c77595159b3): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf094ebac-4d76-4e8f-bd8a-234ef7cef1f4):Listede seçili Tehlikeli Atık Form bilgisinin kayıt bakım modunda açar. Kayıt bakım ekranın açılması için Kullanıcının modül yönetici olması gerekir. Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/ Yönetici Tanımlama menüsünde Atık Yönetimin modülü için Modül Yöneticisi tanımlanması gerekir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6c002efd-fa17-409f-bc61-f587c99b049c): PDF formatında görüntüler.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload70c1f4aa-5019-4f1c-8fb6-fcde88016211):Word olarak görüntüler.

Formlar ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7e9dcd24-2969-403f-9eaf-89a54c500b85) (yeni) butonu ile yeni Tehlikesiz Atık Formu tanımlanmasına başlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9969776b-191c-4bbf-a429-59296f827287)

Eğer taşıyıcı sekmesinin gelmesi isteniyorsa atık yönetimi parametrelerinden 4 numaralı parametre değerinin aktif olması gerekmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload123a41ad-28a5-4d7c-abcb-b5c73bcc8f5e)

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec02cbd1-eacd-49cd-94fa-b6eed46112b6)Değiştir butonu tıklanarak parametre değeri aktif edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf68ca904-37b3-4f21-9ae2-e5c3ca02496c)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3378684a-4de7-4b41-8f16-1f9b682f2d2e)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload72641058-e255-4b72-a373-2d0c9c56cca3)

Tehlikesiz atık formu, üretici ve alıcı bilgileri kaydedildikten sonra yine Formlar ekranına düşer ve sağ üstteki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb02d787b-6b0b-4b72-8181-c175e8d17ff6)(PDF görüntüle) ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbab5086b-9de4-4761-8969-e38930a1425a) (Word görüntüle) butonlar çıkan atığın formu bilgisayara kaydedilip görüntülenebilir.

### **6.2.3.Atık Talep Formu**

**Menü Adı:** Entegre Yönetim Sistemi/Atık Yönetimi/Atık Talep Formu

Atık girişi ekranlarında atık kaydı oluşturulması bir onaya bağlı ise atık talep formu kullanılır. Talep edilen atık girişi bir onaycıya onaya gider. Onaylanan atık bilgisi tehlikeli atık formu ve tehlikesiz atık formu ekranlarında kullanılmak üzere açılır. Atık talebi oluşturmak için sistemde Modül yöneticisi olmak gerekmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9c3d9a98-ccea-4cbc-b661-1fc7f8f29fea)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload71b6f966-3431-4824-8265-afae6abad8a9): Yeni bir Atık Talep Formu tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada5a8c439-df5b-4dee-b6e6-1c77595159b3): Kayıtlar filtrelenerek arama yapılabilir.

Yeni bir atık talebi oluşturmak için ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3d82e5e2-9c62-40de-9546-38b9354592e0) (yeni) butonuna tıklanır. Açılan ekranda atığın tehlikeli olup olmadığı işaretlenir, miktarı girilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1cf79dbc-4226-4170-bffd-301ea0894ea3)Kaydedilen alan atık talebi ekranına taslak olarak düşmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbe5e3c11-fb9b-4ccf-85c6-196a8e1b50d8)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload71b6f966-3431-4824-8265-afae6abad8a9): Yeni bir atık talep formu eklenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec02cbd1-eacd-49cd-94fa-b6eed46112b6): Listede seçili atık talep formu bilgisi günceller.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeaaef181-9a2b-409f-8479-31ff4976070f): Listede seçili Atık Talep Formu bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7ef92a77-69b7-4cd8-9254-f2e413808927): Atık Talep Formu onaya gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada5a8c439-df5b-4dee-b6e6-1c77595159b3): Kayıtlar filtrelenerek arama yapılabilir.

Sistem Altyapı Tanımları/Bsat/Konfigürasyon Ayarları/Rol Tanımlama menüsünde tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3e0d93b9-99a9-46bc-83d6-77b41e8854c0)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1920fdc3-d690-40c0-b25f-9e2b4ff4d68f)(Değiştir) butonu tıklanarak Rol içeriği görüntülenir. Rol tanımlı Atık Talep Onaycısına onaya gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4c1bed49-6b8a-4d0b-87d7-fff73c819403)

Onaya göndermek için ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4aea8c6b-08fc-4a3f-866c-3026212110de) (gönder) butonuna tıklanır ve atık talebi onaya gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload594b73c2-5053-466f-973f-87f3f81a9c43)

Onaycının bekleyen işlerim menüsünde **“Onaylanması Gereken Atık Talepleri”** olarak görev düşmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfc77e586-9fd2-41bb-a9b9-dfe2593b6283)

Talep kodu tıklanarak onaylama veya reddetme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7b24598f-954c-42ca-bf48-361b0ed77f66)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload83aa9e32-ed67-4412-8829-78bcffa33ad9): Önceki ekrana dönülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7651f79e-cd7d-41d6-88c2-b83bd329a7b4): Atık Talep Formu kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9bb8fce9-f3ec-484d-bdf0-3dd2d29051cc): Atık Talep Formu onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1bf49e1b-af19-4a22-947a-f50b9a50a1cb): Atık Talep Formu reddedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1bf49e1b-af19-4a22-947a-f50b9a50a1cb)(Reddet) butonu tıklanırsa ret nedeni yazılarak Atık Talep formu reddedilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd65a289f-bcc3-4ea6-831c-6124ddb10227)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9bb8fce9-f3ec-484d-bdf0-3dd2d29051cc)(Onayla) butonu tıklanarak Atık Talep formu onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4db8043b-1ad6-4614-a035-1b4f6109002b)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb23f30a9-09e5-4bb3-af91-a31c44652a8d)

Atık talep formu ekranındayken onaylanan formlar için ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadea4f4f01-ad40-40dd-ba67-be3d3bcb2b5c) (doldur) butonu ile tehlikeli/ tehlikesiz atık formu oluşturulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d9259af-d328-4105-bb8d-917e53c6184f)

### **6.2.4.Atık Yönetim Planı**

**Menü Adı:** Entegre Yönetim Sistemi/Atık Yönetimi/ Atık Yönetim Planı

Her üretici firmanın üç yılda bir hazırlamakla yükümlü olduğu endüstriyel atık yönetim planları, Atık Yönetim Modülündeki Atık Yönetim Planı menüsünden oluşturularak takibi yapılmaktadır.

### **6.2. 4.1.Plan Oluştur**

Entegre Yönetim Sistemi/Atık Yönetimi/ Atık Yönetim Planı/ Plan Oluştur

Atık Yönetim Planı oluşturmak için Entegre Yönetim Sistemi/ Atık Yönetimi/ Atık Yönetim Planı altındaki Plan Oluştur seçeneği seçilerek Atık Yönetimi Planları ekranına gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload98c75b58-4a51-45e7-a049-5dae764e6186)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload71b6f966-3431-4824-8265-afae6abad8a9): Yeni Atık Yönetim Planı eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload11f6268f-d3e0-46e5-968c-b532422e9491): Listede seçili Atık Yönetim Planı bilgisi görüntülenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeaaef181-9a2b-409f-8479-31ff4976070f): Listede seçili Atık Yönetim Planı bilgisi silinebilir.

Yeni Atık Yönetim Planı Tanımlama ekranına yeni bir Yeni Atık Yönetim Planı eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f57774d-d120-4475-8917-d6c73e233f15)(yeni) butonu tıklanarak Yeni Atık Yönetim Planı Tanımlama /Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc327e8ea-ae97-4a1e-9980-1bbb4e881c18)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Yıl:** Atık Yönetim Planı Hazırlama ekranında atık planın kapsadığı yıl bilgisinin girildiği alandır.

**Üretici Firma:** Atık Yönetim Planı Hazırlama ekranında Üretici Firma bilgisinin sistemde tanımlı Firma listesinden seçilebildiği alandır.

**Sorumlu Kişinin Adı ve Soyadı:** Atık Yönetim Planı Hazırlama ekranında Sorumlu Kişinin Adı ve Soyadı bilgisinin sistemde tanımlı Personel listesinden seçilebildiği alandır.

**Atık Azaltımına Yönelik Yapılacak İşlemler:** Atık Yönetim Planı Hazırlama ekranında Atık azaltımına yönelik yapılacak işlemler bilgisinin girildiği alandır.

**Durum:** Durum bilgisinin Aktif veya Pasif seçilebildiği alandır.

Açılan ekranda Üretici sekmesinde; sırasıyla atık planının kapsadığı yıl, üretici firma, sorumlu kişi, atık azaltılmasına yönelik yapılacak işlemler gibi bilgiler girilir.

Kaynaklar sekmesine gelindiğinde ise burada QDMS’in Çevresel Boyutlar ve Etkileri Modülünün içerisinde bulunan Faaliyet Grupları ve Faaliyetlerden uygun olanlar seçilerek Kaynaklar listesine eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6a9d5fb1-8796-4694-92ce-a8a8d9a82dff)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload71b6f966-3431-4824-8265-afae6abad8a9):Yeni bir Kaynaklar eklenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec02cbd1-eacd-49cd-94fa-b6eed46112b6):Listede seçili Kaynaklar bilgisi ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeaaef181-9a2b-409f-8479-31ff4976070f):Listede seçili Kaynaklar bilgisi silinebilir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload71b6f966-3431-4824-8265-afae6abad8a9)Yeni butonu ile yeni Kaynak ekleme ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload95945daa-4d35-4b0d-b9cf-f4e902a0d863)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Faaliyet Alanı:** Kaynaklar sekmesinde Faaliyet Alanı bilgisi sistemde tanımlı olan Departman Listesinden seçilebildiği alandır.

**Faaliyet:** Kaynaklar sekmesinde Faaliyet bilgisi sistemde tanımlı olan Faaliyet Listesinden seçilebildiği alandır.

**Oluşan Atıklar:** Kaynaklar sekmesinde Oluşan Atıklar bilgisinin girildiği alandır.

**Atık Türü:** Kaynaklar sekmesinde Atık Türü bilgisi sistemde tanımlı olan Atık (Seçilen atığın kodu 6 haneli olmalıdır) Listesinden seçilebildiği alandır.

**Kaynak Durumu:** Kaynaklar sekmesinde durumun Aktif veya Pasif seçilebildiği alandır.

**Atık Toplama Alanı:** Kaynaklar sekmesinde Atık Toplam Alanı bilgisinin girildiği alandır.

Bu ekrandaki faaliyet alanı kısmından üretici firma içerisindeki bir departman, faaliyet kısmından Çevresel Boyutlar ve Etkileri modülünde tanımlanan faaliyetlerden uygun olanı seçilir. Oluşan atıklar kutucuğuna ise o faaliyet sonucu oluşan atıklar yazılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadae3c6563-550f-49f6-b0b5-2c0d16063d3f) (kaydet) butonu ile girilen bilgiler kaydedilir ve kaynaklar listesine bir giriş yapılmış olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf391333d-961a-499a-af42-9985d287fbbb)

Kaynaklar listesine de kayıt girildikten sonra en sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadae3c6563-550f-49f6-b0b5-2c0d16063d3f) (Kaydet) butonuna basılarak bir atık yönetim planı oluşturulmuş olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc88421e-bf74-4cee-8c0f-c8469cee41ec)

Atık yönetim planları ekranında tüm planlar listelenir. Herhangi bir planın detaylı raporuna erişmek için ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload237dfcd9-6407-4fb1-a1a9-7c1c03e06e29) (Görüntüle) butonu vasıtasıyla rapor alma ekranına yönelebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7c5e880e-816f-40b9-83bc-7030545f9a01)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload839258d8-d1bf-405e-96c4-8fea5b257bcd):Yönetim Planı oluşturulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload07330c7b-141e-46dd-95f9-729679675285):Dosya yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb7127b7d-a4d0-49d7-b608-27fbb9d8043f):Atık Plan bilgileri ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade96a3884-6846-4007-96d7-0e93012df0d8):Önceki ekrana geri dönülür.

Bu ekrandaki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade5c4dc2b-2a88-499f-a8f2-e44c86f1ea77)(Yönetim planı oluştur) butonu ile sistem tarafından otomatik olarak atık yönetim planı hazırlanır ve indirme linki ekrana gelir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd7ccbbab-b02d-4dda-9c0c-9f359b332a40)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadda0c47d5-5cf3-451b-b4f4-5770699523e1)

İndirme linki tıklanarak Atık Yönetim Planı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5eb72907-8618-4a18-8c81-831561eb9610)

Aynı ekrandaki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd3e8e4e8-c565-4d6a-b52c-b34d4ba79aae) (dosya yükle) butonu ile istenirse QDMS’in ürettiği Atık Yönetim Planı formatı yerine, firmanın kendi hazırlamış olduğu plan varsa seçilip yüklenebilir. Sistemin ürettiği format yerine geçecektir. Ve son olarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7f7c12f2-d29b-4458-8f0c-3ba13eb477a3) (düzenle) butonu ile de mevcut atık planı bilgileri düzenlenebilir, bilgileri üzerinde değişiklikler yapılabilir.

### **6.2.4.2.Faaliyet Grubu Tanımlama**

**Menü Adı:** Entegre Yönetim Sistemi/Atık Yönetimi/Atık Yönetim Planı/ Faaliyet Grubu Tanımlama

Atık Yönetimi Planı oluşturulurken kaynak ekleme ekranında ihtiyaç duyulan ve esasında Çevresel Boyutlar ve Etkileri Modülünün altında bulunan Faaliyetler ve Faaliyet Grupları; kısa yol olarak Atık Yönetimi Modülünden de tanımlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8edf1d1d-1e55-4fd7-b764-b158f915eb80)

**Açılan ekrandaki butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddfc4479c-2aa8-410c-bd6a-13d4a49a6667): Yeni Faaliyet Grubu tanımlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadac1ad31d-8e04-48f8-ba1f-061a21543138): Listede seçili Faaliyet Grubu bilgisi ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeaaef181-9a2b-409f-8479-31ff4976070f): Listede seçili Faaliyet Grubu bilgisini silmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3e34e7e5-054f-4a88-b682-4fe71680eaef): Veriler Excel’e aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload237b38d8-0288-4c7a-9a4c-2ef29c41008b): Şablon yüklemek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload373e6727-987b-4a12-8fbe-9ee841a60eef): Şablon oluşturmak için kullanılır.

Faaliyet Grubu Tanımlama ekranına yeni bir Faaliyet Grubu eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f57774d-d120-4475-8917-d6c73e233f15)(yeni) butonu tıklanarak Faaliyet Grubu Tanımlama \\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload375f7ead-d418-4a39-aa47-2cd07c241333) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd9b4b8fe-4a37-4dfe-85b6-1a90e9f5043c)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Bağlı Olduğu Faaliyet Grubu:** Faaliyet Grubu Tanımlama ekranında Bağlı Olduğu Faaliyet Grubu bilgisinin seçilebildiği alandır.

**Faaliyet Grubu Kodu:** Faaliyet Grubu Tanımlama ekranında Faaliyet Grubu Kodu bilgisinin girildiği alandır.

**Faaliyet Grubu Tanımı:** Faaliyet Grubu Tanımlama ekranında Faaliyet Grubu Tanımı bilgisinin girildiği alandır.

**Sorumlu Kullanıcı Grupları:** Faaliyet Grubu Tanımlama ekranında Sorumlu Kullanıcı Gruplarının sistemde tanımlı Kullanıcı Grubu Listesinden bilgisinin seçilebildiği alandır.

**Sorumlu Personel:** Faaliyet Grubu Tanımlama ekranında Sorumlu Personel bilgisinin sistemde tanımlı olan Personel Listesinden seçilebildiği alandır.

**Otomatik Kod Şablonu**: Faaliyet Grubu Tanımlama ekranında Otomatik Kod Şablonu bilgisinin verildiği alandır.

**Otomatik Kod Sayacı:** Faaliyet Grubu Tanımlama ekranında Otomatik Kod Sayacı kaçtan başladığının bilgisinin verildiği alandır.

**Durum:** Faaliyet Grubu Tanımlama ekranında Faaliyet Grubu Aktif veya Pasif Durumun seçilebildiği alandır.

**Risk var mı yok mu?:** Faaliyet Grubu Tanımlama ekranında Risk olup olmadığı bilgisinin Evet veya Hayır seçeneklerden bilgisinin seçildiği alandır.

**Tehlike Kaynağı:** Faaliyet Grubu Tanımlama ekranında Tehlike kaynağı bilgisinin girildiği alandır.

Bu sayfada (varsa) faaliyet grubunun bağlı olduğu faaliyet grubu, faaliyet grubu kodu ve tanımı bilgileri girilir. Risk olup olmadığı bilgisi ilgili seçeneklerden seçilir.Eğer sadece belirli kullanıcı gruplarının bu faaliyetlerle işlem yapması isteniyorsa sorumlu kullanıcı grupları kısmından kullanıcı grupları seçilip eklenir. Aktif/ pasif durumu belirlenerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaf8f424d-78be-4724-a60e-ced6acc01bb3) (kaydet) butonu tıklanarak faaliyet grubu tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9e9262e4-e18e-4c75-8fb5-850d529bf6b3)

### **6.2.4.3.Faaliyet Tanımlama**

**Menü Adı:** Entegre Yönetim Sistemi/Atık Yönetimi/Atık Yönetim Planı/ Faaliyet Tanımlama

Atık Yönetim Modülünde Atık Yönetim Planında faaliyet tanımlama işleminin gerçekleştiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload65696ab8-314e-4b1f-8e28-b269aec33899)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddfc4479c-2aa8-410c-bd6a-13d4a49a6667): Yeni Faaliyet tanımlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadac1ad31d-8e04-48f8-ba1f-061a21543138): Listede seçili Faaliyet bilgisi ile ilgili herhangi bir düzeltme, değişiklik veya güncelleme yapılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeaaef181-9a2b-409f-8479-31ff4976070f):Listede seçili Faaliyet bilgisini silmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload213e729c-2dfd-465f-bc45-edd2be16fd47):Listede seçili Faaliyet kopyalanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3e34e7e5-054f-4a88-b682-4fe71680eaef):Veriler Excel’e aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload237b38d8-0288-4c7a-9a4c-2ef29c41008b): Şablon yüklemek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload373e6727-987b-4a12-8fbe-9ee841a60eef): Şablon oluşturmak için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3bb126fb-a2a5-4678-aec2-d38ac3a1b572):Önceki ekrana geri dönülür.

Faaliyet Tanımlama ekranına yeni bir Faaliyet eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f57774d-d120-4475-8917-d6c73e233f15)(yeni) butonu tıklanarak Faaliyet Tanımlama \\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade612ea06-9a5b-4350-a426-197a80e76634)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Faaliyet Grubu:** Faaliyet Tanımlama ekranında Faaliyet Grubu bilgisinin seçebildiği alandır.

**Faaliyet Kodu:** Faaliyet Tanımlama ekranında Faaliyet Kodu bilgisinin sistem tarafından otomatik olarak verildiği alandır.

**Faaliyet Tanımı:** Faaliyet Tanımlama ekranında Faaliyet Tanımı bilgisinin girildiği alandır.

**Sorumlu Kullanıcı Grupları:** Faaliyet Tanımlama ekranında Sorumlu Kullanıcı Gruplarının bilgisinin sistemde tanımlı Kullanıcı Grupları Listesinden seçilebildiği alandır.

**Sorumlu Personel:** Faaliyet Tanımlama ekranında Sorumlu Personel bilgisinin sistemde tanımlı Personel Listesinde seçilebildiği alandır.

**Durum:** Faaliyet Tanımlama ekranında Faaliyet Tanımı Aktif veya Pasif durumun bilgisinin seçilebildiği alandır.

**Risk var mı yok mu?:** Faaliyet Tanımlama ekranında Risk olup olmadığı bilgisinin Evet veya Hayır seçeneklerden bilgisinin seçildiği alandır.

Açılan ekranda sırasıyla faaliyet grubunu, faaliyet kodunu eğer parametreden otomatik kod verme aktif edilmemişse kod bilgisi, faaliyet tanımını ve yine eğer sorumlu kullanıcı grupları kullanılacaksa bu alan doldurulduktan sonra, Riskin olup olmadığı ilgili seçeneklerden seçilir durum bilgisi seçilip ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4f9c3436-f942-4034-a673-79ed620aac72) (kaydet) butonu tıklanarak Faaliyet tanımı kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5cdc326b-1a63-4e81-b327-a05651a4de91)

### **6.2.5.Rapor Oluşturma**

**Menü Adı:** Entegre Yönetim Sistemi/Atık Yönetimi/ Rapor Oluşturma

Sistemde yer alan tüm atık formlarının yer aldığı toplu bir rapor alınmasını sağlayan menüdür. Açılan ekranda, sistemdeki tüm Tehlikeli ve Tehlikesiz Atık formları görüntülenebilir. Arama sekmesine gelinirse, sistemden alınacak raporda görüntülenecek sütunlar seçilebilir. Ayrıca istenirse tüm Tehlikeli ve Tehlikesiz Atık Formları değil de ekranda yer alan kriterler bazında filtreleme yapılarak bu şekilde bir rapor alınması da sağlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cc632f9-1f7d-497f-8b6f-bb9801ee199a)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada5a8c439-df5b-4dee-b6e6-1c77595159b3): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4607bdda-010e-4174-89c1-f44f6c699c1d): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f5e529c-0023-4044-b53c-729b1bcffb58) Excel’e aktar butonu ile Excel formatında raporu görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbab4e049-ef9d-433d-9074-69ed5ffdeba2)

### **6.2.6.En Çoklar Analizi**

**Menü Adı:** Entegre Yönetim Sistemi/Atık Yönetimi/En Çoklar Analizi

En Çoklar Analizi grafiğini almak için, Grafikler menüsünden En Çoklar Analizi sekmesi tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec005dd6-d33b-4db8-b781-af91bd205fae)

En Çoklar Analizi ekranında, Grafik Seçenekleri bölümünde gerekli seçimler gerçekleştirilir. Grafikte olması istenen en çok aralık belirlenir. Grafik Seçeneklerinden X ekseninde yer alması istenen nitelik seçilir. Ana tema, renk paleti özelliklerinden grafik özelleştirilebilir. Grafik başlığı belirtilerek grafik oluşturmak için ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc5b07bf-ae4d-42a5-9a6f-26391c563a30) (grafik çiz) butonuna tıklanır. Atık çıkış tarihe göre filtreleme yapılabilir en çoklar analizi grafikte yer alması sağlanabilir.

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc5b07bf-ae4d-42a5-9a6f-26391c563a30): Belirlenen özelliklere göre ekrana grafiği çizdirir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d4978fc-0415-4547-8ad2-68619fbc3014): İstenen grafiği açılır menüden seçilen format türüne ( excel, jpg, pdf, vb, ) dönüştürerek dış ortama aktarır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload67c05bbf-e7c4-4514-b4dd-d447bc55d5bd): Grafik verileri, Excel listesi biçiminde aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc5b07bf-ae4d-42a5-9a6f-26391c563a30) Grafik çiz butonu tıklanarak Grafik seçeneklerinde belirlenen özelliklere göre grafik çizdirir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload27703001-765d-4634-beb0-378a308238dc) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0381b164-5a6c-432d-8bfe-07a63b470738)

### **6.2.7.İşyeri Bazlı Atık Raporu**

**Menü Adı:** Entegre Yönetim Sistemi/Atık Yönetimi/İş Yeri Bazlı Atık Raporu

İş yeri bazlı Atık raporlarının alındığı menüdür.İş yerlerine sistemde tanımlanan Tehlikeli Atık ve Tehlikesiz Atık raporların alınması amacıyla kullanılmaktadır. İşyeri Bazlı Atık Raporu ekranında Rapor Başlığı alanında raporun adı bilgisi yazılarak Form tipi alanın ilgili Form tipi seçeneklerinden seçim yapılarak işyeri bazlı raporun alınacağı işyeri seçim sistemde tanımlı işyerinden seçim yapılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload67c05bbf-e7c4-4514-b4dd-d447bc55d5bd)(Excel Aktar) butonu tıklanarak istenilen arama kriterilerine göre filtreleme yapılarak Excel formatında rapor alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddd57af35-9874-4bee-a6fd-4bd478d55b03)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Ropor Başlığı:**İşyeri Bazlı Atık Raporu ekranında İşyeri Bazlı Atık raporunun başlık bilgisinin girildiği alandır.

**Form Tipi :** İşyeri Bazlı Atık Raporu ekranında alınacak İşyeri Bazlı Atık Raporun Form tipi seçenekleri olan Tehlikeli Atık ve Tehlikesiz Atık bilgisi seçeneklerinde seçim yapıldığı alan olan filtre arama kriteridir.

**Atık Tanımı:** İşyeri Bazlı Atık Raporu ekranında alınacak İşyeri Bazlı Atık Raporun Atık Tanımı bilgisinin sistemde tanımlı Atık listesinde seçim yapıldığı alan olan filtre arama kriteridir. Hangi Atıkla ilgili rapor alınacak seçimi yapılır.

**İş Yeri:** İşyeri Bazlı Atık Raporu ekranında alınacak İşyeri Bazlı Atık Raporun hangi işyeri için alınacağının sistemde tanımlı işyeri listesinde seçim yapıldığı alan olan filtre arama kriteridir.

**Atık Çıkş Tarihi:** İşyeri Bazlı Atık Raporu ekranında alınacak İşyeri Bazlı Atık Raporun Atık çıkış tarihi bilgisinin Takvim alanında seçim yapıldığı alan olan arama kriteridir.

**Form Tipi Tehlikeli Atık Tipi için İşyeri Bazlı Atık Raporun Excel Formatında alınması;**

İşyeri Bazlı Atık Raporu ekranında Rapor başlığı bilgisi yazılır, Form tipi ilgili seçeneklerde Tehlikeli Atık form tipi seçeneği seçilir, hangi işyeri için rapor alınacak işyeri listesinde seçim yapılır, istenirse Atık Tanım bilgisi seçim yapılır ve Atık çıkış tarihi bilgisi belirlenerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload67c05bbf-e7c4-4514-b4dd-d447bc55d5bd)( Excel Aktar) butonu tıklanarak Excel formatında işyeri bazlı Atık rapor alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3bc220c4-1327-41b5-a462-a77ed324d34f)

İş Yeri alanında raporun alınacağı İş yeri listesinde İşyeri seçimi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload91b8cf98-c3a7-4e6d-a7c3-fe973c8ac6fd)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2960bcb6-9c71-4dbd-ade0-06da5d44d3b5)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload67c05bbf-e7c4-4514-b4dd-d447bc55d5bd)(Excel Aktar) butonu tıklanarak Form tipi Tehlikeli Atık seçeneği için “İşyeri Bazlı Atık Raporu” Excel formatında alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload44900dc7-05f2-44dd-a4cb-7d84d04cec6a)

**Form Tipi Tehlikesiz Atık Tipi için İşyeri Bazlı Atık Raporun Excel Formatında alınması;**

İşyeri Bazlı Atık Raporu ekranında Rapor başlığı bilgisi yazılır, Form tipi ilgili seçeneklerde Tehlikesiz Atık form tipi seçeneği seçilir, hangi işyeri için rapor alınacak işyeri listesinde seçim yapılır, istenirse Atık Tanım bilgisi seçim yapılır ve Atık çıkış tarihi bilgisi belirlenerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload67c05bbf-e7c4-4514-b4dd-d447bc55d5bd)( Excel Aktar) butonu tıklanarak Excel formatında İşyeri Bazlı Atık Rapor alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload72992c5d-b2d3-4a26-aa62-2cc266800496)

İş Yeri alanında raporun alınacağı İş yeri listesinde İşyeri seçimi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload28f0ff44-0aa9-4b94-9828-72b9660f4a7c)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb059ac29-8bbe-4096-a185-b90bb8e2cc62)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload67c05bbf-e7c4-4514-b4dd-d447bc55d5bd)(Excel Aktar) butonu tıklanarak Form tipi Tehlikesiz Atık seçeneği için “İşyeri Bazlı Atık Raporu” Excel formatında alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload209c97b6-bbad-403b-9594-6b26c18ef140)
