---
title: Raporlara Parametrik Alan Ekleme İşlemi ve Genel Tag Listesi
description: Raporlara Parametrik Alan Ekleme İşlemi ve Genel Tag Listesi Kullanıcı Yardım Dokümanı
sidebar_position: 4
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::

**Doküman Yönetim Modülünde Raporlara Parametrik Alan Ekleme İşlemi ve Genel Tag Listesi Kullanıcı Yardım Dokümanı**


# **1.Doküman Yönetim Modülünde Raporlara Parametrik Alan Ekleme İşlemi ve Raporlarda Kullanılan Taglar**

Doküman Yönetimi Modülü raporlarından Doküman Özet Listesi raporunun rapor formatı olan “MasterSablon_TR.xls” formatına parametrik alan ekleme işlemi yapılmaktadır. Raporlara bu parametrik alan ekleme işlem basamakları ve Doküman Yönetimi Modülünde kullanılan taglerin (kısa kodların) listesi bu yardım dokümanında yer almaktadır

## **1.1.Doküman Yönetimi Modülünde Parametrik Alanların Doküman Özet Raporunda  Gösterimi**

Doküman Yönetimi Modülü raporlarında Doküman Özet Listesi raporuna eklenen parametrik alanların raporda gösterilme işlemi için öncelikle dil ayarları menüsünde parametrik alan tanımlama işlemi yapmak gerekiyor. Dil ayarlarında metin, liste, gibi parametrik alan tanımlama işlemi yapılır. Bu tanımlanan parametrik alanlar Doküman Yönetimi modülünde Doküman hazırlama, doküman sisteme aktarım gibi menülerde diğer bilgiler sekmesinde görüntülenir. Bir doküman hazırlama işleminde veya bir doküman sisteme aktarma işlemi yapılarak diğer bilgiler sekmesinde tanımlı parametrik alanların bilgisi girilir. Bir dokümanın Doküman hazırlama veya doküman sisteme aktarma işleminden sonra Rapor formatları menüsüne gidilir. Rapor Formatları menüsünde Doküman Özet listesi raporunun rapor format (MasterSablon_TR.xls) indirilir. İndirilen bu rapor formatına (MasterSablon_TR.xls) dil ayarlarında tanımlanan alanların doküman dosyasına <DOC_ADI\>, <DOC_KODU\> gibi kod olarak kullanmak isterseniz alan kodunun lbl olmadan tag içerisine yazmanız yeterli olacaktır. Örneğin lblALAN2 için indirilen rapor formatına kod kullanmak isterseniz <ALAN2\> kısa kodu olarak yazılır. Bu şekilde doküman hazırlama veya doküman sisteme aktarma menülerinde sisteme aktarılan dokümanın diğer bilgiler sekmesindeki parametrik alanlar Doküman Özet Listesi Rapor formatına tag şeklinde yazılır. Rapor formatına parametrik alanların tag şeklinde yazıldıktan Rapor format (MasterSablon_TR.xls) aynı isimde bilgisayara kaydedilir. Kaydedilen aynı isimde Doküman Özet Listesi Rapor formatı Rapor Formatları menüsünde tekrar sisteme yüklenir. Doküman Özet Listesi Rapor formatının yükleme işleminde sonra Doküman Yönetimin Raporlarında Doküman Özet Listesi Raporu menüsüne gidilir. Açılan ekranda Doküman hazırlama veya Doküman sisteme aktarma işlemleri ile sisteme yüklenen doküman görüntülenir. Doküman seçili iken Excel aktar butonu tıklanarak Excel format alınan raporda parametrik alanların taglerinin bulunduğu kısımda diğer bilgilerde girilen alan bilgilerinin geldiği görülerek taglerin çalıştığı görülür.

### **1.1.1.Doküman Yönetim Modülünde Parametrik Alan Tanımlama**

Doküman Yönetimi Modülünde Parametrik ekleme işlemi için SAT\>BSAT\>Konfigürasyon Ayarları\>Dil ayarları menüsüne gidilir. Modüller alanında Doküman Yönetimi Modülü seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd3d55511-b22a-4d68-b9b8-1bdbf0655f65)

Doküman Yönetimi Modülünü seçildikten sonra Liste geldikten sonra Başlıklar sekmesine gelip içerisine lblALAN yazılır. Burada listelenen ALAN2,ALAN3,....ALAN6 metin tipli alanları ,lblALAN7,lblALAN8 .....lblALAN11 ise liste tipinde parametrik alanlardır. Metin tipli ve Liste tipli parametrik alan tanımlaması yapılarak bu alanların Doküman Özet Listesi raporunda gösterilme işlemini yapmak için öncelikle metin tipli ve sonrasında liste tipli parametrik tanımlama işlemi yapılır.

### **1.1.1.1.Metin Tipli Parametrik Alan Tanımlama İşlemi**

Doküman Yönetimi Modülünde Entegre Yönetim Sistemi\>Doküman İşlemleri\> Doküman Hazırlama gibi diğer menülerde diğer Bilgiler sekmesinde metin tipli bir alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına metin yazarak metin tipli parametrik alanlar aratılır ve metin tipli parametrik alanların listesi Dil ayarları menüsünde listenir. Listenen metin tipli parametrik alanlara alan tanımlaması yapılır. Bu metin tipli alanın daha sonra Doküman Özet listesinde gösterilme işleminde tag’ini kullanmak için tanımlama işlemi yapılacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload731e4438-1ac7-4f35-98ae-9a030118c1a8)

lblALAN2 Metin tipli parametrik alan seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload88e5edc5-5724-4fdd-a8ce-b96dac331940) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9c3eee74-ce31-4f27-9df7-fb7f83e6d679)

Alanın zorunlu olup, olmayacağı sıra no bilgisi gibi gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb95df34a-805f-4c55-b731-bccd9d87b5ff)(kaydet) butonu tıklanarak Metin tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade1d52dac-53e4-4815-a6a4-8577b36c5a85)

### **1.1.1.2.Liste Tipli Parametrik Alan Tanımlama İşlemi**

Doküman Yönetimi Modülünde Entegre Yönetim Sistemi\>Doküman İşlemleri\> Doküman Hazırlama menüsü gibi diğer menülerde diğer bilgiler sekmesinde liste tipli bir parametrik alan tanımlamak için öncelikle Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları menüsüne gelerek tip alanına liste yazarak liste tipli parametrik alanlar aratılır ve liste tipli parametrik alanların listesi Dil Ayarları menüsünde listenir. Listenen liste tipli parametrik alanların alan tanımlaması yapılır. Bu liste tipli alanın daha sonra Doküman Özet listesinde gösterilme işleminde tag’ini kullanmak için tanımlama işlemi yapılacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf417ec5b-6b25-4588-9af7-1d7b67ad8c0b)

lblALAN7 Liste tipli parametrik seçilerek alanın veri girişi için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload88e5edc5-5724-4fdd-a8ce-b96dac331940) (değiştir) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2ff3ceeb-15dd-4412-85b5-a33ed386c686)

Liste tipli alanın liste değerlerini girmek için ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb40d59b5-d397-485c-9724-3c260fa6f13a) (Yeni) butonuna tıklanır, liste değerleri yazılır ve kaydedilir.

Liste değeri 1 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf15f03a2-5ebc-4e4e-a5ec-5d6fac725c21)

Liste değeri 2 için tanımlama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeb8ba119-525b-426f-914a-e99de9345326)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2dd3e952-d45e-4cb3-9a79-b15a50f62e0d)

Alanın zorunlu olup, olmayacağı sıra no bilgisi ve liste elemanları tanımlanarak gerekli alanlar doldurularak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb95df34a-805f-4c55-b731-bccd9d87b5ff)(kaydet) butonu tıklanarak liste tipli parametrik alan tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0eed6ee7-4a66-48e2-8f04-ec7990d1c72a)

Tanımlandığımız bu alanları doküman özet listesi rapor formatına <DOC_ADI\>, <DOC_KODU\> gibi kod olarak kullanmak isterseniz alan kodunun lbl olmadan tag içerisine yazmamız yeterli olacaktır. Metin tipli tanımladığımız lblALAN2 parametrik alan için Doküman Özet Listesi rapor formatında kullanılacak kod <ALAN2\> kısa kodudur.. Liste tipli lblALAN7 parametrik alan için <ALAN7\> kısa kodu Doküman Özet listesi rapor formatında kullanılacaktır.

### **1.1.2.Doküman Özet Listesine Eklenecek Alanlarının Değerlerinin Girilmesi**

Doküman Özet listesine eklenecek alanların değerlerinin girilmesi için Doküman Hazırlama, Doküman Siteme aktarma gibi menülerde diğer bilgiler sekmesinde alanın değerinin girilme işlemi yapılır. Bu işlemin gerekleştirilmesi için sisteme bir doküman yükleme işlemi yapılır. Bu dokümanı yükleme işlemi için SAT\>Doküman İşlemleri\>Doküman Sisteme Aktarma menüsü tıklanılır. Bu menüde onaysız ve kontrolsüz bir şekilde bir dokümanın aktarımı yapılır. Bu menu ile doküman yükleme işleminde diğer bilgiler sekmesindeki bu alanların değerlerinin girilir. Bu alan değerleri girildikten sonra rapor formatına eklenen alanların tagleri ile rapora bu parametrik alanların yansıması işlemi için gerçekleştirilir. Raporda tanımlanan alan değerlerin bilgisinin gelmesi için alan bilgilerin girilmesi gerekmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0e7b9de9-17e5-4317-b148-825bbd9e9771)

Açılan ekranda dokümanın aktarılacağı klasör seçilir ve ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade4264e40-eeca-4091-9e24-4fc1bfb7ebef) (İleri) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb50a41ef-92e1-49af-83ab-af3fbc906b0c)

Doküman Bilgileri sekmesinde doküman bilgileri girilir. Diğer bilgiler sekmesi tıklanarak Dil ayarlarında tanımlanan parametrik alanların bilgisi girilir. Bu alanlar metin tipli “Doküman Açıklaması” ve liste tipli “Doküman Türü” parametrik alanlarıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload09a3bb66-38d2-46d7-b5af-0c809b8ab563)

Doküman detay bilgileri girilir ve yüklenecek doküman seçilir. Bu işlem, doküman hazırlama menüsündeki işlemlerle aynıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada2bfaa38-3ce2-4774-b5dd-759dea21dc6c)

Sisteme tüm bilgiler girildikten sonra “Doküman Dosyası Yükleme (Türkçe)” alanından “Dosya Ekle” butonu ile doküman içeriye aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload991e15f2-cd4f-4993-acbe-8a89e44ff1cb)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada55f743e-9fa1-48a2-9f91-a9e9d9223720)

Doküman sisteme yükleme işleminde sonra “Dosya başarıyla aktarılmıştır” mesaj alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6ea88ed8-f6d5-4c3e-89e7-d10123c48246)

Doküman bilgileri ekranındaki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6d7b4102-2321-40c3-978c-5081dec056d6) (Kaydet) butonu yardımıyla dokümanın sisteme aktarma işlemi tamamlanmış olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7e6cfc2d-756f-4258-a9f6-d7b6d83fdbad)

Doküman sisteme aktarma menüsü bir doküman onaysız ve kontrolsuz bir şekilde sisteme aktarılma işlemi yapılır. Bu dokümanı sisteme aktarılma işleminde Doküman yönetimi modülünde tanımlanan parametrik alanların bilgi girişi yapılır.

### **1.2.3.Doküman Özet Listesine Rapor Formatına Tanımlanan Parametrik Alanların Taglerin  Eklenmesi**

Doküman Özet listesine tanımlanan parametrik alanların taglerin eklenmesi için SAT\>BSAT\> Konfigürasyon Ayarları\>Rapor Formatları menüsüne gidilir. Qdms tüm raporların yüklendiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload998b07cc-6d7a-462e-bab9-751306ae6cfb)

**Ekranda bulanan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7349c1a4-c38e-4d2b-b812-a11b48d12eb3): Sisteme yeni bir rapor formatı yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadded29e04-64c5-4d9b-8034-d3ccfd3cd195): Listede seçili olan rapor formatı görüntülenip, indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload33e5575b-f826-4e9e-b58d-78dabc64fe67): Listede seçili olan rapor formatı silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload69226dc5-ea6a-4198-9488-cedc3dab18f8) (Görüntüle) butonu tıklanarak Doküman Özet Listesi rapor format şablonu (MasterSablon_TR.xls) bilgisayara indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb61ef0d5-5d8a-4a50-8fad-42159fd17e61)

Rapor formatına tanımlanan parametrik alanların alan tanımları ve tagleri ilgili bilgiler yazılırak rapor aynı isimde formatı bilgisayara kaydedilir. Örnekte olduğu gibi Metin tipli parametrik alanın için tag <ALAN2\> kısa kodu yazılır. Liste tipli parametrik alan için tag <Alan7\> kısa kodu yazılır.

Bilgisayara kaydedilen aynı isimdeki Rapor format ((MasterSablon_TR.xls) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb09f9c06-f9b8-4f3b-ac9b-6e1253053872) (Yeni) butonu ile tekrar rapor formatları menüsüne sisteme yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload63ec7334-f9a2-4158-b75f-ece954593b51)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9d39512c-d80c-4f83-a7e7-69a38581afc8)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4cf28305-d491-425f-b6f0-f6c7a5891239)

Rapor formatları menüsünde aynı isimde rapor format yükleme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada487711c-b801-4a73-8314-b48f7762569b)

### **1.2.4.Doküman Özet Listesi Rapor Formatına Eklenen Parametrik Alanların Gösterimi**

Doküman Özet listesi rapor formatına (MasterSablon_TR.xls) tag ekleme işlemi yapılan rapor format yükleme işleminde sonra Entegre Yönetim Sistemi\>Doküman İşlemleri\>Raporlar\>Doküman Özet listesi raporu menüsüne gidilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload03d931d1-a327-4995-b1a8-61e78e655c82)

Açılan ekranda Doküman Sisteme aktarım menüsünde sisteme aktarılan dokümanın bulunduğu klasör Bağlı olduğu klasör alanında seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd4a061bc-0f1f-4fb6-bf90-75eb282e93e8)(Ara) butonu tıklanarak Dokümanın doküman özet listesine gelmesi sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6e7ce2ab-90f5-44ca-9ea7-25e15f2d7bff)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1ac430e8-5db3-4233-82ab-33527b7d2da9) (Excel’e Aktar) butonu ile “Doküman Özet Listesi Raporu” görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada8b112b9-e8af-4871-85db-066fbadc4c09)

Excel aktar butonu ile alınan Excel formatındaki rapordaki taglerin çalıştığı ve tanımlanan parametrik alanların değerlerin raporda bilgisinin geldiği görülür.

# **2.Doküman Yönetimi Modülünde Replacement (Kısa Kodlar) Tag Tablosu**

Doküman Yönetimi Modülünde kullanılan genel taglerin (kısa kodların) listesi aşağıdaki tabloda yer almaktadır.

| **Kısaltma**                                                                                                                | **Açıklaması**                                                 |
|-----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| **<DOC_KODU\>**                                                                                                            | DokümanKodu                                                    |
| **<DOC_TIPI\>**                                                                                                            | DokumanTipi                                                    |
| **<REV**\_**NO\>**                                                                                                         | Revizyon No                                                    |
| **<MANUAL_REVNO\>**                                                                                                        | Manual Revizyon No                                             |
| **<DOC_ADI\>**                                                                                                             | Doküman Adı                                                    |
| **<DOC_ING_ADI\>**                                                                                                         | Doküman İngilizce Adı                                          |
| **<DOC_GRUP_KODU\>**                                                                                                       | DokümanGrupKodu                                                |
| **<DOC_GRUP_ADI\>**                                                                                                        | Doküman GrupAdı                                                |
| **<DOC_HAZ_TAR\>**                                                                                                         | Hazırlanma Tarihi                                              |
| **<HAZ_SICIL\>**                                                                                                           | Hazırlayan Sicil                                               |
| **<HAZ_POZ\>**                                                                                                             | HazırlayanPozisyonKodu                                         |
| **<HAZ_POZ_TAN\>**                                                                                                         | HazırlayanPosizyonTanımı                                       |
| **<HAZIRLAYAN\>**                                                                                                          | HazırlayanınAdıSoyadı                                          |
| **<KONT_SICIL\>**                                                                                                          | KontrolEden SicilNo                                            |
| **<KONT_POZ\>**                                                                                                            | KontrolEden PozisyonKodu                                       |
| **<KONT_POZ_TAN\>**                                                                                                        | KontrolEdenPozisyonTanımı                                      |
| **<KONTROL_EDEN\>**                                                                                                        | KontrolEdeninAdıSoyadı                                         |
| **<SORUMLU_SICIL\>**                                                                                                       | Sorumlu SicilNo                                                |
| **<SORUMLU_POZ\>**                                                                                                         | SorumluPozisyonKodu                                            |
| **<SORUMLU_POZ_TAN\>**                                                                                                     | SorumluPozisyonTanımı                                          |
| **<SORUMLU\>**                                                                                                             | SorumlununAdıSoyadı                                            |
| **<SOR_KISIM_KODU\>**                                                                                                      | SorumluDepartmanKodu                                           |
| **<SORUMLU_KISIM\>**                                                                                                       | SorumluDepartman                                               |
| **<REV_SICIL\>**                                                                                                           | RevizeEdenSicilNo                                              |
| **<REV_POZ\>**                                                                                                             | RevizeEdenPozisyonKodu                                         |
| **<REV_POZ_TAN\>**                                                                                                         | RevizeEdenePozisyonTanımı                                      |
| **<REVIZE_EDEN\>**                                                                                                         | RevizeEdenAdıSoyadı                                            |
| **<REV_TARIHI\>**                                                                                                          | RevizyonTarihi                                                 |
| **<REV_NEDEN\>**                                                                                                           | RevizyonNedeni                                                 |
| **<ONAY_TAR\>**                                                                                                            | Onay Tarihi                                                    |
| **<SON_ONAY_SICIL\>**                                                                                                      | Son Onaycı Sicili                                              |
| **<SON_ONAY_POZ\>**                                                                                                        | Son Onaycı Pozisyon Kodu                                       |
| **<SON_ONAY_POZ_TAN\>**                                                                                                    | Son Onaycı Pozisyon Tanımı                                     |
| **<SON_ONAY\>**                                                                                                            | Son Onaycı adı soyadı                                          |
| **<TUM_ONAY_SICIL\>**                                                                                                      | Tüm Onaycıların sicili                                         |
| **<TUM_ONAY_POZ\>**                                                                                                        | Tüm Onaycıların Pozisyonu                                      |
| **<TUM_ONAY_POZ_TAN\>**                                                                                                    | Tüm onaycıların pozisyon tanımları                             |
| **<TUM_ONAY_ADI\>**                                                                                                        | Tüm Onaycıları adı soyadı                                      |
| **<YAYIMLAYAN_SICIL\>**                                                                                                    | Yayımlayan sicili                                              |
| **<YAYIMLAYAN_POZ\>**                                                                                                      | Yayımlayan pozisyon kodu                                       |
| **<YAYIMLAYAN_POZ_TAN\>**                                                                                                  | Yayımlayan pozisyon tanımı                                     |
| **<YAYIMLAYAN\>**                                                                                                          | Yayımlayan adı soyadı                                          |
| **<YONETIM_SISTEMLERI\>**                                                                                                  | YönetimSistemleri                                              |
| **<REFERANS_DOKUMANLAR\>**                                                                                                 | ReferansDokümanlar                                             |
| **<GRUP_EGITICI\>**                                                                                                        | Eğitmen                                                        |
| **<X_ONAY_ADI\>**                                                                                                          | X. Onaylayanın Adı (X=1,2,3...)                                |
| **<X_ONAY_SCL\>**                                                                                                          | X. Onaylayanın Sicili(X=1,2,3...)                              |
| **<X_ONAY_POZ\>**                                                                                                          | X. Onaylayanın Pozisyon Kodu(X=1,2,3...)                       |
| **<X_ONAY_POZ_TAN\>**                                                                                                      | X. Onaylayanın Pozisyon Tanımı(X=1,2,3...)                     |
| **<PRN_KK\>**                                                                                                              | Kontrollü Kopya Parametresi(QDMS-GEN-10,11 no'lu parametreler) |
| **<P_SICIL\>**                                                                                                             | Print Alan Sicil                                               |
| **<P_ADI\>**                                                                                                               | Print Alan Personel Adı                                        |
| **<P_TARIH\>**                                                                                                             | Print Alınan Tarih(gg.aa.yyyy)                                 |
| **<P_UTARIH\>**                                                                                                            | Print Alınan Tarih (gg.aa.yyyy ss:dd:nn)                       |
| **<KONTROL_DEPARTMAN_ADI\>**                                                                                               | Kontrol eden kişinin Departmanı                                |
| **<ONAYLAYAN_DEPARTMAN_ADI\>**                                                                                             | Son Onaycının Departmanı                                       |
| **<REVIZYON\>**                                                                                                            | Revizyon                                                       |
| **<KONTROL_TAR\>**                                                                                                         | Kontrol tarihi                                                 |
| **<REV_EDEN_DEPARTMAN\>**                                                                                                  | Revize Edenin Departmanı                                       |
| **<SURECLER\>**                                                                                                            | Dokumanın bağlı olduğu süreçler                                |
| **<X_ID\>,\<X_DATE\>,<X_APPROVAL\>,<X_REASON\>,<X_REVISION\>,<X_REVIZE_EDEN\> --79 no’lu parametre ile aktif edilir.** | Revizyon Tarihçesi X=1,2,3..                                   |
| **<SUREC_KODLARI\>**                                                                                                       | Süreç Kodları                                                  |
| **<REVEDEN_DEPARTMAN_KODU\>**                                                                                              | Revize Edenin Departman Kodu                                   |
| **<KONTROL_DEPARTMAN_KODU\>**                                                                                              | Kontrol Edenin Departman Kodu                                  |
| **<ONAYLAYAN_DEPARTMAN_KODU\>**                                                                                            | Son Onaycının Departman Kodu                                   |
| **<ON_KONT_SICIL\>**                                                                                                       | Ön Kontrol Edenin Sicil Numarası                               |
| **<ON_KONT_POZ\>**                                                                                                         | Ön Kontrol Edenin Pozisyon Kodu                                |
| **<ON_KONT_POZ_TAN\>**                                                                                                     | Ön Kontrol Edenin Pozisyon Tanımı                              |
| **<ON_KONT_EDEN\>**                                                                                                        | Ön Kontrol Edenin Adı Soyadı                                   |
| **<KONTROL_GRUP\>**                                                                                                        | Kontrol Grubunun Kodu                                          |
| **<KONTROL_GRUP_ACK\>**                                                                                                    | Kontrol Grubunun Açıklaması                                    |
| **<ONKONTROL_GRUP\>**                                                                                                      | Ön Kontrol Grubunun Kodu                                       |
| **<ONKONROL_GRUP_ACK\>**                                                                                                   | Ön Kontrol Grubunun Açıklaması                                 |
| **<GRUP_EGITICI_POZ_TAN\>**                                                                                                | Eğiticinin Pozisyon Tanımı                                     |
| **<GOZGECPOZ\>**                                                                                                           | Gözden Geçirecek Pozisyon                                      |
| **<GOZ_GEC_TAR\>**                                                                                                         | Gözden Geçirme Tarihi                                          |
| **<SONRAKI_GOZ_GEC_TAR\>**                                                                                                 | Gelecek gözden geçirme tarihi                                  |
| **<HAZIRLAYAN_DEPARTMAN_ADI\>**                                                                                            | Hazırlayan Departman Adı                                       |

<U_TARIH\> : E-imza parametresinde kullanırılır. (Örnek: Bu doküman \<U_TARIH\> tarihinde e-imza ile onaylanmıştır.)

# **3.Kalite Kaydı İçin Kalite Kaydı Dokümanlarında Kullanılan Tagler**

Kalite kaydı için kullanılan taglerin listesi aşağıdaki tabloda yer almaktadır.

| **<KK_NO\>**           | Kalite Kaydı numarası                    |
|-------------------------|------------------------------------------|
| **<KK_ONAY_ADI\>**     | Kalite Kaydını onaylayan ad soyadı       |
| **<KK_ONAY_POZ\>**     | Kalite Kaydını onaylayan pozisyon kodu   |
| **<KK_ONAY_POZ_TAN\>** | Kalite Kaydını onaylayan pozisyon tanımı |
| **<KK_ONAY_TAR\>**     | Kalite Kaydı onay tarihi                 |
| **<KK_HAZIRLAYAN\>**   | Kalite Kaydı hazırlayan kişi             |

# **4.Doküman Özet Listesi Raporu Tag Listesi**

Doküman yönetiminde genel olarak sistemdeki tüm dokümanların listesine ulaşıldığı rapor Doküman Özet Listesi Raporu için kullanılan taglerin adı ve açıklaması tabloda yer almaktadır.

| **\<DOC_KODU\>**      | Doküman Kodu                  |
|-----------------------|-------------------------------|
| **<DOC_ADI\>**       | Doküman Adı                   |
| **<DOC_ING_ADI\>**   | Doküman İngilizce Adı         |
| **<DTIP_ACK\>**      | Doküman Tipi                  |
| **<DOC_HAZ_TAR\>**   | Hazırlama Tarihi              |
| **<REVNO_SON\>**     | Revizyon No                   |
| **<REV_TARIHI\>**    | Revizyon Tarihi               |
| **<REVIZE_EDEN\>**   | Revize Eden                   |
| **<SORUMLU_KISIM\>** | Sorumlu Kısım                 |
| **<REV_NEDEN\>**     | Revizyon Nedeni               |
| **<REVIZYON\>**      | Revizyon                      |
| **<SON_GOZGEC\>**    | Son Gözden Geçirme Tarihi     |
| **<GEL_GOZGEC\>**    | Gelecek Gözden Geçirme Tarihi |
| **<GOZGEC_PER\>**    | Gözden Geçirme Periyodu       |
| **<ONAY_TAR\>**      | Onay Tarihi                   |
| **<SURECLER\>**      | Kullanıldığı Süreçler         |
| **<SORUMLU\>**       | Doküman Sorumlusu             |
| **<IMHASURESI\>**    | Arşivleme Süresi              |
