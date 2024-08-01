---
title: Raporlara Parametrik Alan Ekleme İşlemi ve Genel Tag Listesi
description: Raporlara Parametrik Alan Ekleme İşlemi ve Genel Tag Listesi Kullanıcı Yardım Dokümanı
sidebar_position: 1
---


:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::


**Acil Durumlar Modülünde Raporlara Parametrik Alan Ekleme İşlemi ve Genel Tag Listesi Kullanıcı Yardım Dokümanı**


## **1. Acil Durumlar Modülünde Raporlara Parametrik Alan Ekleme İşlemi ve Raporlarda Kullanılan Taglar**

Acil Durumlar Modülünde raporlarına parametrik alan ekleme işlemi yapılmaktadır. Acil Durum Tatbikatları raporuna parametrik alan ekleme işlem basamakları ve bu module ilgili genel kullanılan taglerin (kısa kodların) listesi bu yardım dokümanında yer almaktadır.

## **1.1. Acil Durumlar Modülünde Parametrik Alan Tiplerinin Acil Durum Tatbikatları Raporunda Gösterimi**

Acil Durumlar Modülü raporlarından Acil Durum Tatbikatları raporuna eklenen parametrik alanların raporda gösterilme işlemi için öncelikle Sistem Altyapı Tanımları kısmında altyapı kurgusunun yapılması gerekmektedir. Altyapısını kurgulama işleminde Alan Tanımlama, Fonksiyon Dizanyer, Rapor Formatları Düzenleme ve Parametreler menüleri kullanılır. Alan tanımlamada Rapor formatı şablonuna taglerin eklenecek alanların tanımlama işlemi yapılır. Fonksiyon Dizanyer da tanımlanan bu alanların fonksiyonların sayfalarında görüntülenmesi için ilişkisi kurulur. Fonsiyon Dizanyer da fonksiyonun sayfası ile ilişkisi kurulan alanların Entegre Yöneti Sistemi\> Acil Durumlar \>Acil Durum Planları menüsünde İş Yeri Seçiniz ekranında İşyeri Listesinde İşyeri seçimi yapılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload816cb177-54fd-4f96-9a2d-cd685a309f24) (ileri) butonu tıklanılır. Açılan Acil Durum Ekipleri ekranında Tatbikatlar sekmesi tıklanılır. Açılan Acil Durum Tatbikatları ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload234d0b84-cf78-445e-9a72-3ca3854f681c)(Ekle) butonu ile yeni bir Tatbikat tanımlama işlemi yapılır. Acil Durum Tatbikatları ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload234d0b84-cf78-445e-9a72-3ca3854f681c)(Ekle) butonu tıklanarak Tatbikat tanımlanırken görüntülenen parametrik alan tiplerinin alan değerleri bilgisi girilir. Parametrik alan tiplerinin bilgi girişleri yapıldıktan sonra Rapor Formatları Düzenleme menüsüne gidilir. Rapor Formatların Düzenleme menüsünde Acil Durum Tatbikatları rapor formatı “AcilDurumTatbikatlari.xls” indirilir. İndirilenen “AcilDurumTatbikatlari.xls” rapor format şoblonuna Alan Tanımlama menüsünde tanımlanan parametrik alanların tag’leri Fonksiyon Dizanyer menüsünde tanımlı alan kodları bakılarak yazılır. Alan kodlarının “Acil Durum Tatbikatı Tanımlama” fonksiyon için hangi parametrik alan tipine göre taglerinin yazım şekli aşağıdaki tabloda yer almaktadır.

| **Fonksiyon No** | **Fonksiyon**                  | **Alan Tipi**                     | **Alan Kodu** | **Tag**        |
|------------------|--------------------------------|-----------------------------------|---------------|----------------|
| 1                | Acil Durum Ekibi Tanımlama     | Metin, Metin Çok Satırlı gibi     | ALAN3         | <ALAN3\>      |
| 1                | Acil Durum Ekibi Tanımlama     | Liste, Personel gibi liste tipli  | ALAN4         | <ALAN4_ACK \> |
| 3                | Acil Durum Tatbikatı Tanımlama | Metin, Metin Çok Satırlı gibi     | ALAN3         | <ALAN3\>      |
| 3                | Acil Durum Tatbikatı Tanımlama | Liste, Personel gibi liste tipli  | ALAN4         | <ALAN4_ACK \> |

3 numaralı “Acil Durum Tatbikatı Tanımlama” fonksiyon için; Örneğin Metin tipli parametrik alan Fonksiyon Dizanyerde alan kodu ALAN3 ise rapor formatına eklenecek tag şekli <ALAN3\> şeklinde olmalıdır. <ALAN KODU\> şeklinde Fonksiyon Dizanyerde menüsündeki Alan kodları \<\> büyüktür ve küçüktür işaretleri arasına yazılacak şeklinde rapor format şablonuna yazılmalıdır. Liste, Personel, departman gibi liste tipli parametrik alan tiplerinde tagleri için “ACK” eki eklenir. Örneğin liste tipli bir alanın Fonksiyon Dizanyer menüsündeki alan kodu ALAN4 ise Alan tag’i <ALAN4_ACK\> şeklinde rapor format şablonu eklenmelidir. <ALAN KODU_ACK\> şeklinde Fonksiyon Dizanyerde menüsündeki Alan kodları \<\> büyüktür ve küçüktür işaretleri arasına “ACK” eki eklenerek yazılacak şeklinde rapor format şablonuna yazılmalıdır. Rapor formatına şablonuna parametrik alanların tag şeklinde yazıldıktan sonra Rapor format “AcilDurumTatbikatlari.xls” aynı isimde bilgisayara kaydedilir. Kaydedilen aynı isimde Acil Durum Tatbikatları raporunu formatı Rapor Formatları Düzenleme menüsünde tekrar sisteme yüklenir. Rapor Formatları Düzenleme menüsünde yüklenen rapor format şablonun adı ve uzantısı ile birlikte kopyalanarak parametreler menüsündeki Acil Durumlar parametrelerinde 19 numaralı “Acil Durum Tatbikat Raporu şablon dosyası” parametresine sağ tıkla/yapıştır işlemi ile tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd967b18c-cb4c-43a0-954f-11f9757e2994)



Acil Durum Tatbikatları raporunun rapor formatının şablonun parametreye tanımlama işleminde sonra Entegre Yönetim Sistemi\> Acil Durumlar \>Raporlar\> Acil Durum Tatbikatları Raporu menüsüne gidilir. Açılan Acil Durum Tatbikatları Raporu ekranında filtre sekmesinde arama kriterlerinden İş yeri alanında İş yeri listesinde tatbikatın yapıldığı İş yeri seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload32f95325-3b0d-423b-ad39-34b1a7937518)(Ara) butonu tıklanılır. Listeden tanımlanan Tatbikat seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddcee3dc5-a053-4d13-9c05-84ffe2a9def2)(Excel Aktar) butonu tıklanılır. Excel formatın alınan raporda parametrik alanların taglerinin bulunduğu kısımda girilen Acil Durum Tatbikatları tanımlama ekranında alan bilgilerinin geldiği ve taglerin çalıştığı görülür.

**Acil Durumlar Modülünde parametrelerindeki raporlar:**

Acil Durumlar Modülün hangi fonksiyon için hangi rapor format şablonun hangi parametreye tanımlanacağı bilgisi aşağıdaki tabloda mevcuttur.

| **Fonksiyon No** | **Fonksiyon**                   | **Rapor Formatı Şablon Adı** | **İlgili Parametre No** | **İlgili Parametre Tanımı**                |
|------------------|---------------------------------|------------------------------|-------------------------|--------------------------------------------|
| 1                | Acil Durum Ekibi Tanımlama      | AcilDurumEkipleri.xls        | 18                      | Acil Durum Ekipleri Raporu şablon dosyası  |
| 3                | Acil Durum Tatbikatı Tanımlama  | AcilDurumTatbikatlari.xls    | 19                      | Acil Durum Tatbikatı Raporu şablon dosyası |
| 3                | Acil Durum Tatbikatı Tanımlama  | AcilDurumTatbikatlari.xls    | 29                      | Acil Durum Tatbikatı pdf şablonu           |

Acil Durumlar Yönetimi Modülünde alan tanımlamada tanımlanan alanların Fonksiyon Dizanyerdeki fonksiyonun sayfalarıyla ilişkilendirildikten sonra alan kodları tabloda belirtilen Rapor Formatları şablonlarına taglerin ekleme işlemi yapılır. Tag ekleme işleminden sonra Rapor Formatları düzenleme menüsünde sisteme yükleme işlemi yapılır. Sisteme yükleme işleminden sonra Rapor formatları düzenleme menüsünde adı ve uzantısı kopyalarak tabloda belirtilen ilgili parametreye tanımlama işlemleri yapılır.

“Acil Durum Tatbikatları raporu” parametrik alanları Fonksiyon Dizayner menüsünden 3 numaralı “Acil Durum Tatbikatı Tanımlama” fonksiyonu seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4e37216-f3de-4341-a8dc-72ecb01fcf87)(Alanlar ) butonuna basıldığı zaman gelen alan kodlarına göre belirlenir.

### **1.1.1.Sistem Altyapı Tanımları/ Acil Durumlar**

Acil Durum Tatbikatları raporunun parametrik alan ekleme işleminin altyapı kurgusunun tasarlandığı kısımdır. Altyapı kurgusu için Alan Tanımlama ve Fonksiyon Dizanyer menüleri kullanılmaktadır. Ayrıca Sistem Altyapı Tanımları Modülünde Rapor format şablonu indirilerek ve indirilen rapor formatına tag ekleme işlemi yapılmış rapor formatının şablonun sisteme aynı isimde yüklenmesi için Rapor Formatları Düzenleme menüsüde kullanılmaktadır. Sisteme yüklenen Acil Durum Tatbikatları raporunun Sistem Altyapı Tanımları\>BSAT\>Konfigürasyon Ayarları\>Parametreler menüsünde ilgili parametreye tanımlama işlemi aynı modülün ilgili parametresinde yapılır. Acil Durumlar parametrelerinde 19 numaralı “Acil Durum Tatbikatı Raporu şablon dosyası” parametresine tanımlama işlemi yapılır. Tanımlanan alan değerlerinin girilmesi için modülün Sistem Altyapı Tanımları kısmında Acil Durum Tipleri ve Acil Durum Ekip Tipi menüleri kullanılmaktadır. Tanımlanan alan değerlerinin girilmesi için kullanılan altyapıdaki menüler Entegre Yönetim Sistemi\> Acil Durumlar\>Acil Durum Planları menüsünde Tatbikatlar sekmesi tıklanarak açılan Acil Durum Tatbikatları ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload234d0b84-cf78-445e-9a72-3ca3854f681c)(Ekle) butonu ile yeni bir Tatbikat tanımlama işlemlerin yapılmasında kullanılır. Acil Durum Tatbikatları Raporu için Acil Durum Planları menüsünde Tatbikatlar sekmesi tıklanarak açılan Acil Durum Tatbikatları ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload234d0b84-cf78-445e-9a72-3ca3854f681c)(Ekle) butonu ile yeni bir Tatbikat tanımlamada görüntülenen alanların değerlerinin girilip, rapora basılması sağlanacaktır.

#### **1.1.1.1. Alan Tanımlama**

**Menü Adı**: Sistem Altyapı Tanımları/ Acil Durumlar /Alan Tanımlama

Fonksiyon Dizanyer menüsünde bulunan menülerin sayfalarında gösterilecek alanların tanımlama işlemi yapıldığı menüdür. Acil Durum Tatbikatları Raporu için 3 numaralı “Acil Durum Tatbikatı Tanımlama” fonksiyonları için alanlar tanımlanır. Bu parametrik alan tanımlamaları metin, numerik, liste, personel gibi parametrik alan tipleridir.

**“Acil Durum Tatbikatı Tanımlama**” **Fonksiyonu için Alan Tanımlaması:**

Fonksiyon için alan tanımlama işlemi için Sistem Altyapı Tanımları/ Acil Durumlar /Alan Tanımlama menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfb9b66ae-c8af-4f00-8ab9-4f19dbd63fff)

“Tatbikat Türü” liste tipli alan tanımlama işlemin yapılması;

Listeye “Tatbikat Türü liste tipli alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload234d0b84-cf78-445e-9a72-3ca3854f681c) (Yeni) butonu tıklanarak Alan Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7e076e6a-c63d-4429-9119-d5d841efd647)

Alan tanımlama ekranında Alan tipi alanında liste tipi seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7e63b796-d808-4ade-bcaf-afc38132353f) (Kaydet) butonu tıklanarak liste tipli alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6bbebe6b-8e11-4633-b393-1bc0c362a692)

“Tatbikat Türü” liste tipli alanına değer eklemek için “Tatbikat Türü” alanı seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload35303ed1-0725-46d0-959c-9058c9a5e21f) (Değerler) butonuna tıklanarak alanın değerlerinin tanıtılacağı ekrana gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4435f8dc-6cd7-4796-91ab-36eddd52cc69)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb10f3ad7-e58f-4c4d-a139-9a0b6b0cdc7f) : Yeni butonuna tıklanarak yeni değer tanımlama işlemine başlanılır. İstenirse ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeb332e6f-2d4a-4969-b5ab-4b98495d9f3e)(Şablon İndir) ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2cbac848-2d46-4b18-bb4f-dd4bffe18d78)(Şablon Yükle) butonları ile sisteme toplu olarak alan değerleri aktarılabilmektedir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeb332e6f-2d4a-4969-b5ab-4b98495d9f3e)(Şablon indir) butonu ile sistem şablonu bilgisayara indirir. İlgili şablon kullanıcılar tarafından doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2cbac848-2d46-4b18-bb4f-dd4bffe18d78)(şablon yükle) butonu ile sisteme yüklendiğinde şablondaki tüm alan değerleri sisteme aktarılmış olacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1a7c2efa-996a-4438-ae93-fd8bee3e8b39)

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7e63b796-d808-4ade-bcaf-afc38132353f) (Kaydet) butonu tıklanarak değer tanımlama işlemi gerçekleştirilir. “Tatbikat Türü” liste tipli alanın liste elemanları (değerleri) aynı şekilde tümü tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6388dde0-2b59-4eb9-b746-4d39b725d516)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload298888de-78c5-40d9-89cb-11f64b553c92)(Geri) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf2177931-e2e4-47d1-94e0-f6f0ca5f6644)

“Alarmın (veriliyorsa) Türü” liste tipli alan tanımlama işlemin yapılması;

Listeye “Alarmın (veriliyorsa) Türü” liste tipli alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload234d0b84-cf78-445e-9a72-3ca3854f681c) (Yeni) butonu tıklanarak Alan Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4786f7f5-47a0-41a3-87e3-d98cbfc950ea)

Alan tanımlama ekranında Alan tipi alanında liste tipi seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7e63b796-d808-4ade-bcaf-afc38132353f) (Kaydet) butonu tıklanarak liste tipli alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada78583f6-3e04-48a7-bbd3-7e523c38ef81)

“Alarmın (veriliyorsa) Türü” liste tipli alanına değer eklemek için “Alarmın (veriliyorsa) Türü” alanı seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload35303ed1-0725-46d0-959c-9058c9a5e21f) (Değerler) butonuna tıklanarak alanın değerlerinin tanıtılacağı ekrana gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload808846ed-80e3-4399-b308-732e33562951)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb10f3ad7-e58f-4c4d-a139-9a0b6b0cdc7f) : Yeni butonuna tıklanarak yeni değer tanımlama işlemine başlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc14fa501-1ed5-4e61-911f-f10523d8ab6f)

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7e63b796-d808-4ade-bcaf-afc38132353f) (Kaydet) butonu tıklanarak değer tanımlama işlemi gerçekleştirilir. “Alarmın (veriliyorsa) Türü” liste tipli alanın liste elemanları (değerleri) aynı şekilde tümü tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload38e93c01-8bed-4290-b4ea-2c5b93aaf720)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload298888de-78c5-40d9-89cb-11f64b553c92)(Geri) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload66238e9e-ef5e-4917-a072-bb386ddcca4c)

“Tatbikat Lideri” Personel tipli alan tanımlama işlemin yapılması;

Listeye “Tatbikat Lideri” Personel tipli alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload234d0b84-cf78-445e-9a72-3ca3854f681c) (Yeni) butonu tıklanarak Alan Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade2a84396-5c92-4af9-9b82-45223eac17cc)

Alan tanımlama ekranında alan tipi alanında Personel seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7e63b796-d808-4ade-bcaf-afc38132353f) (Kaydet) butonu tıklanarak Personel tipli alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload44860119-c6d5-449f-a9f7-f17f5dbee311)

“Tatbikatın Yapıldığı Departmanlar ” departman tipli alan tanımlama işlemin yapılması;

Listeye “Tatbikatın Yapıldığı Departmanlar” departman tipli alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload234d0b84-cf78-445e-9a72-3ca3854f681c) (Yeni) butonu tıklanarak Alan Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf9e7298e-bc90-46e4-9654-259306f7e489)

Alan tanımlama ekranında Alan tipi alanında “Departman” tipi seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7e63b796-d808-4ade-bcaf-afc38132353f) (Kaydet) butonu tıklanarak “Departman” tipli alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada789df4f-e1fb-4291-adcc-26ef1c279642)

“Senaryo” metin çok satırlı tipli alan tanımlama işlemin yapılması;

Listeye “Senaryo” metin çok satırlı tipli alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload234d0b84-cf78-445e-9a72-3ca3854f681c) (Yeni) butonu tıklanarak Alan Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload22194123-dc45-40b0-b39f-31c76bf30e19)

Alan tanımlama ekranında alan tipi alanında metin çok satırlı seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7e63b796-d808-4ade-bcaf-afc38132353f) (Kaydet) butonu tıklanarak metin çok satırlı tipli alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadab4c7530-8209-4970-a9f3-4b3598f45b8f)

“Tatbikatın Genel Sonucu” metin tipli alan tanımlama işlemin yapılması;

Listeye “Tatbikatın Genel Sonucu” metin tipli alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload234d0b84-cf78-445e-9a72-3ca3854f681c) (Yeni) butonu tıklanarak Alan Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc6b1c8ae-57ec-4b89-8cd7-2376ba3e954d)

Alan tanımlama ekranında alan tipi alanında metin seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7e63b796-d808-4ade-bcaf-afc38132353f) (Kaydet) butonu tıklanarak metin tipli alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5e2d920c-b623-4b88-996d-f2a5ea9aa0e8)

#### **1.1.1.2.Fonksiyon Dizayner**

**Menü Adı**: Sistem Altyapı Tanımları/ Acil Durumlar / Fonksiyon Dizayner

Alan Tanımlama menüsünde rapor formatı şablona eklenecek alanların tanımlama işleminde sonra Sistem Altyapı Tanımları/Acil Durumlar/Fonksiyon Dizanyer menüsü tıklanılır. Açılan Fonksiyon Dizanyer ekranında tanımlanacak alanlarının eklenecek 3 fonksiyon bulunur. Bu fonksiyonlardan Acil Durum Tatbikatları Raporu için kullanılacak fonksiyon 3 numaralı “Acil Durum Tatbikatı Tanımlama” fonksiyonudur. Tanımlanan alanların Fonksiyon Dizanyer menüsünde bulunan bu fonksiyonun sayfası ile ilişkilendirme işlemi bu menüde yapılır. Acil Durum Tatbikatları Raporu için tanımlanan alanların fonksiyonun sayfası ilişkilendirilmesi yapılır. Tanımlanan alanların 3 numaralı fonksiyonu sayfası ile ilişkilendirmesi işleminde sonra bir Acil Durum Planları menüsünde Tatbikatlar sekmesi tıklanarak açılan Acil Durum Tatbikatları ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload234d0b84-cf78-445e-9a72-3ca3854f681c)(Ekle) butonu ile Tatbikat Tanımlama işlem aşamasındaki ekranlarda görüntülenmesi sağlanmış olur.

3 numaralı “Acil Durum Tatbikatı Tanımlama” fonksiyonu için tanımlanan alanların ilgili fonksiyonun sayfası ile ilişkilendirilmesi;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cd10c9e-f776-447b-8c7b-8ecc03bce9e1)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4e37216-f3de-4341-a8dc-72ecb01fcf87): Alanlar butonuna tıklanarak alanların ilgili fonksiyonla ilişkilendirilme yapılacağı ekran açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload52274ae9-7cec-40b6-a0fa-4f423eb3807a)

İlgili fonksiyonda kullanılacak alanlar ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload234d0b84-cf78-445e-9a72-3ca3854f681c)(Yeni) butonuna tıklanarak belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2102caa6-766e-439d-9e9c-cf435f21abed) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload31eca3e1-05aa-4dfe-a372-eca62a1a899a)

Açılan ekranda alan bilgileri listeden seçilir, zorunlu bir alan ise kullanıcının bu alanı doldurmadığında karşısına çıkacak mesaj tanımlanır. Tanımlanan alanın görüleceği Aktif statü, Görünür statü ve zorunlu statü durumlaraı belirlenir. Gerekli tüm alanlar doldurulduktan sonra ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2d906d37-f26f-41b6-8052-28a12c8cfe90) (Kaydet) butonu tıklanarak, ilgili alan için fonksiyon sayfalarıyla ile ilişkilendirme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload98ec625a-40d9-41a9-976d-a3403e5425da)

İlgili fonksiyonda kullanılacak alanlar tümü aynı şekilde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload234d0b84-cf78-445e-9a72-3ca3854f681c)(Yeni) butonuna tıklanarak belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb4f552dd-c1d9-41e4-9103-6c0b6d3666a5)

Fonksiyon Dizanyer menüsünde “Acil Durum Tatbikatı Tanımlama” fonksiyonunda liste, personel ve departman gibi liste tipli alanlarda örneğin “Tatbikat Türü” gibi liste tipli alan için

<ALAN1_ACK\> şeklinde tagi Acil Durum Tatbikatları raporunun rapor formatına eklenir. Metin, metin çok satırlı alanlar için örneğin “Senoryo” gibi metin çok satırlı alan için \<ALAN5\> şeklinde tagi Acil Durum Tatbikatları raporunun rapor formatına eklenir.

### **1.1.2. Acil Durum Tatbikatları Raporu Formatına Tag Eklenecek Alanların Değerlerin Girilmesi**

Acil Durum Tatbikatları Raporu formatına tag eklenecek alanların değerlerin girilmesi için Acil Durum Planları menüsünde yeni bir Acil Durum Planı tanımlama işlemi yapılır. Acil Durum Planları menüsünde iş yeri seçiniz ekranında Acil Durum Planın gereçkleştirilecek iş yeri seçimi yapılır. İş Yeri seçimi işleminden sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload669f816f-d1e6-4a37-bc49-f1b2bcbe87f0)(ileri) butonu tıklanılır. Açılan Acil Durumlar Ekipler ekranında Tatbikatlar sekmesi tıklanır. Açılan Acil Durum Tatbikatları ekranın ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload234d0b84-cf78-445e-9a72-3ca3854f681c)(Ekle) butonu ile yeni bir Tatbikat tanımlama işlemi yapılır. Alan Tanımlama menüsünde tanımlanan alanlar Fonksiyon Dizanyer menüsünde bu fonksiyonun sayfası ile ilişkilendirildiği için Acil Durum Planları gerçekleştirmede Tatbikatlar sekmesinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload234d0b84-cf78-445e-9a72-3ca3854f681c)(Ekle) butonu tıklanarak Tatbikat tanımlanırken Tatbikat tanımlama ekranlarında alan değerleri görüntülenir. Görüntülenen bu alan değerlerinin bilgisi girilir. Yeni bir tatbikat tanımlama işlemi gerçekleştirmede Sistem Altyapı Tanımlarında altyapı kurgusunun yapılması gerekmektedir. Yeni bir tatbikat tanımlama işleminin gerçekleştirme altyapı kurgusu için Sistem Altyapı Tanımların kısmında Acil Durum Tipleri ve Acil Durum Ekip Tipi işlemlerinin yapılması gerekmektedir. Altyapısı kurgusu tanımlandıktan sonra Entegre Yönetim Sisteminde Acil Durum Planları menüsünde İş yeri listesinde işyeri seçimi yapılır. Acil Durumlar Ekipler ekranında Tatbikatlar sekmesi ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload234d0b84-cf78-445e-9a72-3ca3854f681c)(ekle) butonu ile Tatbikat tanımlama işlemide gerçekleştirilir.

#### **1.1.2.1.Entegre Yönetim Sistemi/ Acil Durum Planları**

Sistem Altyapı Tanımları/ Acil Durumlar kısmında altyapı kurgusu tanımlanan modülün Acil Durum Planları menüsünde Tatbikatlar sekmesinde Tatbikat tanımlama işlemlerinin gerçekleştirilme işlemin yapıldığı kısımdır. Acil Durumlar Ekipler ekranında Tatbikatlar sekmesinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload234d0b84-cf78-445e-9a72-3ca3854f681c) (Ekle) butonu tıklanarak Tatbikat tanımlama işlemi yapılarak bu tanımlama ekranındaki alan değerlerinin girilmesi sağlanılır.

##### **1.1.2.1.1.Acil Durum Planları**

**Menü Adı:** Entegre Yönetim Sistemi/ Acil Durumlar/ Acil Durum Planları

İş yeri bazında acil durum ekiplerinin oluşturulup tatbikatların planlandığı menüdür. Açılan ekranda iş yerleri ağaç kırılımı şeklinde listelenmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada45cc904-660f-471d-995b-f3b1809da31a)

İşlem yapılacak iş yeri seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload669f816f-d1e6-4a37-bc49-f1b2bcbe87f0)(İleri) butonuna tıklanır. Bu ekranda üç farklı sekme bulunur. Ekipler, Krokiler ve Tatbikatlar sekmesidir. Ekipler sekmesi tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload23bda887-25a7-4f5b-987f-b738eccf6d10)

Yeni bir ekip eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0005c93e-5eb9-4101-a2a3-e38f437bcc33) (Ekle) butonu tıklanarak Acil Durum Ekip Tanımlama/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload42c41fb4-8e0e-4f90-9a12-8d418aaac05a)

Açılan ekranda acil durum ekibinin ekip tipi sistemde tanımlı olan Acil Ekip Tipi listesinden seçilir. Acil durum ekibinin statü bilgisi, revizyon no, revizyon tarihi sistem tarafından verilir. Bu alan sistemde tanımlı olan personel listesinden seçilir. Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7e63b796-d808-4ade-bcaf-afc38132353f) (Kaydet) butonu tıklanarak acil durum ekipleri tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload020c98dc-caa2-48c5-ae60-9e535d351806)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0c2ac09e-1a50-4d66-8be5-b4a5f64b356f)(Ekip Üyesi Ekle) butonu ile acil durumlar ekibine ekip üyesi eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcc2899a4-2c03-4680-adb7-fb68b5d41d5a)

Yeni bir ekip üyesi eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0005c93e-5eb9-4101-a2a3-e38f437bcc33) (Ekle) butonu tıklanarak Acil Durum Ekibi Tanımlama/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb8a08336-b11c-43ee-a217-09c62dd1fd85)

Açılan ekranda personel sistemde tanımlı olan personel listesinden seçilir. Seçilen personeli görev tanımı tanımlı olan Görevlerden seçilir. Örneğin başkan, yardımcı, ekip üyesi gibi. görevlendirmesi yapılan personelin görev tanımı bilgisi girilir. Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7e63b796-d808-4ade-bcaf-afc38132353f) (kaydet) butonu tıklanarak acil durum ekibi tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc8e6d0fb-ed1c-48b8-957e-374e9f42d4f9)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0005c93e-5eb9-4101-a2a3-e38f437bcc33) (Ekle) butonu tıklanarak tüm ekip üyeleri aynı şekilde tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0d5cb047-0e88-41c9-80c1-f01fdf6d15be)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1db7ff34-b2bb-4dbd-adf9-119f6990a43f)

Firmada kullanılacak tüm ekip tipleri bu şekilde kaydedilir. Ekipler oluşturulduktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec63d4e1-a3c6-429b-b115-786c8a2a3939) (Onaya Gönder) butonu ile onaya gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3c1a1f60-eeb7-4487-93b2-5f54a9837344)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6f57c327-9607-4b7f-9590-b48ca6d09b08)

Bekleyen işlerime **“Oluşturma Onayı Bekleyen Acil Durum Ekipleri”** olarak iş düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadad6e80f2-8881-4616-877e-d75083498fb4)

Acil durum ekibinin ilgili kodu tıklanarak Acil Durumu Ekibi Onaylama ekranına gelinerek acil durum ekibi onaylanır veya reddedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8236eaed-367b-4980-bee7-8a4a40aae76c)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf36ee5ab-3f33-4ae5-a5a0-93aeedc22660)Onayla butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb45f97e9-0969-48fd-9e6e-077a053aa47b)

Onaylanan acil durum ekip listesi kişiye mail olarak iletilir ve “**Bekleyen İşlerim**” menüsünde **“Görev Aldığım Acil Durum Ekipleri”** olarak görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload38e81e9e-8203-49f9-92e9-d1bb7e271b50)

Ekip tanımlama işleminden sonra Acil Durum Ekipleri ekranında Tatbikatlar sekmeleri tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc226fa55-8dd3-46a4-88e5-27cf82c0e39f)

Yeni bir tatbikat eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0005c93e-5eb9-4101-a2a3-e38f437bcc33) (Ekle) butonu tıklanarak Tatbikat sekmesi/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade906376c-0825-42fb-a17d-f44142af2a45) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadef074078-312b-4037-8833-b445413e200f)

Alan tanımlamada menüsünde tanımlanan ve Fonksiyon Dizanyer menüsünde Acil Durum Tatbikat tanımlama sayfası ile ilişkilendirilen parametrik alan tipleri görüntülenir. Görüntülenen bu parametrik alan tiplerinin bilgi girişleri yapılır. Bu parametrik alan tiplerinin tagleri daha sonra rapor formatına eklenerek rapora basılması sağlanacaktır. Acil Durum Tatbikatı Tanımlama ekranında gerekli tüm alanlar doldurulduktan sonra ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3a8d7408-d474-472b-8115-235ae69863ac) (Onaya Gönder) butonu tıklanarak, Tatbikat tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload165c7ff2-ee8d-4080-bdc9-fa4cf12a1438)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada2e3a547-39fd-4143-bfe1-674ae5a83e31)

Onaya giden tatbikat Bekleyen İşlerime “**Tamamlanması Gereken Tatbikatlar”** olarak görev düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4afcf54a-07d8-4ae6-b12a-6200496b33ec)

İlgili tatbikat kodu tıklanarak tatbikat onaylanır ya da reddedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload62c25ce7-291c-486e-b998-3598156eee6a)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload22cff248-eb62-4222-ad25-46cd17f23aab)(Onayla) butonu tıklanarak Acil Durum Tatbikatı Tamamlama ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload01ef499a-02c5-4565-a3a3-2c40a41381db)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload22cff248-eb62-4222-ad25-46cd17f23aab)(Onayla) butonu tıklanarak acil durum tatbikatı tamamlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload72c8e928-ea9f-40b7-83ee-4c29f21cf45f)

### **1.2.3. Acil Durum Tatbikatları Raporun Rapor Formatına Tanımlanan Parametrik Alanların Taglerin Eklenmesi**

**Menü Adı**: Sistem Altyapı Tanımları/BSAT/ Konfigürasyon Ayarları/Rapor Formatları Düzenleme

Acil Durum Tatbikatları Raporu tanımlanan parametrik alanların taglerin eklenmesi için Sistem Altyapı Tanımları\>BSAT\> Konfigürasyon Ayarları\>Rapor Formatları Düzenleme menüsüne gidilir. Qdms tüm raporların yüklendiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc96876ff-32d0-450f-a9e2-86c68182fb07)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8d5bd883-5abc-44a8-a1b4-d6eac9e18975) (Görüntüle) butonu tıklanarak Acil Durum Tatbikatları Raporunun rapor format şablonu (AcilDurumTatbikatlari.xls) bilgisayara indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade74174a0-bfcb-420e-9517-08c8fff96773)

Alan Tanımlama tanımlanan alanlar Fonksiyon Dizanyer menüsünde ilgili sayfalarının ilişkilendirildikten sonra Fonksiyon Dizanyer da fonksiyonun seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4e37216-f3de-4341-a8dc-72ecb01fcf87)(Alanlar) butonun tıklatıldığına açılan alan kodları rapor formatında alan değerleri kısmına yazılarak eklenir.

**3 Numaralı “Acil Durum Tatbikat Tanımlama” Fonksiyonu için Acil Durum Tatbikatları Rapor Formatına Eklenecek Tagler;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcd3986e2-da27-4a0a-9268-752f7d1858c5)

Rapor Formatına Fonksiyon Dizanyerdeki Alan kodları \<\> büyüktür ve küçüktür işaretleri arasına yazılır. Tag yazım şekli metin tipli alanlar için <ALANX\> ve liste tipli alanlar için <ALANX_ACK\> şeklindedir. Örneğin ALAN5 kodlu “Senaryo” metin tipli parametrik alanı <ALAN5\> şeklinde rapor format şablonu alan değeri kısmına yazılır. Liste, Personel gibi liste tipli alanlarda “ACK” eki ile birlikte tagi yazmak gerekiyor. Örneğin ALAN1 kodlu “Tatbikat Türü” liste tipli parametrik alanda <ALAN1_ACK\> şeklinde tag’ini rapor formatına şablonuna yazmak gerekiyor.

“Acil Durum Tatbikatı Tanımlama” fonksiyonu için Fonksiyon Dizanyer menüsünde Alan tanımlamada tanımlanan alanlarının kodlarının tag şeklinde yazılmış şekli aşağıdaki tabloda yer almaktadır.

| **Alan Adı**                      | **Alan Tipi**     | **Alan Kodu** | **Tag**       |
|-----------------------------------|-------------------|---------------|---------------|
| Tatbikat Türü                     | Liste             | ALAN1         | <ALAN1_ACK\> |
| Alarmın(veriliyorsa) Türü         | Liste             | ALAN2         | <ALAN2_ACK\> |
| Tatbikat Lideri                   | Personel          | ALAN3         | <ALAN3_ACK\> |
| Tatbikatın Yapıldığı Departmanlar | Departman         | ALAN4         | <ALAN4_ACK\> |
| Senaryo                           | Metin Çok Satırlı | ALAN5         | <ALAN5\>     |
| Tatbikatın Genel Sonucu           | Metin             | ALAN6         | <ALAN6\>     |

Fonksiyon Dizanyerdeki fonksiyonların tablodaki parametrik alan tiplerinin alan tanımları ve tagleri ilgili bilgileri indirilen rapor format şablonuna yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload35645227-e8c7-4dde-8a4b-0977e05ff953)

Rapor formatına şablonuna alan tanımları ve taglerinin yazılımdan sonra rapor “AcilDurumTatbikatlari.xls” aynı isimde formatı bilgisayara kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7dcda5e5-7868-4cdc-9715-d2b1907b7e0d)

Bilgisayara kaydedilen aynı isimdeki Rapor format (AcilDurumTatbikatlari.xls) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7f529701-5c7b-43af-983a-7d072b289a53) (Yeni) butonu ile tekrar rapor formatları düzenleme menüsünden sisteme yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload38dc7ad0-f8e2-4bf0-ba72-e8a9dadda402)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc3bda4de-1c93-4aca-a349-fd45b00a9d58)

Rapor Formatları Düzenleme menüsünde aynı isimde rapor format yükleme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload443cde04-9851-4c5c-a215-77610000af22)

Rapor Formatları Düzenleme menüsünde sisteme yüklenen Rapor Formatının adı ve uzantısı ile birlikte sağ tıkla/kopyala yöntemi ile kopyalanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1ad4a1d5-926e-4de8-92cd-08e4bdef9668)

Sistem Altyapı Tanımları/BSAT/Konfigürasyon Ayarları/Parametreler menüsüne gidilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload84d8c815-5975-4172-9cc7-a71ba8e734d9)

Filtre sekmesinde modül olarak Acil Durumlar modülü seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6d753abe-afb2-4679-9983-8a60d0d23bde)(Ara) butonu tıklanılır. Acil Durumlar Parametreleri liste sekmesinde listelenir. Acil Durumlar modülü parametrelerinede 19 numaralı “Acil Durum Tatbikat Raporu Şablon Dosyası” parametresi seçilerek ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5e8fd18d-5da5-4f20-83da-bf3b933ed7ee)(Değiştir) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload33b03313-a4de-4181-9781-575c8b10db90)

Parametrenin içeriği görüntülenerek Rapor formatları Düzenleme menüsünde sisteme yüklenen rapor format şablonun adı ve uzantısı ile birlikte kopyalanan Rapor formatı şablonu parametre değerine sağ tıkla/yapıştır yöntemi ile yapıştırılarak tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload677510ca-0707-4e54-bab5-910844ef459c)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6d7e5fc8-0fc8-45dc-8db0-b6dae8c09e0e)

Rapor format şablon dosyası ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7e63b796-d808-4ade-bcaf-afc38132353f)(kaydet) butonu tıklanarak parametre değerine tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadded6f0c5-4bc0-4570-afd5-60bd763fa1b6)

### **1.1.4. Acil Durum Tatbikat Raporunun Rapor Formatına Eklenen Parametrik Alanların Gösterimi**

Acil Durum Tatbikat Raporunun rapor formatına (AcilDurumTatbikatlari.xls) tag ekleme işlemi yapılıp, Rapor Formatların Düzenleme menüsünde sisteme yüklenip ve 19 numaralı parametreye tanımlama işlemlerinden sonra Entegre Yönetim Sistemi/ Acil Durumlar /Raporlar/ Acil Durum Tatbikat Raporu menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6d3644c1-8e8d-48e5-8899-4725c29f29e7)

Açılan Acil Durum Tatbikatları ekranında Liste ve Filtre sekmesi karşımıza çıkar. Arama kriterlerinde İş yeri alanına Tanımlanan tatbikatın gerçekleştiği İş yeri listesinde İş yeri bilgisi seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload32f95325-3b0d-423b-ad39-34b1a7937518)( ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload13618182-d6a4-4d44-9e1e-62e18ce1082b)

Liste sekmesinde tanımlama işlemi yapılan Tatbikat seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddcee3dc5-a053-4d13-9c05-84ffe2a9def2)(Excel Aktar)butonu tıklnılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade1ba3bde-3361-47dd-a23f-344b315e67b1)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf21e2691-6c0a-4ed4-9a39-706e4d71c86f)

Alınan Excel formatından Acil Durum Tatbikatları raporununda Alan tanımlama menüsünde tanımlanan parametrik alan tiplerinin değerlerinin bilgisinin raporu geldiği ve şablona eklenen parametrik alan tiplerinin tag’lerinin çalıştığı görülür.

## **1.2. Acil Durumlar Modülünde Genel Replacement (Kısa Kodlar) Tag Tablosu**

Acil Durumlar Modülünde kullanılan Genel taglerin listesi aşağıdaki tabloda yer almaktadır.

| **Replacement (Kısa Kodlar)** | **Açıklaması**                    |
|-------------------------------|-----------------------------------|
| <EKIP_TIPI\>                 | Ekip Tipi Bilgisi                 |
| <ISYERI\>                    | İş Yeri Bilgisi                   |
| <REVIZYON_NO\>               | Revizyon No Bilgisi               |
| <REVIZYON_TARIHI\>           | Revizyon Tarihi Bilgisi           |
| <SON_GOZ_GEC_TARIHI\>        | Son Gözden Geçirme Tarihi Bilgisi |
| <STATU\>                     | Statü Bilgisi                     |
| <TATBIKAT_KODU\>             | Tatbikat Kodu Bilgisi             |
| <TATBIKAT_ADI\>              | Tatbikat Adı Bilgisi              |
| <DURUM_TIP_KODU\>            | Acil Durum Tip Kodu Bilgisi       |
| <DURUM_TIP_ADI\>             | Acil Durum Tip Adı Bilgisi        |
| <SORUMLU_ADI\>               | Sorumlu Adı Bilgisi               |
| <SORUMLU_SOYADI\>            | Sorumlu Soyadı Bilgisi            |
| <TATBIKAT_YERI\>             | Tatbikat Yeri Bilgisi             |
| <TATBIKAT_TARIHI\>           | Tatbikat Tarihi Bilgisi           |
| <TATBIKAT_SURESI\>           | Tatbikat Süresi Bilgisi           |
| <TATBIKAT_ACIKLAMA\>         | Tatbikat Açıklaması Bilgisi       |


