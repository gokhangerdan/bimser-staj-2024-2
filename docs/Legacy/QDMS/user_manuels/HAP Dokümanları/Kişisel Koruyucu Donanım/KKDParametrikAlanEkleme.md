---
title: Parametrik Alan Tanımlama İşlemi
description: Parametrik Alan Tanımlama İşlemi Yardım Dokümanı
sidebar_position: 1
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::


**KKD Modülünde Raporlara Parametrik Alan Ekleme İşlemi ve Zimmet Listesi Tag Listesi Kullanıcı Yardım Dokümanı**


# **1.KKD Modülünde Raporlara Parametrik Alan Ekleme İşlemi ve Raporlarda Kullanılan Taglar**

KKD Modülünde raporlarına parametrik alan ekleme işlemi yapılmaktdır. Zimmet Listesi Raporuna parametrik alan ekleme işlem basamakları ve Zimmet Listesi raporunda taglerin (kısa kodların) listesi bu yardım dokümanında yer almaktadır.

## **1.1.KKD Modülünde Parametrik Alan Tiplerinin Zimmet Listesi Raporunda Gösterimi**

KKD Modülü raporlarından Zimmet Listesi raporuna eklenen parametrik alanların raporda gösterilme işlemi için öncelikle Sistem Altyapı Tanımları kısmında altyapı kurgusunun yapılması gerekmektedir. Altyapısını kurgulama işleminde Alan tanımlama, Fonksiyon Dizanyer ve Rapor Formatları Düzenleme menüleri kullanılır. Alan tanımlamada Rapor formatı şablonuna taglerin eklenecek alanların tanımlama işlemi yapılır. Fonksiyon Dizanyer da tanımlanan bu alanların fonksiyonların sayfalarında görüntülenmesi için ilişkisi kurulur. Fonsiyon Dizanyer da fonksiyonlarının sayfayaları ile ilişkisi kurulan alanların Entegre Yönetim Sistemi\>KKD \>Zimmet işlemleri menüsünde “Zimmet Ver”, “Zimmet Kontrol” ve “Zimmet Geri Al” menülerinde görüntülenen parametrik alan tiplerinin alan değerleri bilgisi girilir. Parametrik alan tiplerinin bilgi girişleri yapıldıktan sonra Rapor Formatları Düzenleme menüsüne gidilir. Rapor Formatların Düzenleme menüsünde Zimmet Listesi rapor formatı “ZIMMET_LISTESI.xlsx” indirilir. İndirilenen ZIMMET_LISTESI.xlsx” rapor format şoblonuna Alan Tanımlama menüsünde tanımlanan parametrik alanların tag’leri Fonksiyon Dizanyer menüsünde tanımlı alan kodları bakılarak yazılır. Alan kodlarının hangi fonksiyonda hangi parametrik alan tipine göre taglerinin yazım şekli aşağıdaki tabloda yer almaktadır.

| **Fonksiyon**      | **Alan Tipi**                  | **Alan Kodu** | **Tag**            |
|--------------------|--------------------------------|---------------|--------------------|
| KKD Zimmet Ver     | Metin, Metin Çok Satırlı gibi  | ALAN3         | <VER_ALAN3\>      |
| KKD Zimmet Ver     | Liste, Personel gibi           | ALAN4         | <VER_ALAN4_ACK\>  |
| KKD Zimmet Kontrol | Metin, Metin Çok Satırlı gibi  | ALAN3         | <KON_ALAN3\>      |
| KKD Zimmet Kontrol | Liste, Personel gibi           | ALAN4         | <KON_ALAN4_ACK\>  |
| KKD Zimmet Al      | Metin, Metin Çok Satırlı gibi  | ALAN3         | <AL_ALAN3\>       |
| KKD Zimmet Al      | Liste, Personel gibi           | ALAN4         | <AL_ALAN4_ACK\>   |

2 numaralı “KKD Zimmet Ver” fonksiyon için; Örneğin Metin tipli parametrik alan Fonksiyon Dizanyerde alan kodu ALAN3 ise rapor formatına eklenecek tag şekli <VER_ALAN3\> şeklinde olmalıdır. <VER_ALAN KODU\> şeklinde Fonksiyon Dizanyerde menüsündeki Alan kodları \<\> büyüktür ve küçüktür işaretleri arasına yazılacak şeklinde rapor format şablonuna yazılmalıdır. Liste, Personel gibi liste tipli parametrik alan tiplerinde tagleri için “ACK” eki eklenir. Örneğin Liste tipli bir alanın Fonksiyon Dizanyer menüsündeki alan kodu ALAN4 ise Alan tag’i <VER_ALAN4_ACK\> şeklinde rapor format şablonu eklenmelidir. Rapor formatına şablonuna parametrik alanların tag şeklinde yazıldıktan sonra Rapor format “ZIMMET_LISTESI.xlsx” aynı isimde bilgisayara kaydedilir. Kaydedilen aynı isimde Zimmet Listesi Raporunu formatı Rapor formatları düzenleme menüsünde tekrar sisteme yüklenir.

Zimmet Listesi Raporunun Rapor formatının şablonun yükleme işleminde sonra Entegre Yönetim Sistemi\> Kişisel Koruyucu Donanım \>Raporlar\>Zimmet Listesi Raporu menüsüne gidilir. Açılan Zimmet Takibi ekranında filtre sekmesinde arama kriterlerinden Zimmet İşlemlerinde alan değerlerini girilen KKD listelenmesi sağlanılır. Listelenen KKD seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload59a1b3a4-4636-4df2-a2d3-dd12c490c796)(Excel aktar) butonu tıklanır. Excel formatın alınan raporda parametrik alanların taglerinin bulunduğu kısımda girilen “Zimmet Ver”, “Zimmet Kontrol” ve “Zimmet Geri Al” ekranında alan bilgilerinin geldiği ve taglerin çalıştığı görülür.

### **1.1.1.Sistem Altyapı Tanımları/Kişisel Koruyucu Donanım**

Zimmet Listesi raporunun parametrik alan ekleme işleminin altyapı kurgusunun tasarlandığı kısımdır. Altyapı kurgusu için Alan Tanımlama ve Fonksiyon Dizanyer menüleri kullanılmaktadır. Ayrıca Sistem Altyapı Tanımları Modülünde Rapor format şablonu indirilerek ve indirilen rapor formatına tag ekleme işlemi yapılmış şablonun sisteme aynı isimde yüklenmesi için Rapor Formatları Düzenleme menüsüde kullanılmaktadır. Tanımlanan alan değerlerinin bilgisinin girilmesi için Tip tanımlama, KKD Tanımlama, Zimmet Verme Nedenler, Zimmet Kontrol Nedenleri ve Zimmet Alma Nedenleri menüleri kullanılmaktadır. Tanımlanan alan değerlerinin bilgisinin girilmesi için kullanılan menüler Entegre Yönetim Sistemi\> Kişisel Koruyucu Donanım \> Zimmet İşlemleri menüsünde bir Zimmet Ver, Zimmet Kontrol ve Zimmet Geri Al işlemlerin yapılmasında kullanılır.

### **1.1.1.1. Alan Tanımlama**

**Menü Adı**: Sistem Altyapı Tanımları/Kişisel Koruyucu Donanım/Alan Tanımlama

Fonksiyon Dizanyer menüsünde bulunan menülerin sayfalarında gösterilecek alanların tanımlama işlemi yapıldığı menüdür. Zimmet listesi Raporu için “**KKD Zimmet Ver**”, “**KKD Zimmet Kontrol**” ve “**KKD Zimmet Al**” fonksiyonları için alanlar tanımlanır. Bu alan parametrik alan tanımlamaları metin, numerik, liste, personel gibi parametrik alan tipleridir.

Fonksiyonlar için alanların tanımlanması:

“KKD Tanımı” metin tipli alan tanımlama işlemin yapılması;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb0cca038-ad49-4dcf-b752-16410eef798b)


Listeye “KKD Tanımı” metin tipli alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade8227446-198c-4f00-8205-f151ed68e853) (Yeni) butonu tıklanarak Alan Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadda2ce106-2b71-434d-b2ef-d3124b4bbdbe)

Alan tanımlama ekranında alan tipi alanında metin seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload75c9ae36-0987-4e7e-a07c-70a69a46c095) (Kaydet) butonu tıklanarak metin tipli alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6170311c-818e-42b2-a202-a3a36f835f5f)

“KKD Tipi” liste tipli alan tanımlama işlemin yapılması;

Listeye “KKD Tipi” liste tipli alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade8227446-198c-4f00-8205-f151ed68e853) (Yeni) butonu tıklanarak Alan Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload51c2a717-fdb0-4165-b462-323c4f1f0213)

Alan tanımlama ekranında Alan tipi alanında liste tipi seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload75c9ae36-0987-4e7e-a07c-70a69a46c095) (Kaydet) butonu tıklanarak liste tipli alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7c609921-e3fd-451c-8003-5ae1eef5fabf)

“KKD Tipi” liste tipli alanına değer eklemek için “KKD tipi” alanı seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddf181487-f5e4-490e-9fcc-f8858120191d) (Değerler) butonuna tıklanarak alanın değerlerinin tanıtılacağı ekrana gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7e3a6fed-bd0b-41f4-94e4-ec3f39fd8f26)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload20b8c36a-a0ec-4fac-ac84-c066fd06b7c8) : Yeni butonuna tıklanarak yeni değer tanımlama işlemine başlanılır. İstenirse ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload460317b3-9ced-4d67-a89d-c0c69f62369a)(Şablon İndir) ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload64a650a0-b7f7-45eb-84e3-5fff3277598b)(Şablon Yükle) butonları ile sisteme toplu olarak alan değerleri aktarılabilmektedir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload460317b3-9ced-4d67-a89d-c0c69f62369a)(Şablon indir) butonu ile sistem şablonu bilgisayara indirir. İlgili şablon kullanıcılar tarafından doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload64a650a0-b7f7-45eb-84e3-5fff3277598b)(şablon yükle) butonu ile sisteme yüklendiğinde şablondaki tüm alan değerleri sisteme aktarılmış olacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf887a6e5-088b-4959-ad9f-72b08e9a4511)

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload75c9ae36-0987-4e7e-a07c-70a69a46c095) (Kaydet) butonu tıklanarak değer tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload63135a54-b951-44ac-855d-4a4b51a7a3f2)

“KKD tipi” liste tipli alanın liste elemanları (değerleri) aynı şekilde tümü tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd0ec4f19-e265-4443-a2b3-d82590d03e6e)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4579abb2-0126-4420-afe1-99d6f2d8575b)

“KKD Sorumlusu” Personel tipli alan tanımlama işlemin yapılması;

Listeye “KKD Sorumlusu” Personel tipli alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade8227446-198c-4f00-8205-f151ed68e853) (Yeni) butonu tıklanarak Alan Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d63b59e-5a43-465f-9680-765b29d72235)

Alan tanımlama ekranında alan tipi alanında Personel seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload75c9ae36-0987-4e7e-a07c-70a69a46c095) (Kaydet) butonu tıklanarak Personel tipli alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload947cde43-ff90-4713-98c7-f9e89a5ab1af)

“KKD Sorumlusunun Departmanı ” Departman tipli alan tanımlama işlemin yapılması;

Listeye “KKD Sorumlusunun Departmanı” Departman tipli alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade8227446-198c-4f00-8205-f151ed68e853) (Yeni) butonu tıklanarak Alan Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload63bb59ba-5991-481c-9946-b316f4ff22da)

Alan tanımlama ekranında Alan tipi alanında “Departman” tipi seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload75c9ae36-0987-4e7e-a07c-70a69a46c095) (Kaydet) butonu tıklanarak “Departman” tipli alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb26e268a-26fc-452d-b353-6fbfc5c40a2b)

“KKD Verilme Saati” Saat tipli alan tanımlama işlemin yapılması;

Listeye “KKD Verilme Saati” saat tipli alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade8227446-198c-4f00-8205-f151ed68e853) (Yeni) butonu tıklanarak Alan Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5cad9bdc-aee4-4c4c-a94c-995f4435ce00)

Alan tanımlama ekranında Alan tipi alanında “Saat” tipi seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload75c9ae36-0987-4e7e-a07c-70a69a46c095) (Kaydet) butonu tıklanarak “Saat” tipli alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3bba4815-395b-4c7f-8676-fc72cabd0b03)

“KKD Detayı” Metin çok Satırlı tipli alan tanımlama işlemin yapılması;

Listeye “KKD Detayı” Metin Çok Satırlı tipli alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade8227446-198c-4f00-8205-f151ed68e853) (Yeni) butonu tıklanarak Alan Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0ad14cb0-8ece-47fc-895d-df7be0a19b2d)

Alan tanımlama ekranında Alan tipi alanında “Metin Çok Satırlı” tipi seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload75c9ae36-0987-4e7e-a07c-70a69a46c095) (Kaydet) butonu tıklanarak “Metin Çok Satırlı” tipli alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9b450558-112f-4c2c-8056-d85f796f4e8a)

“KKD Zimmet Ver”, “KKD Zimmet Kontrol” , “KKD Zimmet Al” fonksiyonları içinde KKD Sorumlusu, KKD Sorumlunun Departmanı ve KKD Detayı alanları ortak alanlar olarak Fonksiyon Dizanyer menüsünde kullanılacaktır.

### **1.1.1.2.Fonksiyon Dizayner**

**Menü Adı**: Sistem Altyapı Tanımları/KKD/ Fonksiyon Dizayner

Alan Tanımlama menüsünde rapor formatı şablona eklenecek alanların tanımlama işleminde sonra Sistem Altyapı Tanımları\>KKD\>Fonksiyon Dizanyer menüsü tıklanılır. Açılan fonksiyon Dizanyer ekranında tanımlanacak alanlarının eklenecek 4 fonksiyon bulunur. Bu fonksiyonlardan Zimmet Listesi Raporu için kullanılacak fonksiyonlar “KKD Zimmet Ver”, “KKD Zimmet Kontrol” ve “KKD Zimmet Al” fonksiyonlarıdır. Tanımlanan alanların Fonksiyon Dizanyer menüsünde bulunan bu fonksiyonları sayfaları ile ilişkilendirme işlemi bu menüde yapılır. Zimmet Listesi Raporu için bu 3 fonksiyon ile tanımlanan alanların fonksiyonun sayfalarıyla ilişkilendirilmesi yapılır. Tanımlanan alanların 3 fonksiyonu sayfalarıyla ile ilişkilendirmesi işleminde sonra Zimmet İşlemleri menüsünde Zimmet Verme, Zimmet Kontrol ve Zimmet Geri Al işlem aşamasındaki ekranlarda görüntülenmesi sağlanmış olur.

2 numaralı “KKD Zimmet Ver” fonksiyonu için tanımlanan alanların ilgili fonksiyonun sayfası ile ilişkilendirilmesi;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfda43ac0-36c9-4618-a5d9-10dd2b987ae5)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd3056414-60bb-4c03-a6e3-6ed9b9018c29): Alanlar butonuna tıklanarak alanların ilgili fonksiyonla ilişkilendirilme yapılacağı ekran açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadff0878eb-854f-4994-9e00-af7dd71a398a)

İlgili fonksiyonda kullanılacak alanlar ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade8227446-198c-4f00-8205-f151ed68e853)(Yeni) butonuna tıklanarak belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0e6d5d70-4630-44e0-bb29-43cac6f80b90)

Açılan ekranda alan bilgileri listeden seçilir, zorunlu bir alan ise kullanıcının bu alanı doldurmadığında karşısına çıkacak mesaj tanımlanır. Gerekli tüm alanlar doldurulduktan sonra ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc4fed3b4-019c-49da-bb60-7902ee74a34b) (Kaydet) butonu tıklanarak, ilgili alan için fonksiyon sayfalarıyla ile ilişkilendirme işlemi gerçekleştirilir. Gerekli olan tüm alanlar bu şekilde ilgili fonksiyona eklenir. Aşağıda görüldüğü üzere Alan No’nun yanında Alan Kodu bölümü vardır. Bu Zimmet Listesi raporuna bu alan düzenlemelerinde <VER_ALAN1\> vb. şekilde tagin raporun rapor formatı şablonuna eklenerek düzenleme yapılmasına imkan sağlayan koddur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb6a32d2e-4f04-4183-8321-20cdbfac2bd8)

İlgili fonksiyonda kullanılacak alanlar tümü aynı şekilde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade8227446-198c-4f00-8205-f151ed68e853)(Yeni) butonuna tıklanarak belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeaa80cef-e7d2-4c39-93e6-9c5377e73066)

“KKD Zimmet Ver” Fonksiyonunda liste, personel ve departman gibi liste tipli alanlarda örneğin “KKD tipi” liste tipli alan için <VER_ALAN2_ACK\> şeklinde tagi Zimmet Listesi raporunun rapor formatına eklenir.

3 numaralı “KKD Zimmet Kontrol” fonksiyonu için tanımlanan alanların ilgili fonksiyonun sayfası ile ilişkilendirilmesi;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload04c69c18-f238-4d33-b5c6-ff880ef8a11f)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd3056414-60bb-4c03-a6e3-6ed9b9018c29): Alanlar butonuna tıklanarak alanların ilgili fonksiyonla ilişkilendirilme yapılacağı ekran açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8ed48e31-548c-47c0-b4ee-3af3d5c571bd)

İlgili fonksiyonda kullanılacak alanlar ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade8227446-198c-4f00-8205-f151ed68e853)(Yeni) butonuna tıklanarak belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload89dba569-a72e-4a79-95ea-6e00bc2988c0)

Açılan ekranda alan bilgileri listeden seçilir, zorunlu bir alan ise kullanıcının bu alanı doldurmadığında karşısına çıkacak mesaj tanımlanır. Gerekli tüm alanlar doldurulduktan sonra ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc4fed3b4-019c-49da-bb60-7902ee74a34b) (Kaydet) butonu tıklanarak, ilgili alan için fonksiyonun sayfalarıyla ile ilişkilendirme işlemi gerçekleştirilir. Gerekli olan tüm alanlar bu şekilde ilgili fonksiyona eklenir. Aşağıda görüldüğü üzere Alan No’nun yanında Alan Kodu bölümü vardır. Bu Zimmet Listesi raporuna bu alan düzenlemelerinde <KON_ALAN6\> metin tipli parametrik alanlar için şekilde tagin raporun rapor formatı şablonuna eklenerek düzenleme yapılmasına imkan sağlayan koddur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfe1fbf15-e295-4908-be62-5d42764c13ca)

İlgili fonksiyonda kullanılacak alanlar tümü aynı şekilde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade8227446-198c-4f00-8205-f151ed68e853)(Yeni) butonuna tıklanarak belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload19551cbd-bb05-4c80-918d-b0b69e34fc94)

“KKD Zimmet Kontrol” Fonksiyonunda liste, personel ve departman gibi liste tipli alanlarda örneğin “KKD Sorumlusu” personel tipli alan için <KON_ALAN3_ACK\> şeklinde tagi Zimmet Listesi raporunun rapor formatına eklenir.

4 numaralı “KKD Zimmet Al” fonksiyonu için tanımlanan alanların ilgili fonksiyonun sayfası ile ilişkilendirilmesi;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload956e5ead-be14-480c-89a4-5a1ff21a7f56)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd3056414-60bb-4c03-a6e3-6ed9b9018c29): Alanlar butonuna tıklanarak alanların ilgili fonksiyonla ilişkilendirilme yapılacağı ekran açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd72c491a-27a4-4359-8fed-5929a8e24ba9)

İlgili fonksiyonda kullanılacak alanlar ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade8227446-198c-4f00-8205-f151ed68e853)(Yeni) butonuna tıklanarak belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf611319b-97b8-4fcb-b29d-528c0e225b74)

Açılan ekranda alan bilgileri listeden seçilir, zorunlu bir alan ise kullanıcının bu alanı doldurmadığında karşısına çıkacak mesaj tanımlanır. Gerekli tüm alanlar doldurulduktan sonra ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc4fed3b4-019c-49da-bb60-7902ee74a34b) (Kaydet) butonu tıklanarak, ilgili alan için fonksiyonun sayflarıyla ile ilişkilendirme işlemi gerçekleştirilir. Gerekli olan tüm alanlar bu şekilde ilgili fonksiyona eklenir. Aşağıda görüldüğü üzere Alan No’nun yanında Alan Kodu bölümü vardır. Bu Zimmet Listesi raporuna bu alan düzenlemelerinde <AL_ALAN6\> metin tipli parametrik alanlar için şekilde tagin raporun rapor formatı şablonuna eklenerek düzenleme yapılmasına imkan sağlayan koddur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1b6bf390-7807-4e19-8401-985197523ad2)

İlgili fonksiyonda kullanılacak alanlar tümü aynı şekilde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade8227446-198c-4f00-8205-f151ed68e853)(Yeni) butonuna tıklanarak belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4661a03c-fdf2-4b11-83fc-660d4a16e723)

“KKD Zimmet Al” Fonksiyonunda liste, personel ve departman gibi liste tipli alanlarda örneğin “KKD Sorumlusu” personel tipli alan için <AL_ALAN3_ACK\> şeklinde tagi Zimmet Listesi raporunun rapor formatına eklenir.

### **1.1.2.Zimmet Listesi Raporu Formatına Tag Eklenecek Alanların Değerlerin Girilmesi**

Zimmet Listesi Raporu formatına tag eklenecek alanların değerlerin girilmesi için Zimmet İşlemleri menüsünde “Zimmet Ver”, “Zimmet Kontrol” ve “Zimmet Geri Al” işlemleri yapılır. Alan Tanımlama menüsünde tanımlanan alanlar fonksiyon dizanyer menüsünde bu foksiyonları sayfalarıyla ilişkilendirildiği için Zimmet İşlemleri menüsünde Zimmet Ver, Zimmet Kontrol ve Zimmet Geri Al ekranlarında alan değerleri görüntülenir. Görüntülenen bu alan değerlerinin bilgisi girilir. Bu Zimmet İşlemleri menüsünde Zimmet Ver, Zimmet Kontrol ve Zimmet Geri Al işlemlerinin yapılması için öncelikle Sistem Altyapı tanımlarında altyapı kurgusunun yapılması gerekmektedir. Zimmet işlemlerin altyapı kurgusu için sistem altyapı tanımların kısmında Tip Tanımlama ,KKD Tanımlama, Zimmet Verme Nedenleri, Zimmet Kontrol Nedenleri ve Zimmet Geri Alma Nedenleri işlemlerinin yapılması gerekmektedir. Altyapısı kurgusu tanımlandıktan sonra Entegre Yönetim Sisteminde Zimmet İşlemleri gereçekleştirilir.

### **1.1.2.1.Entegre Yönetim Sistemi/Kişisel Koruyucu Donanım**

Sistem Altyapı Tanımları\> **Kişisel Koruyucu Donanım** kısmında altyapı kurgusu tanımlanan Zimmet İşlemlerinin gerçekleştirilme işlemin yapıldığı kısımdır.

#### **1.1.2.1.1.Zimmet İşlemleri**

**Menü Adı**: Entegre Yönetim Sistemi/Kişisel Koruyucu Donanım/ Zimmet İşlemleri

Bu menü ile çalışanların verilecek olan ve takibi yapılacak olan KKD’ lerin zimmet işlemleri yapılır. Personeller otomatik ekrana gelir. Zimmet verilecek personel seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade8227446-198c-4f00-8205-f151ed68e853) (Zimmet Ver) butonuna tıklanır ve KKD’ler verilir. Güncelle butonuyla kontrol işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d3bd7b8-e6d3-40bf-8049-9879a478d977)Zimmet verilecek Personel seçilerek yeni bir zimmet eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade8227446-198c-4f00-8205-f151ed68e853) (Zimmet Ver) butonu tıklanarak Zimmet Takibi/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2ecb5d4f-1a04-4428-b22a-53c834de1ea7)

Alan tanımlamada menüsünde tanımlanan ve Fonksiyon Dizanyer menüsünde KKD Zimmet Ver sayfası ile ilişkilendirilen parametrik alan tipleri görüntülenir. Görüntülenen bu parametrik alan tiplerinin bilgi girişleri yapılır. Bu parametrik alan tiplerinin tagleri daha sonra rapor formatına eklenerek rapora basılması sağlanacaktır. Zimmet ver sekmesinde gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload75c9ae36-0987-4e7e-a07c-70a69a46c095) (kaydet) butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9474c4a5-e788-44fb-909a-032890754535)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0c69a0d4-58f5-4cb7-8988-c70a84e2f5e6)(Geri) butonu tıklanarak ana ekrana dönülür. Ana ekrandaki ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3c8b06e6-2622-441b-8915-6cb36d7a681d) (Zimmet Kontrol) butonuyla seçili personel için kontrol işlemleri gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7a773963-a944-4066-a57a-f4f75d4dcc8e)

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3c8b06e6-2622-441b-8915-6cb36d7a681d) (Zimmet Kontrol) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd0a2345c-4320-4bb2-8807-52b469bf8ed6)

Alan tanımlamada menüsünde tanımlanan ve Fonksiyon Dizanyer menüsünde KKD Zimmet Kontrol sayfası ile ilişkilendirilen parametrik alan tipleri görüntülenir. Görüntülenen bu parametrik alan tiplerinin bilgi girişleri yapılır. Bu parametrik alan tiplerinin tagleri daha sonra rapor formatına eklenerek rapora basılması sağlanacaktır. Kontrol Nedeni seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc4fed3b4-019c-49da-bb60-7902ee74a34b) (kaydet) butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbfb1673c-d1de-4981-b2cc-a817369bca8f)

Ana ekrandaki ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c92ed13-1643-4c44-94a0-c3f63cbb1981) (Zimmet Geri Al) butonuyla seçili personel için zimmet geri alma işlemleri gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload75144169-2af7-4154-8d0f-bbe3a88babbd)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload33f73548-2fcc-4890-bd12-97f9564d7970)

Alan tanımlamada menüsünde tanımlanan ve Fonksiyon Dizanyer menüsünde KKD Zimmet Al sayfası ile ilişkilendirilen parametrik alan tipleri görüntülenir. Görüntülenen bu parametrik alan tiplerinin bilgi girişleri yapılır. Bu parametrik alan tiplerinin tagleri daha sonra rapor formatına eklenerek rapora basılması sağlanacaktır. Teslim nedeni bilgisi seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc4fed3b4-019c-49da-bb60-7902ee74a34b) (kaydet) butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload136ac212-c919-4212-afff-7064641afa5a)

### **1.2.3.Zimmet Listesi Raporun Rapor Formatına Tanımlanan Parametrik Alanların Taglerin Eklenmesi**

**Menü Adı**: Sistem Altyapı Tanımları/BSAT/ Konfigürasyon Ayarları/Rapor Formatları Düzenleme

Zimmet Listesi Raporu tanımlanan parametrik alanların taglerin eklenmesi için Sistem Altyapı Tanımları\>BSAT\> Konfigürasyon Ayarları\>Rapor Formatları Düzenleme menüsüne gidilir. Qdms tüm raporların yüklendiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload641443ad-4891-40f5-9d7d-4944273d6a77)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6d4c6b50-3b7e-4214-9aa5-c0bd3c829804) (Görüntüle) butonu tıklanarak Zimmet Listesi Raporunun rapor format şablonu (ZIMMET_LISTESI.xlsx) bilgisayara indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb9376823-6d5e-4612-ae9c-6075176ef7f9)

Alan Tanımlama tanımlanan alanlar Fonksiyon Dizanyer menüsünde ilgili sayfalarının ilişkilendirildikten sonra Fonksiyon Dizanyer da fonksiyonlar seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd3056414-60bb-4c03-a6e3-6ed9b9018c29)(Alanlar) butonun tıklatıldığına açılan alan kodları rapor formatında alan değerleri kısmına yazılarak eklenir.

2 Numaralı “KKD Zimmet Ver” Fonksiyonu için Zimmet Listesi Rapor Formatına Eklenecek Tagler;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeaa80cef-e7d2-4c39-93e6-9c5377e73066)

Rapor Formatına Fonksiyon Dizanyerdeki Alan kodları \<\> büyüktür ve küçüktür işaretleri arasına yazılır. Tag yazım şekli <VER_ALANX\> dir. Örneğin ALAN1 kodlu “KKD Tanımı” metin tipli parametrik alanı <VER_ALAN1\> şeklinde rapor format şablonu alan değeri kısmına yazılır. Liste, Personel gibi liste tipli alanlarda “ACK” eki ile birlikte tagi yazmak gerekiyor. Örneğin ALAN2 kodlu “KKD Tipi” liste tipli parametrik alanda <VER_ALAN2_ACK\> şeklinde tag’ini rapor formatına şablonuna yazmak gerekiyor.

“KKD Zimmet Ver” fonksiyonu için Fonksiyon Dizanyer menüsünde Alan tanımlamada tanımlanan alanlarının kodlarının tag şeklinde yazılmış şekli aşağıdaki tabloda yer almaktadır

| **Alan Adı**                 | **Alan Tipi**     | **Alan Kodu** | **Tag**           |
|------------------------------|-------------------|---------------|-------------------|
| KKD Tanımı                   | Metin             | ALAN1         | <VER_ALAN1\>     |
| KKD Tipi                     | Liste             | ALAN2         | <VER_ALAN2_ACK\> |
| KKD Sorumlusu                | Personel          | ALAN3         | <VER_ALAN3_ACK\> |
| KKD Sorumlusunun Departmanı  | Departman         | ALAN4         | <VER_ALAN4_ACK\> |
| KKD Verilme Saati            | Saat              | ALAN5         | <VER_ALAN5\>     |
| KKD Detayı                   | Metin Çoklu Satır | ALAN6         | <VER_ALAN6\>     |

3 Numaralı “KKD Zimmet Kontrol” Fonksiyonu için Zimmet Listesi Rapor Formatına Eklenecek Tagler;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload19551cbd-bb05-4c80-918d-b0b69e34fc94)

Rapor Formatına Fonksiyon Dizanyerdeki Alan kodları \<\> büyüktür ve küçüktür işaretleri arasına yazılır. Tag yazım şekli <KON_ALANX\> dir. Örneğin ALAN6 kodlu “KKD Detayı” metin tipli parametrik alanı <KON_ALAN6\> şeklinde rapor format şablonu alan değeri kısmına yazılır. Liste, Personel gibi liste tipli alanlarda “ACK” eki ile birlikte tagi yazmak gerekiyor. Örneğin ALAN3 kodlu “KKD sorumlusu” personel tipli parametrik alanda <KON_ALAN3_ACK\> şeklinde tag’ini rapor formatına şablonuna yazmak gerekiyor.

KKD Zimmet Kontrol fonksiyonu için Fonksiyon Dizanyer menüsünde Alan tanımlamada tanımlanan alanlarının kodlarının tag şeklinde yazılmış şekli aşağıdaki tabloda yer almaktadır.

| **Alan Adı**                 | **Alan Tipi**     | **Alan Kodu** | **Tag**           |
|------------------------------|-------------------|---------------|-------------------|
| KKD Detayı                   | Metin Çoklu Satır | ALAN6         | <KON_ALAN6\>     |
| KKD Sorumlusu                | Personel          | ALAN3         | <KON_ALAN3_ACK\> |
| KKD Sorumlusunun Departmanı  | Departman         | ALAN4         | <KON_ALAN4_ACK\> |

4 numaralı “KKD Zimmet Al” Fonksiyonu için Zimmet Listesi Rapor Formatına Eklenecek Tagler;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4661a03c-fdf2-4b11-83fc-660d4a16e723)

Rapor Formatına Fonksiyon Dizanyerdeki Alan kodları \<\> büyüktür ve küçüktür işaretleri arasına yazılır. Tag yazım şekli <AL_ALANX\> dir. Örneğin ALAN6 kodlu “KKD Detayı” metin tipli parametrik alanı <AL_ALAN6\> şeklinde rapor format şablonu alan değeri kısmına yazılır. Liste, Personel gibi liste tipli alanlarda “ACK” eki ile birlikte tagi yazmak gerekiyor. Örneğin ALAN3 kodlu “KKD sorumlusu” personel tipli parametrik alanda <AL_ALAN3_ACK\> şeklinde tag’ini rapor formatına şablonuna yazmak gerekiyor.

“KKD Zimmet Al” fonksiyonu için Fonksiyon Dizanyer menüsünde Alan tanımlamada tanımlanan alanlarının kodlarının tag şeklinde yazılmış şekli aşağıdaki tabloda yer almaktadır.

| **Alan Adı**                 | **Alan Tipi**     | **Alan Kodu** | **Tag**          |
|------------------------------|-------------------|---------------|------------------|
| KKD Detayı                   | Metin Çoklu Satır | ALAN6         | <AL_ALAN6\>     |
| KKD Sorumlusu                | Personel          | ALAN3         | <AL_ALAN3_ACK\> |
| KKD Sorumlusunun Departmanı  | Departman         | ALAN4         | <AL_ALAN4_ACK\> |

Fonksiyon dizanyerdeki fonksiyonların tablodaki parametrik alan tiplerinin alan tanımları ve tagleri ilgili bilgileri indirilen rapor format şablonuna yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada54feca6-216f-4334-9007-90612e380791)

Rapor formatına şablonuna alan tanımları ve taglerinin yazılımdan sonra rapor ZIMMET_LISTESI.xlsx aynı isimde formatı bilgisayara kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc135dea1-ba8c-4288-9583-ade87e16f8f4)

Bilgisayara kaydedilen aynı isimdeki Rapor format (ZIMMET_LISTESI.xlsx) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3e8c0d84-1b04-435c-aef6-7e9660a3ceaa) (Yeni) butonu ile tekrar rapor formatları düzenleme menüsünden sisteme yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeba38ff0-9cac-491c-8143-c3bd7e08b9f4)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1d8b006f-00a1-4666-99fc-fbeb911d469a)

Rapor Formatları Düzenleme menüsünde aynı isimde rapor format yükleme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload51bd976d-30d4-47f6-b422-c2e9de7174fe)

### **1.1.4. Zimmet Listesi Raporunun Rapor Formatına Eklenen Parametrik Alanların Gösterimi**

**Menü Adı**: Entegre Yönetim Sistemi\>Kişisel Koruyucu Donanım \>Raporlar\>Zimmet Listesi

Zimmet Listesi Raporunun rapor formatına (ZIMMET_LISTESI.xlsx) tag ekleme işlemi yapılan rapor format yükleme işleminde sonra Entegre Yönetim Sistemi\>Kişisel Koruyucu Donanım \>Raporlar\>Zimmet Listesi Raporu menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6ea2c09d-248a-4fe7-aeaa-f8cbb9601aa1)

Açılan Zimmet Takibi ekranında Liste ve Filtre sekmesi karşımıza çıkar. Arama kriterlerinde Zimmet Nedeni, Alma Nedeni ve Kontrol Nedeni alanlarındaki seçenekler seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload778b56a7-7ed1-4332-aaa3-b93ea052147e)(Ara) butonu tıklanılır. Zimmet verme, Zimmet Kontrol ve Zimmet Geri al ekranlarında veri tanımlanıp veri girişleri yapılan alanları rapora basılmasının görüntülenmesi için filtreleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb71af00c-56b9-4976-8a0a-4b860ff7e701)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload383c91e6-2cfd-4d84-a1b1-6c7d9ac402ab)

Liste sekmesinde seçili KKD üzerinden ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload59a1b3a4-4636-4df2-a2d3-dd12c490c796) (Excel’e Aktar) butonu tıklanılır. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload59a1b3a4-4636-4df2-a2d3-dd12c490c796) (Excel’e Aktar) butonu ile “Zimmet Listesi Raporu” Excel formatında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0dc4514b-6e0f-4c86-a9ab-c27366d3acea)

Alınan Zimmet Listesi Raporunun da Alan tanımlama menüsünde tanımlanan parametrik alan tiplerinin değerlerinin bilgisinin raporu geldiği ve şablona eklenen parametrik alan tiplerinin tag’lerinin çalıştığı görülür.

## **1.2. Kişisel Koruyucu Donanım Modülünde Zimmet Listesi Raporu Replacement (Kısa Kodlar) Tag Tablosu**

Kişisel Koruyucu Donanım Modülünde kullanılan Zimmet Listesi taglerin listesi aşağıdaki tabloda yer almaktadır.

| **Replacement (Kısa Kodlar)** | **Açıklaması**                 |
|-------------------------------|--------------------------------|
| <ID\>                        | ID Bilgisi                     |
| <ADI\>                       | KKD Adı Bilgisi                |
| <ADISOYADI\>                 | Personel Adı ve Soyadı Bilgisi |
| <ZIMMET_EDEN_ADISOYADI\>     | Zimmet Eden Adı Soyadı Bilgisi |
| <ZIMMET_TAR\>                | Zimmet Tarihi Bilgisi          |
| <ZIMMET_NEDENI\>             | Zimmet Nedeni Bilgisi          |
| <ZIMMET_NEDENLERI\>          | Zimmet Nedenleri Bilgisi       |
| <SON_KONTROL_TAR\>           | Son Kontrol Tarihi Bilgisi     |
| <KONTROL_ACIKLAMASI\>        | Kontrol Açıklaması Bilgisi     |
| <KONTROL_NEDENLERI\>         | Kontrol Nedenleri Bilgisi      |
| <SONRAKI_KONTROL_TAR\>       | Sonraki Kontrol Tarihi Bilgisi |
| <DURUMTEXT\>                 | Durum Bilgisi                  |
| <TESLIM_TARIHI\>             | Teslim Tarihi Bilgisi          |
| <TESLIM_NEDENI\>             | Teslim Nedeni Bilgisi          |
| <ALMA_NEDENLERI\>            | Alma Nedenleri Bilgisi         |
