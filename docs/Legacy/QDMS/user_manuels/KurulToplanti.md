---
title: Kurul Toplantı
description: Kurul Toplantı Yardım Dokümanı
sidebar_position: 49
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::

**Kurul Toplantı Modülü(v.5.24) Kullanıcı Yardım Dokümanı**

Modül Versiyonu: 5.24



**1.GİRİŞ: “QDMS Kurul Toplantı Modülü”**, Firma bünyesinde gerçekleştirilen İSG Kurul

Toplantıları, Toplantılar gibi faaliyetlerin planlama aşamasından bitiş aşamasına kadar bütün süreçlerini içinde barındıran ve takip edilmesini sağlayan Modüldür.

**2.AMAÇ:** Bu yardım kılavuzunun amacı; QDMS “Kurul Toplantı” Modülünün çalışma sürecini anlatmaktır. Kurul Toplantı faaliyetlerinin, sistem üzerinden yönetimi için bu Modül kullanılır.

**3.KISALTMALAR:**

QDMS: Kalite Dokümanları Yönetim Sistemi “ Quality Document Management System”

# **4.KURUL TOPLANTI MODÜLÜ**

Kurul Toplantı Modülü ile planlanan toplantıların duyuruları, toplantıların gerçekleştirilmesi, toplantılar sonucu planlanan aksiyonların atamaları ve takibi yapılır. Bir toplantıdan sonra alınan kararlar sisteme girilerek bu kararlar ile ilgili olarak görevlendirmeler gerçekleştirilebilir.

## **4.1.Sistem Altyapı Tanımları/Kurul Toplantı**

Kurul Toplantı Modülünün altyapısının oluşturularak tanımlamaların yapıldığı kısımdır. Toplantı Kaynağı Tanımlama, Alan Tanımlama ve Fonksiyon Dizayner gibi altyapı tanımlamalarının yapıldığı menülerdir. Bu menülerde Toplantı Kaynağı Tanımlama Modülü kullanmak için zorunludur. Alan tanımlama ve Fonksiyon Dizayner, ise ekstra alan gereksinimi olduğunda kullanılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload83653e0f-d71b-4635-ade3-b5add8631656)



### **4.1.1.Toplantı Kaynağı Tanımlama**

**Menü adı:** Sistem Altyapı Tanımları/Kurul Toplantı/Toplantı Kaynağı Tanımlama

Toplantı Kaynağı tanımlama işleminin yapıldığı menüdür. Toplantı kaynakları, Entegre Yönetim Sistemi menüsü altında yeni bir toplantı planlanmak istendiğinde şablon olarak toplantı bilgilerinin kullanıcının karşısına çıkmasını sağlar ve aynı zamanda toplantıların başlıklar altında toplanmasına imkan verir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload929b41ab-aaad-46a5-98ef-1df23e8033ad)

Toplantı kaynağı ağaç şeklindedir ve istenildiği kadar alt kırılım yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00ac41fe-7c58-4943-a81a-509afd8662ef)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd82b7eff-77ab-483d-a8fc-a4decac92f9c): Yeni bir Toplantı Kaynağı tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc96be829-2922-4058-9c53-93d7d61eee38): Listede seçili Toplantı Kaynağı bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload596c4955-1fc1-4111-8adb-481a885c8d44): Listede seçili Toplantı Kaynağı bilgisi silinebilir.

Toplantı Kaynağı ekranına yeni bir Toplantı Kaynağı eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8956733b-851f-4b30-b15c-b55cb0eedfc7)(Yeni) butonu tıklanarak Toplantı Şablonu Tanımlama ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload38afec5e-fbaf-4aa5-a03b-847be9bb9a37)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Üst İşlem Kaynağı:** Üst işlem kaynağı bilgisinin daha önceden sisteme tanımlanan Toplantı Kaynaklarından seçilebildiği alandır. Toplantı kaynaklarının kırılımlı yapıya sahip olması gerekiyorsa bu alanda üst kırılım seçimi gerçekleştirilmelidir.

**Kod:** Toplantı kaynağının kodunun girildiği alandır.

**Kod Şablonu:** Toplantı kaynağının kod şablonu bilgisinin girildiği alandır. Toplantı planlama ekranında toplantı kaynağına göre tanımlanan toplantının otomatik kod sayacı bilgisi girilir.

**Sayaç:** Toplantı kaynağının sayaç bilgisinin girildiği alandır. Kod sayacının hangi sayıdan başlaması gerekiyorsa bu sayı belirlenerek bu alana yazılır.

**Tanım:** Toplantı kaynağının adı bilgisi girilir.

**Tanım Şablon:** Toplantı planlama ekranında girilen toplantı tanımının nasıl gözükmesi isteniliyorsa ilgili kısa kodu bilgisi girilir.

**Periyodiklik:** Toplantı kaynağının periyodik olup olmaması belirlenir. Tanımlanan toplantı kaynağı periyodik ise “Evet” seçeneği seçilir.

**Periyot:** Toplantı kaynağı periyodik seçeneği seçilerek periyodu tanımlanır ve periyod birimi (gün, ay) seçeneklerinden seçilir.

**Yayınlanacak Format:** Bu toplantı kaynağı seçilerek gerçekleştirilen toplantıları Excel’e aktarmak gerektiğinde kullanılacak Excel şablonunun sisteme tanıtıldığı alandır.  Bu alanda “Şablon Yükle” butonu ile kullanılacak Toplantı Tutanağı Formatı sisteme yüklenir.

**Gelecek Toplantı Tarihi:** Gerçekleşmesi planlanan gelecek toplantı tarihi ve saati seçilir.

**Ön Bildirim:** Toplantı ön bildiriminin katılımcılara kaç gün önceden yapılacağı bilgisi girilir.

**Katılım Onay Süresi:** Toplantı katılımcılarının kaç gün içinde katılım onayını sistemden vermeleri gerektiği belirlenir.

**DÖF İşlem Kaynağı:** Toplantı kararları doğrultusunda açılabilecek  DÖF’lerin işlem kaynağı sistemde tanımlı olan DÖF işlem kaynakları arasından seçilir.

**Kaynak Kodu:** Toplantı kararları doğrultusunda planlanabilecek aksiyonların aksiyon kaynağı sistemde tanımlı olan aksiyon kaynakları arasından seçilir.

**Kimler Görebilsin:** Toplantı kararları doğrultusunda aksiyonların aksiyon modülünde belirlendiği üzere herkes tarafından mı yoksa sadece belirtilen kişiler tarafından mı görüleceği belirlenir.

Katılımcılar sekmesinde; toplantıya katılması planlanan personeller ve yetkileri seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb25bccf7-2d85-4ac1-8491-c0e8b50420eb)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd82b7eff-77ab-483d-a8fc-a4decac92f9c): Yeni bir Katılımcı eklenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc96be829-2922-4058-9c53-93d7d61eee38): Listede seçili Katılımcı bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload596c4955-1fc1-4111-8adb-481a885c8d44): Listede seçili Katılımcı bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload011ae03e-bc1a-4fbc-833d-cb1158d40695):Veriler Excel’ e aktarılabilir.

Toplantı Şablonu-Katılımcılar ekranına yeni bir katılımcı eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8956733b-851f-4b30-b15c-b55cb0eedfc7) (Yeni) butonu tıklanarak Katılımcı Tanımlama ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload14a9fd9b-23c8-424d-a0d3-bd8d4bab5fd5)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Kullanıcı Tipi:** Katılımcı olarak eklenecek Kullanıcı/ Pozisyon/ Rol ya da Kullanıcı Grubu seçilir.

**Kullanıcı/ Pozisyon/ Rol/ Kullanıcı Grubu:** Kullanıcı Tipi olarak seçilen katılımcı tipine göre ilgili seçim ekranı açılır. Bu alandan katılımcı seçimi gerçekleştirilir.

-   **Kullanıcı:** Katılımcı olarak eklenecek kullanıcı, Personel listesinden seçilebilir.
-   **Pozisyon:** Katılımcı olarak eklenecek kullanıcı, Pozisyon listesinden seçilebilir.
-   **Rol:** Katılımcı olarak eklenecek kullanıcı için Rol Tanımlama ekranında tanımlı olan rol seçilebilir.
-   **Kullanıcı Grubu:** Katılımcı olarak eklenecek kullanıcı için Kullanıcı Grubu listesinden kullanıcı grubu seçilebilir.

**Görev:** Katılımcının toplantı kapsamındaki görev tanımı bilgisinin girilir.

**Başkan:** Katılımcı toplantı başkanı ise ilgili check box işaretlenir.

**Planlama:** Katılımcının planlama yetkisi varsa ilgili check box işaretlenir.

**Gündem Ekleme:** Katılımcının gündem ekleme yetkisi varsa ilgili check box işaretlenir.

**Karar Verme:** Katılımcının karar verme yetkisi varsa ilgili check box işaretlenir.

**Sıra No:** Katılımcı sıra numarası girilir.

Toplantı Şablonu Katılımcı Tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb64d82b6-3c9a-4d69-9852-3f9555c6c678) (Kaydet) butonu tıklanarak Toplantı Şablonu Katılımcı Tanımlama işlemi gerçekleştirilir. Bu sayfada eklenen katılımcılar, Entegre Yönetim Sistemi menüsü altından planlanacak olan toplantılar için sistemden otomatik olarak kullanıcıya sunulur. İlgili kullanıcı taslak aşamasında yer alan toplantılar için katılımcılara ekleme çıkarma yapabilir. Bu alanın kullanımı, ilgili toplantıya katılan kişiler çoğunlukla aynı kişiler ya da katılımcıların çoğu genellikle aynı kişiler olduğunda anlam kazanacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload863fbfef-fdc3-4fcd-8365-b388d58d7831)

Gündemler; sekmesinde taslak toplantı gündemi tanımlanarak oluşturulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadedf584f0-fac4-4805-a3d1-de5ca0a2ae5c)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd82b7eff-77ab-483d-a8fc-a4decac92f9c): Yeni bir Gündem tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc96be829-2922-4058-9c53-93d7d61eee38): Listede seçili Gündem bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload596c4955-1fc1-4111-8adb-481a885c8d44): Listede seçili Gündem bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload011ae03e-bc1a-4fbc-833d-cb1158d40695): Veriler Excel’ e aktarılabilir.

Toplantı Şablonu Gündemler ekranına yeni bir Gündem eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8956733b-851f-4b30-b15c-b55cb0eedfc7) (Yeni) butonu tıklanarak Toplantı Şablonu Gündem Tanımlama ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload12f8419a-7a8e-4d6d-9446-f5a8de2c51d1)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Gündem Tanımı:** Detaylı olmamak kaydıyla bir gündem maddesi tanımlanır.

**Gündem Açıklaması:** Tanımı yapılan gündem maddesinin detaylı olarak açıklaması girilir.

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb64d82b6-3c9a-4d69-9852-3f9555c6c678) (Kaydet) butonu tıklanarak Toplantı Şablonu Gündem Tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload39b67b3a-eeef-4b87-832d-06ca29ad19e9)

Tüm sekmelerde bulanan gerekli alanlar doldurulduktan sonra ekranın sağ üst köşesinde bulunan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb7842777-2c77-4821-9787-9b0d8f6792d1) (Kaydet) butonu ile kayıt işlemi gerçekleştirilerek toplantı kaynağı tanımlanma işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2bbd7256-f728-47cf-87f0-034162075dec)

### **4.1.2.Alan Tanımlama**

**Menü adı**: Sistem Altyapı Tanımları/Kurul Toplantı/Alan Tanımlama

Kurul Toplantı Modülünde toplantı şablonu tanımlama ya da toplantı kalemi oluşturma menülerindeki alanlara ek olarak kullanıcı tanımlı bazı alanlar sistemde tanımlanabilir. Alan tanımlama menüsü ile tanımlanan alanlar alan havuzuna kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5cf3baa1-8039-479c-8845-ab7ec952e2a7)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd82b7eff-77ab-483d-a8fc-a4decac92f9c): Yeni bir alan eklenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc96be829-2922-4058-9c53-93d7d61eee38): Var olan alanda değişiklik yapılacaksa kullanılır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload596c4955-1fc1-4111-8adb-481a885c8d44): İlgili alanı silmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadee7fe241-bf08-41a5-9b08-ec2e71a7e0bb): Alanın değerleri tanımlanır.

Alan Tanımlama ekranına yeni bir Alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8956733b-851f-4b30-b15c-b55cb0eedfc7) (Yeni) butonu tıklanarak Alan Tanımlama /Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddbd2512b-e2a9-430a-9aac-c6171d20cdab)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Alan Kodu:** Alan kodu bilgisi tanımlanır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’

**Alan Adı:** Alan adı bilgisi tanımlanır.

**Başlık Notu:** Alanın başlık notu bilgisi tanımlanır.

**Giriş Tipi:** Oluşturulan alanda kullanıcı tarafından veri girişi/seçim mi yapacağı ya da hesaplama yöntemi ile otomatik olarak sistem tarafından mı atanacağı belirlenir.

**Alan Tipi**: Oluşturulan alanın metin, numerik, tarih, liste vb. alan tiplerinden hangisi olacağı belirlenir.

**Görünme Şartı:** Tanımlama işlemi devam eden alanın daha önceden tanımlanan başka bir alanın değerine göre görünüp görünmeyeceği belirlenir. Kullanımı [ALANKODU]=ALAN_DEĞERİ vb. şekildedir. (Örneğin, Fırsat var mı? Alanının alan kodu 01; Fırsat alanının alan kodu 02 olsun. Eğer “Fırsat” Alanının, “Fırsat var mı?” Alanındaki seçeneklerden değer kodu 100 olan “Evet” değeri seçili ise görülmesi gerekiyorsa 02 numaraları “Fırsat” alanının görünme şartı bölümüne formül şu şekilde yazılmalıdır: [01]=100)

**Durum:** Alan durumu aktif veya pasif olarak seçilir.

**Genişlik:** Alanın kolon genişliği bilgisi tanımlanır.

Alan tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb64d82b6-3c9a-4d69-9852-3f9555c6c678) (Kaydet) butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfe39c686-0ee4-485b-95ba-64f96a537690)

Eğer havuza eklenen alanlar Liste, Puanlı Liste, Arama Özellikli Liste ya da Puanlı Liste vb. değer eklenmesi gereken bir alan tiplerinden biriyse, ilgili alan seçildiği takdirde ekranın sağ üst köşesindeki butonlar arasında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf857359f-8aa5-442d-9f7c-e1d12beaa1af) (Değerler) butonu ortaya çıkmaktadır. Bu buton yardımıyla eklenen liste biçimindeki alanın değerleri tanımlanır.

**Sistemde mevcut bulunan alan tiplerinin tam listesi aşağıda belirtilmiştir;**

-   **Metin:** Elle yazım imkanı veren metin kutucuğu ekler.
-   **Metin Çok Satırlı:** Elle yazım imkanı veren karakter sınırı olmayan çok satırlı metin kutucuğu ekler.
-   **Nümerik:** Sayısal olarak veri girişi yaptırır.
-   **Nümerik-Parasal:** Parasal değer olarak nümerik giriş yaptırır.
-   **Nümerik-Birim:** Birim olarak nümerik giriş yaptırır.
-   **Tarih:** Takvim alanı ekler.
-   **Liste:** Birden fazla element arasından tek seçim yaptırır.
-   **Puanlı Liste:** Açılır menüden seçim yaptırır, liste elementlerinin puan değerleri mevcuttur.
-   **Arama Özellikli Liste:** Birden fazla element arasından geniş arama fonksiyonuyla arama yapabilecek şekilde, tekli ve/veya çoklu seçim yapılmasını sağlar.
-   **Ağaç Liste:** Ağaç kırılımına sahip birden fazla element arasından geniş arama fonksiyonuyla arama yapabilecek şekilde seçim yapılmasını sağlar.
-   **Personel:** QDMS personel veri tabanından kişi seçilebilmesini sağlar.
-   **Departman:** QDMS departman veri tabanından departman bilgisi seçilebilmesini sağlar.
-   **Unvan:** QDMS unvan veri tabanından unvan bilgisi seçilebilmesini sağlar.
-   **Doküman:** QDMS doküman veri tabanından doküman seçilebilmesini sağlar.
-   **Süreç:** QDMS süreç veri tabanından süreç seçilebilmesini sağlar.
-   **Yönetim Sistemi:** QDMS yönetim Sistemi veri tabanından yönetim sistemi bilgisi seçilebilmesini sağlar.
-   **Müşteri:** QDMS müşteri veri tabanından müşteri bilgisi seçilebilmesini sağlar.
-   **Tedarikçi:** QDMS tedarikçi veri tabanından tedarikçi bilgisi seçilebilmesini sağlar.
-   **Ürün Grubu:** QDMS ürün grubu veri tabanından ürün grubu bilgisinin seçilebilmesini sağlar.
-   **Ürün:** QDMS ürün veri tabanından ürün bilgisinin seçilebilmesini sağlar.
-   **Şirket Profili:** QDMS şirket profili veri tabanından şirket profili bilgisi seçilebilmesini sağlar.
-   **Başlık:** Formlara koyu harflerle yazılacak başlık alanı ekler.
-   **Dosya:** Dosya eklemesi için uygun alan getirecektir
-   **Resim:** Resim eklemesi için uygun alan getirecektir
-   **Resim Liste:** Resim listesinden seçim sağlar.
-   **Çoklu Resim:** Çoklu resim seçilmesini sağlar.
-   **Tablo:** Tablo tipli alan oluşturulmasını sağlar. (Bu tip bir alan eklendikten sonra alan değerleri olarak yeni alan tanımlamalarının yapılması gereklidir.)
-   **Sorgu:** QDMS/Ensemble veri tabanları içerisindeki ana verilerden seçim yapılabilmesi için tanımlanabilen alan türüdür. (Sadece Bimser Destek Ekibi tarafından tanımlanmalıdır) Tekli ve çoklu seçim yapılabilir.
-   **Sorgu Ağaç:** QDMS/Ensemble veri tabanları içerisindeki ağaç kırılımlı ana verilerden seçim yapılabilmesi için tanımlanabilen alan türüdür. (Sadece Bimser Destek Ekibi tarafından tanımlanmalıdır) Tekli ve çoklu seçim yapılabilir.
-   **Sekme:** Mevcut risk değerlendirme formunda alanların bulunduğu sekmenin haricinde alanların ilişki kurularak içerisinde görülebileceği yeni bir sekme oluşturur.
-   **Onay Kutusu Liste:** Talebe göre tekli veya çoklu seçim yaptırılacak tipte bir liste tipli alandır.
-   **Risk:** Risk tabanlı modüllerden değerlerin seçilebilmesini sağlar. Bu tip bir alan eklendikten sonra hangi modülden değerlerin geleceği alan tanımlama ekranında seçilmesi gereklidir.
-   **Açıklamalı Liste:** Seçilen liste değerinin yanına açıklama yazabilme imkanı sağlayan alan tipidir. Alan Tanımlama menüsünde alan değerleri tanımlanırken her değer için açıklama kutucuğunun aktif olup olmayacağının seçilmesi gerekir. Burada yapılan seçime göre Entegre Yönetim Sistemi menüsü altında bu alanın görüleceği menüde ilgili seçim yapıldığında alan değerinin yanına kullanıcının açıklama yazabilmesi için kutucuk açılmış olur.
-   **Pozisyon:** QDMS pozisyon veri tabanından pozisyon bilgisi seçilebilmesini sağlar.
-   **Saat:** Saat tipli alan ekler.

### **4.1.3.Fonksiyon Dizayner**

**Menü adı**: Sistem Altyapı Tanımları/Kurul Toplantı/ Fonksiyon Dizayner

Fonksiyon Dizayner özelliği ile alan havuzuna eklenen alanlar Kurul Toplantı Modüllerinin ilgili sayfaları ile ilişkilendirilebilir. Alan Tanımlama işlemi yapıldıktan sonra sıradaki işlem, bu alanın modülün hangi bölümlerinde kullanılacağının belirlenmesidir. Açılan ekranda Kurul Toplantı Modülünün alan eklenebilecek fonksiyonları sıralanacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf6cbcc00-da72-4ed0-abce-0d45948d13e9)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade35a9c78-b0f6-4023-864c-86a498e85c75)(Alanlar) butonuna tıklanarak alanların ilgili fonksiyonla ilişkilendirilme yapılacağı ekran açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1010af69-c741-4d63-9b15-e72aa188540e)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd82b7eff-77ab-483d-a8fc-a4decac92f9c): Yeni bir alan eklenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc96be829-2922-4058-9c53-93d7d61eee38): Listede seçili alan değiştirilir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload596c4955-1fc1-4111-8adb-481a885c8d44): Listede seçili alan silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadede26a6d-702b-4766-94cc-f1e52a0d90ac): Önceki ekrana geri dönülür.

İlgili fonksiyonda kullanılacak alanlar ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8956733b-851f-4b30-b15c-b55cb0eedfc7)(Yeni) butonuna tıklanarak belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4f64601c-a6d3-4dd1-bc19-eaeca6452e1f)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Alan Adı:** Alan tanımlama ekranında tanımlanmış alanlardan alan seçimi yapılır.

**Zorunlu Mu? :** Alanın zorunlu olup olmadığı seçilir. (Statü kullanımı olmadığında görülecektir.)

**Zorunluluk Mesajı:** Zorunlu alan doldurulmadığında verilecek uyarı mesajı bilgisi bu alana yazılır.

**Sıra No:** Alanın sıra no belirlenir.

**Varsayılan Rol:** İlgili alanın değeri daha önce tanımlanmış bir üst formdan ya da kaydı giren kişinin adı soyadı, pozisyonu, unvanı, departmanı, iş yeri gibi verileri ise bunlar için tanımlanmış rol seçilebilir. Örneğin, Risk detay formunda risk girişini yapanın departmanı adında bir alanda sisteme kaydı giren kullanıcının departmanı gelmesi gerekiyor varsayılan rol kullanılabilir. Kullanılmadığı durumda kullanıcı kendi departmanını hem yanlış seçebilir hem de kaydı giren kullanıcı fazladan bir işlem yapmış olur. Burada seçilen varsayılan rol sayesinde, kullanıcı risk girişi yapmaya başladığında departmanı otomatik gelecektir.

**Varsayılan Değer Değiştirilmesin:** Seçilen alan varsayılan olarak bir değer getiriyorsa getirdiği değerin değiştirmemesini sağlar.

**Gridde göster:** Alanın gridde gösterilmesi gerekiyorsa ilgili check box işaretlenir.

**Satır Sayısı:** İlgili alan çoklu satır ise, veri girişi ekranında kaç satır gözükmesi gerektiği belirlenir.

**Kolon Genişliği:** İlgili modülde girilen kayıtların listesinde (gridde) alanın kolon genişliği bilgisinin belirlenir. Verinin uzun olduğu alanlar için ort. 250, sadece rakam girilen alanlar için ise 75 kullanılması idealdir. Alana girilecek veriler düşünülerek bu aralıklarda bir değer kullanmak uygun olacaktır.

Alan Tanımlama/Fonksiyonlar/Yeni kayıt ekranında gerekli tüm alanlar doldurulduktan sonra ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb16aa6b0-6326-436b-8b23-fd1d14533d95) (Kaydet) butonu tıklanarak, ilgili alan için ilgili alanı fonksiyon ile ilişkilendirme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadffe0ce68-d5e3-43a1-8a8c-79aa440f15bf)

Fonksiyon Dizayner özelliği ile seçilen Kurul Toplantı Modüllerinin Toplantı Şablonu Tanımlama sayfasında Diğer Alanlar sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadda823b20-b50f-435d-b306-a457665e748d)

#### **4.1.4. Onay Akışı ve Rol Tanımlama**

Sistemde gerçekleştirilen toplantıların taslak onayı ardından karar aşamasında hangi onaycılar tarafından onaylanması gerektiğinin belirlendiği menüdür. Akış tanımlarını Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon ayarları/ Akış Tanımlama ekranından kontrol edilmeli, yoksa akışları tanımlanmalıdır. Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Rol Tanımlama ekranından onay akışları için rol tanımlamaları da gerçekleştirilmelidir. İlgili Akış ve Rol tanımlamalarının detaylı anlatımı için Sistem Altyapı Tanımları /BSAT/ Konfigürasyon Ayarları/Akış ve Rol Tanımlama menüleri incelenmelidir.

## **4.2.Entegre Yönetim Sistemi/Kurul Toplantı**

Kurul toplantılarının, YGG toplantılarının, Birim Toplantıları gibi toplantıların planlanmasın yapılıp, gerçekleştirildiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload84a39339-21fa-4d77-8ad0-088058fd731d)

### **4.2.1.Entegre Yönetim Sistemi/Kurul Toplantı/Toplantılar**

Toplantı planı oluşturma işleminin gerçekleştiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5a57aaeb-393d-483a-9c5d-537045e1092c)

**Ekranındaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd82b7eff-77ab-483d-a8fc-a4decac92f9c): Yeni bir toplantı kalemi oluşturulur.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc96be829-2922-4058-9c53-93d7d61eee38): Listedeki seçili toplantı kalemi bilgisi düzenlenir/ güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload596c4955-1fc1-4111-8adb-481a885c8d44): Listedeki seçili toplantı kalemi bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload011ae03e-bc1a-4fbc-833d-cb1158d40695): Ekrandaki toplantı kalemi listesi Excel’e aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload63961f04-a867-46f6-b04d-dacb50ebe323): Ekrandaki seçili toplantı kalemi için toplantı raporu alınır.

Yeni bir Toplantı Kalemi oluşturmak için ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada8741e2f-02d3-4a93-b683-b955a491c66b) (Yeni) butonuna tıklanır. Açılan ekrandaki ilgili

Toplantı Kaynağı seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade594ffdd-b2dd-4b81-87df-7310ed3e7be9) (ileri) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada6343384-5247-4adb-8ad7-edfe7b86b8f3)

Açılan ekranda ilgili “Şablon Detayı” sekmesinde “Toplantı Kodu” ve “Toplantı Tanımı” alanları alt yapı menüsünde gerçekleştirilen tanımlamalara otomatik gelir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload67f5af9b-b29c-42d9-8cb5-6f5bc01d2926)

Toplantı Tarihi alanından toplantının planlandığı tarih ve saat seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7c134c3d-03d3-4238-a066-96ea9916a284)

Katılımcılar sekmesi ile altyapı menüsünde tanımlanan toplantı kaynağı katılımcıları otomatik olarak gelir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada6eca46b-b8a4-465d-8706-9f3f7025b74f)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd82b7eff-77ab-483d-a8fc-a4decac92f9c): Yeni bir Toplantı Kalemi Katılımcı tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc96be829-2922-4058-9c53-93d7d61eee38): Listede seçili Toplantı Kalemi Katılımcı bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload596c4955-1fc1-4111-8adb-481a885c8d44): Listede seçili Toplantı Kalemi Katılımcı bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload011ae03e-bc1a-4fbc-833d-cb1158d40695):Veriler Excel’ e aktarılabilir.

Toplantı Kalemi Katılımcılar ekranına yeni bir Toplantı Kalemi Katılımcı eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8956733b-851f-4b30-b15c-b55cb0eedfc7) (Yeni) butonu tıklanarak Toplantı Kalemi Katılımcı Tanımlama ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7c8138bb-1404-420b-beff-c418d421de70)

Toplantı Kalemi Katılımcı Tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb64d82b6-3c9a-4d69-9852-3f9555c6c678) (Kaydet) butonu tıklanarak Toplantı Kalemi Katılımcı Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1ff7e2fa-7189-4782-ab13-2b9f5a5f16d5)

Gündemler sekmesi ile altyapı menüsünde tanımlanan toplantı kaynağının gündem maddeleri otomatik olarak gelir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada9504532-ccc6-4db3-b1f9-de74b1bdd099)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd82b7eff-77ab-483d-a8fc-a4decac92f9c): Yeni bir Toplantı Kalemi Gündem tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc96be829-2922-4058-9c53-93d7d61eee38): Listede seçili Toplantı Kalemi Gündem bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload596c4955-1fc1-4111-8adb-481a885c8d44): Listede seçili Toplantı Kalemi Gündem bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload011ae03e-bc1a-4fbc-833d-cb1158d40695): Veriler Excel’ e aktarılabilir.

Toplantı Kalemi Gündemler ekranına yeni bir Toplantı Kalemi Gündem eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8956733b-851f-4b30-b15c-b55cb0eedfc7) (Yeni) butonu tıklanarak Toplantı Kalemi Gündem Tanımlama ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload82ff2631-9218-4480-8424-fcf1c180d27a)

Toplantı Kalemi Gündem Tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb64d82b6-3c9a-4d69-9852-3f9555c6c678) (kaydet) butonu tıklanarak Toplantı Kalemi Gündem Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload73f24175-02d9-41bf-944a-4115957ae667)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2604339b-1bc5-461c-838c-c9551089ff83): Tanımlanan toplantı kalemi kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9674ff3e-a01e-4706-8a6d-1899eb850045): Tanımlanan toplantı kalemi bilgisi onaya gönderilir. (Eğer akış tanımlama ekranında toplantı taslak onayı akışı belirlendiyse toplantı, toplantı taslağının onaylanması için ilgili onaycıya gider. Taslak onayının olmadığı toplantı kurgularında ise toplantı katılım onayı için katılımcılara onaya gidecektir.)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload011ae03e-bc1a-4fbc-833d-cb1158d40695): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload488da5cc-acbd-4e5f-ab2c-9908df8013b6) (Kaydet) butonu ile taslak olarak kaydedilen toplantı planı toplantı kalemi ekranında “Taslak” statüsünde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf65f64d7-928e-49be-b793-88953b77c74e)

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc96be829-2922-4058-9c53-93d7d61eee38) (Güncelle) butonu tıklanarak Taslak statüsünde listede seçili Toplantı Kalemi Gündem bilgisi güncellenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0ed6f6d-a7e8-4161-bb77-c713746752a2)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade287ac8f-04d3-4d07-8d21-45fc110c68a5) (Onaya Gönder) butonu ile oluşturulan toplantı planı katılımcı onayına gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9fa5555c-eab5-4cf9-9c28-00f518f7b8c2)

### **4.2.2.Toplantı Katılım Onayı**

Toplantı katılımcıları, toplantıya katılıp katılamayacaklarını altyapıda tanımlanan toplantı kaynağı katılım onayı süresine göre sisteme bildirir. Katılımcı “Bekleyen İşlerim” menüsünde bulunan **“Toplantı Katılım Onayı”** alanından onay bekleyen toplantılarını görür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5b20982a-cdd7-4862-ac64-3ec47f217138)

Toplantı Kodu”na tıklayarak, Toplantı Kalemi-İSG KURUL TOPLANTILARI ekranı açılır.

Açılan ekranda katılım onayı verilebilir veya Katılım reddedilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf3d6eed7-4d98-4fc0-adf4-33fa4e03453c)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0e0daffa-59fd-4e4c-b3d7-c24763ccfa72): Katılım onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8db37589-b91e-42bf-aa4d-c18b35e724e3): Katılım reddedilir. (Reddet butonu tıkanırsa Toplantı Ret ekranında ret nedeni yazılarak Katılım onayı reddedilebilir. Katılımcı katılım onayını reddederse ret nedenini belirtmek zorundadır.)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload011ae03e-bc1a-4fbc-833d-cb1158d40695): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc1e95b5-d840-41bc-a6a7-3530ab6f3ba2)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0e0daffa-59fd-4e4c-b3d7-c24763ccfa72) (Onayla) butonu tıklanarak Katılım onayı verilir. Katılımcı katılım onayı verdiği takdirde ekranda aşağıdaki gibi bir mesaj görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9a67f1ad-883a-4a90-a10b-eff07cd56a52)

### **4.2.3.Toplantı Kararı Verilmesi**

Toplantı Katılım Onayı girişi tüm katılımcılar tarafından girildikten sonra toplantı, toplantının olup olmayacağının karar verilmesi için toplantı kararına gider.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6120051a-3c9a-4830-aebb-3a3c9a23d632)

Toplantı Karar Onaycısının Bekleyen İşlerim menüsünde **“Toplantı Karar”** olarak görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload10743af9-75e2-47be-aa29-762f7120e7fe)

Karar onaycısı toplantı koduna tıklayarak ilgili toplantı bilgilerine erişir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload329a277d-9f00-477c-b219-888dbf9933b6)

**Ekrandaki butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7a9df04c-149d-410a-b726-792991f663a3) : Toplantı Kararını onaylamak için kullanılır (toplantı gerçekleştirilmesi onayı).

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb307c677-ce29-4d3e-9690-4ac406763f56): Planlanan toplantıyı taslağa çekmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload86dfc30a-66b0-402a-869c-4f03de052046) : Planlanan toplantıyı iptal etmek için kullanılır.

Planlanan Toplantıya gerçekleştirme karar onayı vermek için karar onaycısı tarafından onay verilir. Onaylanan toplantı açık duruma getirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd0dcfc87-8dc4-462f-be13-205ce52d41d3)

Karar Onayı verilen toplantı için katılımcıların Bekleyen İşlerim sayfasına **“Katılacağım Toplantılar”** olarak görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf50d75d3-9de5-46ee-82d1-ce9645f96c81)

Karar Onayı verilen toplantı için toplantı sorumlularının Bekleyen İşlerim sayfasına **“Sorumlusu Olduğum Toplantılar”** olarak görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7a6b3b82-5907-4d70-b1e9-b0eff6577814)

Toplantı Sorumlusu, Toplantı Koduna tıklayarak “Toplantı Başlatma” ekranına ulaşır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5c4a9c28-24c6-4044-bc95-fd9dc0f1f134)

**Ekrandaki butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload85d4f7c4-763d-4991-8424-38bb452d2c84) : Toplantı Başlatmak için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0728b4b0-ebc8-4ad5-9405-a8eb6a3319f4) : Toplantı Raporu almak için kullanılır.

**Toplantı Başlatmak**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload85d4f7c4-763d-4991-8424-38bb452d2c84) (Toplantı Başlat) butonu ile ilgili toplantı başlatılır. Açılan ekranda toplantı katılımcılarının katılım durumu belirlenir**.**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0aeb84f4-920d-4cd1-b891-e989fd478b71)

Katılım Durumları belirlendikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb4db4fd2-13f8-41fc-bc22-9300d52c71b1) (Toplantı Başlat) butonuna tıklanır. Toplantı Kalemi (Planlama) ekranı açılır. Bu ekranda “Kararlar” sekmesine gelinir. Kararlar sekmesindeki toplantıda alınan kararlar sisteme girilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc21fe0a3-5dc5-4b0b-97cd-02edbd73698f)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd82b7eff-77ab-483d-a8fc-a4decac92f9c): Yeni bir Toplantı Kalemi Kararları tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc96be829-2922-4058-9c53-93d7d61eee38): Listede seçili Toplantı Kalemi Kararları bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload596c4955-1fc1-4111-8adb-481a885c8d44): Listede seçili Toplantı Kalemi Kararları bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload011ae03e-bc1a-4fbc-833d-cb1158d40695):Veriler Excel’ e aktarılabilir.

Toplantı Kalemi Kararları ekranına yeni bir Toplantı Kalemi Kararları eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8956733b-851f-4b30-b15c-b55cb0eedfc7)(Yeni) butonu tıklanarak Toplantı Kalemi Kararları Tanımlama ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload446212c4-aebe-4657-8079-902d6d5d4289)

**Karar:** Gündem maddesine uygun olarak toplantı sonucu alınan karar sisteme tanımlanır. Sistemde tanımlanan karar oluşturulacak karar türünde görev olarak atanır.

**Karar Türü (DÖF, Aksiyon, Doküman, Doküman Revizyon, Diğer):** Seçeneklerden karara uygun olan işlem işaretlenir.

Eğer **“DÖF”** seçilirse personel listesinden Ekip Lideri seçimi yapılır, termin tarihi girilir, sistemde tanımlı olan uygunsuzluk kategorilerinden seçim yapılır. Sistem üzerinden DÖF akışı başlatılır, ilgili kişiye görev atanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada222edd4-6437-4da0-b3aa-d823937b8bf7)

**“Aksiyon”** seçilirse personel listesinden Aksiyon Sorumlusu ve İşi Yapacak Kişi seçilir. Aksiyon Başlama ve Bitiş Tarihi seçilir. Sistem üzerinden Aksiyon akışı başlatılır, ilgili kişiye görev atanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2496a263-b0c5-4398-9cd4-943749fba144)

**“Doküman”** seçilirse hazırlanması planlanan dokümanın hangi klasörün içerisine hazırlanacağı belirlenir. Sistem üzerinden ilgili kişiye (Doküman Hazırlama Talebi Onaycısı) doküman hazırlama talebi görevi atanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload44a94df9-a75c-4215-898d-0c7fec0db5fe)

**“Doküman Revizyon”** seçilirse sistemde tanımlı olan hangi dokümanın revizyon yapılacağı belirlenir. Sistem üzerinden ilgili kişiye doküman revizyon görevi atanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload61901ea7-bd72-4728-be7c-3eecffac3ab6)

**“Diğer”** seçilirse kararla ilgili bilgi girişi yapılır, sistem üzerinden herhangi bir görev ataması gerçekleşmez.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload34bf759d-8628-4801-92ed-92c28a271bf6)

**Oylama:** Karara onay veren katılımcılar işaretlenir. Varsa yorumları tanımlanır.

**Karar Durumu:** Oylama alanında hiçbir katılımcı onay vermemiş olursa kararın reddedildiği bilgisi alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade3048d43-576c-4939-a351-f1c6271e682c)

Eğer tüm kullanıcılar onay verirse onaylanmıştır uyarısı alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaff0b638-c977-404b-91a4-a2a64aa61d8b)

Tüm alanlar tanımlandıktan sonra karar atamaları gerçekleştirilmiş olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload35acc1fd-855a-4641-80f6-2c43d04280f7)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload777ad680-1527-4d49-b147-104efb67947e)

Toplantı kararları tanımlanıp, ilgili görev atamaları gerçekleştirildikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload19c479b6-3e04-4071-b5d6-71507c489891) (Toplantıyı Bitir) butonu ile toplantı kapatılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload915a3f86-d849-40ae-8187-bceb77022396)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload65c6ef8f-1182-4534-892e-92f967999da3)

Toplantılar menüsünden oluşturulan toplantı kalemi seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0bf533cd-bea2-4832-8b84-2a698acd1ae4) (Toplantı raporu) oluşturulur.
