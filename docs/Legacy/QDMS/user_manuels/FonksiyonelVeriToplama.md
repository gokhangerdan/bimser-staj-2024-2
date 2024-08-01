---
title: Fonksiyonel Veri Toplama
description: Fonksiyonel Veri Toplama Yardım Dokümanı
sidebar_position: 70
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::




**Fonksiyonel Veri Toplama Modülü (v.5.24) Kullanıcı Yardım Dokümanı**

Modül Versiyonu: 5.24

**1. GİRİŞ**: **“QDMS Fonksiyonel Veri Toplama Modülü”**, veri girişi yapılacak formların, dönemsel periyoda ve farklı onay kurgularına bağlı olarak veri girişlerinin yapılıp, onaylandıktan sonra raporlanmasını sağlayan bir modüldür.

**2. AMAÇ**: Bu yardım kılavuzunun amacı; QDMS “Fonksiyonel Veri Toplama” Modülünün çalışma sürecini anlatmaktır. Bu doküman, sistem altyapı tanımlarındaki tanımlamalar ve parametrelerden başlayarak, Formların doldurulacağı Entegre Yönetim Sistemi menüsü altında bulunan “Raporlar” ve “Grafikler” ile birlikte Form bazında oluşturulan menülerin anlatımını içerir. Veri girişi yapılması hedeflenen değerler için periyodik görev düşürüp, geçmiş kayıtların raporlanmasını hedeflemektedir.

**3. SORUMLULUKLAR**: Veri Girişi Yapacak Kullanıcılar, Veri Girişi Yapacak Kişinin Bir Üst Amiri

**4. KISALTMALAR**:

QDMS: Kalite Dokümanları Yönetim Sistemi “ Quality Document Management System”


# 5.Fonksiyonel Veri Toplama Modülü

Sistem Altyapı Tanımları kısmında veri girişi yapılacak formların tanımlanıp, tanımlanan formun raporlarının ve grafiklerin tanımlanması , tanımlanan bu veri girişi yapılacak formların, dönemsel periyoda ve farklı onay kurgularına bağlı olarak Entegre yönetim sistemi kısmında veri girişlerinin yapılıp, onaylandıktan sonra raporlanması ve grafiklerin alınması, alan tanımlama menüsü ile ekstra alanların tanımlanması yapılıp, alan havuzuna eklenmesi ve alan havuza eklenen bu alanların Fonksiyon Dizayner menüsünde fonksiyon olarak görüntülenen tanımlanan formlarla ilişkilendirilip, formlarının sayfalarında görüntülenmesini işlemlerin yapılması ile form bazında oluşturulan menülerinin anlatımı sağlayan modüldür. Bu modül kapsamında 4 menü Ensemble Süreç Yönetimi ile ortak bulunmaktadır. Bu menüler Uygulama yeri tipi, Uygulama Yeri, Dönem Kırılımı ve Dönem Tanımlama menüleridir. Bu menüler Ensemble Süreç Yönetimi ve Qdms sistemi ile entegre bir şekilde çalışmaktadır. İsteye bağlı olarak Kullanıcılar Qdms veya Ensemble Süreç Yönetimi sisteminde bu menülerle ilgili işlemleri yapılmasına modül olanak sağlamaktadır.

## **5.1. Sistem Altyapı Tanımları / Fonksiyonel Veri Toplama**

Fonksiyonel Veri Toplama Modülünün altyapısını oluşturmak amacıyla gerekli tanımlamaların yapıldığı kısımdır. Yapılan tanımlamalara göre giriş ekranında veriler karşımıza çıkmaktadır

### **5.1.1. Uygulama Yeri Tipi**

**Menü Adı:** Sistem Altyapı Tanımları/ **Fonksiyonel Veri Toplama /**Uygulama Yer Tipi Tanımlama

Fonksiyonel Veri Toplama modülü ile şablon excel formatlarındaki parametrelerin dönemsel periyoda bağlı olarak veri girişlerinin yapılması, onaylanması sonrasında raporlanması çalışmaları yürütülebilmektedir. Bunun için Fonksiyonel Veri Toplama modülünün sistem altyapı tanımları altından Uygulama Yeri Tipi menüsüne gelinir. Uygulama Yerleri forma girilen verilerin ölçüldüğü yerleri ifade etmektedir. Uygulama Yeri Tipi ise bu yerlerin kategorize edilmiş halidir. Örneğin Kalite Güvence Departmanı bir “Uygulama Yeri” iken, Departman Kategorisi “Uygulama Yeri Tipi” olarak adlandırılır.

Sistem Altyapı Tanımları / Fonksiyonel Veri Toplama / Uygulama Yeri Tipi Tanımlama menüsünde “Yeni Ölçüm Yeri Tipi” butonuna tıklanarak, yeni Uygulama Yeri Tipi tanımlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload502c2a6b-4117-40a9-9167-f63ae408a231)


**Açılan ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7021cd9c-ce32-4b25-a0cb-00480558204e)**:**Yeni Ölçüm Yeri Tipi (Uygulama Yer Tipi) tanımlamak için kullanılan butondur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5412c83f-d8c1-4d92-9c6c-232b703a95ee)**Düzenle:**Tanımlı olan Ölçüm Yeri Tipleri düzenleme, pasif edilme işlemi için kullanılan butondur. Bu buton tıklanıldığında Ölçüm Yeri Tipi Düzenleme penceresi açılır. Tanımlı olan Ölçüm Yeri Tipi ile ilgili düzenleme, pasif edilme işlemi bu pencereden yapılır. Tanımlı olan Ölçüm Yerinin özellikleri değiştirilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8eb6949f-1cee-4e7c-9067-64580f68b155)**Sil:** Pasif Ölçüm yeri tipleri sekmesinde görüntülen butondur. Aktif Ölçüm yeri Tipleri sekmesinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5412c83f-d8c1-4d92-9c6c-232b703a95ee)(Düzenle) butonu tıklanarak Durumu pasif edilen Ölçüm Yeri Tipi Pasif Ölçüm yeri sekmesindeki listede listenir. Listenen pasif durumundaki Ölçüm yeri tipi silerek sistemden kaldırmak için kullanılan butondur. (Ölçüm Yeri Tipinin Silme işlemin yapılması için ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5412c83f-d8c1-4d92-9c6c-232b703a95ee)(Düzenle) butonu tıklanarak açılan ekranda Ölçüm yeri tipinin durumun pasif edilerek Pasif Ölçüm yeri Tipleri sekmesindeki listede yer almasının sağlanması gerekir. Silme işlemi yalnızca pasif kayıtlar üzerinde yapılabilir. Bu sebeple silinmesi gereken kayıt öncelikle pasif edilmelidir.) Bu buton tıklanıldığında “Bu ölçüm yeri tipini silmek istediğinizden emin misiniz?” uyarı mesajı gelir. Evet butonu tıklanıldığında “Ölçüm yeri tipi başarıyla silindi” mesajı gelir. Pasif Ölçüm yeri Tipleri sekmesindeki listede yer alan Pasif durumdaki Ölçüm Yeri Tipi istenirse ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5412c83f-d8c1-4d92-9c6c-232b703a95ee)(Düzenle) butonu tıklanarak durumu aktif edilerek Aktif Ölçüm yeri Tipleri sekmesindeki listede yer alması sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfe2e89f8-196c-416b-9ea4-ba043309c837)

**Yeni bir Yeni Ölçüm Yeri Tipi Tanımlamak için;**

Sistem Tanımları/ **Fonksiyonel Veri Toplama** /Ölçüm Yeri Tipi Tanımlama/Yeni Ölçüm Yeri Tipi butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9e0e9f71-c23f-47e7-9732-c84db6d7883f)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Adı :**Tanımlanan Ölçüm Yeri Tipinin Adı bilgisinin girildiği zorunlu alandır.

Ölçüm Yeri Tanımlamada Ölçüm Yerlerini Otomatik oluşturulması için gereken alanlardır.

**Boyutları Oluştur:** İlgili ölçüm yeri tipine göre tanımlanacak ölçüm yerlerinin (departman, iş yeri, personel vb.) QDMS veritabanından tek seferlik manuel olarak topluca çekilmesini sağlayan özelliktir. Referans Kolonu, Tanım Kolonu, Sembol Kolonu, Bulma Yöntemi gibi alanların doldurulması için Bimser Destek Bölümünden destek alınmalıdır.

“Yeni Ölçüm Yeri Tipi” butonuna basıldıktan sonra “Adı” alanının doldurulması Uygulama Yeri Tipi tanımlamak için yeterlidir. QDMS verileri içerisinden, Departman, Pozisyon, İşyeri gibi bilgilerin Uygulama Yeri olarak otomatik oluşması talep ediliyorsa Referans, Tanım ve Sembol kolonları SQL tablo alan isimleriyle, Bulma Yöntemi ise SQL sorgusuyla doldurulduktan sonra “Boyutları Oluştur” seçeneği “Aktif” edilerek Uygulama Yerleri tek seferde oluşturulabilir. Bu işlem için Bimser Destek Ekibi’nden yardım alınmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd6a83062-2ac4-4f97-bb1c-d5ffc8ab1d7f)

### **5.1.2. Uygulama Yeri Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ **Fonksiyonel Veri Toplama /**Uygulama Yeri Tanımlama

Uygulama Yerleri forma girilen verilerin ölçüldüğü yerleri ifade etmektedir. Ölçüm yapacağımız yerlerin tanımlandığı menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6607cc70-cfe9-4fa4-bd76-f3651047becb)

**Açılan ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada1cd88d7-be63-4a77-9197-becd14b9a45c)**:**Yeni Ölçüm Yeri (Uygulama Yeri) tanımlamak için kullanılan butondur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5412c83f-d8c1-4d92-9c6c-232b703a95ee)**Düzenle:**Tanımlı olan Ölçüm Yeri düzenleme, pasif edilme işlemi için kullanılan butondur. Bu buton tıklanıldığında Ölçüm Yeri Düzenleme penceresi açılır. Tanımlı olan Ölçüm Yeri ile ilgili düzenleme, pasif edilme işlemleri bu pencereden yapılır. Tanımlı olan Ölçüm Yerinin özellikleri değiştirilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6311cbe0-691e-48a2-b511-f1a3672bc018)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada5b3687e-c61e-4eb8-bdff-a17c15b1199d)**Kopyala:** Tanımlı olan Ölçüm Yerini kopyalama işlemi için kullanılan butondur. Bu butonu ile var olan bir kaydın kopyalama işlemi yapılır. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada5b3687e-c61e-4eb8-bdff-a17c15b1199d)(Kopyala) butonu ile açılan Ölçüm Yeri Düzenle ekranında Sembol, Adı, gibi görüntülenen alanları bilgisi değiştirilerek yeni bir Ölçüm yerinin kopyalama işlemleri gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7c3d58ed-d8f4-4ef7-8580-d5f151c11570)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8eb6949f-1cee-4e7c-9067-64580f68b155)**Sil:** Liste Görünüm (Pasif) sekmesinde görüntülen butondur. Hiyerarşik ve Liste Görünüm sekmelerinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5412c83f-d8c1-4d92-9c6c-232b703a95ee)(Düzenle) butonu tıklanarak durumu pasif edilen Ölçüm Yeri Liste Görünüm (Pasif) sekmesindeki listede listenir. Listenen pasif durumundaki Ölçüm yeri silerek sistemden kaldırmak için kullanılan butondur. (Ölçüm Yeri Tipinin Silme işlemin yapılması için ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5412c83f-d8c1-4d92-9c6c-232b703a95ee)(Düzenle) butonu tıklanarak açılan ekranda Ölçüm yeri durumun pasif edilerek Liste Görünüm (Pasif) sekmesindeki listede yer almasının sağlanması gerekir. Silme işlemi yalnızca pasif kayıtlar üzerinde yapılabilir. Bu sebeple silinmesi gereken kayıt öncelikle pasif edilmelidir.) Bu buton tıklanıldığında “Bu ölçüm yeri silmek istediğinizden emin misiniz?” uyarı mesajı gelir. Evet butonu tıklanıldığında “Ölçüm yeri başarıyla silindi” mesajı gelir.Liste Görümü(Pasif) sekmesinde pasif durumundaki Ölçüm yeri istenirse ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5412c83f-d8c1-4d92-9c6c-232b703a95ee)(Düzenle) butonu tıklanarak tekrar durumu aktif edilerek Hiyerarşik ve Liste Görünüm sekmesinde listede görüntülenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6d7d4eb9-1463-4ec1-873f-b623a9053f0d)

**Yeni bir Uygulama Yeri Tanımlamak için;**

Sistem Altyapı Tanımları / Fonksiyonel Veri Toplama / Uygulama Yeri Tanımlama menüsünde “Yeni Ölçüm Yeri Tipi” butonuna tıklanarak, Yeni Uygulama Yeri tanımlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfc44ccb1-64e5-4b9c-aedd-8c25783e4f9f)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Sembol:** Tanımlanan Ölçüm Yerinin Sembol bilgisinin girildiği zorunlu alandır. Bu alanda sadece İngilizce karakter, rakam veya \_ bulunabilir. Eğer QDMS sistemindeki departman gibi tanımlar kullanılıyorsa oradaki kodları kullanmak faydalı olacaktır. Örn:Test_Symbol

**Adı:** Tanımlanan Ölçüm Yerinin Adı bilgisinin girildiği zorunlu alandır.

**Ölçüm Yeri Tipleri:** Tanımlanan Ölçüm Yerinin Ölçüm Yeri Tipleri bilgisinin sistemde tanımlı olan Ölçüm Yeri Tipleri listesinden seçilebildiği zorunlu alandır.

**Üst Ölçüm Yeri:** Tanımlanan Ölçüm Yerinin Üst Ölçüm Yeri bilgisinin sistemde tanımlı olan Üst Ölçüm Yeri listesinden seçilebildiği alandır. Tanımlanan ölçüm yeri, hiyerarşide bulunan başka bir ölçüm yerinin altında yer alıyorsa, listeden bu ölçüm yerinin seçileceği alandır.

**Sahibi:** Tanımlanan Ölçüm Yerinin Sahibi bilgisinin sistemde tanımlı olan Kullanıcılar, Pozisyon veya Kullanıcı Grupları listesinden seçilebildiği alandır.

**Veri Sorumlusu:** Tanımlanan Ölçüm Yerinin Veri Sorumlusu bilgisinin sistemde tanımlı olan Kullanıcılar, Pozisyon veya Kullanıcı Grupları listesinden seçilebildiği alandır.

**Gösterge Özet Tablosunda Gösterilsin:** Karne görüntüleme ekranında yer alan gösterge özet tablosu adındaki görselde, bu ölçüm yerine ait verilerin istenip istenmediği ayarlanır.

“Yeni Ölçüm Yeri” butonuna basıldıktan sonra, Sembol alanında kaydın kodu belirlenir. Adı alanına Uygulama Yerinin adı yazılır. Daha önce “Uygulama Yeri Tipi” menüsünde tanımlanmış kayıtlardan “Ölçüm Yeri Tipi” seçilir. Oluşturulan kaydın bağlı olduğu bir “Üst Uygulama Yeri” (Örnek olarak, üst departman veya bağlı olduğu işyeri) var ise yine daha önce tanımlanmış Uygulama Yerleri içerisinden seçilir. Uygulama Yerinin Sahibi ve Veri Giriş Sorumluları QDMS Personelleri içerisinden seçildikten sonra “Kaydet” butonuna basılarak “Uygulama Yeri” tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9bf44e7c-434d-4356-9355-c353a172801d)

### **5.1.3. Dönem Kırılımı Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ **Fonksiyonel Veri Toplama /**Dönem Kırılımı Tanımlama

Fonksiyonel Veri Toplama modülünde, Periyodik olarak ölçülen verilerin sisteme giriş periyotları “Dönem Kırılımı Tanımlama” menüsünde oluşturulan değerler içerisinden seçilir. Belirlenen dönem kırılımına göre veri girişi yapacak personellere periyodik görevler düşürülmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload071d2933-33f0-44f1-94a2-93c428328735)

**Açılan ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb236bf07-55a4-44e9-af05-24011e9231d2)**:**Yeni Dönem Kırılımı tanımlamak için kullanılan butondur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5412c83f-d8c1-4d92-9c6c-232b703a95ee)**Düzenle:**Tanımlı olan Dönem Kırılımı düzenlemek için kullanılan butondur. Bu buton tıklanıldığında Dönem Kırılımı penceresi açılır. Tanımlı olan Dönem Kırılımı ile ilgili düzenlemeler bu pencereden yapılır. Tanımlı olan Dönem Kırılımının özellikleri değiştirilebilir.Zorunlu olmayan alanlar üzerinde değişiklik ve düzenleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload74b39b7f-683b-483a-ac4f-5218f798b15b)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8eb6949f-1cee-4e7c-9067-64580f68b155)**Sil:**Tanımlı olan Dönem Kırılımını silerek sistemden kaldırmak için kullanılan butondur. Bu buton tıklanıldığında “Bu dönem kırılımını silmek istediğinizden emin misiniz?” uyarı mesajı gelir. Evet butonu tıklanıldığında “Dönem kırılımı başarıyla silindi” mesajı gelir.

**Yeni bir Dönem Kırılımı Tanımlamak için;**

Sistem Altyapı Tanımları / Fonksiyonel Veri Toplama / Dönem Kırılımı Tanımlama menüsünde “Yeni Dönem Kırılımı” butonuna tıklanarak, Yeni Dönem Kırlımı tanımlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf6fae720-f4ff-4581-842b-d02579bf6be0)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Adı:**Tanımlanan Dönem Kırılımının Adı bilgisinin girildiği zorunlu alandır.

**Üst Dönem Kırılımı:** Tanımlanan dönem kırılımı, hiyerarşide bulunan başka bir dönem kırılımının altında yer alıyorsa, listeden bu dönemin yerinin seçileceği alandır.

**Dönem Tipi:** Tanımlanan Dönem Kırılımının tipi bilgisinin seçilebildiği zorunlu alandır.

**Sistem Adı:** Tanımlanan Dönem Kırılımının eğer raporda farklı şekilde isimlendirilmesi için kullanılan zorunlu alandır.

**Dönem Uzunluğu:** Tanımlanan Dönem Kırılımının gün bazında uzunluğunun tanımlandığı zorunlu alandır.

Dönem Kırılımları penceresinde gerekli alanlar doldurularak Kaydet butonu tıklanarak Yeni Dönem Kırılımları tanımlama kayıt işlemi gerçekleştirilir.

“Yeni Dönem Kırılımı” butonuna basıldıktan sonra, Adı alanına dönem kırılımının adı (Yıl, Yarıyıl vb.) yazılır. Oluşturulan kaydın bağlı olduğu bir “Üst Dönem Kırılımı” var ise yine daha önce tanımlanmış dönem kırılımları içerisinden seçilir. Sistemde tanımlı olan periyotlardan hangisine karşılık geldiğini belirlemek adına “Dönem Tipi” alanında seçim yapılır. Sistem Adı alanında dönem kırılımının sembolü belirlenir. Dönem Uzunluğu alanında ise içerdiği toplam gün sayısı yazılır ve “Dönem Kırılımı” kaydedilir. Dönem kırılımları yıl, yarıyıl, çeyrek yıl, ay ve gün bazında tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload88fb477e-df63-408f-88a7-3c60aa7c9118)

### **5.1.4. Dönem Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ **Fonksiyonel Veri Toplama /**Dönem Tanımlama

Veri girişi yapılacak dönemlerin başlangıç-bitiş zamanlarının belirlendiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload662eb397-3e6e-4a67-8a52-aa52d74d092b)

**Açılan ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3a730f35-b780-46cb-b367-8b0735517014)**:**Yeni Dönem tanımlamak için kullanılan butondur.

Tanımlı Dönem üzerinde sağ tıklayarak açılan menü;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf7ad72a7-2a02-4738-b2f8-76c08d261e65)

**Ekle:** Hiyerarşide altına yeni bir Dönemin eklendiği seçenektir.

**Düzenle:** Tanımlı olan Dönemi düzenlemek için kullanılan seçenektir. Bu seçenek tıklanıldığında Dönem Düzenle penceresi açılır. Tanımlı olan Dönem ile ilgili düzenlemeler bu pencereden yapılır. Tanımlı olan Dönemin özellikleri değiştirilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload58490bc0-af6a-427e-9da6-3fa948f9dde4)

**Sil:** Tanımlı olan Dönemi silerek sistemden kaldırmak için kullanılan seçenektir. Bu seçenek tıklanıldığında “Bu dönemi silmek istediğinizden emin misiniz?” uyarı mesajı gelir. Evet butonu tıklanıldığında “Dönem başarıyla silindi” mesajı gelir.

**Dönemleri Oluştur:** Seçili Dönemin Kriterleri belirlenerek otomatik olarak Dönemlerin oluşturulmasını sağlayan seçenektir.

**Dönem Kilitle:**Seçili Dönemin, Döneme bağlı olan tüm kırılımlarına veri girişinin engellendiği seçenektir.

**Dönem Kilidi Aç:** Veri girişi engellenen göstergenin tekrar veri girişine açılmasını sağlayan seçenektir.

**Yeni bir Dönem Tanımlamak için;**

Sistem Altyapı Tanımları / Fonksiyonel Veri Toplama / Dönem Tanımlama menüsünde “Yeni Dönem” butonuna tıklanarak, yeni dönem tanımlanabilir..

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2328bb6d-607c-4bee-81ef-8570d56ec9a9)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Adı:** Dönem hiyerarşisinde gösterilmesi istenen adın bilgisinin tanımlanacağı zorunlu alandır.

**Tam Adı:** Tanımlanan Dönemin Tam Adı bilgisinin girildiği zorunlu alandır.

**Dönem Kırılımı:** Tanımlanan Dönemin sistemde tanımlı olan Dönem Kırılımı listesinden seçilebildiği alandır.

**Bağlı Olduğu Dönem:** Tanımlanan Dönemin hiyerarşide bulunan başka bir dönemim altında yer alıyorsa, listeden bu dönemin seçileceği alandır.

**Başlangıç Tarihi:** Tanımlanan Dönemin Başlangıç Tarihinin bilgisinin seçilebileceği zorunlu alandır.

**Bitiş Tarihi:** Tanımlanan Dönemin Bitiş Tarihi bilgisinin seçilebildiği zorunlu alandır.

**Veri Başlangıç Tarihi:**Tanımlanan Dönemin Veri Giriş Tarihinin hangi tarihte başlayacağı bilgisinin seçilebildiği zorunlu alandır.

**Veri Bitiş Tarihi:** Tanımlanan Dönemin Veri Giriş Tarihinin hangi tarihte biteceğinin bilgisinin seçilebildiği zorunlu alandır.

“Yeni Dönem” butonuna basıldıktan sonra, Adı ve Tam Adı alanlarına dönem adı (2020 Yılı vb.) yazılır. Oluşturulan kaydın bağlı olduğu “Dönem Kırılımı” daha önce tanımlanmış dönem kırılımları içerisinden seçilir. Eğer tanımlanan dönemin üst dönemi bulunuyorsa (örneğin; 2020 yılına bağlı 1. Yarıyıl) daha önce tanımlanmış dönemler içerisinden seçilir. Dönemin başlangıç ve bitiş tarihleri belirlenir. Aynı dönem için veri girilebilecek tarih aralığı belirlenir. Yeni Dönem penceresinde gerekli alanlar doldurularak Kaydet butonu tıklanarak Yeni Dönem tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload173b0895-d32d-4801-89c3-e8b50c03c93f)

“Dönemleri oluştur” seçeneği ile dönemler otomatik olarak oluşturulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload597bcd8e-e9ae-41de-a794-88c4a7da1e57)

Bağlı dönemlerin toplu olarak oluşturulabilmesi için ana dönem oluşturulduktan sonra dönem üzerinde sağ tıklanarak “Dönemleri Oluştur” satırı seçilir. Açılan ekranda ana dönem altında oluşturulacak dönem (yarıyıl, çeyrek yıl, ay vb.) tipleri seçilir. Oluşacak dönemlere veri giriş başlangıç ve bitişinin, dönem bitiş tarihinden kaç gün sonra başlayacağı gün sayısı olarak yazılır. Kaydet butonuna basılarak seçilen dönem tipi bazında dönemler otomatik olarak oluşturulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeaff3c32-9029-4812-8369-1068fb9e3a57)

### **5.1.5. Form Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ **Fonksiyonel Veri Toplama /**Form Tanımlama

Formları tanımlanıp, taslak şablon hallerinin yüklendiği ve uygulama yeri bazında, yetkilerinin verildiği menüdür. Bunun için Fonksiyonel Veri Toplama modülünün sistem altyapı tanımları altından Form Tanımlama menüsüne gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3975baa4-ec18-4624-acaa-e5b9739aa590)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd0b5d1f4-89c6-4fbf-9534-7d7b7fc20f42):Yeni form tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload51ba7728-25b8-4e51-839d-4de51472ddf7):Listede seçili form bilgisi ile **ilgili herhangi bir düzeltme, değişiklik veya güncelleme işlemi yapılır.**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf2ace56a-2f82-4bdc-8e84-2b458e75021d):Listede seçili Form bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload12e60fc7-90ff-4dbe-9488-85a95b1f4a08):Listede seçili formun Şablon tanımlama menüsünü açar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd4d6b8ee-82b7-44c1-b608-14c88bb5952b):Listede seçili form için Yetki Matrisi tanımlama menüsü açarak uygulama yerlerine görüntüleme, yeni kayıt, güncelleme ve silme yetkileri verilmesi işlemini yapar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7b527271-a988-455c-abf2-84cfbcacd1b8):Listede seçili form için Rapor Tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd8824f6e-6d60-4c02-81fc-73253b52e18d):Listede seçili form için Grafik Tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload08be41cf-b6fb-4410-a28f-a6ed77e59e9d) (Yeni) butonuna tıklanarak Form tanımlama ekranı açılarak Form tanımlama işlemine başlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb5f3c917-e7c3-4224-aae4-a242b2fdc3b4)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Tanım:**Form Tanımlama ekranında tanımlanan Formun adı bilgisinin girildiği alandır.

**Açıklama:** Form Tanımlama ekranında tanımlanan Formun varsa açıklama bilgisinin girildiği alandır.

**Kod Şablonu:** Form Tanımlama ekranında tanımlanan Formun kod şablonu bilgisinin girildiği alandır. Veri girişi yapılacak formların kodlarının nasıl olacağı bilgisidir. Ör. ESTD.\#\# kod sablonu sayac değeri 0 girildiğinde tanımlanan Form kodları sırasıyla ESTD.01, ESTD.02….ESTD.99 kadar 2 haneli olacak şeklinde gelmesinin sistem otomatik olarak getirir.

**Kod Sayaç:** Form Tanımlama ekranında tanımlanan Formun kod şablonu sayaç değeri bilgisinin girildiği alandır. Sayaç değeri 1 olduğunda Formu kod şablonu sistem ESTD.02 şeklinde ataması yapar.

**Uygulama Yerleri:** Form Tanımlama ekranında tanımlanan forma Ölçüm yapacağımız yerlerin sistemde tanımlı ölçüm yerleri listesinde seçildiği alandır.

**Dönemsel:** Form Tanımlama ekranında tanımlanan Formun Dönemsel olarak veri girişi yapılması istenirse ilgili check box işaretlendiği alandır. Örneğin Dönemsel veri girişi ilgili check box işaretlenip Dönem kırılımı aylık seçilip aylık bazda veri girişi yapılması sağlanır.

**Dönem Kırılımı:** Form Tanımlama ekranında tanımlanan Formun Dönemsel olarak veri girişi yapılması ilgili check box işaretlendiğinde hangi dönem kırılımım da veri girişinin yapılacağı bilgisinin seçildiği alandır.

**Otomatik Oluşsun:** Form Tanımlama ekranında tanımlanan Formun veri girişin ajan tarafında görev düşmesi için otomatik oluşmasının sağlandığı alandır.

**Onay Politikası:** Form Tanımlama ekranında tanımlanan Form için bir onay akışı tasarlanmak isteniyorsa ve Akış tanımı varsa tanımlanan akış tanımı bilgisinin seçildiği alandır. SAT/BSAT/Konfigürasyon Ayarları/Akış Tanımlama menüsünde Akış Tanımlaması yapılır.

**Onay Talep Mesajı:** Form Tanımlama ekranında tanımlanan Form için bir onay akışı tasarlanmak istenirse bu onay akışı için Onay Talep Mesajı bilgisinin seçildiği alandır. SAT/BSAT/Tanımlar/Mesaj Gövdesi Tanımlama menüsünde Mesaj tanımlama işlemi yapılır.

**Onay Tamam Mesajı:** Form Tanımlama ekranında tanımlanan Form için bir onay akışı tasarlanmak istenirse bu onay akışı için Onay Tamam Mesajı bilgisinin seçildiği alandır. SAT/BSAT/Tanımlar/Mesaj Gövdesi Tanımlama münüsünde Mesaj tanımlama işlemi yapılır.

**Onay Red Mesajı:** Form Tanımlama ekranında tanımlanan Form için bir onay akışı tasarlanmak istenirse bu onay akışı için Onay Red Mesajı bilgisinin seçildiği alandır. SAT/BSAT/Tanımlar/Mesaj Gövdesi Tanımlama menüsünde Mesaj tanımlama işlemi yapılır.

**Onaycı Başlatan ise Onay Geçilmesin:** Form Tanımlama ekranında tanımlanan Form için check box işaretlendiğinde sisteme veri girişi yapıp onaya gönderen personel onaycının kendisi ise onay sürecini atlayarak akış sürecini bir sonraki basamağa geçmesini sağlandığı alandır.

Tanımlayacağımız forma, kod şablonu verip, hangi uygulama yerleri için yetki vereceğimizi belirleriz. Dönemsel seçilirse, dönem kırılımı belirlenip otomatik oluşsuna tıklanıldığında veri giriş zamanı gelen parametreler için ilgili kullanıcının bekleyen işlerine görev otomatik düşer. Dönem seçilmeyip, devam edildiğinde ise ilgili form için görev oluşturma manuel bir şekilde devam edebilir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb34f516c-323c-4a8a-a107-2d067f83465a) (kaydet) butonu ile form kaydedilir. Bu menüde farklı formlar tanımlayıp,

veri giriş görevi düşmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9c872851-25ae-4970-b49f-3ac4aee93db6)

**Şablon Tanımlama;**

Form Tanımlama ekranında listeden form seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1f3895d4-a115-4a7e-9110-4ed97d0598fa) (Şablon Tanımlama) butonu tıklanarak şablon tanımlama menüsü açılır. Veri girişi yapılacak şablonun sisteme yüklendiği kısımdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7d4a868c-c4cf-4940-8ce7-cd1a06a9dc45)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload12b01bb1-4e59-4588-bc77-03af253b2aae):Önceki ekran geri dönülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6d441bea-ce7b-4801-bd3c-a14b8ffedf85):Listede seçili formun rapor şablonu yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3a809521-6b79-4da7-aaf9-a7f2ab9182a9):Listede seçili form yüklendikten sonra kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6d441bea-ce7b-4801-bd3c-a14b8ffedf85) (Rapor yükle) butonuna tıklandığında ilgili formun şablonu yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd9ba87eb-11f8-4890-aa77-24bb68e658b8)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb4d0fc96-c40e-42c1-8512-a153b19f19b2)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0b45e621-7493-4fa8-bed4-5190368e98dc)

QDMSDATA sheetinde raporlamalarda görmek istenilen değerleri formüllenip tanımlanır. Ör: CPL-Ortalama için =Elektrik!G2 değeri aynı şekilde tanım alanın karşılığı değer sutündaki hücreleri formül şeklinde yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6bfe26a8-bc7a-4748-a210-089d5041aa2d)

QDMSINTEGRATION sekmesinde ise, kurumsal veri tabanlarından çekilmesi istenen alanların karşılıkları yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload94ca740f-e2a6-460f-a316-8830a6573b85) (Excele aktar) butonu ile şablonun istenildiği zaman alınabilmesi sağlanmaktadır. Excel Aktar butonu ile veriler Excel aktarılıp, kurumsal veri tabanlarından çekilmesi istenen alanların karşılıkları yazılarakta sistem yüklenmesi yapılır. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload960df4a8-a1fe-41cb-915a-13b20cc27f8c) (Kaydet) butonu ile düzenlenen şablon kaydedilir.

**Yetki Matrisi Tanımlama;**

İlgili şablon seçildikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd4d6b8ee-82b7-44c1-b608-14c88bb5952b) (Yetki matrisi tanımlama) butonu ile daha önceden seçilmiş uygulama yerlerine görüntüleme, yeni kayıt, güncelleme ve silme yetkileri verilir. Kullanıcı, Pozisyon ve kullanıcı grubu bazlı yetkilendirme işlemin yapıldığı kısımdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb70aaad4-e6f8-4418-9dd4-5a1fcefd9f66)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd0b5d1f4-89c6-4fbf-9534-7d7b7fc20f42):Yeni yetki tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload51ba7728-25b8-4e51-839d-4de51472ddf7):Listede seçili yetki bilgisi ile ilgili düzenleme, güncelleme ve değişiklik işlemleri yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf2ace56a-2f82-4bdc-8e84-2b458e75021d):Listede seçili yetki bilgisi silinir

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd0b5d1f4-89c6-4fbf-9534-7d7b7fc20f42)(Yeni) butonu tıklanarak Form Tanımlama- Yetki Matrisi ekranın açılarak Yeni Yetki verme işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload637da577-bdee-47d4-884b-c012401c8280)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Uygulama Yerleri:**Form Tanımlama- Yetki Matrisi ekranında Form ilişkilendirilmiş Uygulama yerleri listesi bilgisinin seçim yapıldığı alandır.

**Yetki Tipi:** Form Tanımlama- Yetki Matrisi ekranında kullanıcı, rol ve kullanıcı grubu bazlı yetkilendirme işlemin yapılması için yetki tipinin seçildiği alandır. Kullanıcı tipi yetkilendirme yapıldığında sistemde tanımlı personel listesinde seçim yapılır. Pozisyon tipi yetkilendirme yapıldığında sistemde tanımlı Pozisyon listesinde seçim yapılır. Kullanıcı Grubu tipi yetkilendirme yapıldığında sistemde tanımlı Kullanıcı Grubu listesinde seçim yapılır.

**Yetkiler:**

**Görüntüleme:** Taslakta veya onaylanmış formların görüntülenmesini sağlar.

**Yeni kayıt**: Veri giriş için görev oluşturma yetkisidir.

**Güncelleme:**Taslakta olan veya onaylanmış formların girilmiş verilerinde güncelleme yetkisidir.

**Silme:** Veri girilmiş formdaki silebilme yetkisidir.

**Rapo**r: İlgili uygulama yeri için Rapor alabilme yetkisidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload24e0c147-4b1e-45c3-8225-6248a0c91acb)

**Rapor Tanımlama;**

Tanımlanan ve yetkisi verilen formlar tamamlandıktan sonra, ilgili form seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload00c909b5-0665-481b-bb8e-2d5c21bd8482) (Rapor tanımlama) butonu ile rapor için yeni bir format oluşturulur. Bu formata QDMSDATA sheetinde yer alan “Alan Tanımlarının” değerlerinin yazılması gerekmektedir. Örnek olarak aşagıdaki Rapor şablonunda \<CPL-Ortalama\>, \<RCM-1-Ortalama\> tag şeklinde yazılmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbd995201-9bf3-4fd7-9296-385ea28ac6a6)

Aşağıdaki alanların tagleri Fonksiyonel Veri Toplama Modülü kapsamında yer alan standart tag bilgileridir. Diğer alanlardaki tag bilgileri kullanıcılar tarafında bilgisi girilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload95427199-0093-4be9-a40f-df7d8a040ffe)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb7fb2465-f547-4858-973c-0205c9e820a2)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd0b5d1f4-89c6-4fbf-9534-7d7b7fc20f42):Yeni bir rapor tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload51ba7728-25b8-4e51-839d-4de51472ddf7):Listede seçili rapor bilgisi ile ilgili düzenleme, güncelleme ve değişiklik işlemleri yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf2ace56a-2f82-4bdc-8e84-2b458e75021d):Listede seçili rapor bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd0b5d1f4-89c6-4fbf-9534-7d7b7fc20f42)(Yeni) butonu tıklanarak Form Tanımlama-Rapor Formatları ekranın açılarak Rapor tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9038fccf-8d11-45da-9f50-829126481bea)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Şablon Adı:**Form Tanımlama-Rapor formatları ekranında Şablon adı bilgisinin girildiği alandır.

**Şablon:** Form Tanımlama-Rapor formatları ekranında Rapor şablonun yüklendiği alandır. Sistemde tanımlanan dil paketlerine göre de rapor şablonu yükleme işlemi yapılır. Ör: İngilizce dil paketine göre sistem rapor şablonu yükleme işlemi yapılır.

**Uygulam Yerlerin Ayrı Raporla:** Form Tanımlama-Rapor formatları ekranında ilgili check box işaretlenirse Rapor şablonun raporu alınırken veri girişi yapılan uygulama yerlerin ayrı ayrı sheetlerde görüntülenmesi sağlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6d441bea-ce7b-4801-bd3c-a14b8ffedf85) (Rapor yükle) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3f37e786-d27b-46cc-b0fa-71fc502501db)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5f526481-6368-4fa7-aae6-565c0776f664)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload75269a6a-ecb5-4de8-bf32-03bf4dff951b)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8d0a50be-6b23-43ea-800a-2fab5ef71ad7)

Rapor tanımlama butonuna tıkladıktan sonra yeni kayıt butonu ile açılan sayfada, şablon adı verilip, şablon excel yüklenir. Aşağıda örnek excel formatı yer almaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbd995201-9bf3-4fd7-9296-385ea28ac6a6)

Tanımlanan rapor menüsü için Yetki Grupları Tanımlama menüsünden ilgili kullanıcılar için menü görme yetkisi verilir. Ardından, Entegre Yönetim Sistemi/Fonksiyonel Veri Toplama/

/Raporlar/İlgili Form seçilerek raporun Excele alınması sağlanır.İlgili rapor seçildiğinde, raporu alınmak istenen uygulama yeri ve tarih aralığı belirlenip, ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9bbd8f41-073a-4e86-98a1-391131241d7d) (Excel Aktar)butonu ile excele aktarılır.

Entegre Yönetim Sistemi\>Fonksiyonel Veri Toplama\>Raporlar\>Elektrik Su Tüketim Değerleri Formu\>Elektrik Tüketim Değerleri Raporu menüsü tıklanılır. Raporun alınması için (**Raporun alınması için:**Entegre Yönetim Sistemi\>Fonksiyonel Veri Toplama\> Elektrik Su Tüketim Değerleri menüsünde Formla ilişkilendirilmiş uygulama yerleri için veri girişlerin yapılması gerekmektedir.)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload96ba1640-1f13-43c1-8fcf-1b371c3900fb)

Açılan Raporlar-Elektrik Su Tüketim Değerleri Formu-Elektrik Tüketim Değerleri Raporu ekranıda İlgili Dönem alanında Takvim alanında raporun alınacağı tarih belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfc103bf0-27bd-4e7f-8cce-9f076f0201e7) Açılan ekranda Uygulama Yeri seç alanında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf61565da-186c-4fa7-8005-d7bf706dc5c9)(Ekle) butonu tıklanarak tanımlı form ilişkilendirilen uygulama yerleri listesinde seçim yapılır. Uygulama yerleri listesinde formla ilişkilendirilmiş uygulama yerleri gelir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload47155cc4-2f40-4b43-aca7-788d3cce8b26)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc9068720-1463-40e8-af2f-320878af4ba1) (seç) butonu tıklanarak uygulama yerleri seçim yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade2c2329b-75d9-41e1-b7ae-c9bfd9d00a9e)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2100c2cc-7be3-4880-8813-8229220defbe)(Excel Aktar) butonu tıklanarak seçim yapılan uygulama yerleri için veri girişleri form için Excel Formatında rapor alınması sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4ad2c7da-ece7-4b71-bff6-c0147f0c95b5)

Rapor tanımlama ekranında “Uygulama yerlerin ayrı ayrı raporla” check box işaretli olduğu için ayrı sheetlerde uygulama yerlerin raporu Excel Formatında alınır.

**Grafik Tanımlama;**

Grafik formatları oluşturmak için; form tanımlama menüsünden, ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload545fc4b0-921e-4470-ab60-544490b19576)(Grafik Tanımlama) butonuna giriş yapılır.Grafik tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload82d46403-216f-44ae-b677-dad142426fe5)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd0b5d1f4-89c6-4fbf-9534-7d7b7fc20f42):Yeni grafik tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload51ba7728-25b8-4e51-839d-4de51472ddf7):Listede seçili grafik bilgisi ile ilgili düzenleme, güncelleme ve değişiklik işlemleri yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf2ace56a-2f82-4bdc-8e84-2b458e75021d):Listede seçili grafik bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd0b5d1f4-89c6-4fbf-9534-7d7b7fc20f42)(Yeni) butonu tıklanarak Form Grafik Tanımlama ekranı açılarak Grafik tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload82a4d06e-59cd-4144-bc45-f4dbdbc2b5fc)

Alan Tanımı ve Alan Kısaltmasını alanların bilgisi girilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf61565da-186c-4fa7-8005-d7bf706dc5c9) (Ekle) butonu ile Alanlar alanı kısmına eklenir. Tüm alan Tanımı ve Alan Kısaltmaları bilgileri girildikten sonra Alan Tanımı ve Alan Kısaltması alanları zorunlu alan olduğu için herhangi veri girilmesi gerekmektedir. Boş bırakılmamalıdır.Ör: Alan tanımı ve Alan Kısaltması kısmına “X” değerinin girilmesi.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9ba6cfc4-8cc5-41f9-9bd3-112769d93f11)

Grafik adı verilip, kıyaslama yapılacak alan tanımı yazılır. Alan kısaltması QDMSDATA sheetinden alınır. Aylık girilen değerlerin yıl bazında raporlaması istendiğinde, birikim yöntemi alanından ortalama, toplam vb. değerler seçilir. Rapor alınması istenen parametre, hangi ölçüm yerleri için kıyaslanması gerekiyorsa, uygulama yerlerinden ilgili olanları seçilir ve kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload626282a6-c593-4833-b0b9-483002536caf)

Tanımlanan grafik için SAT\>BSAT\>Tanımlar\>Yetki Grupları menüsünde menü görme yetkisi verildiğinde Entegre Yönetim Sistemi\>Fonksiyonel Veri Toplama\>Grafikler menüsü altında görüntülenmesi sağlanır. **(Grafiğin alınması için:**Entegre Yönetim Sistemi\>Fonksiyonel Veri Toplama\> Elektrik Su Tüketim Değerleri menüsünde Formla ilişkilendirilmiş uygulama yerleri için veri girişlerin yapılması gerekmektedir.) Oluşturulan grafik altyapıları, Entegre yönetim Sistemi / Fonksiyonel Veri Toplama / Grafikler menüsünden ilgili grafik seçilir. Açılan Grafikler ekranında Grafikler sekmesi tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload71d6e93f-3075-43de-bcf0-b5ab84504b00)

Grafikler sekmesinde Grafikler alanında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf61565da-186c-4fa7-8005-d7bf706dc5c9)(Ekle) butonu tıklanarak form için tanımlanan grafik seçimi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload11d5e24f-264b-48aa-9c62-8f7ba1148526)

Raporlanmak istenilen tarih aralığı belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc2c58bdb-a1f5-4ea2-89d3-6185db2a7da3)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2c83ed90-b46e-4476-8c33-d87430e9bd22)(Filtreleme) butonu tıklanarak grafiğin ekranda görüntülenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbbdfc076-0709-439b-88c6-710a5fdaedbd)

Ekrana yansıyan grafikler ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb289956d-057d-4797-ad82-b7a009c4298c)(Excel Aktar) butonu tıklanarak grafiğin Excele aktarılması ile Excel formatında grafiğin alınması sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade75dcf19-35dc-479b-bc40-79d76d3d7314)

**Fonksiyonel Veri Toplama Modülünde tanımlanan forma menü yetkisi verilmesi:**

Fonksiyonel Veri Toplama Modülünde tanımlanan formun Entegre Yönetim Sistemi modülünde görüntülenmesi SAT\>BSAT\>Tanımlar\>Yetki Grubu Tanımlama menüsünde menü görme yetkisi verilmesi gerekir.Ayrıca tanımlanan rapor ve grafikler için de Yetki Grupları menüsünde menü görme yetkisi verilmedir. Aksi takdirde Entegre Yönetim Sistemi/Fonksiyonel Veri Toplama modülünde menü olarak tanımlanan form, grafik ve raporlar görüntülenmez. SAT\>BSAT\>Tanımlar\>Yetki Grubu Tanımlama menüsü tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0e0f4783-4ec4-4a64-8701-3c8d74da73d8)

Açılan ekranda listeden kullanıcı grubu seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload51ba7728-25b8-4e51-839d-4de51472ddf7)(Değiştir) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload485cc55d-2ca6-4a5c-8991-8bf91749a7e2)

QDMS Yönetim Sistemi- Kayıt Güncelle ekranında Modül olarak Fonksiyonel Veri Toplama modülü seçilerek tanımlanan form, rapor ve grafik seçimi yapılarak menü görme yetkisi verilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3166687c-e68f-4181-973f-58d3784e4974)(kaydet) butonu tıklanılır.

### **5.1.6. Alan Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ **Fonksiyonel Veri Toplama /**Alan Tanımlama

Formlar için ekstra açıklama, ek dosya vb. alanların girilmesi isteniyorsa, alan tanımlama yapılır. Tanımlanan alanlar alan havuzuna eklenir.Bunun için Fonksiyonel Veri Toplama modülünün Sistem Altyapı Tanımları altından Alan Tanımlama menüsüne gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadde9894af-88c6-4024-84a1-0047632f5257)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd0b5d1f4-89c6-4fbf-9534-7d7b7fc20f42):Yeni alan tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload51ba7728-25b8-4e51-839d-4de51472ddf7):Listede seçili alan bilgisi düzenleme, güncelleme ve değiştirme işlemleri yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf2ace56a-2f82-4bdc-8e84-2b458e75021d):Listede seçili alan bilgisi silinir.

Listeye yeni bir alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8ad113be-ab1d-474a-933b-679f01169be7) (Yeni) butonu tıklanarak Alan Tanımlama/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2e96734b-95c7-4d55-bb69-5a37e21136a1)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Alan Kodu:** Alan kodu bilgisi tanımlanır. Daha önce tanımlamış alanlarla aynı olmayacak şekilde boşluk, Türkçe karakter gibi karakterler kullanmadan tanımlanmalıdır. Ör. ‘001’ , ‘RK’

**Alan Adı:** Alan adı bilgisi tanımlanır.

**Başlık Notu:** Alanın başlık notu bilgisi tanımlanır.

**Giriş Tipi:** Oluşturulan alanda kullanıcı tarafından veri girişi/seçim mi yapacağı ya da hesaplama yöntemi ile otomatik olarak sistem tarafından mı atanacağı belirlenir.

**Alan Tipi**: Oluşturulan alanın metin, numerik, tarih, liste vb. alan tiplerinden hangisi olacağı belirlenir.

**Görünme Şartı:** Tanımlama işlemi devam eden alanın daha önceden tanımlanan başka bir alanın değerine göre görünüp görünmeyeceği belirlenir. Kullanımı [ALANKODU]=ALAN_DEĞERİ vb. şekildedir. (Örneğin, Fırsat var mı? Alanının alan kodu 01; Fırsat alanının alan kodu 02 olsun. Eğer “Fırsat” Alanının, “Fırsat var mı?” Alanındaki seçeneklerden değer kodu 100 olan “Evet” değeri seçili ise görülmesi gerekiyorsa 02 numaraları “Fırsat” alanının görünme şartı bölümüne formül şu şekilde yazılmalıdır: [01]=100)

**Durum:** Alan durumu aktif veya pasif olarak seçilir.

**Genişlik:** Alanın kolon genişliği bilgisi tanımlanır.

Alan tanımlama ekranında gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3166687c-e68f-4181-973f-58d3784e4974) (Kaydet) butonu tıklanarak kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd5778c7d-872d-4ef5-baff-3bdab10bd7c4)

**Sistemde mevcut bulunan alan tiplerinin tam listesi aşağıda belirtilmiştir;**

**Metin:** Elle yazım imkanı veren metin kutucuğu ekler.

**Metin Çok Satırlı:** Elle yazım imkanı veren karakter sınırı olmayan çok satırlı metin kutucuğu ekler.

**Nümerik:** Sayısal olarak veri girişi yaptırır.

**Nümerik-Parasal:** Parasal değer olarak nümerik giriş yaptırır.

**Nümerik-Birim:** Birim olarak nümerik giriş yaptırır.

**Tarih:** Takvim alanı ekler.

**Liste:** Birden fazla element arasından tek seçim yaptırır.

**Puanlı Liste:** Açılır menüden seçim yaptırır, liste elementlerinin puan değerleri mevcuttur.

**Arama Özellikli Liste:** Birden fazla element arasından geniş arama fonksiyonuyla arama yapabilecek şekilde, tekli ve/veya çoklu seçim yapılmasını sağlar.

**Ağaç Liste:** Ağaç kırılımına sahip birden fazla element arasından geniş arama fonksiyonuyla arama yapabilecek şekilde seçim yapılmasını sağlar.

**Personel:** QDMS personel veri tabanından kişi seçilebilmesini sağlar.

**Departman:** QDMS departman veri tabanından departman bilgisi seçilebilmesini sağlar.

**Unvan:** QDMS unvan veri tabanından unvan bilgisi seçilebilmesini sağlar.

**Doküman:** QDMS doküman veri tabanından doküman seçilebilmesini sağlar.

**Süreç:** QDMS süreç veri tabanından süreç seçilebilmesini sağlar.

**Yönetim Sistemi:** QDMS yönetim sistemi veri tabanından yönetim sistemi bilgisi seçilebilmesini sağlar.

**Müşteri:** QDMS müşteri veri tabanından müşteri bilgisi seçilebilmesini sağlar.

**Tedarikçi:** QDMS tedarikçi veri tabanından tedarikçi bilgisi seçilebilmesini sağlar.

**Ürün Grubu:** QDMS ürün grubu veri tabanından ürün grubu bilgisinin seçilebilmesini sağlar.

**Ürün:** QDMS ürün veri tabanından ürün bilgisinin seçilebilmesini sağlar.

**Şirket Profili:** QDMS şirket profili veri tabanından şirket profili bilgisi seçilebilmesini sağlar.

**Başlık:** Formlara koyu harflerle yazılacak başlık alanı ekler.

**Dosya:** Dosya eklemesi için uygun alan getirecektir

**Resim:** Resim eklemesi için uygun alan getirecektir

**Resim Liste:** Resim listesinden seçim sağlar.

**Çoklu Resim:** Çoklu resim seçilmesini sağlar.

**Tablo:** Tablo tipli alan oluşturulmasını sağlar. (Bu tip bir alan eklendikten sonra alan değerleri olarak yeni alan tanımlamalarının yapılması gereklidir.)

**Sorgu:** QDMS/Ensemble veri tabanları içerisindeki ana verilerden seçim yapılabilmesi için tanımlanabilen alan türüdür. (Sadece Bimser Destek Ekibi tarafından tanımlanmalıdır) Tekli ve çoklu seçim yapılabilir.

**Sorgu Ağaç:** QDMS/Ensemble veri tabanları içerisindeki ağaç kırılımlı ana verilerden seçim yapılabilmesi için tanımlanabilen alan türüdür. (Sadece Bimser Destek Ekibi tarafından tanımlanmalıdır) Tekli ve çoklu seçim yapılabilir.

**Sekme:** Mevcut risk değerlendirme formunda alanların bulunduğu sekmenin haricinde alanların ilişki kurularak içerisinde görülebileceği yeni bir sekme oluşturur.

**Onay Kutusu Liste:** Talebe göre tekli veya çoklu seçim yaptırılacak tipte bir liste tipli alandır.

**Risk:** Risk tabanlı modüllerden değerlerin seçilebilmesini sağlar. Bu tip bir alan eklendikten sonra hangi modülden değerlerin geleceği alan tanımlama ekranında seçilmesi gereklidir.

**Açıklamalı Liste:** Seçilen liste değerinin yanına açıklama yazabilme imkanı sağlayan alan tipidir. Alan Tanımlama menüsünde alan değerleri tanımlanırken her değer için açıklama kutucuğunun aktif olup olmayacağının seçilmesi gerekir. Burada yapılan seçime göre Entegre Yönetim Sistemi menüsü altında bu alanın görüleceği menüde ilgili seçim yapıldığında alan değerinin yanına kullanıcının açıklama yazabilmesi için kutucuk açılmış olur.

**Pozisyon:** QDMS pozisyon veri tabanından pozisyon bilgisi seçilebilmesini sağlar.

**Saat:** Saat tipli alan ekler.

### **5.1.7. Fonksiyon Dizayner**

**Menü Adı:** Sistem Altyapı Tanımları/ **Fonksiyonel Veri Toplama /**Fonksiyon Dizayner

Fonksiyon Dizayner özelliği ile alan havuzuna eklenen alanlar Fonksiyonel Veri Toplama modülünün istenilen formların sayfaları ile ilişkilendirilebilir. Fonsiyonel Veri Toplama modülü kapsamında veri girişi yapılacak tanımlanan formlar bu menüde fonksiyon olarak listenir. Listenen bu formlar tanımlanan alan tanımlama menüsündeki alanlar ilişkilendirilip , bu alanların tanımlanan formlarının sayfalarında görüntülenmesi sağlanır.Bunun için Fonksiyonel Veri Toplama modülünün Sistem Altyapı Tanımları altından Fonksiyon Dizayner menüsüne gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc7241471-0770-45e3-81e9-f4c682febe45)

İlgili form seçilerek, ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d9d57d6-3900-4ada-a46e-c9ade16076d6) (Alanlar) butonu ile formların detaylarında kullanılacak “Alanlar” belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload08762257-596a-4e61-b0f4-8daa3f07530c)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada8fe8d2e-e550-4b87-b061-69865d458cb7): Yeni bir fonksiyon eklenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6959fa7e-9f42-4f16-b645-aa1a77cc1231): Listede seçili fonksiyon bilgisi değiştirilir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbc6f3769-e4ad-4281-8bd6-71fbbfccc125): Listede seçili fonksiyon bilgisi silinebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5dea5362-19c2-4098-8088-4a36f6ea6aaf): Önceki ekrana geri dönülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d9d57d6-3900-4ada-a46e-c9ade16076d6)(Alanlar) butonu ile açılan ekranda seçili fonksiyonda kullanılacak alanlar ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8ad113be-ab1d-474a-933b-679f01169be7)(Yeni) butonuna tıklanarak belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d38cb2c-767d-42a0-985d-0cd8417013be)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Alan Adı:** Alan tanımlama ekranında tanımlanmış alanlardan alan seçimi yapılır.

**Zorunlu Mu? :** Alanın zorunlu olup olmadığı seçilir. (Statü kullanımı olmadığında görülecektir.)

**Zorunluluk Mesajı:** Zorunlu alan doldurulmadığında verilecek uyarı mesajı bilgisi bu alana yazılır.

**Sıra No:** Alanın sıra no belirlenir.

**Gridde göster:** Alanın gridde gösterilmesi gerekiyorsa ilgili check box işaretlenir.

**Satır Sayısı:** İlgili alan çoklu satır ise, veri girişi ekranında kaç satır gözükmesi gerektiği belirlenir.

Açılan ekranda alan bilgileri listeden seçilir, zorunlu bir alan ise kullanıcının bu alanı doldurmadığında karşısına çıkacak mesaj tanımlanır (Olasılık alanı zorunludur vb.), sıra numarası belirlenir. Zorunlu olup olmadığı, gridde gösterilip gösterilmeyeceği, kolon genişliği belirlenerek gerekli tüm alanlar doldurulduktan sonra ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload35f69373-0a85-4fb2-b552-cb1f81a4a5dd) (Kaydet) butonu tıklanarak, ilgili alan için fonksiyon ile ilişkilendirme işlemi gerçekleştirilir. Gerekli olan tüm alanlar bu şekilde ilgili fonksiyona eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload10cf1736-9302-4312-ac15-8bf351df071a)

### **5.1.8.Genel Rapor Formatları Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/ **Fonksiyonel Veri Toplama /**Genel Rapor Formatları

Birden fazla formun verilerinin tek bir excel raporunda gözükmesini istenilen durumlar için genel rapor formatları tanımlanır. Örnek olarak, atık formunda bir alanın ve Rapor Şablonu Elektrik Su Tüketim formundaki bir alanın QDMSDATA sheette yer alan, değer tanımları \<CPL-Ortalama\> örnekteki benzer çalışma gibi alınarak excel şablon formatına yazılır. Fonksiyonel Veri Toplama modülünün Sistem Altyapı Tanımları menüsünden Genel Rapor Formatları tanımlama menüsüne giriş yapılarak, tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf669b35c-c6c4-4f1f-b3ce-2e153b260c98)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7db86ff8-2a05-442a-b3b9-68fa689edeaf)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd0b5d1f4-89c6-4fbf-9534-7d7b7fc20f42):Yeni bir rapor formatı tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload51ba7728-25b8-4e51-839d-4de51472ddf7):Listede seçili rapor formatı bilgisi üzerinde düzenleme, güncelleme, değişiklik yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf2ace56a-2f82-4bdc-8e84-2b458e75021d):Listede seçili rapor formatı bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd0b5d1f4-89c6-4fbf-9534-7d7b7fc20f42)(Yeni) butonu tıklanarak Form Tanımlama-Rapor Formatı ekranın açılarak Rapor formatı tanımlama işlemi yapılır.

Örnek Rapor Formatı şablonu; Rapor formatı şablonu Elektrik Su Tüketim formundaki bir alanın QDMSDATA sheette yer alan, değer tanımları \<CPL-Ortalama\>,\<RCM-1-Ortalama\> tag şeklinde rapora eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload81f4ad0a-53cd-44ed-86e5-067e889ef681)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd6c84752-1b18-446b-92a7-894eae1d5ccb)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Şablon Adı:**Form Tanımlama-Rapor formatları ekranında Şablon adı bilgisinin girildiği alandır.

**Şablon:** Form Tanımlama-Rapor formatları ekranında Rapor şablonun yüklendiği alandır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6d441bea-ce7b-4801-bd3c-a14b8ffedf85) (Rapor yükle) butonuna tıklandığında ilgili formun şablonu yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3ce7430d-418d-4810-adca-77320b8ddee8)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf7c9603d-c97b-4df9-b5c7-90aee32e19a4)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4eb842f0-f143-4051-9c0d-4c840c12b699)

Form Tanımlama-Rapor Formatları ekrnanında rapor adı verilip oluşturulan rapor formatı yüklenip kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc853415d-d2d4-4808-b489-45b7d8d6aeab)

Tanımlanan bu rapor menüsü ilgili kullanıcı ve yetki grupları için SAT/BSAT/Tanımlar/Yetki grupları düzenleme menüsünden menü görme yetkisi verilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1372881a-b6b3-4437-aba0-cc6c2aeebb3b) QDMS menülerinde Entegre Yönetim Sistemi\>Fonksiyonel Veri Toplama\>Raporlar\>Genel Raporlar menüsünde gözükmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd51b1141-9a02-4634-a9f0-3312efb97272)

Açılan Raporlar-Genel Rapor Formu ekranında ilgili Dönem Takvim alanında seçilerek , Uygulama Yeri Seç alanında sistemde tanımlı uygulama yerleri listesinde seçim yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0d956f60-c0fc-4e65-938a-b6a0e7580132)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2100c2cc-7be3-4880-8813-8229220defbe)(Excel) Aktar butonu tıklanarak birden fazla formun Excel formatında raporun alınması sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload107dbda0-1fb3-4905-ac09-13b433f0851a)

### **5.1.9. E-Posta Ayarları**

Veri girişleri onaylandıktan sonra mail gitmesi istenen roller için mail ayarlarının yapıldığı menüdür. Bunun için Fonksiyonel Veri Toplama modülünün Sistem Altyapı Tanımları altından E-Posta Ayarları menüsüne gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd64fc5f1-ad0e-4664-8f49-20e69c91e150)

İlgili form seçildikten sonra, ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload51ba7728-25b8-4e51-839d-4de51472ddf7) (Değiştir) butonu ile mail düzenleme menüsüne giriş yapılır. İlgili roller ve mesaj gövdeleri belirlenerek kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf3eabba3-44f3-46e1-a07e-0004f3aea77b)

### **5.1.10. Parametreler**

**Menü Adı**: Sistem Altyapı Tanımları/Fonksiyonel Veri Toplama/ Parametreler

Fonksiyonel Veri Toplama Modülünün kullanıcının istek ve ihtiyaçlarına göre sistemsel ayarlarının yapıldığı ve bunlara göre parametreleri belirlendiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfe078b69-ed05-482b-8dc8-e0297734045f)

**Ekrandaki bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6959fa7e-9f42-4f16-b645-aa1a77cc1231): Listede seçili parametre değiştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload96b0512d-8797-4e99-aeb7-3f9f38d2b1df): Kayıtlar filtrelenerek arama yapılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload94ca740f-e2a6-460f-a316-8830a6573b85): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7a96ce9f-6d74-4bdb-a4fb-53d36dd21554)

## **5.2. Entegre Yönetim Sistemi/ Fonksiyonel Veri Toplama Modülü**

Fonksiyonel Veri Toplama modülü kapsamında tanımlanan formlara veri girişlerinin yapıldığı, tanımlanan rapor ve grafiklerin görüntülendiği kısımdır.

### **5.2.1.Elektrik Su Tüketim Değerleri(Fonksiyonel Veri Toplama Modülünde Altyapıda Tanımlama Form)**

Manuel veri girişi yapılması istenen formlar için görev oluşturulabilir. Görevler otomatik olarak oluşsun istenirse form tanımlamada belirlenebilir. Otomatik oluşan görevler bekleyen işlerde Taslakta Bekleyen olarak yer alacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload59846da9-f135-42cf-ac4d-03cb89a7be2a)

Manuel veri girişi yapılmak istenen form seçilir. Formlar listesinde daha önceden oluşturulmuş uygulama yerlerine ait aktif, onay ve taslak statüdeki kayıtlar yer almaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade39b8d3f-b9f7-4c01-b5d8-86ddbc428cbe)

**Ekrandaki butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd0b5d1f4-89c6-4fbf-9534-7d7b7fc20f42): Yeni form oluşturulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload51ba7728-25b8-4e51-839d-4de51472ddf7): Listedeki seçili form bilgisi düzenlenir/ güncellenir. Doldurulan formda düzenleme(yanlış veriyi düzeltme) ihtiyacı olursa, sistem yöneticisi ile iletişime geçilir. Sistem yöneticisi tarafından ilgili kullanıcıya güncelleme yetkisi verilerek, formlarda güncelleme yapılabilir.

Bu buton ile Taslak veya Onay statüsünde yer alan formlarda değişiklik yapılabilir. Daha önceden onaylanmış formlarda değişiklik yapılmasının istendiği durumlar için de kullanılabilmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload655c1b80-7bcc-4737-89c9-01e1d29f32c2):Listede seçili form bilgisi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb68e5eca-a00a-45c0-badf-45c8a87fc0fe):Listede seçili form bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload96b0512d-8797-4e99-aeb7-3f9f38d2b1df): Kayıtlar filtrelenerek arama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload94ca740f-e2a6-460f-a316-8830a6573b85): Veriler Excel’ e aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd0b5d1f4-89c6-4fbf-9534-7d7b7fc20f42)(Yeni) Butonu tıklanarak yeni bir form oluşturmak için Yeni Form- Elektrik Su Tüketim Değerleri ekranın görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload84f72a67-d27c-45d6-bf7d-99a9939641b6)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Form Kodu:**Form kodu bilgisi sistem tarafından otomatik verilir. Sistem Altyapı Tanımları/Fonksiyonel Veri Toplama/Form Tanımlama menüsünde Yeni butonu tıklanarak açılan Form Tanımlama ekranında Kod şablon ve Kod sayacı bilgisi alanları tanımlandığı için sistem tarafından otomatik verilir.

**Uygulama Yeri:**Uygulama yerleri bilgisinin seçildiği alandır. Sistem Altyapı Tanımları kısmında Form Tanımlama menüsünde ilişkilendirilen uygulama yerleri liste halinde gelir ve seçim yapılır.

**İlgili Dönem:** Veri girişinin yapılacağı ilgili dönem bilgisi takvim alanında seçimin yapıldığı alandır.

Uygulama yeri veri girişi yapılacak dönem seçilip, ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload77ab123e-a35e-4cff-bdd4-269e1c588b9f)(ileri) butonu tıklanılır ve Form Düzenleme-Elektrik Su Tüketim Değerleri -Kocaeli Genel Merkez Ofis için veri girişi yapılacak ekran açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7b0cfdd3-ca3e-4c1f-95e7-f08077825387)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8a315f56-8ce9-4db3-b232-5cf15209c16b):Önceki ekrana geri dönülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2b99df81-c422-46e2-90a5-710b9bc686a2):Form Taslak olarak kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf77aff35-c4d1-44b2-bd31-5ef5ee3f35e2):Kaydet butonu kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5fddce73-5cd0-4872-b5bb-b9c7e190547f):Veriler Excel Aktarılır.

Formdaki veri girişi yapılacak hücreler doldurulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc8d851dc-55d4-4962-8a89-c418ccfb1e6d)

Detaylar sekmesinde alan tanımlamada tanımlanan alanların fonksiyon Dizanyer menüsünde ilgili formla ilişkilendirilip, bu sekmede görüntülenmesi sağlanır. Örnek: Dosya tipli parametrik alan eklenmesi

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade4b1a5d8-a499-47cb-905b-cb08ff9016e6)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf61565da-186c-4fa7-8005-d7bf706dc5c9):Yeni bir dosya eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada7cd74cc-cfed-4016-a68e-96f23341e8a5):Listede seçili dosya bilgisi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadab406743-706e-4f91-bd9b-6ffd0f947b05):Listede seçili dosya bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf61565da-186c-4fa7-8005-d7bf706dc5c9) (Ekle) butonu tıklanarak istenirse forma bir ek dosya yükleme işlemi yapılır. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada7cd74cc-cfed-4016-a68e-96f23341e8a5)(görüntüle) butonu ile eklenen ek dosya görüntülenir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadab406743-706e-4f91-bd9b-6ffd0f947b05)(Sil) botunu ile listede seçili Dosyanın silinmesi sağlanır.

Önlemler sekmesinde veri girişi yapılan form için gerektiği durumlar önlem alınması sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadee21d492-65e4-4b9f-ba7e-4f669e7f57ea)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6c13ec4c-2fa6-4f4f-82ae-c3ba23c1340b): Yeni bir önlem tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload40f6ee2c-785a-4522-8de5-74a5598584e5): Listede seçili önlem bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbc6f3769-e4ad-4281-8bd6-71fbbfccc125): Listede seçili önlem bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada4d69379-c6dc-44f2-83bd-7783b2c28ecd): Listede seçili önlem bilgisi görüntülenir.

Önlemler sekmesine gelindiğinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadef14823f-1969-4164-90fa-b98320acd2af) (Yeni) butonuyla yeni önlem girişi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec7c35a2-e6b7-4e8a-bfaf-03009ea58b1e)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Referans Tipi:** Referans Tipi bilgisi aksiyon ve doküman seçilebildiği alandır. Referans tipi listeden seç seçeneği seçilirse referans tipi bilgisi listeden seçilir. Referans tipi yeni oluştur seçeneği seçilirse referans tipi bilgisi yeni oluşturulur.

**Referans Bilgisi:** Referans tipi aksiyon ve doküman olarak seçildiğinde ilgili referans kayıt seçilir.

**Önlem Tipi:** Mevcut veya planlanan olarak seçilir.

**Önlem Tarihi:** Önlem tarihi bilgisi seçilir.

**Açıklama:** Açıklama bilgisi tanımlanır.

Açılan ekranda referans tipi açılır menüsünden önlemin türü seçilir. ( aksiyon, doküman, ). Daha sonra önlem tipi (mevcut, planlanan) ve önlem tarihi belirlendikten sonra önlemin açıklaması girilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3166687c-e68f-4181-973f-58d3784e4974) (Kaydet) butonu tıklanarak kayıt işlemi gerçekleştirilir.

Referans tipi olarak Doküman ve aksiyon seçilirse, QDMS’teki Doküman ve aksiyon modülleri ile bağlantı kurulacaktır. Mevcut açılmış Doküman ve aksiyonlardan herhangi biri önlemle ilişkilendirilebileceği gibi, yeni kayıtta açılabilir. Referans tipi olarak doküman seçilirse, QDMS’teki doküman ağacından doküman seçilir.

Örneğin önlem türü olarak aksiyon seçilir, listeden seç ve yeni oluştur seçeneklerinden yeni oluştur seçeneği seçilerek aksiyon oluşturulursa aşağıdaki şekilde aksiyon modülü ile bağlantı kurulur. Not: Fonksiyonel Veri Toplama Modülü için Aksiyon Tanımlama işleminin yapılması için SAT\>Fonksiyonel Veri Toplama\>Parametreler menüsünde önceden Aksiyon Modülü ilgili parametrelerde sistemsel ayarlamaların yapılması gerekmektedir. 15 numaralı “FVT Form önlemi için Ana Aksiyon No” parametresi için Aksiyon Modülünde bir Ana aksiyon planı kodunun tanımlı olması gerekmektedir. EYS\>Aksiyon Yönetimi\>Planlama menüsünde yeni bir aksiyon planı tanımlanır veya mevcut aksiyon planın kodu parametre seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload40f6ee2c-785a-4522-8de5-74a5598584e5)(Değiştir) butonu tıklanarak parametre içeriği görüntülenerek parametre değerine bu kod yazılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3166687c-e68f-4181-973f-58d3784e4974)(Kaydet) butonu tıklanarak tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1a2ed210-f9fe-4159-948a-d39a8ea1688d)

Aksiyon Bilgileri sekmesi Aksiyon ile ilgili bilgilerin girildiği sekmedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload257282a1-ecf2-429d-bc45-162daf46a0a1)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada0b51b6f-2190-499a-8276-6951168d639e)

Gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3166687c-e68f-4181-973f-58d3784e4974)(Kaydet) butonu tıklanarak form için Önlem olarak bir aksiyon tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6e8a4794-4f36-40b6-b25f-9aa5657e8d7f)

Formdaki veri girişi yapılacak hücreler doldurulur. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb34f516c-323c-4a8a-a107-2d067f83465a) (Taslağı kaydet) butonuna tıklanıldığında bekleyen işlerimde taslak formlar olarak duracaktır. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload11cbb6cd-9a8c-4b72-a720-52cc4c2a0de8) (Kaydet) butonuna tıklandığında ise onaya düşecektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd149b752-5e0b-4b97-8db7-cab9a199af65)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4d71d468-7df4-4223-b630-40295cb8ecf1)

Onayda bekleyen formlar bekleyen işlerime “Onay Bekleyen Formlar” olarak görev olarak iş düşer. Form kodu linki tıklanıp onay ve red işlemlerinin yapılacağı ekran açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6327d20f-a5a3-4ae2-a4a1-0127573e71f0)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload11cbb6cd-9a8c-4b72-a720-52cc4c2a0de8) (Onayla) butonuna tıklandığında form statüsü “Aktif” olarak gözükecektir. Onay aşamasında onaycılar, form verilerinde değişiklik yapabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadafd3587d-6270-45f6-8aa9-82bbe4f95760)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2a2176d7-7105-49ea-986e-bdf064e57dd3)

Ret butonuna tıklandığında, onay notu açıklaması ekranında ret nedeni yazılmalıdır. Bu şekilde uygulama yerleri ile ilişkisi kurulan formların veri giriş işlemleri yapılarak statü aktif duruma getirilir.

### **5.2.2.Grafikler**

**Menü Adı:** Sistem Altyapı Tanımları/ **Fonksiyonel Veri Toplama /**Grafikler

Fonksiyonel Veri Tanımlama Modülün menü yetkisi tanımlanan formu için tanımlanan menü yetkisi verilen grafiğin raporun alındığı menüdür.Açılan Grafik Raporları ekranında iki sekme karşımıza çıkar. Bu sekmeler Grafikler ve Filtre sekmelerdir.

**Grafikler sekmesi;**

Grafikler sekmesinde Grafikler alanında sistemde tanımlı menü yetkisi verilen grafik Grafikler alanında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload477c4357-cc66-411c-9da2-f4b5d9879bfd)(Ekle) butonu tıklanarak grafik seçimi ile , ilgili dönem alanında takvim alanında tarih seçimi yapılarak , Dönem kırılım alanında ilgili dönem kırılım seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload96b0512d-8797-4e99-aeb7-3f9f38d2b1df)(Filtreleme) butonu tıklanarak grafik raporu alınması sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd8e67ec9-5c70-4a56-84a3-f3894dc91461)

**Filtre sekmesinde;**

Filtre sekmesinde grafik ayarlama seçeneklerine olarak yer alan alanlara göre istenilen grafik alınır. Örneğin Grafik Tipi Bar ve PieChart seçeneğinde seçim yapılarak seçim tipinde grafik raporu alınması sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload03f3f9bc-f0e3-4e13-8c47-f655b71826d1)

Grafikler alanında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload477c4357-cc66-411c-9da2-f4b5d9879bfd)(Ekle) butonu tıklanarak Grafikler alanında grafik seçimi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload603f7945-7698-4e00-90c3-4efee094cbab)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload96b0512d-8797-4e99-aeb7-3f9f38d2b1df)(Filtrele) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload559aceba-9669-4e51-989b-7bc9409780d2)

Dönem Kırımlı Bazlı alanı ilgili check box işaretlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c646ec3-77a2-4b73-98fc-3c457cc0d639)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload96b0512d-8797-4e99-aeb7-3f9f38d2b1df)(Filtrele) butonu tıklanarak Dönem Kırımlı Bazlı Grafik alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2d0fbe26-1d32-4bc7-8080-631f01f504af)

Filtre sekmesi tıklanarak Grafik tipi alanında Grafik tipi PieChart seçeneği seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload96b0512d-8797-4e99-aeb7-3f9f38d2b1df)(Filtreleme) bu grafik tipinde Grafik Raporu alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload621ee319-2d23-490a-836d-320643eb4704)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1fcecd94-5501-45e7-b204-4ab271d7c7ae)

### **5.2.3.Raporlar**

**Menü Adı:** Sistem Altyapı Tanımları/ **Fonksiyonel Veri Toplama /**Raporlar

Fonksiyonel Veri Tanımlama Modülün menü yetkisi tanımlanan formu için tanımlanan menü yetkisi verilen raporun alındığı menüdür. İlgili Dönem alanında Takvim alanın İlgili Dönem seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06459994-8676-4c0d-ba65-51639c0a80d3)

Uygulama Yeri Seç alanında veri girişi yapılan formla ilişkilendirilen ve veri girişi yapılan uygulama yerleri listesinde seçim yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddd793539-52f2-4b3a-bab3-e9027245a23a)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2100c2cc-7be3-4880-8813-8229220defbe)(Excel Aktar) butonu tıklanarak Form Tanımlama menüsünde Rapor Tanımlama butonu ile tanımlanan raporun Excel Formatında alınması sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload175111e7-68ae-4ed2-b5e5-ed1b1ae1cb60)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload68cd8aae-fda6-417e-9602-100b98e54014)

Rapor tanımlama ekranında “Uygulama yerlerin ayrı ayrı raporla” check box işaretli olduğu için ayrı sheetlerde uygulama yerlerin raporu Excel Formatında alınır.

**Kocaeli Genel Merkez Ofis;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload67b4a30a-cd90-44dd-ac7d-7ac5c57397b5)

**Derince Ofis;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8b90937d-1c96-4e3c-b682-549d854bfcd5)

**İzmit Ofis;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4e9a41da-7c2e-4e94-bf05-52f12551376a)
