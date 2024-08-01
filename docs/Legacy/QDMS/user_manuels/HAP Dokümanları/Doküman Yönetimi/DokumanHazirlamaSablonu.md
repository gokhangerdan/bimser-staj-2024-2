---
title: Doküman Hazırlama Şablonu Oluşturma
description: Doküman Hazırlama Şablonu Oluşturma Yardım Dokümanı
sidebar_position: 1
---


:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::

**Doküman Yönetimi Modülünde Doküman Hazırlama Şablonu Oluşturma Yardım Dokümanı**


## **1.Doküman Yönetimi Modülü**

Doküman yönetimi modülü, standartlara uygun olarak doküman yönetim sürecini sağlayan bir modüldür. Yönetim sistemleri dokümantasyonunun Qdms sistemi üzerinde onay sürecinden geçirilerek hazırlanmasını, kontrol edilmesini, onaylanmasını, revize edilmesini, yayınlanarak elektronik ortamda ilgili personellere dağıtılmasını, raporlanmasını ve tüm dokümantasyonun arşivlenmesini ve iptal sürecinin yürütülmesini sağlar. Personellerin yetkili oldukları klasörler/ dokümanlar kapsamında dokümanlara ulaşıp, dokümanlar üzerinde işlem yapmasına olanak sağlar.

## **1.1.Sistem Altyapı Tanımları/ Doküman İşlemleri**

### **1.1.1.Doküman Hazırlama Şablonu Oluşturma**

Firmanın yönetim sistemleri kapsamında doküman hazırlamak için kullandığı Doküman hazırlama şablonları Qdms’te kullanılabilir. Doküman hazırlama şablonunda alt bilgi/ üst bilgi kısmında bulunan “doküman kodu, doküman adı, hazırlanma tarihi, revizyon no, revizyon tarihi, ilk yayın tarihi, hazırlayan, kontrol eden, onaylayan” gibi bilgilerin Qdms’te doküman hazırlanırken girilen bilgilerden şablona otomatik olarak gelmesi sağlanabilir. Bunun için firma Doküman hazırlama şablonunun Qdms Doküman kısa kodları ile işaretlenmesi gerekir.

Doküman Yönetimi Modülünde Doküman hazırlama şablonu oluşturmada kullanılan kısa kodlar aşağıdaki tablonda yer almaktadır. Kısaca Doküman kısaltma tablosu adı da denilebilir. Doküman hazırlama şablonu hazırlanırken bu kısa kodlar kullanılır. Örneğin; Doküman Kodu alanın bilgi girişinde **<DOC_KODU\>** doküman kısaltması kullanılacaktır. Dokümanın adı alanın bilgi girişinde **<DOC_ADI\>** doküman kısaltması kullanılacaktır. Şablonun içerisinde hangi alanın bilgi girişi kullanılacaksa ilgili doküman kısaltmaları yerleştirilerek alt bilgi ve üst bilgi kısmı oluşturuluyor. Firmanın Doküman hazırlama şablonu sistemde oluşturularak firma yeni bir doküman hazırlarken bu şablonun kullanılmasını sağlanarak standart bir yapıda bir doküman hazırlamasını işlemini gerçekleştirir.

| **Doküman Yönetimi Modülü Doküman Hazırlama Şablonunda kullanılanan Kısa Kodlarının Listesi** |                                                               |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| **Kısaltma**                                                                                  | **Açıklaması**                                                |
| **<DOC_KODU\>**                                                                              | DokümanKodu                                                   |
| **<DOC_TIPI\>**                                                                              | DokumanTipi                                                   |
| **<REV_NO\>**                                                                                | Revizyon No                                                   |
| **<DOC_ADI\>**                                                                               | Doküman Adı                                                   |
| **<DOC_GRUP_KODU\>**                                                                         | DokümanGrupKodu                                               |
| **<DOC_GRUP_ADI\>**                                                                          | Doküman GrupAdı                                               |
| **<DOC_HAZ_TAR\>**                                                                           | Hazırlanma Tarihi                                             |
| **<HAZ_SICIL\>**                                                                             | Hazırlayan Sicil                                              |
| **<HAZ_POZ\>**                                                                               | HazırlayanPozisyonKodu                                        |
| **<HAZ_POZ_TAN\>**                                                                           | HazırlayanPosizyonTanımı                                      |
| **<HAZIRLAYAN\>**                                                                            | HazırlayanınAdıSoyadı                                         |
| **<KONT_SICIL\>**                                                                            | KontrolEden SicilNo                                           |
| **<KONT_POZ\>**                                                                              | KontrolEden PozisyonKodu                                      |
| **<KONT_POZ_TAN\>**                                                                          | KontrolEdenPozisyonTanımı                                     |
| **<KONTROL_EDEN\>**                                                                          | KontrolEdeninAdıSoyadı                                        |
| **<SORUMLU_SICIL\>**                                                                         | Sorumlu SicilNo                                               |
| **<SORUMLU_POZ\>**                                                                           | SorumluPozisyonKodu                                           |
| **<SORUMLU_POZ_TAN\>**                                                                       | SorumluPozisyonTanımı                                         |
| **<SORUMLU\>**                                                                               | SorumlununAdıSoyadı                                           |
| **<SOR_KISIM_KODU\>**                                                                        | SorumluDepartmanKodu                                          |
| **<SORUMLU_KISIM\>**                                                                         | SorumluDepartman                                              |
| **<REV_SICIL\>**                                                                             | RevizeEdenSicilNo                                             |
| **<REV_POZ\>**                                                                               | RevizeEdenPozisyonKodu                                        |
| **<REV_POZ_TAN\>**                                                                           | RevizeEdenePozisyonTanımı                                     |
| **<REVIZE_EDEN\>**                                                                           | RevizeEdenAdıSoyadı                                           |
| **<REV_TARIHI\>**                                                                            | RevizyonTarihi                                                |
| **<REV_NEDEN\>**                                                                             | RevizyonNedeni                                                |
| **<ONAY_TAR\>**                                                                              | Onay Tarihi                                                   |
| **<SON_ONAY_SICIL\>**                                                                        | Son Onaycı Sicili                                             |
| **<SON_ONAY_POZ\>**                                                                          | Son Onaycı Pozisyon Kodu                                      |
| **<SON_ONAY_POZ_TAN\>**                                                                      | Son Onaycı Pozisyon Tanımı                                    |
| **<SON_ONAY\>**                                                                              | Son Onaycı adı soyadı                                         |
| **<TUM_ONAY_SICIL\>**                                                                        | Tüm Onaycıların sicili                                        |
| **<TUM_ONAY_POZ\>**                                                                          | Tüm Onaycıların Pozisyonu                                     |
| **<TUM_ONAY_POZ_TAN\>**                                                                      | Tüm onaycıların pozisyon tanımları                            |
| **<TUM_ONAY_ADI\>**                                                                          | Tüm Onaycıları adı soyadı                                     |
| **<YAYIMLAYAN_SICIL\>**                                                                      | Yayımlayan sicili                                             |
| **<YAYIMLAYAN_POZ\>**                                                                        | Yayımlayan pozisyon kodu                                      |
| **<YAYIMLAYAN_POZ_TAN\>**                                                                    | Yayımlayan pozisyon tanımı                                    |
| **<YAYIMLAYAN\>**                                                                            | Yayımlayan adı soyadı                                         |
| **<YONETIM_SISTEMLERI\>**                                                                    | YönetimSistemleri                                             |
| **<REFERANS_DOKUMANLAR\>**                                                                   | ReferansDokümanlar                                            |
| **<GRUP_EGITICI\>**                                                                          | Eğitmen                                                       |
| **<X_ONAY_ADI\>**                                                                            | X. Onaylayanın Adı (X=1,2,3...)                               |
| **<X_ONAY_SCL\>**                                                                            | X. Onaylayanın Sicili(X=1,2,3...)                             |
| **<X_ONAY_POZ\>**                                                                            | X. Onaylayanın Pozisyon Kodu(X=1,2,3...)                      |
| **<X_ONAY_POZ_TAN\>**                                                                        | X. Onaylayanın Pozisyon Tanımı(X=1,2,3...)                    |
| **<PRN_KK\>**                                                                                | Kontrollü Kopya Parametresi(QDMS-GEN-29,30 nolu parametreler) |
| **<P_SICIL\>**                                                                               | Print Alan Sicil                                              |
| **<P_ADI\>**                                                                                 | Print Alan Personel Adı                                       |
| **<P_TARIH\>**                                                                               | Print Alınan Tarih(gg.aa.yyyy)                                |
| **<P_UTARIH\>**                                                                              | Print Alınan Tarih (gg.aa.yyyy ss:dd:nn)                      |
| **<DOC_TIPI\>**                                                                              | Doküman Tipi                                                  |
| **<KONTROL_DEPARTMAN_ADI\>**                                                                 | Kontrol eden kişinin Departmanı                               |
| **<ONAYLAYAN_DEPARTMAN_ADI\>**                                                               | Son Onaycının Departmanı                                      |
| **<REVIZYON\>**                                                                              | Revizyon                                                      |
| **<KONTROL_TAR\>**                                                                           | Kontrol tarihi                                                |
| **<REV_EDEN_DEPARTMAN\>**                                                                    | Revize Edenin Departmanı                                      |
| **<SURECLER\>**                                                                              | Dokumanın bağlı olduğu süreçler                               |
| **<X_ID\>,<X_DATE\>,<X_APPROVAL\>,** **<X_REASON\>,<X_REVISION\>**                       | Revizyon Tarihçesi X=1,2,3..                                  |
| **<ON_KONT_EDEN\>**                                                                          | Ön Kontrol eden ad soyad                                      |
| **<ON_KONT_POZ_TAN\>**                                                                       | Ön kontrol eden pozisyon tanımı                               |

Firmaya ait bir Doküman hazırlama şablonu olmadığında durumda firmanın Prosedürleri ya da Talimatlar dokümanları alınıp içeriğindeki bilgiler boşaltılıp alt ve üst başlık kısımların şablon hazırlamadaki işlemler uygulanarak bir Doküman hazırlama şablonu yapısı standart bir şekilde hazırlanılabilir. Doküman hazırlama şablonun doküman hazırlarken kullanılmaktaki amaç hazırladığımız dokümanın standart bir yapıda oluşmasının sağlamaktır. Örnekte bir Doküman hazırlama şablonu yer almaktadır. Bu Doküman hazırlama şablonunda Doküman kısaltma tablosundaki kısaltmalar kullanılmıştır. Bu kullanıcı yardım dokümanında Doküman Yönetimi Modülünde sisteme Doküman hazırlama şablonu nasıl tanıtılır, tanıtılan Doküman hazırlama şablonları klasörlere nasıl atanır ve tanıtılan Doküman hazırlama şablonu ile bir Doküman hazırlama işlemi gerçekleşme aşamaları anlatılacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddd2fd786-025e-4143-8ec4-d535c6602a08)

### **1.1.2.Doküman Yönetimi Modülünde Sisteme Doküman Hazırlama şablonun atanması işlemi**

Doküman Yönetimi Modülünde sisteme Doküman hazırlama şablonun atanması işlemi Doküman Sisteme Aktarım menüsü ile oluşturulan şablon uygun bir klasör içerisine (örneğin; Şablonlar klasörü) kontrolsüz/ onaysız olarak, “Doküman Türü: Form/ Doküman Şablonu” seçilerek yüklenir.

### **1.1.3.Doküman Sisteme Aktarım**

**Menü Adı**: Sistem Altyapı Tanımları/ Doküman İşlemleri/ Doküman Sisteme Aktarım

Daha önce onay ve dağıtım süreçlerini tamamlamış olan dokümanların, sistemde onay ve kontrole gitmeden hızlıca sisteme dahil edilebildiği menüdür. Doküman Hazırlama menüsünden tek farkı onay mekanizmalarının olmamasıdır. Doküman Sisteme Aktarımı sistem yöneticileri tarafından kullanılmaktadır. Bu menu yardımıyla Doküman hazırlama şablonu kontrol/Onaysız olarak Doküman türü alanında Doküman Türü Form seçilerek ilgili seçenek Doküman Şablonu check box işaretlenerek sisteme yüklenilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcc055930-1521-47e8-bd87-ce0a17e366ae)

Açılan ekranda dokümanın aktarılacağı klasör seçilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf7d26375-885b-4ecb-977c-4d7fc21e1328) (İleri) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload76e089ca-638f-4b4a-bea7-c9df3080503a)

Doküman bilgileri sekmesinde Doküman adı, dokümanın Hazırlama tarihi gibi detaya bilgiler girilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload71442d8d-f134-4e62-a247-cf5013157913)

Diğer bilgiler sekmesinde sisteme yükleceğimiz dokümanın türü Doküman ve Form seçeneklerinde ilgili check box işaretlenilerek belirlenir. Sisteme yükleceğimiz Doküman hazırlama şablonu olduğu için doküman Türü Form seçilir. Form kullanım seçeneklerinden Doküman hazırlama şablonu bir şablon olduğu için Doküman şablonu ile ilgili check box işaretlenir. Doküman hazırlama şablonun bir doküman şablon olduğu belirtildikten sonra Doküman sekmesi tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0374ce12-30e5-4a32-ae20-fa449233cdb7)

Sisteme tüm bilgiler girildikten sonra “Doküman Dosyası Yükleme (Türkçe)” alanından ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7ff00301-90aa-4b92-93d3-5ce8bd983d87) (Dosya Ekle) butonu ile doküman içeriye aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4f2fbfd-fa71-4719-831d-5655ebbf6ed2)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload93efdb31-90c9-4e46-96ef-2340198ac09b)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1ca6d5dc-a4da-4fe3-9c9d-dcfbcb3552d8)

Doküman bilgileri ekranındaki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8095e73c-7e20-4e92-b6a7-1116feda98d4) (Kaydet) butonu yardımıyla Doküman hazırlama şablonu sisteme aktarma işlemi tamamlanmış olup Doküman Yönetimi Modülünde Doküman Hazırlama şablonu tanıtılma işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade3861110-81b4-409b-81ed-26b8180be92b)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9c319650-5838-4b08-a591-a39e3bf7a03f)

Sisteme Aktarım işlemi yapılan Doküman Hazırlama Şablonun sisteme yüklendiği görüntülemek için Doküman Görme menüsüne gidilir.

## **1.2.Entegre Yönetim Sistemi/ Doküman İşlemleri**

### **1.2.1.Doküman Görme**

**Menü Adı**: Entegre Yönetim Sistemi/ Doküman işlemleri/ Doküman Görme

Yayınlanmış olan bütün dokümanların görüntülendiği menüdür. Doküman görüntüleme yetkisi olan personeller/ kullanıcı grupları ilgili dokümanı görüntüleyebilirler. Doküman sisteme Aktarma menüsü ile yüklediğimiz Doküman Hazırlama Şablonu bu menüde görüntüleme işlemini gerçekleştireceğiz. Doküman Görme menüsü açıldığı zaman, sol tarafta klasör ağacı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06dfe9c0-e213-4e45-9c99-ee6cdf77a648)

Doküman Görme ekranındaki “Doküman Arama” sekmesinde, dokümanlar arasında istenen kriterlere göre filtreleme yapılarak arama işlemi gerçekleştirilir. Doküman arama sekmesinde Doküman türü alanında Form ilgilli check box işaretlenerek seçeneği seçilir. Seçilen Form seçeneğinden sonra Form kullanım şekli alanında Doküman hazırlama şablonumuz bir şablon olduğu için Doküman şablonu check box işaretlenir. Dokümanımız yüklediğimiz Klasörü Bağlı olduğu Klasör alanında Doküman Klasör Seç Listesinde bağlı olduğu klasör seçerek istenen kritere göre arama işlemini ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3a2e18af-c371-4285-a11c-f45826fe5b29)(ara) butonu tıklayarak gerçekleştiririz.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadde3200bd-294d-43d8-bafe-9efd4cd99a08)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1fd9c912-8019-4172-9029-44ebba1cbb22)

Doküman Görme menüsünde sisteme yüklenen Doküman hazırlama Şablonu kodu tıklarak içeriğinin görüntülenmesi sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf2f96d46-c28c-4656-b741-01dd62c92784)

Doküman görme menüsünde sisteme yüklenen Doküman hazırlanan şablonunda kısa kodların çalışmamadığı ekran görüntüsünde görülmüştür. Bu kısa kodların çalışmama sebebi bu şablon kullanılarak henüz bir Doküman Hazırlama menüsünde doküman hazırlama işlemi yapılmamıştır.

### **1.2.2.Doküman Yönetimi Modülünde Doküman Hazırlama Şablonun Klasör atanması işlemi**

Doküman Hazırlama Şablonun Klasörlere atanması işleminin gerçekleştirilmesi için Klasör Tanımlama menüsünde yeni bir klasör tanımlama ya da sistemde tanımlı bir klasörün güncelleme işlemi yapılarak açılan ekranda Klasör bilgileri sekmesinde Doküman Hazırlama şablonu alanın sisteme yüklenen Doküman Hazırlama şablonun eklenmesi ile klasöre atanması işlemi yapılır.

### **1.2.3.Klasör Tanımlama**

**Menü Adı: Entegre Yönetim Sistemi/ Doküman İşlemleri/ Klasör Tanımlama**

Qdms’te ki dokümanların yönetileceği klasörlerin oluşturulduğu ve düzenlendiği menüdür. Klasör Tanımlama ekranında öncelikle klasör ağaç yapısına karar verilmesi gerekmektedir. Organizasyon yapısına, süreçlere, doküman tiplerine, yönetim sistemlerine, departmanlara ya da firmanın uygun gördüğü yapıya göre klasör ağaç yapısı oluşturulur. Doküman hazırlama şablonu doküman hazırlamada hangi klasör için kullanılacaksa, klasör tanımlama ekranında tanımlanan, uygun klasör ile eşleştirilir. Doküman hazırlama şablonu eşleştirilecek ilgili klasör seçilip, değiştir butonu ile açılır. “Klasör ayarları/ doküman hazırlama şablonu” alanından uygun doküman hazırlama şablonu seçilir ve klasör bilgileri sekmesinden kaydedilir. Böylece; işlem yapılan bu klasörün içerisine bir doküman hazırlarken, eşleştirilen bu doküman hazırlama şablonu kullanılabilir. Firma prosedür, talimat, el kitabı gibi her doküman tipi için farklı şablon kullanabileceği gibi, tek bir şablon da kullanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbe46c0ed-e268-4179-89e2-7661c655a13c)

Klasör Tanımlama ekranındaki “0-Entegre Yönetim Sistemi” adlı klasör, sistemde tanımlı olarak bulunur. Bu klasörün altına firmanın kullandığı klasör yapısı kurulur. Klasör Tanımlama ekranına yeni bir klasör eklemek için “0-Entegre Yönetim Sistemi” klasörü seçili iken, ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade88ef1ce-75d5-425b-9363-ad8eaf6f64db) (Yeni) butonuna tıklanarak, Klasör Tanımlama/ Yeni Kayıt ekranı açılır. Firmanın klasör yapısı, Ağaç kırılımı şeklinde sistemde istenildiği detayda tanımlanabilir. Sisteme Yeni butonu tıklanarak Klasör Tanımlama-Yeni Kayıt ekranında Klasör Ayarları sekmesinde Doküman hazırlama şablonu alanında daha önceden Qdms’ e şablon olarak yüklenmiş olan Doküman hazırlama şablonlarından hangisi veya hangilerinin, bu klasöre bağlı olarak doküman hazırlarken kullanılabileceğini sisteme Doküman Seç Listesinde seçilerek belirtilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5142d8fa-ebef-4ef7-b6be-a7664678ece4)

Sistemde tanımladığımız Ana Klasör Bimser Genel klasörü ve alt klasörlerin olan Şablonlar klasörüne bir Doküman hazırlama şablonu tanımlama işlemin gerçekleştirilmesi için ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadda4e197b-327f-4e1b-884a-715ee44d0046)(Değiştir) butonu tıklanarak yapılmaktadır. Daha önceden sisteme Klasör Tanımlama işlemi yapıldığı için seçili olan klasör ile ilgili bilgiler düzenlenme işlemi yapılarak tanıtılan şablonların klasörlere atanma işlemi gerçekleştirilecektir. Yeni bir Klasör tanımlama aşamasında işlem basamakları aynı şekilde yapılmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload300ac6b9-2de5-4152-9d5b-e08b512b2a7a)

Klasör Tanımlama menüsünde Doküman hazırlama şablonu tanıtılması işlemi için yapılacak Klasör seçilir. Klasör seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadda4e197b-327f-4e1b-884a-715ee44d0046)(Değiştir) butonu tıklanılırak Klasör Tanımlama-Kayıt Güncelleme ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec380c85-3459-45ff-a385-26b857ed2fb5)

Klasör Tanımlama-Kayıt Güncelleme ekranında ilk sekmede tanımlı olan klasörün Klasör bilgileri görüntülenir. Doküman Hazırlama Şablonu klasörde tanımlama işlemi için ilk olarak Klasör Ayarları sekmesi tıklanır. Doküman hazırlama şablonu alanı kısmına gelinir. Doküman hazırlama şablonu alanında daha önceden Qdms’ e şablon olarak yüklenmiş olan doküman hazırlama şablonlarından hangisi veya hangilerinin, bu klasöre bağlı olarak doküman hazırlarken kullanılabileceğini belirtmek için kullanılır. Klasöre bağlı hazırlanacak dokümanlarda “bu şablonu kullan” demek için bu özellik kullanılmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload42d1f9d4-3922-40e3-86c2-7f5ef19feea5)

Klasör Ayarları sekmesinde Doküman Hazırlama Şablonu alanında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade9a63138-011c-47bd-8fc3-ab6cf428046f)(ekle) butonu tıklanılır. Açılan sistemde tanımlı Doküman Seçme Listesinde sisteme yüklenen Doküman Hazırlama Şablonu ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbe49fe16-b911-4b25-8f01-3484ecc2c8f7) (Seç) butonu yardımıyla seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc3b3c187-eb1f-40cc-936a-6a21ed181114)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload613c6854-7aad-484d-b422-996892eb9ba7)

Doküman Hazırlama Şablonu alanında ilgili Doküman hazırlama şablonu ile Klasör bilgileri sekmesine gelip ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8095e73c-7e20-4e92-b6a7-1116feda98d4)(Kaydet) butonu tıklanarak Doküman hazırlama şablonu Klasörle ilişkilendirilir. Klasörle ilişkilendirilen bu Doküman hazırlama şablonu ile bu Klasörde bir doküman hazırlanırken doküman Hazırlama menüsünde bu şablon baz alınarak Doküman Hazırlama işlemi yapılacaktır. Doküman Hazırlama işleminde şablonla ilişkilendirilen Klasörde yapıldığında Kısa kodlar da Doküman Hazırlama İşlemi bittikten sonra çalışır duruma gelecektir. Şablonun Kısa kodlarının çalıştığı görmek için Doküman Hazırlama menüsünde Şablon ilişkisi kurulan Klsörde doküman Hazırlama işlemini Onaysız ve Kontrolsuz bir şekilde yapıldığını göstermek için Klasör Ayarları sekmesinde Onaysız/Kontrolsüz ilgili check box işaretlenir. Onay ve Kontrol aşaması olmadan sistemde bir dokümanın Doküman Hazırlama menüsünde şablon kullanarak hazırlanması işlemi gerçekleştirilecektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadab15e87a-c153-4fc4-8724-43d0ecc5f55d)

### **1.2.4.Doküman Hazırlama Süreci**

Menü Adı: Entegre Yönetim Sistemi/ Doküman İşlemleri/ Doküman Hazırlama

Yönetim sistemleri kapsamında yeni bir doküman hazırlamak için “Doküman Hazırlama” menüsü kullanılır. Personelin klasör üzerinde doküman hazırlayabilmesi için, klasör yetki matrisi sekmesinde kullanıcı grubu ya da pozisyon olarak tanımlı olması ve doküman hazırlama yetkisinin de atanmış olması gerekir. Personel, yetkisi olmayan klasörde doküman hazırlayamaz, “Bu klasöre doküman hazırlama yetkiniz yoktur” uyarısı alır. Bu yüzden klasör yetki matrisinin doğru bir şekilde oluşturulması önemlidir. Yeni bir doküman hazırlamak için “Doküman Hazırlama” menüsü açılır. Klasör ağaç yapısından doküman hazırlanmak istenilen klasör seçilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbe32d65b-0190-4fb2-b1c2-9f85bf2ab59d) (İleri) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload29ea7e53-88e5-4fbe-acd4-e7a272b7bf0e)

Doküman Bilgileri sekmesinde, dokümana ait temel bilgiler tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6a54cca9-ff5e-410a-98dd-2268939faf74)

Doküman Türü seçili seçilir. Eğer üzerinde işlem yapılan bir dokümansa “Form”, prosedür-talimat gibi dokümanlar ise “Doküman” seçeneği işaretlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload07fa6fed-af47-49c7-82d0-c6546a5516a4)

Klasörde ilişkilendirilen şablon Doküman Hazırlama Şablonu alanında yüklendiği görülür. Bu dokümanı hazırlarken bu Doküman Hazırlama Şablonu kullan anlamına bu alan gelmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload97fa83a3-7b0a-4834-82c1-5cdb9c2d653d)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload50e5ecfd-6d01-49b7-87ad-fe851bde732a)butonu ile Doküman Hazırlama Şablonu bilgisayar indirilir. Diğer dillerde tercümeleri varsa diğer dil seçeneklerinden doküman indirilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8ca01d2b-4ae1-4ea6-b928-f12d0119cc88)

Sisteme indirilen doküman Hazırlama Şablonu kaydedilir. Doküman sekmesinde, sisteme yüklenecek olan doküman, Doküman Dosyası Yükleme (Türkçe) alanında bulunan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2ffc74d6-5441-4cfd-9936-95c372fb0e4e) (dosya ekle butonu) ile seçilir ve yükleme işlemi gerçekleştirilir. Dokümanın mevcut dillerdeki versiyonları dil açıklamalarından yüklenebilir. Yüklenen doküman ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5b300974-a771-44da-860e-42d703b86c30) (dosya görüntüle) butonu ile görüntülenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload071ce257-6193-40cc-bacb-45e094072eb7)

Gözat butonu yardımıyla yüklecek dosya sistemden seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfdbaa93e-1a07-41e4-a330-208ffefce712)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload03ffa04f-5ad4-4417-a74b-909db6bc8aea)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload34be1ffd-d9a2-4525-bb1e-d4b5fb184b5a)

“Dosya başarıyla aktarılmıştır” mesajı ile dosyanın yüklendiği sistem tarafında belirtilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbc929570-9566-4d7e-8f5c-2709fc38ddc3)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload86bb5504-fd1a-4eeb-880e-9aa7dcf4adcc)(Gönder) butonu tıklanarak Dokümanın yayınlanıp kullanıma açılması sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload397d5ada-8106-41f0-ad0e-a8323c79004b)

Dokümanın görüntülemek için EYS\>Doküman İşlemleri\>Doküman Görme menüsü tıklanılır. Açılan ekranda Doküman Hazırlama işlemi yapılan klasör seçilir. Klasör seçildikten sonra içerisinde bulunan dokümanlar listenilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc0cebbbc-065d-4574-9d7a-7b9df9ee4cf1)

Şablonla doküman hazırlanan Dokümanın doküman kodu tıklanılır. Doküman Görme ekranında görüntülen dokümanda Kısa kodlarının çalıştığı görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9bf4ae35-581b-483f-b20c-fa214171affc)
