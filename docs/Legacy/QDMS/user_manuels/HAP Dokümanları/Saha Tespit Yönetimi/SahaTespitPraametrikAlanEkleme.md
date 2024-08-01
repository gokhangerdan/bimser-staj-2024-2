---
title: Parametrik Alan Tanımlama İşlemi
description: Parametrik Alan Tanımlama İşlemi Yardım Dokümanı
sidebar_position: 1
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::


**Saha Tespit Modülünde Raporlara Parametrik Alan Ekleme İşlemi ve Genel Tag Listesi Kullanıcı Yardım Dokümanı**


# **1. Saha Tespit Yönetimi Modülünde Raporlara Parametrik Alan Ekleme İşlemi ve Raporlarda Kullanılan Taglar**

Saha Tespit Yönetimi Modülünde raporlarına parametrik alan ekleme işlemi yapılmaktadır. Bulgu raporuna parametrik alan ekleme işlem basamakları ve bu module ilgili genel kullanılan taglerin (kısa kodların) listesi bu yardım dokümanında yer almaktadır.

## **1.1. Saha Tespit Yönetimi Modülünde Parametrik Alan Tiplerinin Bulgu Raporunda Gösterimi**

Saha Tespit Yönetimi Modülü raporlarından Bulgu raporuna eklenen parametrik alanların raporda gösterilme işlemi için öncelikle Sistem Altyapı Tanımları kısmında altyapı kurgusunun yapılması gerekmektedir. Altyapısını kurgulama işleminde Alan Tanımlama, Fonksiyon Dizanyer, Rapor Formatları Düzenleme ve Parametreler menüleri kullanılır. Alan tanımlamada Rapor formatı şablonuna taglerin eklenecek alanların tanımlama işlemi yapılır. Fonksiyon Dizanyer da tanımlanan bu alanların fonksiyonların sayfalarında görüntülenmesi için ilişkisi kurulur. Fonsiyon Dizanyer da fonksiyonun sayfası ile ilişkisi kurulan alanların Entegre Yönetim Sistemi\>   
Saha Tespit Yönetimi \>Saha Denetim menüsünde Plansız Denetip Yap butonu tıklanarak bir Plansız Denetim Tanımlama işlemi yapılır. Bu Plansız Denetim gerçekleştrime aşamasında Bulgu Tanımlama ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada2ac6a6b-2dd3-4af8-924c-ff6e11d364a4)(Yeni) butonu tıklanarak Bulgu tanımlanrken görüntülenen parametrik alan tiplerinin alan değerleri bilgisi girilir. Parametrik alan tiplerinin bilgi girişleri yapıldıktan sonra Rapor Formatları Düzenleme menüsüne gidilir. Rapor Formatların Düzenleme menüsünde Bulgu rapor formatı “bulguraporu.xlsx” indirilir. İndirilenen “bulguraporu.xlsx” rapor format şoblonuna Alan Tanımlama menüsünde tanımlanan parametrik alanların tag’leri Fonksiyon Dizanyer menüsünde tanımlı alan kodları bakılarak yazılır. Alan kodlarının Bulgu Tanımlama fonksiyon için hangi parametrik alan tipine göre taglerinin yazım şekli aşağıdaki tabloda yer almaktadır.

| **Fonksiyon No** | **Fonksiyon**   | **Alan Tipi**                     | **Alan Kodu** | **Tag**        |
|------------------|-----------------|-----------------------------------|---------------|----------------|
| 3                | Bulgu Tanımlama | Metin, Metin Çok Satırlı gibi     | ALAN3         | <ALAN3\>      |
| 3                | BulguTanımlama  | Liste, Personel gibi liste tipli  | ALAN4         | <ALAN4_ACK \> |

3 numaralı “Bulgu Tanımlama” fonksiyon için; Örneğin Metin tipli parametrik alan Fonksiyon Dizanyerde alan kodu ALAN3 ise rapor formatına eklenecek tag şekli <ALAN3\> şeklinde olmalıdır. <ALAN KODU\> şeklinde Fonksiyon Dizanyerde menüsündeki Alan kodları \<\> büyüktür ve küçüktür işaretleri arasına yazılacak şeklinde rapor format şablonuna yazılmalıdır. Liste, Personel, departman gibi liste tipli parametrik alan tiplerinde tagleri için “ACK” eki eklenir. Örneğin Liste tipli bir alanın Fonksiyon Dizanyer menüsündeki alan kodu ALAN4 ise Alan tag’i <ALAN4_ACK\> şeklinde rapor format şablonu eklenmelidir. <ALAN KODU_ACK\> şeklinde Fonksiyon Dizanyerde menüsündeki Alan kodları \<\> büyüktür ve küçüktür işaretleri arasına “ACK” eki eklenerek yazılacak şeklinde rapor format şablonuna yazılmalıdır Rapor formatına şablonuna parametrik alanların tag şeklinde yazıldıktan sonra Rapor format “bulguraporu.xlsx” aynı isimde bilgisayara kaydedilir. Kaydedilen aynı isimde Bulgu Raporunu formatı Rapor Formatları Düzenleme menüsünde tekrar sisteme yüklenir. Rapor Formatları Düzenleme menüsünde yüklenen rapor format şablonun adı ve uzantısı ile birlikte kopyalanarak parametreler menüsündeki Saha Tespit Yönetimi parametrelerinde 29 numaralı “Bulgu Raporu şablon Dosyası” parametresine sağ tıkla/yapıştır işlemi ile tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf553809f-d92f-40c4-87af-9c9e6c94394c)




Bulgu raporunun Rapor formatının şablonun parametreye tanımlama işleminde sonra Entegre Yönetim Sistemi\> Saha Tespit Yönetimi \>Raporlar\> Bulgu Raporu menüsüne gidilir. Açılan Bulgu Raporu ekranında filtre sekmesinde arama kriterlerinden Saha alanında Şirket Profili listesinde Plansız Denetim yapıldığı şirket seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcf738b38-3da6-476b-a70f-fb11ec38199a)(Ara) butonu tıklanılır. Listeden plansız Saha Denetim seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc48b6967-17d6-46ca-9eec-c55a43fd2a49)(Excel Aktar) butonu tıklanılır. Excel formatın alınan raporda parametrik alanların taglerinin bulunduğu kısımda girilen Bulgu Tanımlama ekranında alan bilgilerinin geldiği ve taglerin çalıştığı görülür.

**Saha Tespit Yönetimi Modülünde parametrelerindeki raporlar:**

Saha Tespit Yönetimi Modülün hangi fonksiyon için hangi rapor format şablonun hangi parametreye tanımlanacağı bilgisi aşağıdaki tabloda mevcuttur.

| **Fonksiyon No** | **Fonksiyon**    | **Rapor Formatı Şablon Adı** | **İlgili Parametre No** | **İlgili Parametre Tanımı** |
|------------------|------------------|------------------------------|-------------------------|-----------------------------|
| 3                | Bulgu Tanımlama  | bulguraporu.xlsx             | 29                      | Bulgu Raporu Şablon Dosyası |

Saha Tespit Yönetimi Modülünde alan tanımlamada tanımlanan alanların Fonksiyon Dizanyerdeki fonksiyonun sayfalarıyla ilişkilendirildikten sonra alan kodları tabloda belirtilen Rapor Formatları şablonlarına taglerin ekleme işlemi yapılır. Tag ekleme işleminden sonra Rapor Formatları düzenleme menüsünde sisteme yükleme işlemi yapılır. Sisteme yükleme işleminden sonra Rapor formatları düzenleme menüsünde adı ve uzantısı kopyalarak tabloda belirtilen ilgili parametreye tanımlama işlemleri yapılır.

“Bulgu Raporu” parametrik alanları Fonksiyon Dizayner menüsünden 3 numaralı “Bulgu Tanımlama” fonksiyonu seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade641c325-4b4c-4de9-8bec-4c4803b73678)(Alanlar ) butonuna basıldığı zaman gelen alan kodlarına göre belirlenir.

### **1.1.1.Sistem Altyapı Tanımları/ Saha Tespit Yönetim**

Bulgu raporunun parametrik alan ekleme işleminin altyapı kurgusunun tasarlandığı kısımdır. Altyapı kurgusu için Alan Tanımlama ve Fonksiyon Dizanyer menüleri kullanılmaktadır. Ayrıca Sistem Altyapı Tanımları Modülünde Rapor format şablonu indirilerek ve indirilen rapor formatına tag ekleme işlemi yapılmış rapor formatının şablonun sisteme aynı isimde yüklenmesi için Rapor Formatları Düzenleme menüsüde kullanılmaktadır. Sisteme yüklenen Bulgu Raporunun Sistem Altyapı Tanımları\>BSAT\>Konfigürasyon Ayarları\>Parametreler menüsünde İlgili parametreye tanımlama işlemi aynı modülün ilgili parametresinde yapılır. Saha Tespit Yönetimi parametrelerinde 29 numaralı “Bulgu Raporu Şablon Dosyası” parametresine tanımlama işlemi yapılır. Tanımlanan alan değerlerinin girilmesi için modülün Sistem Altyapı Tanımları kısmında Soru Havuzu, Soru Listesi Tanımlama ve Yetki Matrisi menüleri kullanılmaktadır. Tanımlanan alan değerlerinin girilmesi için kullanılan altyapıdaki menüler Entegre Yönetim Sistemi\> Saha Tespit Yönetimi \>Saha Denetim menüsünde Planlı yada Plansız Saha Denetimi tanımlama işlemlerin yapılmasında kullanılır. Bulgu Raporu için Saha Denetim menüsünde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeb390eb9-ffde-443a-9980-e2b0f0873fbb)(Plansız Denetim Yap) butonu tıklanarak bir Plansız Saha Denetiminde Bulgular sekmesinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada2ac6a6b-2dd3-4af8-924c-ff6e11d364a4)(Yeni) butonu ile Bulgu tanımlama ekranında görüntülenen alanların değerlerinin girilip, rapora yansıması sağlanacaktır.

### **1.1.1.1. Alan Tanımlama**

**Menü Adı**: Sistem Altyapı Tanımları/ Saha Tespit Yönetimi /Alan Tanımlama

Fonksiyon Dizanyer menüsünde bulunan menülerin sayfalarında gösterilecek alanların tanımlama işlemi yapıldığı menüdür. Bulgu Raporu için 3 numaralı “Bulgu Tanımlama” fonksiyonları için alanlar tanımlanır. Bu parametrik alan tanımlamaları metin, numerik, liste, personel gibi parametrik alan tipleridir.

**“Bulgu Tanımlama” Fonksiyonu için Alan Tanımlaması:**

“Bulgu Raporu Adı” metin tipli alan tanımlama işlemin yapılması;

Listeye “Bulgu Raporu Adı” metin tipli alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada2ac6a6b-2dd3-4af8-924c-ff6e11d364a4) (Yeni) butonu tıklanarak Alan Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload169d4e6c-e3f7-403f-9fad-da217595ca4c)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload30645f64-5209-4834-acac-dcc83e918cf7)

Alan tanımlama ekranında alan tipi alanında metin seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload64895601-5a60-4869-9e4e-11fd86cbc5c8) (Kaydet) butonu tıklanarak metin tipli alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload14103052-dda6-478c-82c2-cc1c535dd869)

“Bulgu Raporu Numarası” Nümerik tipli alan tanımlama işlemin yapılması;

Listeye “Bulgu Raporu Numarası” Nümerik tipli alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada2ac6a6b-2dd3-4af8-924c-ff6e11d364a4) (Yeni) butonu tıklanarak Alan Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1d660bac-aff2-42b3-b35a-d14f926a61fc)

Alan tanımlama ekranında alan tipi alanında Nümerik seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload64895601-5a60-4869-9e4e-11fd86cbc5c8) (Kaydet) butonu tıklanarak Nümerik tipli alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload646967ef-5150-4e46-868b-22cc2e23d309)

“Bulgu Raporu Tarihi” Tarih tipli alan tanımlama işlemin yapılması;

Listeye “Bulgu Raporu Tarihi” Tarih tipli alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada2ac6a6b-2dd3-4af8-924c-ff6e11d364a4) (Yeni) butonu tıklanarak Alan Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6714fa13-7761-4402-bd76-43bf87470b04)

Alan tanımlama ekranında Alan tipi alanında Tarih tipi seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload64895601-5a60-4869-9e4e-11fd86cbc5c8) (Kaydet) butonu tıklanarak Tarih tipli alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload42d371f5-6e7f-4964-b8d8-42e4fde37828)

“Bulguyu Tespit Eden Sorumlu” Personel tipli alan tanımlama işlemin yapılması;

Listeye “Bulguyu Tespit Eden Sorumlu” Personel tipli alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada2ac6a6b-2dd3-4af8-924c-ff6e11d364a4) (Yeni) butonu tıklanarak Alan Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7e19e4c8-7286-4554-9922-fed7c11d7f11)

Alan tanımlama ekranında alan tipi alanında Personel seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload64895601-5a60-4869-9e4e-11fd86cbc5c8) (Kaydet) butonu tıklanarak Personel tipli alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5029bdce-48f6-4d4e-adfd-1e508baa2bb7)

“Bulguyu Tespit Eden Departman” Departman tipli alan tanımlama işlemin yapılması;

Listeye “Bulguyu Tespit Eden Departman” Departman tipli alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada2ac6a6b-2dd3-4af8-924c-ff6e11d364a4) (Yeni) butonu tıklanarak Alan Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2df02b47-6990-4ccb-ada8-d3642eda989d)

Alan tanımlama ekranında Alan tipi alanında “Departman” tipi seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload64895601-5a60-4869-9e4e-11fd86cbc5c8) (Kaydet) butonu tıklanarak “Departman” tipli alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9e79206d-70d2-445d-b864-785b2f82c9e9)

“Tespit Edilen Bulgu Önemli midir?” liste tipli alan tanımlama işlemin yapılması;

Listeye “Tespit Edilen Bulgu Önemli midir?” liste tipli alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada2ac6a6b-2dd3-4af8-924c-ff6e11d364a4) (Yeni) butonu tıklanarak Alan Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0e6f1a37-e0e7-45c5-8ae9-7d88f52a5730)

Alan tanımlama ekranında Alan tipi alanında liste tipi seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload64895601-5a60-4869-9e4e-11fd86cbc5c8) (Kaydet) butonu tıklanarak liste tipli alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0d9cf789-44a6-401a-880b-6fa339fad328)

“Tespit Edilen Bulgu Önemli midir?” liste tipli alanına değer eklemek için “Tespit Edilen Bulgu Önemli midir?” alanı seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf1b328bf-850a-41c3-a56b-11b7c1a5482b) (Değerler) butonuna tıklanarak alanın değerlerinin tanıtılacağı ekrana gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc3f200c4-0880-42e1-9a63-4cdc640fc347)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7278ccc9-88a9-49e8-9487-b88c5fbb3bba) : Yeni butonuna tıklanarak yeni değer tanımlama işlemine başlanılır. İstenirse ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4fe2270e-6338-44b6-b434-dd9b12ecd7ff)(Şablon İndir) ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload91dcd97e-1274-424b-976b-e0eefbb4bd04)(Şablon Yükle) butonları ile sisteme toplu olarak alan değerleri aktarılabilmektedir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4fe2270e-6338-44b6-b434-dd9b12ecd7ff)(Şablon indir) butonu ile sistem şablonu bilgisayara indirir. İlgili şablon kullanıcılar tarafından doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload91dcd97e-1274-424b-976b-e0eefbb4bd04)(şablon yükle) butonu ile sisteme yüklendiğinde şablondaki tüm alan değerleri sisteme aktarılmış olacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7d016462-21ac-4bbe-b3c8-cdba19a09882)

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload64895601-5a60-4869-9e4e-11fd86cbc5c8) (Kaydet) butonu tıklanarak değer tanımlama işlemi gerçekleştirilir. “Tespit Edilen Bulgu Önemli midir?” liste tipli alanın liste elemanları (değerleri) aynı şekilde tümü tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc185bea6-fc36-4cfc-bf7a-d0bf034ff6eb)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6801bf5a-2c04-4c89-a1ea-6435a8789be9)(Geri) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddd7f037f-23b9-48a6-9ff7-953d52ab6677)

### **1.1.1.2.Fonksiyon Dizayner**

**Menü Adı**: Sistem Altyapı Tanımları/Saha Tespit Yönetimi / Fonksiyon Dizayner

Alan Tanımlama menüsünde rapor formatı şablona eklenecek alanların tanımlama işleminde sonra Sistem Altyapı Tanımları/Saha Tespit Yönetimi /Fonksiyon Dizanyer menüsü tıklanılır. Açılan Fonksiyon Dizanyer ekranında tanımlanacak alanlarının eklenecek 7 fonksiyon bulunur. Bu fonksiyonlardan Bulgu Raporu için kullanılacak fonksiyon 3 numaralı “Bulgu Tanımlama” fonksiyonudur. Tanımlanan alanların Fonksiyon Dizanyer menüsünde bulunan bu fonksiyonun sayfası ile ilişkilendirme işlemi bu menüde yapılır Bulgu Raporu için tanımlanan alanların fonksiyonun sayfası ilişkilendirilmesi yapılır. Tanımlanan alanların 3 numaralı fonksiyonu sayfası ile ilişkilendirmesi işleminde sonra bir Plansız Saha Denetim gerçekleştirmede Bulgular sekmesinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada2ac6a6b-2dd3-4af8-924c-ff6e11d364a4)(Yeni) butonu ile Bulgu Tanımlama işlem aşamasındaki ekranlarda görüntülenmesi sağlanmış olur.

3 numaralı “Bulgu Tanımlama” fonksiyonu için tanımlanan alanların ilgili fonksiyonun sayfası ile ilişkilendirilmesi;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcd25f081-3cc0-498f-9b9b-79af12045d7e)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade641c325-4b4c-4de9-8bec-4c4803b73678): Alanlar butonuna tıklanarak alanların ilgili fonksiyonla ilişkilendirilme yapılacağı ekran açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4ec8698a-1c94-43b7-ace1-886935b9328f)

İlgili fonksiyonda kullanılacak alanlar ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada2ac6a6b-2dd3-4af8-924c-ff6e11d364a4)(Yeni) butonuna tıklanarak belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5564a17d-26f3-4fee-aad0-e29d9abb8142)

Açılan ekranda alan bilgileri listeden seçilir, zorunlu bir alan ise kullanıcının bu alanı doldurmadığında karşısına çıkacak mesaj tanımlanır. Gerekli tüm alanlar doldurulduktan sonra ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload68de938e-3eaa-4ea0-b84d-34d915c684e9) (Kaydet) butonu tıklanarak, ilgili alan için fonksiyon sayfalarıyla ile ilişkilendirme işlemi gerçekleştirilir. Gerekli olan tüm alanlar bu şekilde ilgili fonksiyona eklenir. Aşağıda görüldüğü üzere Alan No’nun yanında Alan Kodu bölümü vardır. Bu Bulgu raporuna bu alan düzenlemelerinde \< ALAN1\> vb. şekilde tagin raporun rapor formatı şablonuna eklenerek düzenleme yapılmasına imkan sağlayan koddur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3bccab1a-ec98-4eaf-bdc8-db54a0e2a2b6)

İlgili fonksiyonda kullanılacak alanlar tümü aynı şekilde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada2ac6a6b-2dd3-4af8-924c-ff6e11d364a4)(Yeni) butonuna tıklanarak belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload499f803e-83ee-4423-89fe-91d127c738c5)

“Bulgu Tanımlama” fonksiyonunda liste, personel ve departman gibi liste tipli alanlarda örneğin “Tespit Edilen Bulgu Önemli midir?” liste tipli alan için\< ALAN6_ACK\> şeklinde tagi Bulgu raporunun rapor formatına eklenir.

### **1.1.2. Bulgu Raporu Formatına Tag Eklenecek Alanların Değerlerin Girilmesi**

Bulgu Raporu formatına tag eklenecek alanların değerlerin girilmesi için Saha Denetimi menüsünde yeni bir Plansız Saha Denetimi tanımlama işlemi yapılır. Denetim gerçekleştirmede Bulgular sekmesinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada2ac6a6b-2dd3-4af8-924c-ff6e11d364a4)(Yeni) butonu ile Bulgu tanımlama işlemi yapılır. Alan Tanımlama menüsünde tanımlanan alanlar Fonksiyon Dizanyer menüsünde bu fonksiyonun sayfası ile ilişkilendirildiği için Plansız Saha Denetimi gerçekleştirmede Bulgular sekmesinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada2ac6a6b-2dd3-4af8-924c-ff6e11d364a4)(Yeni) butonu tıklanarak Bulgu tanımlanırken Bulgu tanımlama ekranlarında alan değerleri görüntülenir. Görüntülenen bu alan değerlerinin bilgisi girilir. Plansız Saha Denetimi gerçekleştirmede Sistem Altyapı Tanımlarında altyapı kurgusunun yapılması gerekmektedir. Plansız Saha Denetimin gerçekleştirme işleminin altyapı kurgusu için Sistem Altyapı Tanımların kısmında Soru Havuzu, Soru Listesi Tanımlama ve Yetki Matrisi işlemlerinin yapılması gerekmektedir. Altyapısı kurgusu tanımlandıktan sonra Entegre Yönetim Sisteminde Saha Denetimi menüsünde Plansız Saha Denetimi işlemi yapılır. Açılan Denetimi Gerçekleştir ekranında Bulgular sekmesinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada2ac6a6b-2dd3-4af8-924c-ff6e11d364a4)(Yeni) butonu ile Bulgu tanımlama işlemide gerçekleştirilir.

### **1.1.2.1.Entegre Yönetim Sistemi/ Saha Tespit Yönetimi**

Sistem Altyapı Tanımları/ Saha Tespit Yönetimi kısmında altyapı kurgusu tanımlanan modülün Saha Denetimi menüsünde![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeb390eb9-ffde-443a-9980-e2b0f0873fbb)( Plansız Denetim Yap) butonu tıklanarak bir Plansız Saha Denetimi tanımlama işlemlerinin gerçekleştirilme işlemin yapıldığı kısımdır. Denetimi gerçekleştir ekranında Bulgular sekmesinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada2ac6a6b-2dd3-4af8-924c-ff6e11d364a4) (Yeni) butonu tıklanarak Bulgu tanımlama işlemi yapılarak bu tanımlama ekranındaki alan değerlerinin girilmesi sağlanılır.

#### **1.1.2.1.1.Saha Denetimi**

**Menü Adı:** Entegre Yönetim Sistemi/ Saha Tespit Yönetimi/ Saha Denetimi

Saha Tespit Yönetimi modülünde saha denetimin gerçekleştirildiği menüdür. Saha tespit yönetimi planlı saha denetimi ve plansız saha denetimi olmak üzere ikiye ayrılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6d0d7efc-47f3-497c-9dc9-a8b7cf9a9567)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeb390eb9-ffde-443a-9980-e2b0f0873fbb) (Plansız Denetim Yap) butonu tıklanarak plansız saha denetim işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload21b4e5d0-af1f-4828-832a-dbbe45dd4935)

Denetim ilgili gerekli bilgiler doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9ebbabfb-dcc4-4a18-9f26-6af7ea1b9668) İleri butonu tıklanır. Denetim soruları ekranı açılır. İstenirse soru havuzundan soru eklenir yada Soru Listesinde tanımlı soru listesi eklenir. Soru eklemeden bir Plansız Saha Denetim gerçekleştirilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6b996389-8b43-4819-b97d-3bf996224a1e)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec8513dd-3983-4be8-b6b2-0baaff2f33e3) (Soru Listesi Ekle) butonu tıklanarak Denetime Soru Listesi eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload24eaa893-2277-4a28-8d71-b6a3ee7d09e5)

Soru Seç ekranında Soru Listesi seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2d082091-3db1-41ce-914c-5dba8d254a7c)(Seç) botunu tıklanarak Plansız Saha Denetime Soru listesi ekleme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd1125c2b-430e-4cdb-98f7-7c4cc6dc0aa2)

Denetime Soru listesi ekleme işleminde sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9ebbabfb-dcc4-4a18-9f26-6af7ea1b9668) İleri butonu tıklanır. Denetimi gerçekleştir ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload88dbf628-81f3-4bc1-9171-b0066621556a)

Denetim gerçekleştir ekranında zorunlu alan yorum kısmı doldurulur ve sorulara verilecek cevapların seçenekleri seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2d46acd0-21d1-40ef-928f-ed08c828e8a8)

Bulgular sekmesi tıklanır. Plansız Saha denetimde tespit edilen bulgular tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaa32b175-1201-47c6-a053-a40b8458fa80)

Bulgular sekmesinde ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6ec4176b-a5d3-4711-bafa-51d77509a6de)(Yeni) butonu tıklanarak bulgu tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5fff3893-e259-4b51-9d8d-9edd9dc6779b)

Alan tanımlamada menüsünde tanımlanan ve Fonksiyon Dizanyer menüsünde Bulgu tanımlama sayfası ile ilişkilendirilen parametrik alan tipleri görüntülenir. Görüntülenen bu parametrik alan tiplerinin bilgi girişleri yapılır. Bu parametrik alan tiplerinin tagleri daha sonra rapor formatına eklenerek rapora basılması sağlanacaktır. Bulgu Tanımlama ekranında gerekli tüm alanlar doldurulduktan sonra ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload68de938e-3eaa-4ea0-b84d-34d915c684e9) (kaydet) butonu tıklanarak, Bulgu tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfe00ff72-a148-4e80-ba03-2462e4e54bb1)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload64895601-5a60-4869-9e4e-11fd86cbc5c8) (Kaydet )butonu tıklanarak Plansız Saha denetimi kapatılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade131a176-e883-4806-b1e3-457cfd3c73a4)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada223b6ef-3d9f-4e06-8954-5432f4c33b08)

### **1.2.3.Bulgu Raporun Rapor Formatına Tanımlanan Parametrik Alanların Taglerin Eklenmesi**

**Menü Adı**: Sistem Altyapı Tanımları/BSAT/ Konfigürasyon Ayarları/Rapor Formatları Düzenleme

Bulgu Raporu tanımlanan parametrik alanların taglerin eklenmesi için Sistem Altyapı Tanımları\>BSAT\> Konfigürasyon Ayarları\>Rapor Formatları Düzenleme menüsüne gidilir. Qdms tüm raporların yüklendiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3169c3df-88c0-42ad-b982-d4edc80fb1f0)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload481b9756-8b49-4d69-929e-185630918c27) (Görüntüle) butonu tıklanarak Bulgu Raporunun rapor format şablonu (bulguraporu.xlsx) bilgisayara indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbd877385-ba83-47ef-942f-05e24875e2cc)

Alan Tanımlama tanımlanan alanlar Fonksiyon Dizanyer menüsünde ilgili sayfalarının ilişkilendirildikten sonra Fonksiyon Dizanyer da fonksiyonun seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade641c325-4b4c-4de9-8bec-4c4803b73678)(Alanlar) butonun tıklatıldığına açılan alan kodları rapor formatında alan değerleri kısmına yazılarak eklenir.

**3 Numaralı “Bulgu Tanımlama” Fonksiyonu için Bulgu Rapor Formatına Eklenecek Tagler;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload313ca5da-d4b1-4c7d-8f22-85b8c7e80b25)

Rapor Formatına Fonksiyon Dizanyerdeki Alan kodları \<\> büyüktür ve küçüktür işaretleri arasına yazılır. Tag yazım şekli <ALANX\> dir. Örneğin ALAN1 kodlu “Bulgu Raporu Adı” metin tipli parametrik alanı <ALAN1\> şeklinde rapor format şablonu alan değeri kısmına yazılır. Liste, Personel gibi liste tipli alanlarda “ACK” eki ile birlikte tagi yazmak gerekiyor. Örneğin ALAN4 kodlu “Bulgu Tespit Eden Sorumlu” personel tipli parametrik alanda <ALAN4_ACK\> şeklinde tag’ini rapor formatına şablonuna yazmak gerekiyor.

“Bulgu Tanımlama” fonksiyonu için Fonksiyon Dizanyer menüsünde Alan tanımlamada tanımlanan alanlarının kodlarının tag şeklinde yazılmış şekli aşağıdaki tabloda yer almaktadır

| **Alan Adı**                      | **Alan Tipi** | **Alan Kodu** | **Tag**       |
|-----------------------------------|---------------|---------------|---------------|
| Bulgu Raporu Adı                  | Metin         | ALAN1         | <ALAN1\>     |
| Bulgu Raporu Numarası             | Nümerik       | ALAN2         | <ALAN2\>     |
| Bulgu Raporu Tarihi               | Tarih         | ALAN3         | <ALAN3\>     |
| Bulguyu Tespit Eden Sorumlusu     | Personel      | ALAN4         | <ALAN4_ACK\> |
| Bulguyu Tespit Eden Departmanı    | Departman     | ALAN5         | <ALAN5_ACK\> |
| Tespit Edilen Bulgu Önemli midir? | Liste         | ALAN6         | <ALAN6_ACK\> |

Fonksiyon Dizanyerdeki fonksiyonların tablodaki parametrik alan tiplerinin alan tanımları ve tagleri ilgili bilgileri indirilen rapor format şablonuna yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload379489d9-66b3-4da7-94be-9034c82758be)

Rapor formatına şablonuna alan tanımları ve taglerinin yazılımdan sonra rapor “bulguraporu.xlsx” aynı isimde formatı bilgisayara kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload438d3ce4-6cf2-4847-b75a-ca9be87eaec7)

Bilgisayara kaydedilen aynı isimdeki Rapor format (bulguraporu.xlsx) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2dcb9efb-f4a0-4b4e-9942-4332e6bc8f30) (Yeni) butonu ile tekrar rapor formatları düzenleme menüsünden sisteme yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade228f074-2e18-4272-9e8d-3dbcf7b9305b)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5d0b3e12-2c21-4628-a495-e708538f8b2f)

Rapor Formatları Düzenleme menüsünde aynı isimde rapor format yükleme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1ea3154f-38dc-4012-afb1-bdfdcfad58cc)

Rapor Formatları Düzenleme menüsünde sisteme yüklenen Rapor Formatının adı ve uzantısı ile birlikte sağ tıkla/Kopyala yöntemi ile kopyalanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload451b501a-1e4a-41bc-b959-e276b6749c07)

Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Parametreler menüsüne gidilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f55f4cd-64bd-42f3-b605-6ca10764da82)

Filtre sekmesinde Modül olarak Saha Tespit Yönetimi seçilirek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6b40dc31-7d1b-439e-9e3c-4434ea70c003)(Ara) butonu tıklanılır. Saha Tespit Yönetim Parametreleri liste sekmesinde listelenir. Saha Tespit Yönetim parametrelerinede 29 numaralı “Bulgu Raporu Şablon Dosyası” parametresi seçilerek ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd3849d4d-59a8-4b70-b016-d860be01a22d)(Değiştir) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaf27592a-8230-4f18-bd64-9b48762f28cd)

Parametrenin içeriği görüntülenerek Rapor formatları Düzenleme menüsünde sisteme yüklenen rapor format şablonun adı ve uzantısı ile birlikte kopyalanan Rapor formatı şablonu parametre değerine sağ tıkla/Yapıştır yöntemi ile yapıştırılarak tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6bdb46bd-ec41-4d84-b0c5-d5c55b96f5b0)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0c2f16c6-1b6c-4e6e-b27a-11af6cd84acf)

Rapor format şablon dosyası ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload64895601-5a60-4869-9e4e-11fd86cbc5c8)(kaydet) butonu tıklanarak parametre değerine tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1dd3be62-7059-431f-8d1b-d62ddc42e31c)

### **1.1.4. Bulgu Raporunun Rapor Formatına Eklenen Parametrik Alanların Gösterimi**

**Menü Adı**: Entegre Yönetim Sistemi/ Saha Tespit Yönetim /Raporlar/Bulgu Raporu

Bulgu Raporunun rapor formatına (bulguraporu.xlsx) tag ekleme işlemi yapılıp, Rapor Formatların Düzenleme menüsünde sisteme yüklenip ve 29 numaralı parametreye tanımlama işlemlerinden sonra Entegre Yönetim Sistemi/ Saha Tespit Yönetim /Raporlar/Bulgu Raporu menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9b961c93-1cc4-4f35-ace2-2eec89f643c6)

Açılan Bulgu Raporu ekranında Liste ve Filtre sekmesi karşımıza çıkar. Arama kriterlerinde Saha alanına Plansız Saha Denetimin gerçekleştiği Şirketin Şirket Profili listesinde Şirket bilgisi seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcf738b38-3da6-476b-a70f-fb11ec38199a)( ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada989a643-790e-4320-bb96-5edc3f0e4b5f)

Liste sekmesinde gerçekleştirme işlemi yapılan Plansız Saha denetim seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc48b6967-17d6-46ca-9eec-c55a43fd2a49)(Excel Aktar)butonu tıklnılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d3628dc-b3ed-47aa-a7da-0a1d84b9d7ac)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd2d8974e-461d-4198-a0c8-1910367485d5)

Alınan Excel formatından Bulgu raporununda Alan tanımlama menüsünde tanımlanan parametrik alan tiplerinin değerlerinin bilgisinin raporu geldiği ve şablona eklenen parametrik alan tiplerinin tag’lerinin çalıştığı görülür.

## **1.2. Saha Tespit Yönetimi Modülünde Genel Replacement (Kısa Kodlar) Tag Tablosu**

Saha Tespit Yönetimi Modülünde kullanılan Genel taglerin listesi aşağıdaki tabloda yer almaktadır.

| **Replacement (Kısa Kodlar)** | **Açıklaması**             |
|-------------------------------|----------------------------|
| <ID\>                        | Denetim ID Bilgisi         |
| <TANIM\>                     | Denetim Tanımı Bilgisi     |
| <PLAN_TARIHI\>               | Plan Tarihi Bilgisi        |
| <YAPACAK\>                   | Yapacak Bilgisi            |
| <DENETLENEN_SAHA\>           | Denetlenen Saha Bilgisi    |
| <GERCEKLESME_TARIHI\>        | Gerçekleşme Tarihi Bilgisi |
| <DENETIM_SAATI\>             | Denetim Saati Bilgisi      |
| <YORUM\>                     | Yorum Bilgisi              |
| <STATU\>                     | Statü Bilgisi              |
| <ONAY_TARIHI\>               | Onay Tarihi Bilgisi        |
| <RED_ONAY_ACK\>              | Ret Onay Açıklama Bilgisi  |
| <BULGU_ID\>                  | Bulgu No Bilgisi           |
| <BULGU_OZET\>                | Bulgu Özeti Bilgisi        |
| <BULGU_DETAY\>               | Bulgu Detayı Bilgisi       |
| <BULGU_TIPI\>                | Bulgu Tipi Bilgisi         |
| <AKSIYON_NO\>                | Aksiyon No Bilgisi         |
| <AKSIYON_DURUMU\>            | Aksiyon Durumu Bilgisi     |
| <DOF_NO\>                    | DÖF No Bilgisi             |
| <DOF_DURUM\>                 | DÖF Durumu Bilgisi         |
| <SORU_ID\>                   | Soru No Bilgisi            |
| <SORU\>                      | Soru Bilgisi               |
| <CEVAP\>                     | Cevap Bilgisi              |
| <MPUAN\>                     | Max Puan Bilgisi           |
| <AGIRLIK\>                   | Ağırlık Bilgisi            |
| <SORU_PUAN\>                 | Puan Bilgisi               |
| <OLUMLU_CEVAP\>              | Olumlu Cevap Bilgisi       |
| <OLUMSUZ_CEVAP\>             | Olumsuz Cevap Bilgisi      |
| <NOTR_CEVAP\>                | Nötr Cevap Bilgisi         |
