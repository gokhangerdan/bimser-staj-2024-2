---
title: Rapor Formatları Tanımlama İşlemi ve Sabit Tag Listesi
description: Rapor Formatları Tanımlama İşlemi ve Sabit Tag Listesi  Yardım Dokümanı
sidebar_position: 2
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::



**Risk Modüllerinde Rapor Formatları Tanımlama İşlemi ve Sabit Tag Listesi Kullanıcı Yardım Dokümanı**


# **1.Risk Modüllerinde Rapor Formatları Tanımlama İşlemi**

Risk Modüllerini tüm kullanıcılar için farklı kurgulandığı için sabit bir rapor şablonu bulunmuyor. Bu nedenle her rapor için ayrı rapor şablonu sıfırdan hazırlanıyor ve sisteme aktarılma işlemi yapılmaktadır. Risk Modüllerinde Rapor şablonları tasarlama işleminde Sistem Altyapı Tanımları kısmında altyapısı kurgulanır. Altyapı kurgulama işleminde Alan Tanımlama, Fonksiyon Dizanyer ve Rapor Formatları menüsü kullanılır. Alan Tanımlama Rapor formatında bulanan Alanların tanımlama işlemi yapılır. Fonksiyon Dizanyer da tanımlan bu alanların 4 numaralı Risk Değerlendirme Detay fonksiyonu sayfalarında görüntülenmesi için ilişkisi kurulur. Fonksiyon Dizanyer da ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload41ad1371-f463-4e88-9bed-9153d04d9164)(alanlar) butonu tıklanarak açılan ekranda Alan kodların tagleri Rapor formatında alan değerleri kısmına eklenir. Tag ekleme işlemi yapılan Rapor formatı sistem yüklenir. Rapor formatı şablonun sisteme yükleme işlemi Sistem Altyapı Tanımları\>BSAT\>Konfigürasyon ayarları\>Rapor Formatları Düzenleme menüsünde ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0fbd9fe7-f9e5-4cc1-a6e1-9a8687ba9a44)(Yeni) butonu ile yapılır. Sistem Altyapı Tanımları\>İlgili Risk\>Rapor Formatları menüsü tıklatılır. Açılan Rapor Formatları menüsünde ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0fbd9fe7-f9e5-4cc1-a6e1-9a8687ba9a44)(Yeni) butonu tıklanılır. Açılan Rapor Formatları menüsünde Rapor Formatı şablonun adı yazılır. Rapor Formatları Düzenleme menüsünde gidilerek sistem yüklenen Rapor formatı şablonu seçilerek adı ve uzantısı kopyala işlemi yapıldıktan sonra Rapor Formatları ekranındaki Rapor şablonu alanına yapıştırma işlemi yapılır. Rapor formatları ekranında Rapor şablon formatı tanımladıktan sonra Rapor şablonu alanında istenilen seçeneğe göre rapor seçimi yapılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5ae3d184-f2b0-47d6-9854-4f5daca7c8cd)(kaydet) butonu tıklanarak Rapor formatı tanımlama işlemi gerçekleştirilir. Rapor şablonu seçenekleri Form Bazında, Kayıt Bazında ve Genel olmak üzere 3 seçenektir. Entegre Yönetim Sistemi\> Risk \> Risk Değerlendirme Formu Tanımlama \> Detaylar menüsünde tıklanılır. Açılan Risk Değerlendirme Formu-Detaylar ekranında listeden Risk seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7472bf2e-86e9-4f64-8d14-b546ec07c7c9)(Excel’e Aktar)butonuna basılarak rapor alınma işlemi yapılır.

## **1.1.Risk Modüllerinde Rapor Formatları Menüsünün Rapor Şablon Seçenekleri**

**Menü Adı**: Sistem Altyapı Tanımları/İSG Risk Değerlendirme/ Rapor Formatları

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload08c9fb83-15eb-4384-ac68-7f88fc4a5260)


Risk Modüllerinde Sistem Altyapı Tanımları\>Risk\>Rapor Formatları menüsü tıklanarak açılan Rapor Formatları ekranında en alt kısımda yer alan Rapor Şablonu alanın Rapor formatlarının seçenekleri yer almaktadır. Bu seçenekler Form Bazında, Kayıt Bazında ve Genel olmak üzere 3 seçenektir. Kayıt bazında seçeneğinde seçeneği seçildiğinde PDF ile ilgili check box işaretlendiğinde PDF formatında rapor alınabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfa7b86c2-5789-4372-a979-ac0b980ac1fb) (Yeni) butonuna tıklanarak açılan Rapor Formatları-Yeni Kayıt ekranında en alt kısmında Rapor Şablonu alanında Rapor seçeneklerinin bilgisi görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload691d2f04-874d-4ddb-bef0-a331daa30042)

### **1.1.1.Form Bazında Seçeneğine Bağlı Olarak Rapor Formatı Alınması**

Entegre Yönetim Sistemi\> Risk \> Risk Değerlendirme Formu Tanımlama \> Detaylar menüsünde (Excel’e Aktar) butonuna basılarak alınan rapor adımları takip ederek rapor şablonu oluşturulabilir.

İlk olarak yeni bir Excel dosyası oluşturulur. Dosyanın adına bir isim verilir. İsim verilirken dikkat edilmesi kısım dosya adında boşluk karakterinin olmamasıdır. Örneğin dosya adının "DETAY_RISK.xlsx" olduğu gibi.

Sistemde tanımlı olan sabit alanlar için dokümanda yer alan "sabit tagler.txt" dosyasını kontrol edilir. Sistem Altyapı Tanımları\> İlgili Risk \> Alan Tanımlama menüsünde tanımlanan parametrik alanları rapora basabilmek için ise; Sistem Altyapı Tanımları \> İlgili Risk \> Fonksiyon Dizayner menüsüne gelerek 4 numaralı fonksiyon olan Risk Değerlendirme Detay fonksiyonu seçilir. Risk Değerlendirme Detay fonksiyonu seçili iken sağ üstte yer alan![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload41ad1371-f463-4e88-9bed-9153d04d9164) (Alanlar) butona tıklatılır. Açılan ekranda "Risk Tanımı" adında bir alanınız olduğunu ve bu alan için "Alan Kodu" alanında ALAN5 ise bu durumda "Risk Tanımı" alanını rapora basabilmek için kullanmanız gereken tag <ALAN5\> şeklinde olacaktır. Rapor formatında “Risk tanımı” alanın değerinin bulunduğu kısma <ALAN5\> tag bilgisi yazılacaktır. Eğer rapora eklemek istediğiniz alan liste, puanlı liste, personel, departman, pozisyon tipli alan tipleri ise bu durumda, <ALANKODU_ACK\> şeklinde bir tag kullanmanız gerekiyor. Örneğin "Risk Sahibi" adında personel tipli bir alanınız varsa ve bu alanın "Alan Kodu" ALAN4 ise kullanmanız gereken tag <ALAN4_ACK\> şeklinde olacaktır. Bu alan tag’in de Rapor format da “Risk Sahibi” alanın değerinin bulunduğu kısma <ALAN4_ACK\> tag yazılacaktır. Kullanılan tag’ların başında ve sonunda herhangi bir boşluk karakteri olmamasına dikkat edilmemesi gerekmektedir. Tüm taglerin bilgisi rapor şablona yazılır. Rapor şablonunuzu bu bilgiler doğrultusunda hazırladıktan sonra Sistem Altyapı Tanımları\> BSAT \> Konfigürasyon Ayarları \> Rapor Formatları Düzenleme menüsünde ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0fbd9fe7-f9e5-4cc1-a6e1-9a8687ba9a44)(Yeni)butonu tıklanarak rapor formatının sisteme aktarma işlemi yapılır. Sisteme aktarılan rapor formatı Rapor Formatları Düzenleme menüsünde seçilir. Seçilen Rapor Formatı uzantısıyla birlikte sağ tıkla/ Kopyala komutu ile kopyalanır. Sistem Altyapı Tanımları\>İlgili Risk\<Rapor formatları menüsüne gidilir. Açılan Rapor Formatları menüsünde ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0fbd9fe7-f9e5-4cc1-a6e1-9a8687ba9a44)(Yeni) butonu tıklatılır. Açılan Rapor Formatları ekranında Rapor Tanımı kısmına Raporun adı bilgisi yazılır. Rapor Şablonu alanında Rapor Formatlarında adı ve uzantısıyla kopyalanan Rapor formatı bilgisi sağ tıkla/yapıştır komutu ile yapıştırma işlemi yapılır. Rapor Şablonu alanında sisteme aktardığınız şablonun tam adını, uzantısıyla birlikte yazmanız gerekir. Örneğin rapor formatlı düzenleme menüsünde şablonunuzu "DETAY_RISK.xlsx" ismi ile aktardıysanız, Rapor Şablonu alanına DETAY_RISK.xlsx yazmanız gerekiyor.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4788ef58-7bb6-4e26-8faa-72f82592e827)

**Form Bazında:** Her risk formu altındaki risk detay kayıtlarının tek bir liste halinde Excel’e aktarıldığı durumlar için seçilir. (Entegre Yönetim Sistemi/ Risk /Risk Değerlendirme Formu Tanımlama menüsünde Detaylar butonuna basıldıktan sonra çıkan “Excel” butonuyla alınır.)

En alt yer alan Rapor Şablonu alanı ise "Form Bazında" seçeneği seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4636e0e-a98d-4fad-b6cb-7fd3aa002a4a)(kaydet) butonu tıklanarak form bazında rapor alma işlem basamakları tamamlanmış olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd4d352cd-71c1-4571-843f-828543f72435)

### **1.1.2.Kayıt Bazında Seçeneğine Bağlı Olarak Rapor Alınması**

Entegre Yönetim Sistemi\> Risk \> Risk Değerlendirme Formu Tanımlama \> Detaylar menüsünde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7472bf2e-86e9-4f64-8d14-b546ec07c7c9)(Excel’e Aktar) butonuna basılarak alınan rapor adımları takip ederek rapor şablonu oluşturulabilir. İlk olarak yeni bir Excel dosyası oluşturulur. Dosyanın adına bir isim verilir. İsim verilirken dikkat edilmesi kısım dosya adında boşluk karakterinin olmamasıdır. Örneğin dosya adının " "TEKLIBASIM_RISK.xlsx" olduğu gibi.

Sistemde tanımlı olan sabit alanlar için dokümanda yer alan "sabit tagler.txt" dosyasını kontrol edilir. Sistem Altyapı Tanımları\> İlgili Risk \> Alan Tanımlama menüsünde tanımlanan parametrik alanları rapora basabilmek için ise; Sistem Altyapı Tanımları \> İlgili Risk \> Fonksiyon Dizayner menüsüne gelerek 4 numaralı fonksiyon olan Risk Değerlendirme Detay fonksiyonu seçilir. Risk Değerlendirme Detay fonksiyonu seçili iken sağ üstte yer alan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload41ad1371-f463-4e88-9bed-9153d04d9164)(Alanlar) butona tıklanır. Açılan ekranda "Risk Tanımı" adında bir alanınız olduğunu ve bu alan için "Alan Kodu" alanında ALAN5 ise bu durumda "Risk Tanımı" alanını rapora basabilmek için kullanmanız gereken tag <ALAN5\> şeklinde olacaktır. Eğer rapora eklemek istediğiniz alan liste, puanlı liste, personel, departman, pozisyon tipli alan tipleri ise bu durumda, <ALANKODU_ACK\> şeklinde bir tag kullanmanız gerekmiyor. Alanlar tümü “ACK” eki eklenemeyecek <ALANKODU\> şeklinde olur. Kullanılan tag’ların başında ve sonunda herhangi bir boşluk karakteri olmamasına dikkat edilmemesi gerekmektedir. Tüm taglerin bilgisi rapor şablona yazılır. Rapor şablonunuzu bu bilgiler doğrultusunda hazırladıktan sonra Sistem Altyapı Tanımları\> BSAT \> Konfigürasyon Ayarları \> Rapor Formatları Düzenleme menüsünde ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0fbd9fe7-f9e5-4cc1-a6e1-9a8687ba9a44)(Yeni) butonu tıklanarak rapor formatının sisteme aktarma işlemi yapılır. Sisteme aktarılan rapor formatı Rapor Formatları Düzenleme menüsünde seçilir. Seçilen Rapor Formatı uzantısıyla birlikte sağ tıkla/ Kopyala komutu ile kopyalanır. Sistem Altyapı Tanımları\>İlgili Risk\<Rapor formatları menüsüne gidilir. Açılan Rapor Formatları menüsünde ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0fbd9fe7-f9e5-4cc1-a6e1-9a8687ba9a44)(Yeni) butonu tıklanılır. Açılan Rapor Formatları ekranında Rapor Tanımı kısmına Raporun adı bilgisi yazılır. Rapor Şablonu alanında Rapor Formatlarında uzantısıyla kopyalanan Rapor formatı bilgisi sağ tıkla/yapıştır komutu ile yapıştırma işlemi yapılır. Rapor Şablonu alanında sisteme aktardığınız şablonun tam adını, uzantısıyla birlikte yazmanız gerekir. Örneğin rapor formatlı düzenleme menüsünde şablonunuzu " TEKLIBASIM_RISK.xlsx " ismi ile aktardıysanız, Rapor Şablonu alanına TEKLIBASIM_RISK.xlsx yazmanız gerekiyor.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada437411d-8ec9-4aca-b0ff-7b5362a2e8fc)

**Kayıt Bazında:** Her bir risk kaydının ayrı olarak raporlanması talep edildiğinde seçilir. (EYS/İSG Risk Değerlendirme/Risk Değerlendirme Formu tanımlama menüsünde Detaylar butonuna basıldıktan sonra çıkan “PDF” butonuyla alınır.

En alta yer alan Rapor Şablonu alanı ise " Kayıt Bazında " seçeneği seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4636e0e-a98d-4fad-b6cb-7fd3aa002a4a)(kaydet) butonu tıklanarak kayıt bazında rapor alma işlem basamakları tamamlanmış olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada128763e-930a-4438-b0ef-178ec0359b2b)

### **1.1.3.Genel Seçeneğine Bağlı Rapor Alınması**

Entegre Yönetim Sistemi\> Risk \> Risk Değerlendirme Formu Tanımlama \> Detaylar menüsünde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7472bf2e-86e9-4f64-8d14-b546ec07c7c9)(Excel’e Aktar) butonuna basılarak alınan rapor adımları takip ederek rapor şablonu oluşturulabilir.

İlk olarak yeni bir Excel dosyası oluşturulur. Dosyanın adına bir isim verilir. İsim verilirken dikkat edilmesi kısım dosya adında boşluk karakterinin olmamasıdır. Örneğin dosya adının " GENEL_RISK.xlsx " olduğu gibi. Sistemde tanımlı olan sabit alanlar için dokümanda yer alan "sabit tagler.txt" dosyasını kontrol edilir. Sistem Altyapı Tanımları\> İlgili Risk \> Alan Tanımlama menüsünde tanımlanan parametrik alanları rapora basabilmek için ise; Sistem Altyapı Tanımları \> İlgili Risk \> Fonksiyon Dizayner menüsüne gelerek 4 numaralı fonksiyon olan Risk Değerlendirme Detay fonksiyonu seçilir. Risk Değerlendirme Detay fonksiyonu seçili iken sağ üstte yer alan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload41ad1371-f463-4e88-9bed-9153d04d9164)(Alanlar) butona tıklanılır. Açılan ekranda "Risk Tanımı" adında bir alanınız olduğunu ve bu alan için "Alan Kodu" alanında ALAN5 ise bu durumda "Risk Tanımı" alanını rapora basabilmek için kullanmanız gereken tag <ALAN5\> şeklinde olacaktır. Rapor formatında “Risk tanımı” alanın değerinin bulunduğu kısma <ALAN5\> tag bilgisi yazılacaktır. Eğer rapora eklemek istediğiniz alan liste, puanlı liste, personel, departman, pozisyon tipli alan tipleri ise bu durumda, <ALANKODU_ACK\> şeklinde bir tag kullanmanız gerekiyor. Örneğin "Risk Sahibi" adında personel tipli bir alanınız varsa ve bu alanın "Alan Kodu" ALAN4 ise kullanmanız gereken tag <ALAN4_ACK\> şeklinde olacaktır. Bu alan tag’in de Rapor format da “Risk Sahibi” alanın değerinin bulunduğu kısma <ALAN4_ACK\> tag yazılacaktır. Kullanılan tag’ların başında ve sonunda herhangi bir boşluk karakteri olmamasına dikkat edilmemesi gerekmektedir. Tüm taglerin bilgisi rapor şablona yazılır. Rapor şablonunuzu bu bilgiler doğrultusunda hazırladıktan sonra Sistem Altyapı Tanımları\> BSAT \> Konfigürasyon Ayarları \> Rapor Formatları Düzenleme menüsünde ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0fbd9fe7-f9e5-4cc1-a6e1-9a8687ba9a44)(Yeni) butonu tıklanarak rapor formatının sisteme aktarma işlemi yapılır. Sisteme aktarılan rapor formatı Rapor Formatları Düzenleme menüsünde seçilir. Seçilen Rapor Formatı uzantısıyla birlikte sağ tıkla/ Kopyala komutu ile kopyalanır. Sistem Altyapı Tanımları\>İlgili Risk\<Rapor formatları menüsüne gidilir. Açılan Rapor Formatları menüsünde ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0fbd9fe7-f9e5-4cc1-a6e1-9a8687ba9a44)(Yeni) butonu tıklanılır. Açılan Rapor Formatları ekranında Rapor Tanımı kısmına Raporun adı bilgisi yazılır. Rapor Şablonu alanında Rapor Formatlarında uzantısıyla kopyalanan Rapor formatı bilgisi sağ tıkla/yapıştır komutu ile yapıştırma işlemi yapılır. Rapor Şablonu alanında sisteme aktardığınız şablonun tam adını, uzantısıyla birlikte yazmanız gerekir. Örneğin rapor formatlı düzenleme menüsünde şablonunuzu " GENEL_RISK.xlsx " ismi ile aktardıysanız, Rapor Şablonu alanına GENEL_RISK.xlsx yazmanız gerekiyor.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb2867f44-ca5f-416b-b2ba-db6cb6e0f300)

**Genel:** Tüm risk detay kayıtlarının tek bir Excel’de görülmesi talep edildiği durumda seçilir.(Entegre Yönetim Sistem/Risk /Raporlar/Genel Risk Listesi Rapor ekranından alınır.)

En alt yer alan Rapor Şablonu alanı ise "Genel" seçeneği seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4636e0e-a98d-4fad-b6cb-7fd3aa002a4a)(kaydet) butonu tıklanarak Genel seçeneği olarak rapor alma işlemi basamakları tamamlanmış olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2a8a8bd8-f2b7-4898-8f55-ed8ad23493ff)

## **1.2.İSG Risk Değerlendirme Modülünde Kayıt Bazında Rapor Alma İşlemi**

İSG Risk Değerlendirme Modülüne Kayıt bazında Rapor alma işlemi için öncelikle Risk Modülün Altyapı kurgusunun tanımlama işlemi yapılır. İkinci aşamada altyapı kurgusu tanımlanan İSG Risk Modülün Entegre Yönetim Sistemi\>İSG Risk Değerlendirme\> Risk Değerlendirme Formu Tanımlama \> Risk Değerlendirme Formu -Detaylar menüsünde Risk Tanımlama işlemi yapılır. Risk Değerlendirme Formu-Detaylar ekranında Risk tanımlaması işlemi yapılan Risk seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload762a66e2-7444-4efb-8f38-26d0fd6741be)(Yazdır) butonu tıklanarak Kayıt bazında ve Excel Aktar butonu tıklanarak Excel formatında kayıt bazında rapor alma işlemi yapılır.

### **1.2.1.Sistem Altyapı Tanımları/İSG Risk Değerlendirme**

Rapor formatlarında Kayıt bazında rapor alma işleminin altyapı kurgusunun tasarlandığı kısımdır. Altyapı kurgusu için Alan tanımlama, Fonksiyon Dizanyer ve Kayıt bazında raporun tanımlama işlemi için de Rapor formatları menüleri kullanılacaktır. Ayrıca ek olarak Sistem Altyapı Tanımları Modülünde Rapor Formatları Düzenleme menüsüne Rapor şablon formatının sisteme aktarılma işlemi yapılacaktır.

### **1.2.1.1. Alan Tanımlama**

**Menü Adı**: Sistem Altyapı Tanımları/İSG Risk Değerlendirme/Alan Tanımlama

Rapor formatına Fonksiyon dizanyer menüsünde alan kodlarının tag’lerin eklenmesi işlemi için alan tanımlama menüsünde rapor şablon formatında bulunan alanların tanımlama işlemi yapılır. Bu alan tanımlamaları metin, numerik, liste, puanlı liste, personel tipli gibi alan tipli alandır. Örnek Rapor Formatı Şablonu aşağıda yer almaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2aacc018-8611-46ab-8e4f-450dd979dc98)

İlk olarak rapor formatı şablon örneğindeki bulanan alanların alan tiplerinin Alan tanımlama menüsünde Alan tanımlama işlemi yapılır.

Örnek Rapor format Şablonunda “Riskin Tanımı” metin tipli alan Tanımlama işlemin yapılması;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadda840e53-b86c-4ec7-bf05-74816015a988)

Listeye “Riskin Tanımı” metin tipli alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfa7b86c2-5789-4372-a979-ac0b980ac1fb) (Yeni) butonu tıklanarak Alan Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbcdb62bb-8988-4604-a1c3-371299111e4e)

Alan tanımlama ekranında alan tipi alanında metin seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4636e0e-a98d-4fad-b6cb-7fd3aa002a4a) (Kaydet) butonu tıklanarak metin tipli alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc72694b7-cdd6-48dc-b39f-b998f81b8a7e)

Örnek Rapor format Şablonunda “Riskin Tipi” liste tipli alan Tanımlama işlemin yapılması;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06425498-f34d-42bc-b86c-ac0fd1d51bc4)

Listeye “Riskin Tipi” liste tipli alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfa7b86c2-5789-4372-a979-ac0b980ac1fb) (Yeni) butonu tıklanarak Alan Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaea27732-0294-4532-80a7-0b12035ccfcd)

Alan tanımlama ekranında Alan tipi alanında liste tipi seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4636e0e-a98d-4fad-b6cb-7fd3aa002a4a) (Kaydet) butonu tıklanarak liste tipli alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload79709d8d-fe14-4d12-a6f6-f05ecb55c004)

“Risk Tipi” liste tipli alanına değer eklemek için “Risk tipi” alanı seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf41a9294-15f6-4db5-930c-bf3da77017a6) (Değerler) butonuna tıklanarak alanın değerlerinin tanıtılacağı ekrana gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddbc9c8c9-b88d-49ea-b877-73aa8b9d87af)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc3df9aa5-1f92-42ce-a064-bcb7d55e8307) : Yeni butonuna tıklanarak yeni değer tanımlama işlemine başlanılır. İstenirse ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload47389d4a-cce5-4606-9ee3-6467474e9ef6)(Şablon İndir) ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload82ae9066-58f0-4abd-bd37-eb2fef8612c7)(Şablon Yükle) butonları ile sisteme toplu olarak alan değerleri aktarılabilmektedir. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload47389d4a-cce5-4606-9ee3-6467474e9ef6)(Şablon indir) butonu ile sistem şablonu bilgisayara indirir. İlgili şablon kullanıcılar tarafından doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload82ae9066-58f0-4abd-bd37-eb2fef8612c7)(şablon yükle) butonu ile sisteme yüklendiğinde şablondaki tüm alan değerleri sisteme aktarılmış olacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload81fc2da8-eb27-4b9a-9302-dc6f07d91604)

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4636e0e-a98d-4fad-b6cb-7fd3aa002a4a) (Kaydet) butonu tıklanarak değer tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfa3a7a13-a0f2-4274-8f0f-48edcb5d677c)

“Risk tipi” liste tipli alanın liste elemanları (değerleri) aynı şekilde tümü tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload58c877ca-43bc-4bb5-ae11-fb9194dd49ef)

Örnek Rapor format Şablonunda “Riskin Sahibi” Personel tipli alan tanımlama işlemin yapılması;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload461ec3bc-7626-4f6b-91bb-888ad5d7cf8a)

Listeye “Riskin Sahibi” Personel tipli alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfa7b86c2-5789-4372-a979-ac0b980ac1fb) (Yeni) butonu tıklanarak Alan Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9e5b4e14-9c80-49a9-bcf9-d16c135e8e80)

Alan tanımlama ekranında alan tipi alanında Personel seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4636e0e-a98d-4fad-b6cb-7fd3aa002a4a) (Kaydet) butonu tıklanarak Personel tipli alan tanımlama kayıt işlemi gerçekleştirilir.

Örnek Rapor format Şablonunda “Doğal Etki” Puanlı liste tipli alan Tanımlama işlemin yapılması;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbe7abdeb-e7f7-4b42-bf4e-c64ed0bca771)

Listeye “Doğal Etki” puanlı liste tipli alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfa7b86c2-5789-4372-a979-ac0b980ac1fb) (Yeni) butonu tıklanarak Alan Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbc8efb29-07d8-4ae7-bd2f-6b6c1d1ccbde)

Alan tanımlama ekranında Alan tipi alanında “Puanlı liste” tipi seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4636e0e-a98d-4fad-b6cb-7fd3aa002a4a) (Kaydet) butonu tıklanarak “Puanlı liste” tipli alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadef4dceaf-3996-4375-9219-94d88f1578b2)

“Doğal etki” Puanlı liste tipli alanına değer eklemek için “Doğal Etki” alanı seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf41a9294-15f6-4db5-930c-bf3da77017a6) (Değerler) butonuna tıklanarak alanın değerlerinin tanıtılacağı ekrana gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade9732e42-bfe6-4805-a965-75a42374859e) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc3df9aa5-1f92-42ce-a064-bcb7d55e8307): Yeni butonuna tıklanarak yeni değer tanımlama işlemine başlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload54b57e44-7cd9-4a46-bc05-2eb1391656a9)

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4636e0e-a98d-4fad-b6cb-7fd3aa002a4a) (Kaydet) butonu tıklanarak değer tanımlama işlemi gerçekleştirilir. “Doğal etki” Puanlı liste tipli alanın liste elemanları (değerleri) aynı şekilde tümü tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5533cff5-6128-4e7c-890d-f63c0b9f45d3)

Örnek Rapor format Şablonunda “Doğal Olasılık” Puanlı liste tipli alan Tanımlama işlemin yapılması;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload87fa1119-3108-42dc-95ec-86b451726f2d)

Listeye “Doğal Olasılık” puanlı liste tipli alan eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfa7b86c2-5789-4372-a979-ac0b980ac1fb) (Yeni) butonu tıklanarak Alan Tanımlama\\Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload21fb654c-6ba9-4cdb-9b02-fc2d51497548)

Alan tanımlama ekranında Alan tipi alanında Puanlı liste tipi seçilerek gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4636e0e-a98d-4fad-b6cb-7fd3aa002a4a) (Kaydet) butonu tıklanarak Puanlı liste tipli alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7362cbfd-d431-4244-841c-346975bc313e)

Doğal olasılık liste tipli alanına değer eklemek için “Doğal Olasılık” alanı seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf41a9294-15f6-4db5-930c-bf3da77017a6) (Değerler) butonuna tıklanarak alanın değerlerinin tanıtılacağı ekrana gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7bf02c48-2501-4df4-89ab-3a588c3bf999)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc3df9aa5-1f92-42ce-a064-bcb7d55e8307): Yeni butonuna tıklanarak yeni değer tanımlama işlemine başlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload49f2a7df-70b1-4234-be14-6110c0d2657e)

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4636e0e-a98d-4fad-b6cb-7fd3aa002a4a) (Kaydet) butonu tıklanarak değer tanımlama işlemi gerçekleştirilir. “Doğal Olasılık” Puanlı liste tipli alanın liste elemanları (değerleri) aynı şekilde tümü tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb775a774-5241-459a-9abd-f81d8f220817)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload54588b2c-44ec-4b6f-842d-6fac0eec66ef)

Giriş tipi olarak veri girişi seçilen alanların tanımlanması yukarıdaki gibi gerçekleştirilir. Giriş tipleri hesaplanan olacak alanlar ise formülleri ile birlikte tanımlanır.

Örnek Rapor format Şablonunda “Doğal Risk Skoru” Giriş tipi hesaplanan seçilen Metin Tipli alan tanımlanması;

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload54e8499c-f61b-4190-aae6-4e65a05d09b1)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd2dff299-e271-4a7c-871d-b186a9ec24cb)

Formül girişleri ilgili alanların tanımlama ekranlarında gerçekleştirilir. Örnek olarak bir formül aşağıdaki gibi analiz edilebilir.

([04]\*[05]) şeklinde yazılan bir alanda köşeli parantez içinde yazılan ifade alan kodlarını temsil etmektedir. Bu ifadeler alan tanımlama ekranında alanları tanımlarken kullanıcı tarafından belirlenir.

Doğal etki alanı için, 04 yerine ET; Doğal Olasılık alanı için, 05 yerine OL; yerine kodlama yapılmış olsaydı formül, ([ET]\*[OL]) şeklinde olacaktır. Bu formülün sonucu olarak “Doğal Risk Skoru Alanı” için Doğal etki, Doğal Olasılık alanında seçilen değerlerin çarpımı olmak üzere sistem tarafından otomatik olarak hesaplanacaktır. Hesaplanan alanlarda bir diğer formül kullanımı ise IF fonksiyonu ile olmaktadır. IF Fonksiyonunun liste tipli alanlar için kullanılabilmesi için öncelikle ilgili alana değer tanımlanması gereklidir.

Örnek Rapor format Şablonunda “Doğal Risk Skoru Açıklama” Liste Tipli Alan tipinin tanımlama

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1fdd6471-7513-4a4f-ab8e-64437444603c)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload30afe76c-3aa1-46c9-aa9e-cf5ed14114f3)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc3df9aa5-1f92-42ce-a064-bcb7d55e8307): Yeni butonuna tıklanarak yeni değer tanımlama işlemine başlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4c901f8-3682-43db-8fce-7420cd0a2f4a)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc296bb3b-12bd-4eb4-ba22-32eecc6af50e)

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf4636e0e-a98d-4fad-b6cb-7fd3aa002a4a) (Kaydet) butonu tıklanarak değer tanımlama işlemi gerçekleştirilir. “Doğal Risk Skoru Açıklama” liste tipli alanın liste elemanları (değerleri) bu şekilde tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload658f0240-fda5-4886-9b35-d534491bd5ab)

İlgili alan değerleri tanımlandıktan sonra formül girişi yapılır. Formül girişi için alan tanımlama ekranındayken ilgili alanın üzerine tıklanır ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4b001d28-3599-4cc9-81c3-b16d0253ac3e) (Değiştir) butonu ile alan detaylarına girilir. Bu alanda formül girişi gerçekleştirirken daha önce belirtildiği üzere alan kodlarının köşeli parantez olarak yazılması gereklidir. Formül, bazı ifadelerin farklı olması haricinde (noktalı virgül, virgül vb.) Excel’de kullanılan IF fonksiyonu ile aynı mantıkta yazılmalıdır. Formül kullanımı: IF([ALANKODU]KoşulŞartı; Doğru ise Değer Kodu; Yanlışsa Değer Kodu şeklindedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload08c6b304-ad31-4083-ba39-96bb2e66241d)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf7950042-e7a4-43ea-bbec-c420a7400199) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0b20c4f2-eb89-43f3-b8ff-13976087eb0d)

“Doğal Risk Skoru Açıklama” liste tipli alanın Formül alanın Formül bilgisi yazılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5ae3d184-f2b0-47d6-9854-4f5daca7c8cd)(Kaydet) butonu tıklanarak Kayıt güncelleme kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5faa40e9-711e-4d76-bd86-54fc566debab)

### **1.2.1.2.Fonksiyon Dizayner**

**Menü Adı**: Sistem Altyapı Tanımları/İSG Risk Değerlendirme/ Fonksiyon Dizayner

Alan Tanımlama menüsünde örnek rapor formu şablonundaki alanların tanımlama işleminde sonra Sistem Altyapı Tanımları\>İSG Risk Değerlendirme\>Fonksiyon Dizanyer menüsü tıklanılır. İSG Risk Değerlendirme Modülün tanımlanan alanlar Fonksiyon Dizanyer menüsünde bulunan fonksiyonları sayfaları ile ilişkilendirme işlemi yapılır. Bu menüde kullanılacak butonlar İSG Risk Değerlendirme Modülü parametrelerinden “Statü kullanılsın mı?” (22. Parametre) parametresine bağlı olarak değişir. Bu parametre değeri “Evet” ise aşağıda bulunan butonların tamamı gözükür; ancak parametre değeri “Hayır” olduğu durumlarda sadece “Alanlar” butonu görünür durumda olur. Bu menüde alanların ilgili fonksiyonların sayfalarıyla ilişkilendirme işleminde öncelikle ilgili fonksiyonların önce statü ve buton tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc06b0274-4145-44f4-b6da-88dc10b81425)

Risk Değerlendirme Form Tanımlama fonksiyonu statü tanımlama işlemi yapılır. Fonksiyon Dizayner menüsünden ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc463c15-b1f2-47da-8eba-867d51596601) (Statüler) butonu ile statüler tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6f7d3338-bdb4-4091-b781-52e334fabe3f)

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0fbd9fe7-f9e5-4cc1-a6e1-9a8687ba9a44) Yeni butonu ile yeni statü tanımlama ekranına gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade3d87c33-ed7b-451c-87c0-67fd74a08282)

Açılan ekranda statü kodu, statü adı, akışın başlatılıp başlatılmayacağı, yeni statü, durum, akış tanımı, onay talep mesajı, onay tamam mesajı ve onay ret mesajı girişleri yapılarak kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0efd9afd-6a4c-44a7-92c1-f993c05e35e5)

Fonksiyon Dizayner ‘dan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload468c13ce-6e5c-457d-958e-6f2811d0854a) (Butonlar) butonu ile statülerde kullanılacak butonlar tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload38b6d1d0-931e-4607-927d-484189ef7dc8)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade96a25bc-257c-4492-992f-4999270cb7b3)

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0fbd9fe7-f9e5-4cc1-a6e1-9a8687ba9a44)Yeni butonu ile yeni buton tanımlama ekranına gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload96a81ba6-882e-4fd0-88e6-ec6511cbd004)

Açılan ekranda Buton Kodu, Buton Adı belirlenir. Buton tipi ve Resmi belirlenir. Görünür Statüsü, Yeni Statü ve Durumu seçilir. Gerekli alanlar doldurulduktan sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2642307c-f3a6-4927-bb6b-5bd266054dd6)(kaydet) butonuyla kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf6a82115-f6f1-4370-b5ee-8c7c236adf36)

Aynı şekilde Risk Değerlendirme Detay fonksiyonu için statü ve buton tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7c4a41bb-b16f-4049-8eeb-03ce733c9099)

Risk değerlendirme detay fonksiyonu için statüler tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3504271e-ad4c-4fd7-ac1f-f81fa04d445f)

Risk değerlendirme detay fonksiyonu için butonlar tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload767f6763-7977-4011-b92f-f37c63877a77)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb0b5f8b8-669f-4a38-904a-bc21d4ea9826)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload41ad1371-f463-4e88-9bed-9153d04d9164): Alanlar butonuna tıklanarak alanların ilgili fonksiyonla ilişkilendirilme yapılacağı ekran açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd7250047-b35f-4c80-8cac-99ae543dd521)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcddef18a-a1d0-4c77-8981-7f007526bac0)

İlgili fonksiyonda kullanılacak alanlar ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfa7b86c2-5789-4372-a979-ac0b980ac1fb)(Yeni) butonuna tıklanarak belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfdb69da0-ae3a-4dc1-b3f1-7373e226d887)

Açılan ekranda alan bilgileri listeden seçilir, zorunlu bir alan ise kullanıcının bu alanı doldurmadığında karşısına çıkacak mesaj tanımlanır (Doğal Olasılık alanı zorunludur vb.), sıra numarası belirlenir. Aktif statü, Görünür Statü ve Zorunlu Statü durumları seçilir. Zorunlu olup olmadığı, gridde gösterilip gösterilmeyeceği, kolon genişliği belirlenerek gerekli tüm alanlar doldurulduktan sonra ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5ae3d184-f2b0-47d6-9854-4f5daca7c8cd) (Kaydet) butonu tıklanarak, ilgili alan için fonksiyon ile ilişkilendirme işlemi gerçekleştirilir. Gerekli olan tüm alanlar bu şekilde ilgili fonksiyona eklenir. Aşağıda görüldüğü üzere Alan No’nun yanında Alan Kodu bölümü vardır. Bu alan Risk raporu düzenlemelerinde <ALAN1\> vb. şekilde rapora eklenerek düzenleme yapılmasına imkan sağlayan koddur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload57eba3e2-badd-4206-84a5-42807d9da470)

İlgili fonksiyonda kullanılacak alanlar ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfa7b86c2-5789-4372-a979-ac0b980ac1fb)(Yeni) butonuna tıklanarak belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload364f20ff-1ec5-42b4-985a-474554220c3c)

Akış tanımları Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Akış tanımlama ekranından kontrol edilmeli yoksa akışları tanımlanmalıdır. Ayrıca Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Rol Tanımlama ekranından da onay akışları için rol tanımlamaları yapılır. Rol tanımlama işlemlerinde SQL ve QDMS veri tabanı bilgisi gerekeceğinden Bimser Teknik Destek ekibiyle iletişime geçilerek gerekli rol talep edilebilir.

### **1.2.1.3.Raporun Rapor Formatına Tag’leri Eklenmesi.**

Alan Tanımlama tanımlanan alanlar Fonksiyon Dizanyer menüsünde ilgili sayfalarının ilişkilendirildikten sonra Fonksiyon Dizanyer da 4 numaralı fonksiyon olan Risk Değerlendirme detay seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload41ad1371-f463-4e88-9bed-9153d04d9164)(Alanlar) butonun tıklatıldığına açılan alan kodları rapor formatında alan değerleri kısmına yazılarak eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload364f20ff-1ec5-42b4-985a-474554220c3c)

Rapor formatları menüsünde kayıt bazında form tanımlama işlemi yapılacaktır. Kayıt bazında raporlarda \<ALANKODU\> yazmak yeterli olmaktadır. \<ALAN5\> gibi. Liste, Puanlı liste ve Personel tipli alanlarda kayıt bazlı raporlarda \_ACK yazmak gerekmiyor.

| **Alan Adı**              | **Alan Tag’i(ALANKODU)** |
|---------------------------|--------------------------|
| Risk Tanımı               | <ALAN1\>                |
| Risk Tipi                 | <ALAN2\>                |
| Riskin Sahibi             | <ALAN3\>                |
| Doğal Etki                | <ALAN4\>                |
| Doğal Olasılık            | <ALAN5\>                |
| Doğal Risk Skoru          | <ALAN6\>                |
| Doğal Risk Skoru Açıklama | <ALAN7\>                |

Tablodaki Alan Tagleri Rapor formatına ilgili Alanların değerlerin bulunduğu kısma bilgisi yazılarak eklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload926381f2-90ac-4bce-8c9b-6212e07afc50)

Rapor formatına Risk Değerlendirme Detay fonksiyonun sayfalarıyla ilişkilendirilmiş alanların kodları Fonksiyon Dizanyer de 4 numaralı fonksiyon olan Risk değerlendirme Detay fonksiyonu seçilerek![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload41ad1371-f463-4e88-9bed-9153d04d9164)( Alanlar) butonu tıklanarak açılan ekrana bakılarak alan tag’ler yazılırak bilgisayara kaydedilir.

### **1.2.1.4.Rapor Formatı Şablonun Sistem Aktarılma İşlemi**

**Menü Adı**: Sistem Altyapı Tanımları\>BSAT\> Konfigürasyon Ayarları\>Rapor Formatları Düzenleme

Rapor formatına taglerin eklenmesi için Sistem Altyapı Tanımları\>BSAT\> Konfigürasyon Ayarları\>Rapor Formatları Düzenleme menüsüne gidilir. Qdms tüm raporların yüklendiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada05f2e12-1836-41d0-9b25-196f6db61940)

Rapor formatları menüsünde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7a68d225-64b5-4bc2-9b6e-306ea3674c1c) (Yeni) butonu ile Tag ekleme işlemi yapılan bilgisayara kaydedilen rapor formatı şablonu sisteme yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada2d023a4-bcfc-4fa6-b91e-232daecf2d6c)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade9a7bbff-ed3f-499e-b515-c41d7e89e488)

Rapor formatları Düzenleme menüsünde sisteme rapor formatın yükleme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadebfb2ae8-67af-47b6-9b9d-fbf0281db268)

### **1.2.1.5.Rapor Formatları Menüsünde Kayıt Bazında Rapor Formatı Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/İSG Risk Değerlendirme/ Rapor Formatları

İSG Risk Değerlendirme metotlarına göre farklı rapor formatları oluşturmak için rapor formatları menüsü kullanılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6f046eaf-db7d-40a6-a581-e3fab5ae2f04)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfa7b86c2-5789-4372-a979-ac0b980ac1fb) (Yeni) butonuna tıklanarak rapor formatı eklemesi yapılır ve rapor formatının adı uzantısıyla beraber kopyalanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8b3e1270-79b8-494a-873c-996f72b0bb65)

Açılan ekranda ilgili alanlar tanımlanır:

**Rapor Tanımı:** Rapor tanımı bilgisinin girilir.

**Rapor Şablonu:** Rapor şablonun adı ve uzantısı bilgisi girilir. Sistem Altyapı Tanımları\>BSAT\>Konfigürasyon Ayarları menüsünde sisteme yüklenen rapor formatı şablonun adı ve uzantısı kopyalanarak alana yapıştırma işleminin yapıldığı alandır.

**Rapor Tipi:** Kayıt bazında, form bazında ve genel olmak üzere üç seçenek rapor tipi bilgisi seçilebilir.

Sistem Altyapı Tanımları\>BSAT\>Konfigürasyon Ayarları\>Rapor Formatlarında tanımlama menüsü tıklanılır. Açılan Varsayılan Rapor formatları Düzenleme ekranında tag’lerin ekleme işlemi yapılan rapor formatı şablonu seçilerek Sağ tıkla/Kopyala komutu ile kopyalanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0952ae44-5b06-490e-84c2-c7d86026387f)

Kopyala işlemi tamamlanan Rapor formatı şablonu Rapor Formatları menüsünde ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0fbd9fe7-f9e5-4cc1-a6e1-9a8687ba9a44)(Yeni) butonu ile açılan Rapor formatları ekranında Rapor şablonu alanına sağ Tıkla/yapıştır işlemi tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload779301c9-0fe2-4064-a826-d3155f2a7a3f)

Rapor Tanımı alanına raporu alanına Raporun adı bilgisi, Rapor şablonu alanına tag ekleme işlemi yapılan rapor formatı tanımlanıp ve Rapor şablonu seçeneklerinde kayıt bazında seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5ae3d184-f2b0-47d6-9854-4f5daca7c8cd)(kaydet) butonu tıklanarak kayıt bazında rapor formatı tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1f1903d9-9aa2-45d1-9414-5b3324fc8228)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload79efdd4d-7fa7-43be-842b-39b145abb14d)

### **1.2.2. Entegre Yönetim Sistemi/İSG Risk Değerlendirme**

Bu kısımda örnek Rapor Format Şablonu kullanılarak kayıt bazında Rapor formatı tanımlama işleminde sonra Risk Değerlendirme Formu tanımlama işlemi yapılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8c811a4c-5d9a-4c7e-9e75-e19659883b21)(Detaylar) butonu tıklanır. Açılan Risk Değerlendirme Formu-Detaylar ekranında ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0fbd9fe7-f9e5-4cc1-a6e1-9a8687ba9a44)(Yeni) butonu ile tasarlanan formun Risk tanımlama işlemi yapılır. Tanımlanan Risk seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload762a66e2-7444-4efb-8f38-26d0fd6741be)(Yazdır )butonu tıklanarak Kayıt bazında rapor formatı alma işlemi gerçekleştirilir.

### **1.2.2.1.Risk Değerlendirme Formu Tanımlama**

**Menü Adı:** Entegre Yönetim Sistemi/İSG Risk Değerlendirme/ Risk Değerlendirme Formu Tanımlama

Risk Değerlendirme formu tanımlama işleminin yapıldığı menüdür. Bu menüde yeni bir Risk Değerlendirme Formu Tanımlama işlemi yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadde7d7b89-b939-4094-a04d-3addc58ec66b)

Risk Değerlendirme Formu Tanımlama ekranında ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9b8e282f-aaa0-4c1b-94f8-3326bed7b35b) (Yeni) butonuyla yeni Risk Değerlendirme Formu Tanımlaması işlemi gerçekleştirilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc97df715-a387-4a3a-a1be-7a017f42aba2)

RDF tanımlama ekranında formun kodunu eğer otomatik kod verilmemişse kullanıcı tarafından girilir, formun tanımı ve sorumlu kullanıcı grupları eklenerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload463d31c5-7d9d-4ca7-b010-021e9cb02919) (Kaydet) butonu tıklanarak risk değerlendirme formu tanımlama işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cb48835-254e-4487-984a-7795663dcd67)

Bu şekilde bütün RDF’ler tanımlandıktan sonra, risk detayı eklenilecek RDF seçili iken sağ üstteki butonlardan ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8c811a4c-5d9a-4c7e-9e75-e19659883b21) (Detaylar) butonu tıklanarak Risk Değerlendirme Formu Detayı (RDFD) ekranına gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload549c565b-1fe5-43f0-8256-7caa08d150cf)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9b8e282f-aaa0-4c1b-94f8-3326bed7b35b)(Yeni) butonuyla Risk Değerlendirme Formu/Detaylar ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb1ae9618-35e2-49f7-952b-03b0fc23b6d4)

Risk değerlendirme sekmesinde risk analizi için gerekli olan temel bilgiler ve kullanıcı tanımlı alanlar doldurulur. ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfbe4d68a-6526-4198-b1b4-88758d570a62)(Onaya Gönder) butonu tıklanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload15f3656b-0b38-46e6-9074-b55ad423ccd2)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload043f207c-e1b4-4bd3-a10a-bb2a64ea1567)

Onaydaki kişinin bekleyen işlerine “**Onay Bekleyen İSG Risk Değerlendirme Detay Formları**” listesine iş olarak düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4a23887e-c13c-4091-9988-b3bc5dd61a94)Formu kodu tıklanarak Risk Değerlendirme Formu -Detaylar ekranı açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9db8ef44-75a0-4df0-bae2-427a542940a4)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload72236b23-5d2a-46ff-97a6-4b79bf8f7dee) Onayla butonu tıklanarak Risk Değerlendirme Detayı onaylanarak statü değiştirme ekranında onay notu bilgisi yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf8bbb707-633a-466b-871f-2a33823b8f33)

Onaylama işleminde statü “Tamamlanan” olarak Risk Değerlendirme Formu-Detaylar ekranında görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf8662395-d5f1-4f12-9ce2-1f071fcbe9e1)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload762a66e2-7444-4efb-8f38-26d0fd6741be)(Yazdır) butonu tıklanarak Rapor formatlarında tanımlanan kayıt bazında Rapor alınma işlemi gerçekleştirilir. Rapor formatına eklenen taglerin çalıştığı görülür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbf2322bb-9c54-44f7-b6a9-b48ae9f1446e)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload18caded9-b0ae-404c-b7de-9dfc28059104)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload38a12da2-2643-4910-af83-61cb143762d5)(Excel’e Aktar) butonu tıklanarak kayıt bazında tanımlanan rapor formatları raporu Excel formatında alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1cca45e5-3f0c-4f67-a774-7b73a8b411e0)

Aynı işlem basamakları Form bazında ve genel seçenekleri seçilerek yapılır. Rapor formatlarında kayıt nazında farklı olarak liste, puanlı liste, personel tipli alanların alan kodlarının tagleri <ALAN1_ACK\> \_ACK ekleme işlemi yapılarak rapor formatına eklenir. Tag ekleme işleminde sonra rapor formatı Rapor Formatları Düzenleme menüsünde sisteme yüklenilir. Sisteme yüklenen Rapor formatları düzenleme menüsünde rapor formatı seçilerek rapor formatının adı ve uzantısı ile birlikte kopyalanır. Sistem Altyapı Tanımları\>İSG Risk Değerlendirme \>Rapor Formatları menüsüne gidilir. ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0fbd9fe7-f9e5-4cc1-a6e1-9a8687ba9a44)(Yeni) butonu tıklanarak Rapor Formatları ekranı açılır. Açılan ekranda Rapor adı bilgisi yazılır. Rapor şablonu kısmına Rapor formatları Düzenleme menüsünde Kopyalanan Rapor Formatının şablonu Rapor Şablonu alanı yapıştır işlemi ile tanımlanır. Alt kısmında Rapor Şablonu seçeneklerinden Form bazında rapor alınacaksa form bazında seçeneği, Genel olarak rapor alınacaksa Genel seçeneği seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5ae3d184-f2b0-47d6-9854-4f5daca7c8cd)(kaydet) butonu tıklanarak rapor formatı tanımlanır.

## **1.3. Risk Modüllerinde Sabit Tagler Listesi**

Risk Modüllerinde Sabit Tag’ler listesi aşağıdaki tabloda yer almaktadır.

| **Kısaltma**             | **Açıklama**                                                          |
|--------------------------|-----------------------------------------------------------------------|
|  <RDF_KODU\>            |  RDF Kodu (Form Kodu)                                                 |
|  <RDF_TANIMI\>          |  RDF Tanımı(Form Tanımı)                                              |
|  <RDFD_KODU\>           |  RDFD Kodu                                                            |
|  <RDF_NO\>              |  RDF Numarası                                                         |
|  <RDFD_NO\>             |  RDFD Numarası                                                        |
|  <MSDS_KODU\>           |  MSDS Kodu                                                            |
|  <REV_NO\>              |  Revizyon No                                                          |
|  <REV_TAR\>             |  Revizyon Tarihi                                                      |
|  <HAZIRLAYAN\>          |  Hazırlayanın Adı Soyadı                                              |
|  <SISTEME_GIREN\>       |  Sisteme Girenin Adı Soyadı                                           |
|  <REVIZE_EDEN\>         |  Revize Edenin Adı Soyadı                                             |
|  <STATU_ADI\>           |  Statü Adı                                                            |
|  <RISK_KAYNAGI\>        |  Risk Kaynağı                                                         |
|  <REVIZE_EDEN_ACK\>     |  Revize Edenin Sicil Numarası                                         |
|  <SISTEME_GIREN_ACK\>   |  Sisteme Girenin Sicil numarası                                       |
|  <COLOR\>               |  Risk ekranındaki renk                                                |
|  <TREND\>               |  Risk ekranındaki oklar                                               |
|  <SURECLER\>            |  Süreçler Sekmesinde Seçilen Süreç Bilgisi                            |
|  <MEVCUT_ONLEMLER\>     | Önlemler sekmesinde Önlem tipi alanında Mevcut seçeneğini bilgisi     |
|  <PLANLANAN_ONLEMLER\>  |  Önlemler sekmesinde Önlem tipi alanında Planlanan seçeneğini bilgisi |
| **ÖNLEMLER İÇİN TAGLER** |                                                                       |
| <YAPILANIS\>            | Yapılan iş                                                            |
| <REF_KODU\>             | Alt aksiyonlar -DÖF kodu                                              |
| <STATU_ADI\>            | Statü Adı                                                             |
|  <ACIKLAMA\>            |  Önlem tanımı                                                         |
|  <SORUMLU\>             |  Aksiyon Sorumlusu Olan Kişi                                          |
|  <YAPACAK\>             |  Aksiyon Yapacak Olan Kişi                                            |
|  <DURUM\>               |  Aksiyon Durumu -DÖF durumu                                           |
|  <BITIS_TARIHI\>        |  Aksiyon Bitiş Tarihi                                                 |
|  <REF_TIPI\>            |  Referans Tipi (Doküman, Aksiyon, DÖF, Diğer seçenekleri bilgisi)     |
|  <ONLEM_TIPI\>          |  Önlem Tipi (Mevcut ve Planlanan Seçenek bilgisi)                     |
|  <ONLEM_TARIHI\>        |  Önlem Tarihi                                                         |
|  <ONLEM_NO\>            |  Önlem No                                                             |
|  <GERCEKLESME_TARIHI\>  |  Aksiyon Gerçekleşme Tarihi                                           |

Geçmiş revizyon alanları için <ALAN6_PREV\> gibi tag kullanabilirsiniz. Liste tipli alanlarda prev tagı desteklenmemektedir. Prev tagı sadece numerik ve text tipli alan için çalışmaktadır.
