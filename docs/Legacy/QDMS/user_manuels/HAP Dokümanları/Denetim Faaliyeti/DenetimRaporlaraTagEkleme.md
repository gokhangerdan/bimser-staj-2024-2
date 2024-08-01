---
title: Raporlara Parametrik Alan Ekleme İşlemi ve Genel Tag Listesi
description: Raporlara Parametrik Alan Ekleme İşlemi ve Genel Tag Listesi Kullanıcı Yardım Dokümanı
sidebar_position: 2
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::


**Denetim Faaliyetleri Modülünde Raporlara Parametrik Alan Ekleme İşlemi ve Denetim Raporu Tag Listesi Kullanıcı Yardım Dokümanı**


## **1.Denetim Faaliyeti Modülünde Raporlara Parametrik Alan Ekleme İşlemi ve Raporlarda Kullanılan Taglar**

Denetim Faaliyetleri Modülünde Denetim raporuna, Denetim Bulgu raporu, Denetim planı, ve Denetim Detay planına parametrik alan ekleme işlemi yapılmaktdır. Denetim Bulgu Raporuna parametrik alan ekleme işlem basamakları ve Denetim Faaliyetleri Modülünde kullanılan taglerin (kısa kodların) listesi bu yardım dokümanında yer almaktadır.

## **1.1.Denetim Faaliyetleri Modülünde Parametrik Alan Tiplerinin Denetim Bulgu Raporunda Gösterimi**

Denetim Faaliyetleri Modülü raporlarında Denetim Bulgu raporuna eklenen parametrik alanların raporda gösterilme işlemi için öncelikle Sistem Altyapı Tanımları kısmında altyapı kurgusunun yapılması gerekmektedir. Altyapı kurgulama işleminde Alan tanımlama, Fonksiyon Dizanyer ve Rapor Formatları Düzenleme menüleri kullanılır.Alan tanımlamada Rapor formatı şablonuna taglerin eklenecek alanların tanımlama işlemi yapılır. Fonksiyon Dizanyer da tanımlan bu alanların 1numaralı Bulgu tanımlama fonksiyonu sayfalarında görüntülenmesi için ilişkisi kurulur. Bulgu tanımlama sayfası ilişkisi kurulan alanların Entegre Yönetim Sistemi\>Denetim Faaliyetleri\>Plansız Denetim menüsünde bir denetim gerçekleştirilerek Bulgu sekmesinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaded9fa79c-837f-4106-9378-695c44b3adbc)(Yeni) butonu tıklanarak açılan Bulgu Tanımlama ekranda görüntülenir. Görüntülenen parametrik alan tiplerinin alan değerleri bilgisi girilir. Bilgi girişleri yapıldıktan sonra Rapor Formatları Düzenleme menüsüne gidilir. Rapor formatların düzenleme menüsünde Denetim Bulgu rapor formatı“DENETİM_BULGU_RAPORU.xls”indirilir.İndirilenen“DENETİM_BULGU_RAPORU.xls”alan tanımlama menüsünde tanımlanan parametrik alanların tag’leri Fonksiyon Dizanyer menüsünde tanımlı alan kodları bakılarak yazılır. Fonksiyon Dizayner menüsündeki 1 nolu Bulgu tanımlama ekranına eklenen alanlar Denetim raporunda <BULGU_ALANX\> olarak Denetim Bulgu raporunda ise normal <ALANX\> olarak eklenerek kullanılmaktadır. Örneğin Metin tipli parametrik alan Fonksiyon Dizanyerde alan kodu ALAN1 ise rapor formatına eklenecek tag şekli <ALAN1\> şeklinde olmalıdır. <ALAN KODU\> şeklinde Fonksiyon Dizanyerde menüsündeki Alan kodları \<\> büyüktür ve küçüktür işaretleri arasına yazılacak şeklinde rapor format şablonuna yazılmalıdır. Liste, Personel gibi liste tipli parametrik alan tiplerinde tagleri için “ACK” eki eklenir. Örneğin Liste tipli bir alanın Fonksiyon Dizanyer menüsündeki alan kodu ALAN2 ise Alan tag’i <ALAN2_ACK\> şeklinde rapor format şablonu eklenmelidir. Rapor formatına şablonuna parametrik alanların tag şeklinde yazıldıktan sonra Rapor format “DENETİM_BULGU_RAPORU.xls”” aynı isimde bilgisayara kaydedilir. Kaydedilen aynı isimde Denetim Bulgu Raporu formatı Rapor formatları düzenleme menüsünde tekrar sisteme yüklenir.

Denetim Bulgu Raporu Rapor formatının şablonun yükleme işleminde sonra Entegre Yönetim Sistemi\>Denetim Faaliyeti\>Raporlar\>Denetim Bulgu Raporu menüsüne gidilir. Açılan Denetim Bulgu Raporu-Denetimler ekranında filtre sekmesinde arama kriterlerinden Denetim kodu alanına Denetim Kodu yazılırak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4f82cfc1-8d28-444e-acb2-fd8bb0494c25)(Excel aktar) butonu tıklanır. Excel formatın alınan raporda parametrik alanların taglerinin bulunduğu kısımda girilen bulgu tanımlama ekranında alan bilgilerinin geldiği ve taglerin çalıştığı görülür.

### **1.1.1.Sistem Altyapı Tanımları/Denetim Faaliyetleri**

Denetim Bulgu raporunun parametrik alan ekleme işleminin altyapı kurgusunun tasarlandığı kısımdır. Altyapı kurgusu için Alan Tanımlama ve Fonksiyon Dizanyer menüleri kullanılmaktadır. Ayrıca Sistem Altyapı Tanımları Modülünde Rapor format şablonu indirilerek ve indirilen rapor formatına tag ekleme işlemi yapılmış şablonun sisteme aynı isimde yüklenmesi için Rapor Formatları Düzenleme menüsünde kullanılmaktadır. Tanımlanan alan değerlerinin bilgisinin girilmesi için Soru Grubu Tanımlama, Soru Havuzu, Soru Listesi Tanımlama, Denetim Tipi Tanımlama, Denetçi Tanımlama ve Denetim Tanımlama menüleri kullanmaktadır. Tanımlanan alan değerlerinin bilgisinin girilmesi için kullanılan menüler Entegre Yönetim Sistemi\>Denetim Faaliyetleri\>Plansız Denetim menüsünde bir Denetim gerçekleşme işlemi yapılmasında kullanılır.

### **1.1.1.1. Alan Tanımlama**

**Menü Adı**: Sistem Altyapı Tanımları/Denetim Faaliyetleri/Alan Tanımlama

Fonksiyon Dizanyer menüsünde bulunan menülerin sayfalarında gösterilecek alanların tanımlama işlemi yapıldığı menüdür. Bulgu Denetim Raporu için Foksiyon Dizanyer menüsünde bulunan 1 numaralı Bulgu Tanımlama fonksiyonu için alanlar tanımlanır. Bu alan tanımlamaları metin, numerik, liste, puanlı liste, personel tipli gibi paramerik alan tipli alandır,

“Riskin Tanımı” metin tipli alan tanımlama işlemin yapılması;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload704e9eb5-d065-4beb-92cb-433461c93a10)

Listeye “Riskin Tanımı” metin tipli alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaded9fa79c-837f-4106-9378-695c44b3adbc) (Yeni) butonu tıklanarak Alan Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcdaa5225-9356-4668-ba74-b734db95a373)

Alan tanımlama ekranında alan tipi alanında metin seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5cc06842-1433-4019-83b4-6ec152086b94) (Kaydet) butonu tıklanarak metin tipli alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf2eeb273-3070-49dc-9015-a98be601fc0a)

“Riskin Tipi” liste tipli alan tanımlama işlemin yapılması;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0960360d-05e4-4f8b-945d-051742301750)

Listeye “Riskin Tipi” liste tipli alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaded9fa79c-837f-4106-9378-695c44b3adbc) (Yeni) butonu tıklanarak Alan Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb951703d-a513-46cd-9564-f9374f21db28)

Alan tanımlama ekranında Alan tipi alanında liste tipi seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5cc06842-1433-4019-83b4-6ec152086b94) (Kaydet) butonu tıklanarak liste tipli alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddfda2cf1-99ef-4ae1-af6d-315d3bb45d47)

“Risk Tipi” liste tipli alanına değer eklemek için “Risk tipi” alanı seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfec31afe-ebb7-4dbd-848e-62397efac81f) (Değerler) butonuna tıklanarak alanın değerlerinin tanıtılacağı ekrana gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload788acddf-7525-40cf-918e-510d74c3aaf6)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaf827fa8-8859-4e29-9aad-219a91948647) : Yeni butonuna tıklanarak yeni değer tanımlama işlemine başlanılır. İstenirse ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload84c1894a-e333-40b3-9067-cf81e300895f)(Şablon İndir) ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00a665a6-cea9-481d-b8a9-8684eaf27611)(Şablon Yükle) butonları ile sisteme toplu olarak alan değerleri aktarılabilmektedir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload84c1894a-e333-40b3-9067-cf81e300895f)(Şablon indir) butonu ile sistem şablonu bilgisayara indirir. İlgili şablon kullanıcılar tarafından doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00a665a6-cea9-481d-b8a9-8684eaf27611)(şablon yükle) butonu ile sisteme yüklendiğinde şablondaki tüm alan değerleri sisteme aktarılmış olacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1b86ad19-f2ff-4f14-a376-2ae2c9c57737)

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5cc06842-1433-4019-83b4-6ec152086b94) (Kaydet) butonu tıklanarak değer tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadafdaaa42-624b-4acf-a48b-6f94b4298128)

“Risk tipi” liste tipli alanın liste elemanları (değerleri) aynı şekilde tümü tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload02656f30-9d58-4f0b-abb2-120c2461e76b)

“Riskin Sahibi” Personel tipli alan tanımlama işlemin yapılması;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload164f5574-53f0-443a-9246-59aed6251b1e)

Listeye “Riskin Sahibi” Personel tipli alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaded9fa79c-837f-4106-9378-695c44b3adbc) (Yeni) butonu tıklanarak Alan Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeb6937f1-203c-4831-80fd-d7e5b920c8f5)

Alan tanımlama ekranında alan tipi alanında Personel seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5cc06842-1433-4019-83b4-6ec152086b94) (Kaydet) butonu tıklanarak Personel tipli alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadef1512fb-8da2-45bc-a516-add4447aff09)

“Riskin Başlama Tarihi” Tarih tipli alan tanımlama işlemin yapılması;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload85e5491a-6117-48b7-b7f2-8c4af00d6c88)

Alan tanımlama ekranında Alan tipi alanında “Riskin Başlama Tarihi” tipi seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5cc06842-1433-4019-83b4-6ec152086b94) (Kaydet) butonu tıklanarak “Tarih” tipli alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0e89555a-9670-4f50-950a-e360ccb217ed)

“Riskin Başlama Saati” Saat tipli alan tanımlama işlemin yapılması;

Listeye “Riskin Başlama Saati” saat tipli alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaded9fa79c-837f-4106-9378-695c44b3adbc) (Yeni) butonu tıklanarak Alan Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8e31387d-fe88-4d93-888c-9fd2efd1f8b1)

Alan tanımlama ekranında Alan tipi alanında “Saat” tipi seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5cc06842-1433-4019-83b4-6ec152086b94) (Kaydet) butonu tıklanarak “Saat” tipli alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcbe946ca-04d2-4173-abbf-3308b8c4131f)

### **1.1.1.2.Fonksiyon Dizayner**

**Menü Adı**: Sistem Altyapı Tanımları/İSG Risk Değerlendirme/ Fonksiyon Dizayner

Alan Tanımlama menüsünde rapor formutı şablona eklenecek alanların tanımlama işleminde sonra Sistem Altyapı Tanımları\>Denetim Faaliyetleri\>Fonksiyon Dizanyer menüsü tıklanılır.

Açılan fonksiyon Dizanyer ekranında tanımlanacak alanlarının eklenecek iki fonksiyon bulunur. Bu fonksiyonlar Bulgu tanımlama ve Denetim Tanımlama fonksiyonlarıdır.Tanımlanan alanların Fonksiyon Dizanyer menüsünde bulunan bu fonksiyonları sayfaları ile ilişkilendirme işlemi bu menüde yapılır. Denetim Bulgu Raporu için 1 numaralı Bulgu Tanımlama foksiyonu ile tanımlanan alanların ilişkilendirilmesi yapılır. Tanımlanan alanların Bulgu Tanımlama fonksiyonu ile ilişkilendirmesi işleminde sonra Denetim Gerçekleştirme aşamasında Bulgular sekmesinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaded9fa79c-837f-4106-9378-695c44b3adbc)(Yeni) butonu tıklanarak açılan Bulgu tanımlama ekranında görüntülenmesi sağlanmış olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload48d8bdb8-d42f-41d3-b36d-e1b709c4c674)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload693125f2-bdca-49c0-88fe-a0ed89e9553d): Alanlar butonuna tıklanarak alanların ilgili fonksiyonla ilişkilendirilme yapılacağı ekran açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload16d873ed-1f8f-42b2-a017-190916c75344)

İlgili fonksiyonda kullanılacak alanlar ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaded9fa79c-837f-4106-9378-695c44b3adbc)(Yeni) butonuna tıklanarak belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbc1032c1-6522-4585-a642-57fa7d4bb47e)

Açılan ekranda alan bilgileri listeden seçilir, zorunlu bir alan ise kullanıcının bu alanı doldurmadığında karşısına çıkacak mesaj tanımlanır. Gerekli tüm alanlar doldurulduktan sonra ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload672c1f30-6138-4ae1-ad19-416d95f0483f) (Kaydet) butonu tıklanarak, ilgili alan için fonksiyon ile ilişkilendirme işlemi gerçekleştirilir. Gerekli olan tüm alanlar bu şekilde ilgili fonksiyona eklenir. Aşağıda görüldüğü üzere Alan No’nun yanında Alan Kodu bölümü vardır. Bu Denetim Bulgu Raporuna bu alan düzenlemelerinde <ALAN1\> vb. şekilde raporun rapor formatı şablonuna eklenerek düzenleme yapılmasına imkan sağlayan koddur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0d946165-3219-48b9-99f5-93c7aab02c78)

İlgili fonksiyonda kullanılacak alanlar tümü aynı şekilde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaded9fa79c-837f-4106-9378-695c44b3adbc)(Yeni) butonuna tıklanarak belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload35fe72cb-b4ba-4fd7-a9bf-525a6460023c)

### **1.1.1.3.Denetim Bulgu Raporu Formatına Tag Eklenecek Alanların Değerlerin Girilmesi**

Denetim Bulgu Raporu formatına tag eklenecek alanların değerlerin girilmesi için Denetim Faaliyetleri Modülünde Plansız yada Planlı Denetim tanımlanarak değerlerin girilmesi sağlanılır. Örnek olarak Plansız bir Denetim tanımlanır. Tanımlanan Plansız Denetim gerçekleştirme ekranında Bulgular sekmesinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaded9fa79c-837f-4106-9378-695c44b3adbc)(Yeni) butonu tıklanır. Açılan Bulgu Tanımalama ekranında alan tanımlama menüsünde tanımlanıp Fonksiyon Dizanyer menüsüne ilgili fonksiyonlar sayfası olan bulgu tanımlama ile ilişkilendirilen alanlar görüntülenir. Açılan Bulgu tanımlama ekranında alan değerlerinin bilgisi girilir. Denetim gerçekleştirme işleminde de ilk olarak Denetim tanımlama işlemi yapılabilmesi için Soru Havuzu , Soru Grubu Tanımlama, Soru Listesi Tanımlama, Denetçi Tanımlama ve Denetim Tipi Tanımlama menülerinde altyapı kurgusu tanımlanması gerekir.Soru havuzu menüsünde denetimde sorulacak soruların tanımlama işlemi yapılır. Tanımlanan Soruların Soru Grubu Tanımlama menüsünde tanımlanan soru grubu ile ilişkisi kurulur. Soru Listesi tanımlama menüsünde Soru listesi tanımlama işlemi yapılarak soruların ekleme işlemi yapılır. Denetim Tanımlamada kullanacak Denetim Tipi Denetim Tipi tanımlama işleminde tanımlanır. Altyapıda tanımlama işlemlerinden sonra son olarak Denetim Tanımlama işlemi yapılır.

### **1.1.1.4.Denetim Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/Denetim Faaliyeti/ Denetim Tanımlama

Denetim tanımlama işleminin yapıldığı menüdür. Bu menüde Plansız bir denetim tanımlama işlemi yapılacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8bf6262f-92db-4dd7-8546-b58d01a98824)

Denetim tanımlama ekranına yeni bir denetim eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf63ad0f3-1591-41ae-8f3a-343d857c268d) (yeni) butonu tıklanarak Denetim Tanımlama/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd161ea97-b005-41c6-a733-6365d3894bb0)

Denetim tanımlamada Plansız bir Denetim işlemi gerçekleştirileceği için Denetim Tanımlama-Yeni Kayıt ekranında Plansız ilgili check box’ın işaretlenmesi gerekir. Sistem Altyapı Tanımları/Denetim Faaliyetleri/Denetim Tanımlama menüsünde açılan ekranda Denetim Plansız mı? Seçeneğinin görüntülenebilmesi için Sistem Altyapı Tanımları/ BSAT/ Konfgürasyon Ayarları / Dil Ayarları menüsüne giriş yapılır ve Denetim modülü seçilir. Adı gridine “lblplansiz” yazılır ve Değiştir butonuna tıklanarak alan değeri doldurulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload13532f1a-893d-45b9-8836-5ffd6a729923)

Denetim Tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5cc06842-1433-4019-83b4-6ec152086b94) (kaydet) butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1f3cf612-a7f3-490b-92c5-bb0890b24e14)

### **1.1.2.Entegre Yönetim Sistemi/Denetim Faaliyeti**

Sistem Altyapı Tanımları\>Denetim Faaliyetleri kısmında altyapı kurgusu tanımlanan Plansız Denetimin gerçekleştirilme işlemin yapıldığı kısımdır.

### **1.1.2.1.Plansız Denetimler**

**Menü Adı:** Entegre Yönetim Sistemi/Denetim Faaliyetleri/Plansız Denetimler

Plansız denetimlerin gerçekleştiği menüdür. Herhangi bir plan ile ilişkilendirilmez. Denetim tanımlama menüsünde plansız olarak belirlenen denetimler bu menüde yer alır. Denetçi buradaki menü üzerinden tanımlanmış denetimi herhangi bir zamanda gerçekleştirir. Denetim gerçekleştirme menüsünde yapılan işlemlerin aşamaları aynıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd7c43c6b-282a-498c-af4c-fda74b575bcb)

Denetim Planları ekranına yeni bir denetim planı eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf63ad0f3-1591-41ae-8f3a-343d857c268d) (yeni) butonu tıklanarak Denetim Planları/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadab05d522-9684-4afa-9565-0c6bc8f319dd)

Denetim Planları ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5cc06842-1433-4019-83b4-6ec152086b94) (kaydet) butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0526fa15-dee2-4cb3-8b6a-ca042f239fd1)

Denetim Planı tanımlama işleminde sonra Sistem Altyapı Tanımları\>Denetim Faaliyetleri\>Denetim Parametreleri menüsü gidilir. Denetim Parametrelerinde 100 numaralı “Plansız Denetimler için kullanılacak plan ID” parametre değerine tanımlanan parametre Denetim Plan nosu bilgisi yazılır. Bu şekilde plansız gereçekleştirilecek Denetimler bu plan içeresinde dahil olması sağlanılır.

Entegre Yönetim Sistemi\>Denetim Faaliyetleri\>Plansız Denetim menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb2953440-ee4e-4103-a28a-97fa360af5cc)

Plansız Denetim menüsünde listelenen denetim seçilerek denetimi gerçekleştirmek için, ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada044d041-395d-4aaa-b41f-e0f658b4b3eb) (denetimi gerçekleştir) butonu tıklanarak sırası ile cevaplar, bulgular, diğer bilgiler, varsa ek dosyalar girilir, son olarak denetim raporu hazırlanır.

Cevaplar sekmesinde sorulara verilecek cevap seçenekleri işaretlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload985acff1-a891-480d-8e61-4f23933a907c)

Bulgular sekmesi tıklanılır

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb436ae0e-d00b-42a2-9e57-074cc82a0afa)

Bulgular sekmesinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5351a999-24f7-4eab-a1d4-79a45133b680)(yeni ) butonu tıklanarak Bulgu tanımlama ekranında Denetimde tespit edilen bulgular girilir. Alan tanımlamada menüsünde tanımlanan ve Fonksiyon Dizanyer menüsünde Bulgu Tanımlama sayfası ile ilişkilendirilen parametrik alan tipleri görüntülenir. Görüntülenen bu parametrik alan tiplerinin bilgi girişleri yapılır. Bu parametrik alan tiplerinin tagleri daha sonra rapor formatına eklenerek rapora basılması sağlanacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload33ec9945-6306-417c-b9b7-7e0ae02cda5a)![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload13cb166c-d03d-4db0-9ce1-fc6d5bc238be)

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5cc06842-1433-4019-83b4-6ec152086b94) (kaydet) butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3f500b58-6844-4d7a-b333-b45e9fd9fe7a)

Diğer bilgiler sekmesinde ilave bilgiler ve notlar eklenebilir. Bu sekmeye alan eklenilmesi isteniyorsa dil ayarların menüsünden düzenleme yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd684502d-2ff9-4bf1-81c8-a6e21db37b3a)

Ek dosyalar sekmesinde denetimle ilgili ek dosya eklenmek isteniyorsa eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7206ed7f-f30d-4461-b360-9b53ae852b51)

Denetim Raporu sekmesinde Denetime ait bilgiler girildikten sonra denetim raporu oluşturulup denetim kapatılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfa1306be-4518-4121-84f4-369a1fa58fd4)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload04aa1456-e82c-4dd9-ab99-ad5a09538be6)

İstenirse İlgili linke tıklayarak denetim raporuna ulaşılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0e34069f-5024-4c17-bed4-d2bc2eebe69e)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfd1aa4ab-41a2-4c66-935a-562b167de412) Denetim kapat botunu tıklanılarak Denetim kapatılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8def023f-ce1a-4acd-a017-891c79df1764)

### **1.2.3.Denetim Bulgu Raporun Rapor Formatına Tanımlanan Parametrik Alanların Taglerin Eklenmesi**

Denetim Bulgu Raporu tanımlanan parametrik alanların taglerin eklenmesi için Sistem Altyapı Tanımları\>BSAT\> Konfigürasyon Ayarları\>Rapor Formatları Düzenleme menüsüne gidilir. Qdms tüm raporların yüklendiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload299b2e9d-e33f-4b3a-a396-a5d0d4a03f49)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload82f25f13-7b82-4635-ae92-7abff8a09ad2) (Görüntüle) butonu tıklanarak Denetim Bulgu Raporunun rapor format şablonu (DENETİM_BULGU_RAPORU.xls) bilgisayara indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload55ab54a3-0ac1-43e4-9d59-300ed139f540)

Alan Tanımlama tanımlanan alanlar Fonksiyon Dizanyer menüsünde ilgili sayfalarının ilişkilendirildikten sonra Fonksiyon Dizanyer da 1 numaralı fonksiyon olan Bulgu Tanımlama seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload693125f2-bdca-49c0-88fe-a0ed89e9553d)(Alanlar) butonun tıklatıldığına açılan alan kodları rapor formatında alan değerleri kısmına yazılarak eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload35fe72cb-b4ba-4fd7-a9bf-525a6460023c)

Rapor Formatına Fonksiyon Dizanyerdeki Alan kodları \<\> büyüktür ve küçüktür işaretleri arasına yazılır. Tag yazım şekli <ALANX\> dir. Örneğin ALAN1 kodlu “Risk Tanımı” alanı <ALAN1\> şeklinde rapor format şablonu alan değeri kısmına yazılır. Liste, Personel gibi liste tipli alanlarda “ACK” eki ile birlikte tagi yazmak gerekiyor. Örneğin ALAN2 kodlu “Risk Tipi” liste tipli parametrik alanda <ALAN_ACK\> şeklinde tag’ini rapor formatına şablonuna yazmak gerekiyor.

Fonksiyon Dizanyer menüsünde Alan tanımlamada tanımlanan alanlarının kodlarının tag şeklinde yazılmış şekli aşağıdaki tabloda yer almaktadır.

| **Alan Adı**                        | **Alan Tag’i(ALANKODU)** |
|-------------------------------------|--------------------------|
| Risk Tanımı (Metin Tipli)           | <ALAN1\>                |
| Risk Tipi (Liste Tipli)             | <ALAN2_ACK\>            |
| Riskin Sahibi (Personel Tipli)      | <ALAN3_ACK\>            |
| Riskin Başlama Tarihi (Tarih Tipli) | <ALAN4\>                |
| Riskin Başlama Saati (Saat Tipli)   | <ALAN5\>                |

Tablodaki parametrik alan tiplerinin alan tanımları ve tagleri ilgili bilgileri indirilen rapor format şablonuna yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload19a123de-1822-4457-9bf8-b2bc6a51961b)

Rapor formatına şablonuna alan tanımları ve taglerinin yazılımdan sonra rapor DENETİM_BULGU_RAPORU.xls aynı isimde formatı bilgisayara kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload196f28dc-0346-48ec-96bd-b1f4755b6ab4)

Bilgisayara kaydedilen aynı isimdeki Rapor format (DENETİM_BULGU_RAPORU.xls) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4e5bd331-6536-471a-a210-ed986bd32758) (Yeni) butonu ile tekrar rapor formatları düzenleme menüsünden sisteme yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload54355b84-447d-4591-91d7-63d58b207bde)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0c6330a6-957c-495d-9ed2-befdd1249c9c)

Rapor formatları düzenleme menüsünde aynı isimde rapor format yükleme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload35053e16-a1f0-4408-856b-cb3ad8c7dd62)

### **1.1.4. Denetim Bulgu Raporunun Rapor Formatına Eklenen Parametrik Alanların Gösterimi**

Denetim Bulgu Raporunun rapor formatına (DENETİM_BULGU_RAPORU.xls) tag ekleme işlemi yapılan rapor format yükleme işleminde sonra Entegre Yönetim Sistemi\>Denetim Faaliyetleri \>Raporlar\>Denetim Bulgu Raporu menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload305c4107-813b-40e7-91c7-dda0cc47edc3)

Açılan Denetim Bulgu Raporu-Denetimler ekranında Liste ve Filtre sekmesi karşımıza çıkar. Filtre sekmesinde arama kriterlerinden Denetim Kodu alanına tanımlanan parametrik alan tiplerinin bilgi girişleri yapılan gerçekleştirilip kapatılan Denetimin kod bilgisi girilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload47397be8-b78c-4685-b221-4feb6ab9f972)(Ara) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload11152588-7735-496d-8efa-374ca6f888a9)

Liste sekmesinde seçili Denetim üzerinden ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4f82cfc1-8d28-444e-acb2-fd8bb0494c25) (Excel’e Aktar) butonu tıklanılır. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4f82cfc1-8d28-444e-acb2-fd8bb0494c25) (Excel’e Aktar) butonu ile “Denetim Bulgu Raporu” Excel formatında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4c5ab805-bceb-4961-a865-daae9595ffc1)

Alınan Denetim Bulgu Raporunun da Alan tanımlama menüsünde tanımlanan parametrik alan tiplerinin değerlerinin bilgisinin raporu geldiği ve şablona eklenen parametrik alan tiplerinin tag’lerinin çalıştığı görülür.

## **1.5. Denetim Faaliyetleri Modülünde Denetim Raporu Replacement (Kısa Kodlar) Tag Tablosu**

Denetim Faaliyetleri Modülünde kullanılan Denetim Raporu taglerin listesi aşağıdaki tabloda yer almaktadır.

| **Kısaltma (Kısalmalar tag şeklinde \< \>  isaretleri arasına yazılacaktır.)** | **Açıklama**                                                                  |
|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| DENETIM_KODU                                                                   | Denetim Kodu Bilgisi                                                          |
| DENETIM_TANIMI                                                                 | Denetim Tanım Bilgisi                                                         |
| DENETIM_TARIHI                                                                 | Denetim Tarihi Bilgisi                                                        |
| BAS_DENETCI                                                                    | Denetim Baş denetçi Bilgisi                                                   |
| DENETIM_KONUSU                                                                 | Denetim Konusu Bilgisi                                                        |
| DENETIM_EKIBI                                                                  | Denetim Ekibi Bilgisi                                                         |
| DENETLENEN_BIRIMLER                                                            | Denetlenen Birimler Bilgisi                                                   |
| DENETLENEN_BIRIM_SORUMLULARI                                                   | Denetlenen Birim Sorumları Bilgisi                                            |
| ILGILI_YONETIM_SISTEMLERI                                                      | İlgili Yonetim Sistemleri Bilgisi                                             |
| ILGILI_SURECLER                                                                | İlgili Süreçler Bilgisi                                                       |
| ILGILI_DOKUMANLAR                                                              | İlgili Dokümanlar Bilgisi                                                     |
| DENETIM_SAATI                                                                  | Denetim Saati Bilgisi                                                         |
| KAPATMA_TARIHI                                                                 | Kapatma Tarihi Bilgisi                                                        |
| DENETIM_BITIS_TARIHI                                                           | Denetim Bitiş Tarihi Bilgisi                                                  |
| BASLANGIC_ZAMANI                                                               | Denetimin Başlangıç Zaman Bilgisi                                             |
| BITIS_ZAMANI                                                                   | Denetimin Bitiş Zaman Bilgisi                                                 |
| DENETIM_SURESI                                                                 | Denetim Süresi Bilgisi                                                        |
| NOTLAR                                                                         | Notlar Bilgisi                                                                |
| ISYERI                                                                         | İşyeri Bilgisi                                                                |
| DENETIM_ISYERI                                                                 | Denetim İşyeri Bilgisi                                                        |
| DENETIM_TIPI                                                                   | Denetim Tipi Bilgisi                                                          |
| SORU_SAYISI                                                                    | Soru Sayısı Bilgisi                                                           |
| DEGERLENDIRILEN_SORU_SAYISI                                                    | Değerlendirilen Soru Sayısı Bilgisi                                           |
| DEGERLENDIRILMEYEN_SORU_SAYISI                                                 | Değerlendirilmeyen Soru Sayısı Bilgisi                                        |
| DENETIM_PUANI                                                                  | Denetim Puan Bilgisi                                                          |
| DENETIM_YUZDESI                                                                | Denetim Yüzdesi Bilgisi                                                       |
| SORU_NO                                                                        | Soruya ait Soru No Bilgisi                                                    |
| SIRA_NO                                                                        | Sıra No Bilgisi                                                               |
| SORU                                                                           | Soruya Ait Soru Alanı Bilgisi                                                 |
| CEVAP                                                                          | Soruya Ait Cevap Bilgisi                                                      |
| PUAN                                                                           | Soruya Ait Puan Bilgisi                                                       |
| MPUAN                                                                          | Puanlı Denetimlerde Max Puan Bilgisi                                          |
| MAX_PUAN                                                                       | Soruya Ait Max Puan Bilgisi                                                   |
| MIN_PUAN                                                                       | Soruya Ait Min Puan Bilgisi                                                   |
| AGIRLIK                                                                        | Ağırlık Bilgisi                                                               |
| BEKLENEN_CEVAP                                                                 | Soruya Ait Beklenen Cevap Bilgisi                                             |
| SORU_ILGILI_MADDE_NUMARALARI                                                   | Soru Ait İlgili Madde Numaraları                                              |
| UYGUNLUK_DURUMU                                                                | Uygunluk Durumu Bilgisi                                                       |
| SORU_GRUBU                                                                     | Soru Grubu Bilgisi                                                            |
| SORU_GRUBU_KODU                                                                | Soru Grubu Kodu Bilgisi                                                       |
| SORU_GRUBU_AGIRLIK                                                             | Soru Grubu Ağırlık Bilgisi                                                    |
| HESAPLAMAYA_DAHIL_MI                                                           | Hesaplamaya Dahil mi Bilgisi                                                  |
| DOF_ACILSIN                                                                    | DÖF Açılsın Bilgisi                                                           |
| AKSIYON_ACILSIN                                                                | Aksiyon Açılsın Bilgisi                                                       |
| SECENEKLER                                                                     | Seçenekler Bilgisi                                                            |
| KONTROLLER                                                                     | Kontroller Bilgisi                                                            |
| SORU_BULGU_TIPI_TANIMI                                                         | Soru Bulgu Tipi Tanım Bilgisi                                                 |
| SORU_TERMIN_TARIHI                                                             | Soru Termin Tarihi Bilgisi                                                    |
| SORU_ISLEM_TIPI                                                                | Soru İşlem Tipi Bilgisi                                                       |
| SORU_EK                                                                        | Soruda Eklenen Ek Dosya Bilgisi                                               |
| BULGU_NO                                                                       | Bulgu No Bilgisi                                                              |
| BULGU_OZETI                                                                    | Bulgu Özeti Bilgisi                                                           |
| BULGU_DETAYI                                                                   | Bulgu Detayı Bilgisi                                                          |
| BULGU_TIPI                                                                     | Bulgu Tipi Bilgisi                                                            |
| BULGU_DOF_NO                                                                   | Bulgu Ait DÖF No Bilgisi                                                      |
| BULGU_AKSIYON_NO                                                               | Bulgu Ait Aksiyon No Bilgisi                                                  |
| BULGU_ILGILI_SORU                                                              | Bulgu Ait ilgili soru bilgisi                                                 |
| BULGU_ILGILI_SORU_CEVABI                                                       | BulguAit İlgili Soru Cevabı Bilgisi                                           |
| BULGU_ILGILI_SORU_GRUBU                                                        | Bulgu Ait İlgili Soru Grubu bilgisi                                           |
| BULGU_ILGILI_MADDE_NUMARALARI                                                  | Bulgu Ait İlgili Madde Numaraları Bilgisi                                     |
| BULGU_ILGILI_YONETIM_SISTEMI                                                   | Bulgu Ait İlgili Yönetim Sistemi Bilgisi                                      |
| BULGU_ILGILI_DOKUMANLAR                                                        | Bulgu Ait İlgili Dokümanlar Bilgisi                                           |
| BULGU_AKS_BITISTARIHI                                                          | Bulgu Ait Aksiyon Bitiş Tarihi Bilgisi                                        |
| BULGU_AKS_GERCEKLESMETARIHI                                                    | Bulgu Ait Aksiyonun Gerçekleşme Tarihi Bilgisi                                |
| BULGU_AKS_BASLAMATARIHI                                                        | Bulgu Ait Aksiyon Başlama Tarihi Bilgisi                                      |
| BULGU_AKS_SORUMLU                                                              | Bulguya Ait Aksiyon Sorumlu Bilgisi                                           |
| BULGU_AKS_GIREN                                                                | Bulguya Ait Aksiyonun Sisteme Giren Bilgisi                                   |
| BULGU_AKS_TANIM                                                                | Bulguya Ait Aksiyonun Tanım Bilgisi                                           |
| BULGU_AKS_YAPILANIS                                                            | Bulguya Ait Aksiyonun Yapılan İş Bilgisi                                      |
| BULGU_AKS_YAPACAK                                                              | Bulguya Ait Aksiyonu Yapacak Bilgisi                                          |
| BULGU_AKS_SORUMLUD                                                             | Bulguya Ait Sorumlu Departman Bilgisi                                         |
| BULGU_DOF_SISTEMEKT                                                            | Bulguya Ait DÖF'ün Sisteme Ekleme Tarihi                                      |
| BULGU_DOF_KAPATMAT                                                             | Bulguya Ait DÖF'ün Kapatma Tarihi                                             |
| BULGU_DOF_LIDER                                                                | Bulguya Ait DÖF'ün Ekip Lideri Bilgisi                                        |
| BULGU_EK                                                                       | Bulguya Eklenen Ek Dosya Bilgisi                                              |
| BULGU_BULGU_ID                                                                 | Bulguya ID Bilgisi                                                            |
| BULGU_BULGU_OZET                                                               | Bulgu Özeti Bilgisi                                                           |
| BULGU_BULGU_DETAY                                                              | Bulgu Detayı Bilgisi                                                          |
| BULGU_BULGU_TIPI                                                               | Bulgu Tipi Bilgisi                                                            |
| BULGU_SORU_ID                                                                  | Bulgu Soru ID Bilgisi                                                         |
| BULGU_ANA_AKSIYON_ID                                                           | Bulgu Ana Aksiyon ID Bilgisi                                                  |
| BULGU_ALT_AKSIYON_ID                                                           | Bulgu Alt Aksiyon ID Bilgisi                                                  |
| BULGU_ISLEMTIP1                                                                | Bulgu İşlem Tipi Bilgisi                                                      |
| BULGU_ISLEMTAR1                                                                | Bulgu İşlem Tarihi bilgisi                                                    |
| BULGU_ISLEMSORUMLU1                                                            | Bulgu İşlem Sorumlusu Bilgisi                                                 |
| BULGU_ISLEMTIP2                                                                | Bulgu İslem Tipi Bilgisi                                                      |
| BULGU_ISLEMTAR2                                                                | Bulgu İşlem Sorumlusu Bilgisi                                                 |
| BULGU_ISLEMSORUMLU2                                                            | Bulgu İşlem Sorumlusu 2 Bilgisi                                               |
| BULGU_ISLEMTIP3                                                                | Bulgu İşlem Tipi Bilgisi                                                      |
| BULGU_ISLEMTAR3                                                                | Bulgu İşlem Tarihi Bilgisi                                                    |
| BULGU_ISLEMSORUMLU3                                                            | Bulgu İşlem Sorumlusu Bilgisi                                                 |
| BULGU_ONAY                                                                     | Bulgu Onay Bilgisi                                                            |
| BULGU_RED_NEDENI                                                               | Bulgu Red Nedeni Bilgisi                                                      |
| BULGU_SORU_REV_NO                                                              | Bulgu Soru Revizyon No Bilgisi                                                |
| BULGU_DOF_GELRAPTAR                                                            | Bulguya Ait DÖF Gelişme Raporu Tarihi                                         |
| BULGU_AKS_BITTAR                                                               | Bulguya Ait Aksiyon Bitiş Tarihi                                              |
| BULGU_DOF_TERMIN_TARIHI                                                        | Bulguya Ait DÖF Termin Tarihi Bilgisi                                         |
| BULGU_TPARAM1                                                                  | Bulgu Tanımlama Ekranına Eklenen Metin Tipli Parametrik Alan                  |
| BULGU_TPARAM2                                                                  | Bulgu Tanımlama Ekranına Eklenen Metin Tipli Parametrik Alan                  |
| BULGU_TPARAM3                                                                  | Bulgu Tanımlama Ekranına Eklenen Metin Tipli Parametrik Alan                  |
| BULGU_TPARAM4                                                                  | Bulgu Tanımlama Ekranına Eklenen Metin (Çoklu Satır) Tipli Parametrik Alan    |
| BULGU_TPARAM5                                                                  | Bulgu Tanımlama Ekranına Eklenen Metin (Çoklu Satır) Tipli Parametrik Alan    |
| BULGU_LPARAM1                                                                  | Bulgu Tanımlama Ekranına Eklenen Liste Tipli Parametrik Alan                  |
| BULGU_LPARAM2                                                                  | Bulgu Tanımlama Ekranına Eklenen Liste Tipli Parametrik Alan                  |
| BULGU_LPARAM3                                                                  | Bulgu Tanımlama Ekranına Eklenen Liste Tipli Parametrik Alan                  |
| BULGU_LPARAM4                                                                  | Bulgu Tanımlama Ekranına Eklenen Liste Tipli Parametrik Alan                  |
| BULGU_LPARAM5                                                                  | Bulgu Tanımlama Ekranına Eklenen Liste Tipli Parametrik Alan                  |
| BULGU_DPARAM1                                                                  | Bulgu Tanımlama Ekranına Eklenen Tarih Tipli Parametrik Alan                  |
| BULGU_DPARAM2                                                                  | Bulgu Tanımlama Ekranına Eklenen Tarih Tipli Parametrik Alan                  |
| BULGU_DPARAM3                                                                  | Bulgu Tanımlama Ekranına Eklenen Tarih Tipli Parametrik Alan                  |
| BULGU_DPARAM4                                                                  | Bulgu Tanımlama Ekranına Eklenen Tarih Tipli Parametrik Alan                  |
| BULGU_DPARAM5                                                                  | Bulgu Tanımlama Ekranına Eklenen Tarih Tipli Parametrik Alan                  |
| BULGU_NPARAM1                                                                  | Bulgu Tanımlama Ekranına Eklenen Nümerik Tipli Parametrik Alan                |
| BULGU_NPARAM2                                                                  | Bulgu Tanımlama Ekranına Eklenen Nümerik Tipli Parametrik Alan                |
| BULGU_NPARAM3                                                                  | Bulgu Tanımlama Ekranına Eklenen Nümerik Tipli Parametrik Alan                |
| BULGU_NPARAM4                                                                  | Bulgu Tanımlama Ekranına Eklenen Nümerik Tipli Parametrik Alan                |
| BULGU_NPARAM5                                                                  | Bulgu Tanımlama Ekranına Eklenen Nümerik Tipli Parametrik Alan                |
| BULGU_NPARAM1_BIRIM                                                            | Bulgu Tanımlama Ekranına Eklenen Nümerik Birim Tiplerine Ait Parametrik Alan  |
| BULGU_NPARAM2_BIRIM                                                            | Bulgu Tanımlama Ekranına Eklenen Nümerik Birim Tiplerine Ait Parametrik Alan  |
| BULGU_NPARAM3_BIRIM                                                            | Bulgu Tanımlama Ekranına Eklenen Nümerik Birim Tiplerine Ait Parametrik Alan  |
| BULGU_NPARAM4_BIRIM                                                            | Bulgu Tanımlama Ekranına Eklenen Nümerik Birim Tiplerine Ait Parametrik Alan  |
| BULGU_NPARAM5_BIRIM                                                            | Bulgu Tanımlama Ekranına Eklenen Nümerik Birim Tiplerine Ait Parametrik Alan  |
| BULGU_T2_PLAN_ID                                                               | Bulguya Ait Denetim Plan ID Bilgisi                                           |
| BULGU_T2_DENETIM_ID                                                            | Bulguya Ait Denetim ID Bilgisi                                                |
| BULGU_T2_PLANLANAN_DENETIM_TARIHI                                              | Bulguya Ait Denetim Tarihi Bilgisi                                            |
| BULGU_T2_DENETIM_BITIS_TARIHI                                                  | Bulguya Ait Denetim Bitiş Tarihi Bilgisi                                      |
| BULGU_T2_DURUM                                                                 | Bulguya Ait Denetim Durum Bilgisi                                             |
| BULGU_T2_KAPATMA_TARIHI                                                        | Bulguya Ait Denetim Kapatma Tarihi Bilgisi                                    |
| BULGU_T2_DENETIM_KODU                                                          | Bulguya Ait Denetim Kodu Bilgisi                                              |
| BULGU_T2_DENETIM_SAATI                                                         | Bulguya Ait Denetim Saati Bilgisi                                             |
| BULGU_T2_DENETIM_KONUSU                                                        | Bulguya Ait Denetim Konusu Bilgisi                                            |
| BULGU_T2_BAS_DENETCI                                                           | Bulguya Ait Denetim Baş Denetçi Bilgisi                                       |
| BULGU_T3_BULGU_TIPI_TANIMI                                                     | Bulguya Ait Bulgu Tipi Tanımı Bilgisi                                         |
| BULGU_T3_ISLEM_TIPI                                                            | Bulguya Ait DÖF İşlem Tipi Bilgisi                                            |
| BULGU_T4_ADISOYADI                                                             | Bulguya Ait DÖF Lider Adı Soyadı Bilgisi                                      |
| BULGU_T5_ADISOYADI                                                             | Bulguya Ait Aksiyon Sorumlusu Adı Soyadı Bilgisi                              |
| BULGU_T6_ADISOYADI                                                             | Bulguya Ait Aksiyon Yapacak Adı Soyadı Bilgisi                                |
| BULGU_T7_DENETIM_TANIMI                                                        | Bulgunun Bağlı Olduğu Denetimin Tanımı                                        |
| BULGU_T8_ADISOYADI                                                             | Bulgunun Bağlı Olduğu Denetimin Baş Denetçisi                                 |
| BULGU_ALAN1                                                                    | Bulgu Tanımlama İçin Eklenen Alan Bilgisi                                     |
| BULGU_ALAN3                                                                    | Bulgu Tanımlama İçin Eklenen Alan bilgisi                                     |
| BULGU_T4_SORU                                                                  | Bulgu İlgili Soru Bilgisi                                                     |
| BULGU_T4_SORU_GRUBU                                                            | Bulgu İlgili Soru Grubu Bilgisi                                               |
| BULGU_BULGU_AKS_BITISTARIHI                                                    | Bulgu Aksiyon Bitiş Tarihi Bilgisi                                            |
| BULGU_BULGU_AKS_GERCEKLESMETARIHI                                              | Bulgu Aksiyon Gerçekleşme Tarihi Bilgisi                                      |
| BULGU_BULGU_AKS_BASLAMATARIHI                                                  | Bulgu Aksiyon Başlama Tarihi Bilgisi                                          |
| BULGU_BULGU_AKS_SORUMLU                                                        | Bulgu Aksiyon Sorumlu Bilgisi                                                 |
| BULGU_BULGU_AKS_YAPACAK                                                        | Bulgu Aksiyon Yapacak Bilgisi                                                 |
| BULGU_BULGU_AKS_SORUMLUD                                                       | Bulgu Aksiyon Sorumlu Departman Bilgisi                                       |
| BULGU_BULGU_AKS_GIREN                                                          | Bulgu Aksiyon Giren Bilgisi                                                   |
| BULGU_BULGU_AKS_TANIM                                                          | Bulgu Aksiyon Tanım Bilgisi                                                   |
| BULGU_BULGU_AKS_YAPILANIS                                                      | Bulgu Aksiyon Yapılan İş Bilgisi                                              |
| BULGU_BULGU_DOF_SISTEMEKT                                                      | Bulgu DÖF Sisteme Ekleme Tarihi Bilgisi                                       |
| BULGU_BULGU_DOF_KAPATMAT                                                       | Bulgu DÖF Kapatma Tarihi Bilgisi                                              |
| BULGU_BULGU_DOF_LIDER                                                          | Bulgu DÖF Lider Bilgisi                                                       |
| DPARAM2                                                                        | Tarih Tipli Parametrik Alan                                                   |
| PARAM3                                                                         | Parametrik Alan Bilgisi                                                       |
| DOSYALAR                                                                       | Ek Dosya Bilgisi                                                              |
| SORU_AKSIYON_NO                                                                | Soruya Ait Aksiyon No Bilgisi                                                 |
| SORU_DOF_NO                                                                    | Soruya Ait DÖF No Bilgisi                                                     |
