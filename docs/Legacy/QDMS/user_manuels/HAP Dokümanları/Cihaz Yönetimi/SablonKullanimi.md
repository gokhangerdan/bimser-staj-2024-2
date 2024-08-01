---
title: Şablon Kullanımı
description: Şablon Kullanımı Yardım Dokümanı
sidebar_position: 3
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::


**Cihaz Yönetim Sistemi Modülü Şablon Kullanımı Yardım Dokümanı**

## **1.Cihaz Yönetim Sistemi Modülü**

Kalibrasyon, doğrulama gibi cihaza yönelik işlemlerin takibi, cihaz envanterlerini izleme, kalibrasyon rapor ve tarihçesine anlık olarak erişim, cihaz ve işlem sorumlularını e-mail ile bilgilendirme, işlem maliyetlerinin takibini yapan modüldür.

## **1.1.Sistem Altyapı Tanımları/ Cihaz Yönetim Sistemi**

Cihaz Yönetim Sistemi Modülünün alt yapısının oluşturulacak tanımlamaların yapıldığı kısımdır. Yapılan tanımlamalara göre veriler karşımıza çıkmaktadır.

### **Cihaz Yönetim Sistemi Modülü Şablon Kullanımı**

Cihaz Yönetim Sisteminde, ölçüm sabitleri sekmesinde referans değerlere bir sekme altında girilen gerçekleşen değer kısmını tek tek girme yönetimi yerine, şirketin istediği bir şablon üzerinde bu değerleri girme işlemi geliştirilmiştir. Cihaz Yönetim Sistemi Modülü Şablon Kullanımı için kullanılan 2 yöntem şekli vardır.

1-Cihaz Yönetim sistemi Modülü Genel Şablon Tanıtımı

2-Cihaz Yönetim Sistemi Modülü Cihaz Kategori Bazlı Şablon Ekleme

### **1.1.1.1.Cihaz Yönetim Sistemi Modülü Genel Şablon Tanıtımı**

Cihaz Yönetim sisteminde Modülün genel Şablon tanıtım işlemini tüm cihazlar için geçerli bir yöntem şeklidir. Firmanın istediği şablonlar sisteme tanıtılma işlemi gerçekleştirilir. Firmanın istediği şablonların formatının tanıtılması işlemi yapılırken Qdms uygun hale getirilmesi gerekir. Şablonların formatının tanıtılması işlemi yapılırken Qdms uygun hale getirilmesi için için raplacementler yani Kalibrasyon Raporu kısa kodları kullanılır. Kullanılan Kalibrasyon Raporu şablonu için kullanılan Raplecementler (Kısa Kodlar) aşağıdaki gibidir.

| **RAPLECEMENTLER (KISA KODLAR)** |                     |
|----------------------------------|---------------------|
| **TİPİ**                         | **KODU**            |
| Cihaz Kodu                       | <CIHAZ_KODU\>      |
| Cihaz Adı                        | <ADI\>             |
| Kategorisi                       | <KATEGORI\>        |
| Marka                            | <MARKA\>           |
| Model                            | <MODEL\>           |
| Seri No                          | <SERI_NO\>         |
| Periyot                          | <PERIYOD\>         |
| İşlem Tipi                       | <ISLEM_TIPI\>      |
| İş Emri no                       | <ISEMRI_NO\>       |
| Cihazın Sorumlusu                | <CIHAZ_SOR\>       |
| Bulunduğu yer                    | <BUL_YER\>         |
| Son İşlem Tarihi                 | <SON_ISLEM_TAR\>   |
| Gelecek İşlem Tarihi             | <GEL_ISLEM_TAR\>   |
| İşlem Sorumlusu                  | <KAL_SOR\>         |
| Cihazın Maliyeti                 | <CIHAZ_MALIYETI\>  |
| Cihaza Yönelik İşlem             | <CIHAZ_ISLEM\>     |
| Açıklama                         | <CIHAZ_ISLEM_ACK\> |
| Kalibrasyonu Yapan               | <KAL_SOR\>         |
| Onaylayan                        | <ONAYLAYANLAR\>    |


Kalibrasyon Raporu şablonu format firmanın isteği doğrultusunda hazırlamak için bu Kalibrasyon Raporu şablonun formatında kullanılacak alanları kısa kodlar karşılığı şablon formatına yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0f7bc52f-1be1-4de8-919e-cecdd6300788)

Hazırladığımız bu Kalibrasyon Raporu şablonu formatı SAT\>BSAT\>Konfigürasyon Ayarları menüsünde Rapor Formatları menüsünde yükleme işlemi geçekleştirmemiz gerekmektedir.

#### **1.1.1.1.1.Rapor Formatları Düzenleme**

**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Rapor Formatları Düzenleme

Modüllerde yer alan raporların formatlarında gerekli düzenlemelerin yapıldığı, yeni rapor formatlarının eklendiği menüdür. Cihaz Yönetim Sistemi Modülünde rapor formatlarının yükleme işlemi bu menüden gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8dc05e5e-adfc-46d8-9640-c61827e176b7)

**Ekranda bulanan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload31824e10-5c73-4a44-8935-6d2daa41deb2): Sisteme yeni bir rapor formatı yüklenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload222a1e5d-b7b7-41aa-85cc-d597e78f983f): Listede seçili olan rapor formatı görüntülenip, indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload70b2c060-15ca-43cd-96bc-00f0fa5699ab): Listede seçili olan rapor formatı silinir.

Sisteme yeni bir rapor formatı eklemek için ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload31824e10-5c73-4a44-8935-6d2daa41deb2)Yeni butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8bf40629-1762-4b28-b760-c81ff01b661f)

“Gözat” butonu ile sisteme yüklenmek istenilen rapor formatı seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2c729aad-7d6c-4070-86e6-fc975c6ba4c6)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfe6b4496-0ea7-406d-97d0-f444d9669e36)

Sistemdeki bir rapor formatını üzerinde değişiklik yapılmak isteniliyorsa; rapor formatı seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload121c1d57-5000-476d-a025-cc81bfa6ec51) (Görüntüle) butonu ile rapor formatı bilgisayara indirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaded97ca5e-f3b5-493b-b16f-0db0bd44c894)

Rapor formatı üzerinde alan ekleme, alan çıkarma, rapor formatının düzenlenmesi gibi istenilen değişiklikler yapıldıktan sonra rapor formatının adı hiç değiştirilmeden ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload31824e10-5c73-4a44-8935-6d2daa41deb2)(Yeni) butonu ile sisteme yüklenir. Böylece; sistemde değişiklik yapılan rapor formatının yerine, oluşturulan yeni rapor formatı tanımlanmış olur. Son olarak da Sistem Altyapı Tanımları\>Cihaz Yönetim Sistemi \> Cihaz Yönetim Sistemi Parametreleri menüsüne gelerek Cihaz Yönetim sistemi parametrelerinde 48 numaralı parametreye Rapor formatları Düzenleme menüsüne tanıttığımız raporun ismini seçerek sağ tıkla/Kopyala komutu ile kopyalayarak 48 numaralı parametrenin değeri alanı sağ tıkla/yapıştır komutu ile yapıştırmamız gerekecektir.

### **1.1.2.Cihaz Yönetimi Parametreleri**

**Menü Adı:** Sistem Altyapı Tanımları/ Cihaz Yönetim Sistemi/ Cihaz Yönetimi Parametreleri

Cihaz Yönetimi Modülünün kullanıcının istek ve ihtiyaçlarına göre sistemsel ayarlarının yapıldığı ve bunlara göre parametreleri belirlendiği menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4705e560-41ef-4a3c-9588-784971764ff2)


Cihaz Yönetimi Sistemi Modülü parametreleri menüsüne Cihaz Yönetimi Sistemi Modülü kapsamında ulaşıldığı gibi BSAT/SAT/Konfigürasyon Ayarları/Parametreler menüsünden bu menüye de ulaşılmaktadır. Bsat Modülü menüsünde açılan ekranda tüm Modüllere ait parametrik ayarlamaların yapıldığı bölümdür. Açılan ekrandan filtre sekmesinden Cihaz Yönetimi Sistemi Modülü seçilerek arama yapıldığında, ilgili Modülün parametreleri ekrana gelmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5092a31a-7e69-4ec4-ba38-a352b52339b7)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf9e6ffd2-e6ac-4dda-9a8f-42d8680779fe)

**Ekranda bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfdc08d86-c070-45ad-8a2f-2792d2d80bec): Listede seçili olan parametre için düzeltme/ değişiklik/ güncelleme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade7cdcba3-0274-4c25-a6a0-5383ad22f974): Kayıtlar filtrelenerek arama yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload40a9aebd-d2bd-4d16-8639-17b89eb01d95): Veriler Excel’ e aktarılır.

Bir paramatreden değişiklik yapılmak isteniyorsa, değişiklik yapılmak istenilen parametre seçilir. Parametrenin seçilmesi için parametre no alanına parametrenin numarası yazılır. Yada parametrenın numarası bilinmiyorsa tanım kısmına parametre ile ilgili anahtar bir kelime yazılırak parametre seçilir. ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfdc08d86-c070-45ad-8a2f-2792d2d80bec)(Değiştir) butonu tıklanarak parametrenin içeriği görüntülenir. Cihaz Yönetimi Sistemi Modülü parametrelerinden 48 numaralı “Kalibrasyon Raporu Ölçüm Değerlerinin girileceği Excel Şablonu” parametresi bulunmaktadır. Bu yardım dokümanında Cihaz Yönetimi Sistemi Modülünde Genel Şablon tanımlama işleminin gerçekleştirmek için 48 numaralı Cihaz Yönetim sistemi Modülü parametresi Rapor Formatları Düzenleme menüsünda yüklediğimiz Kalibrasyon Raporunu parametre değerine tanımlayacağız.

**Parametre No:**48

**Parametre Tanımı:** Kalibrasyon Raporu Ölçüm Değerlerinin girileceği Excel Şablonu

**Parametrenin Açıklaması:** Cihaz işlem gerçekleştirme sayfasında ölçüm değerlerini girerken sistem üzerinden bir Excel kullanılarak işlem yapılması isteniyorsa bu Excel rapor formatı sisteme uygun olarak (yeni oluşturulan veya istenilen alanlar taglenerek) rapor formatları menüsüne yüklenir. Buraya yüklenen raporun adı bu parametreye tanımlanmalıdır. Tanımlanan rapor adının Cihaz kategori bazlı şablon ekleme işlemi yapılmamamışsa bu paramatreye göre çalışması sağlanılır.

Sistem Altyapı Tanımları/ Cihaz Yönetim sistemi / Cihaz Yönetim sistemi Parametreleri menüsü tıklanılır. Açılan ekranda Parametre No alanına 48 numarası yazılarak 48 numaralı “Kalibrasyon Raporu Ölçüm Değerlerinin girileceği Excel Şablonu” parametresi seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6e714ff8-4cd9-4ef3-a0a6-96464521c67e)

Cihaz Yönetim sistemi Modülünün 48 numaralı “Kalibrasyon Raporu Ölçüm Değerlerinin girileceği Excel Şablonu” parametresi seçili iken ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfdc08d86-c070-45ad-8a2f-2792d2d80bec) (Değiştir) butonu tıklanarak parametrenin içeriği görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload828e8f06-cdaa-41ed-b20d-61d46ed94c5a)

Cihaz Yönetim Sistemi Parametrelerinde 48 numaralı parametrenin içeriği ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfdc08d86-c070-45ad-8a2f-2792d2d80bec)(Değiştir) butonu içeriği görüntülendiğinde parametre değeri alanında herhangi bir rapor formatı tanıtılma işlemi yapılmadığı görülmektedir. Yüklediğimiz Rapor Formatını parametre değerine tanıtma işlemini gerçekleştirmek için SAT\>BSAT\>Konfigürasyon Ayarları\>Rapor Format Düzenleme menüsüne tıklanılır. Açılan ekranda Yüklenen Rapor Formatı seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload049f9151-2c33-493c-9422-dd072c45d16c) Seçilen Rapor Formatı sağ tıkla/Kopyala komutu tıklanarak kopyalanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4bf88d47-6f7f-461b-b0fd-18e22dab162c) Kopyalan Rapor Formatı Parametreler menüsünde değiştir butonu tıklanarak içeriği görüntülenen 48 numaralı parametrenin değerine alanı sağa tıkla/Yapıştır komutu ile yapıştırılarak tanıtma işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload4f3dc83e-c029-478d-a2c3-cdb736b087f2)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload49d50645-5b21-4fbc-b45e-637eaaf637f1)

Cihaz Yönetim Sistemi Modülü parametrelerinde 48 numaralı “Kalibrasyon Raporu Ölçüm Değerlerinin girileceği Excel Şablonu” parametresinde parametre değerine Rapor Formatları Düzenleme menüsünde yüklenen Rapor Formatı tanımladıktandı sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3045fd34-81bf-4bba-a174-07e6ec3d9ceb) (Kaydet) butonu tıklanarak parametre kayıt güncelleme işlemi gerçekleştirilir.

Bu işlemi tamamladıktan sonra cihaz’ a kalibrasyon işlemi uygularken ölçüm değerleri sekmesi eklediğimiz Excel şablonuna göre gelecektir.

## **1.2.Entegre Yönetim Sistemi/ Cihaz Yönetim Sistemi**

Cihaz Sistemi Yönetimi Modülün Cihaz tanımlama, İşlem Gerçekleştirme, İşlem Tarihçesi menüleri gerçekleştirme ve raporlarının görüntülendiği kısımdır.

### **1.2.1.Cihaz Tanımlama**

**Menü Adı:** Entegre Yönetim Sistemi/ Cihaz Yönetim Sistemi/ Cihaz Tanımlama

Bu ekranda tanımlanan cihazların listesi bulunmaktadır. Cihaz tanımlama işleminin yapıldığı menüdür. Parametrede tanımladığımız Genel Şablonun görüntülenmesi ilk olarak işlem basamağı olarak Yeni bir cihaz Tanımlama işlemi yapılması gerekmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfbf6e918-5a07-49b6-b6ae-c3d76d5569b4)

Listeye yeni bir cihaz eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbbe4dc49-268e-4431-9830-96ec76029e81) (yeni) butonu tıklanarak Cihaz Tanımlama/ Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada27dc7de-661c-4112-b909-482235dc890f)

Gerekli tüm alan bilgileri girildikten sonra, ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeae171d5-7d55-4366-88ea-37a44875ff7f) (Kaydet) butonu tıklanarak Cihaz Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6beaeb3f-4c96-4096-86eb-8bd0ec2f7c61)

Cihaz Tanımlama işleminde sonra Cihazda yapılacak işlem tiplerini tanımlanacaktır. Cihaz listesi ekranındaki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade3000131-17a3-4234-829f-2d1553d8b050) (işlem tipleri) butonuyla tanımlanmış işlem tiplerinden biri ya da birkaçı seçilen cihaza atanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload46f73add-398e-4cee-8fc4-fe163f73bddb)

Açılan ekranda ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb3347a0c-8c35-4e82-b0ee-017999ceb85e) (Yeni) butonuna basılarak cihaza yeni işlem tipi tanımlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade761882a-a31f-498c-ae38-2bf20ad948d7)

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3045fd34-81bf-4bba-a174-07e6ec3d9ceb) (kaydet) butonu tıklanarak Cihaza Ait İşlem Tipleri Tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload04016252-ca43-41be-b874-4363e92c58ed)

### **1.2.2. İşlem Gerçekleştirme**

**Menü Adı:** Entegre Yönetim Sistemi/ Cihaz Yönetim Sistemi/ İşlem Gerçekleştirme

Cihaz Yönetimi Modülünde 26 numaralı “iş emirleri günü geldiğinde otomatik olarak açılsın mı” parametresi “evet” olarak seçilirse tüm iş emirleri zamanı geldiğinde otomatik olarak açılacaktır. Parametreyi aktif hale getirmek için, Sistem Altyapı Tanımları/ Konfigürasyon Ayarları/ Parametreler menüsü izlenerek Cihaz Yönetimi parametreleri sayfasına gelinir. Burada ilgili parametre “evet” olarak seçilirse tüm iş emirleri zamanı geldiğinde otomatik olarak açılmaya başlayacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadec4c314b-e531-43be-9061-afdfdf2c256a)

Ancak zamanından önce işlem yapmak için manuel olarak da iş emri açmak mümkündür. Manuel olarak iş emri açmak ve otomatik olarak açılan iş emirlerini gerçekleştirmek için Cihaz Yönetimi Modülünün Entegre Yönetim Sistemi menüsü altındaki İşlem Gerçekleştirme menüsüne gelinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfbb655e7-2684-4733-8c91-30171eb329ad)

Listeye yeni iş emri eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbbe4dc49-268e-4431-9830-96ec76029e81) (yeni) butonu tıklanarak İş emri Listesi/ Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload51ce9fe9-7821-498f-b9c0-1ef9157779c2)

Bu bilgiler girildikten sonra ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadba58e460-d172-4b7b-b4a5-4687e1ddc457) (kaydet) butonuyla iş emri kaydedilmiş ve işlem sorumlusu olan kişiye atanmış olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcbfd46da-402d-4479-bccb-91d51455f3ec)

İşlem zamanı yaklaştığı zaman parametrelerde belirlenen gün sayısı kadar önce (25. parametre: İş emirleri kaç gün önce haber verilsin (İçerde yapılan), 27. Parametre: İş emirleri kaç gün önce haber verilsin (Dışarda yapılan) ayarlanarak) cihaz sorumlusuna ve işlem sorumlusuna hatırlatma maili gidecektir ve işlem sorumlusunun **Bekleyen İşlerim** ekranında **İşlem Yapılacak Cihazlar** şeklinde bir sekme belirecektir. Planlanan İşlem tarihine dek bu iş emri gerçekleştirilmelidir, aksi takdirde gecikme mailleri gönderilmeye başlanır. Bekleyen işlerim ekranında gecikmiş işler kırmızı renkte, planlanan bitiş tarihi henüz gelmemiş olan işler ise sarı renkte görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddb0c0498-0887-4e78-b8c4-84f3b8d0e480)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcdf1da00-e1eb-4300-9c8d-4be76eb9e329)

İşlem Sorumlusu, cihaz koduna tıklayarak iş emri listesi ekranına yönlenecektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1240858a-55f1-42bc-b189-80574fb2a226)

Listede iş emri seçili iken ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1aab22f7-9435-4668-aaec-58312d68c008) (Kalibrasyon raporu) butonuna basılarak iş emri raporunun yazılacağı ekrana gelinir. Açılan ekranda 3 sekme karşımıza çıkar. Bu işlemler aşama aşama tamamladıktan sonra cihaz’ a kalibrasyon işlemi uygularken ölçüm değerleri sekmesi eklediğimiz Excel şablonuna göre gelecektir. SAT\>Bsat\>Konfigürasyon Ayarları\>Rapor Formatları Düzenleme menüsünde yüklediğimiz ve Cihaz Yönetim sistemi Modülün 48 numaralı “ Kalibrasyon Raporu Ölçüm Değerlerinin girileceği Excel Şablonu” parametresinde tanımladığımız Kalibrasyon Raporu Örneği Ölçüm Değerleri sekmesinde görüntülecektir. Ayrıca bu raporda kullanılan Genel Kalibrasyon Raporu şablonu için kullanılan Raplecementler (Kısa Kodlar) sistem tarafında otomatik olarak çalıştığı ekranda görüntülecektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb82af68a-1ad5-4dbc-8e87-7c3d5f4f4567)

### **1.1.1.2.Cihaz Yönetim Sistemi Modülü Cihaz Kategori Bazlı Şablon Ekleme**

Cihaz Yönetim Sistemi Modülün tanımlanan Cihaz kategorisine de özel şablon hazırlamak mümkündür. Bu işlemin gerçekleştirilmesi için bu şablonlar müşteri ile birlikte Qdms ‘ e uygun hale getirilmesi gerekir. Genel Şablon tanıtılma işleminde olduğu Qdms uygun hale getirilmesi için için Raplacementler yani Kalibrasyon Raporu kısa kodları Cihaz Kategori Bazlı Şablon Ekleme işleminde de kullanılır. Cihaz Kategorisine de özel şablon hazırlamak için öncelikle SAT\>BSAT\>Konfigürasyon Ayarları\>Rapor Formatları menüsünde Hazırlanan Rapor Şablonun yüklememiz gerekir. Sonraki işlem aşaması SAT\>BSAT\>Konfigürasyon Ayarları\>Dil ayarları menüsünde tıklanır. Açılan ekranda Modül alanı kısmında Cihaz yönetim Sistemi Modülü seçilir. Adı Alanı kısmına **“lblKalRapExcelTemplate”** label kodu yazılır. Çıkan alan seçilerek değiştir butonu tıklanarak bu alana isim verilme işlemi yapılır. Bu işlemi gerçekleştirmek için Öncelik Cihaz Yönetim sistemi Modülünde Cihaz Kategorisi menüsün de bir Cihaz kategori tanımlama işlemi yapmak gerekmektedir.

#### **1.1.1.2.1.Dil Ayarları**

**Menü Adı:** Sistem Altyapı Tanımları/ BSAT/ Konfigürasyon Ayarları/ Dil Ayarları

Dil ayarları menüsünden QDMS üzerinde görülen menülerin isimleri, alanların isimleri değiştirilebilir. Modüllere yeni alanlar eklenebilir. Var olan alanların zorunluluk durumları düzenlenebilir. Alanların ekran üzerinde göründükleri sıralama değiştirilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfa0896c8-4802-49b8-94ac-b02248ae4ac3)

Mevcut bir alan değiştirilmek istenildiği zaman TR kısmı seçilir. İlgili alan seçilerek değişiklik (isim değişikliği, zorunluluk durumu vb.) yapılacak alan ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfdc08d86-c070-45ad-8a2f-2792d2d80bec)(değiştir) butonuna ile açılır. Açılan ekranda değiştirilmek istenilen kısımlar değiştirilerek kaydedilir.

Dil ayarları menüsünde Modüler kısmında Cihaz Yönetim Sistemi Modülü seçilir. Cihaz Yönetim sistemi Modülü seçili olduğu dil ayarları menüsünde Başlıklar sekmesinde Cihaz Yönetim Sistemi ile ilgili tanımlı alanlar listelenir. Cihaz Yönetim Sistemi Modülünde Kategori Bazlı Şablon ekleme işlemi için ilgili alanın ismin tanımlamasının Dil ayarları menüsünde yapılmaktadır. Dil Ayarlarında Başlıklar sekmesi tıklanılır. Açılan ekranda Adı Alanı kısmına **“lblKalRapExcelTemplate”** label kodu yazılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload015f01af-aa88-48e1-9215-243e74f9e815)

Label Kodu seçili iken ![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfdc08d86-c070-45ad-8a2f-2792d2d80bec)(Değiştir) butonu tıklanarak alanın içeriği görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1c751d90-a401-49af-86f4-d3a32f6c8818)

Rapor Formatları Düzenleme menüsünde yüklenecek Raporun ismi Dil ayarların ekranında değeri alanın kısmına yazılarak ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3045fd34-81bf-4bba-a174-07e6ec3d9ceb) (Kaydet) butonu tıklanarak alan tanımlanarak Cihaz Kategori menüsünde tanımlı olarak gelmesi sağlanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbd413c50-49b1-471f-a4ad-87c7b390f94d)

Bu işlem aşamasında sonra Cihaz İşlem Raporunun SAT\>BSAT\>Konfigürasyon Ayarları\>Rapor Formatları menüsünde yükleme işlemi için Rapor Formatları menüsü tıklanarak açılır.

Sisteme yeni bir rapor formatı eklemek için ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload31824e10-5c73-4a44-8935-6d2daa41deb2)Yeni butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc6d901da-0df9-4c5b-be31-a4ab07039b9e)

“Gözat” butonu ile sisteme yüklenmek istenilen rapor formatı seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6616a268-0ac1-4480-97a0-33172653aa04)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf8440a12-5c82-46ea-95bf-eb007e0c3331)

Bilgisayarda kayıtlı Rapor formatı seçilerek Rapor formatları Düzenleme menüsü yüklenilir. Rapor Formatları menüsünde yüklenen bu Cihaz İşlem Raporu adında Rapor formatının Cihaz Kategori Bazlı ekleme işlemi için bir Cihaz Kategorisi menüsün de Cihaz Kategori tanımlamayarak yapılan ekleme işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddaea592f-d444-40aa-8a7e-0c88aeaad384)

### **1.1.3.Cihaz Kategorileri**

**Menü Adı:** Sistem Altyapı Tanımları/ Cihaz Yönetim Sistemi/ Cihaz Kategorileri

Cihaz Kategorileri, Cihaz Yönetim Sistemi’nde kullanılacak olan cihazların kategori oluşturma işleminin gerçekleştiği menüdür. Bu menüde Cihazları genel olarak ağırlık ölçerler nelerdir, basınç ölçerler nelerdir ve uzunluk ölçerler nelerdir belirleyerek kategorize ediyoruz. Örneğin ağırlık ölçülerin altında kantarlar ve teraziler olabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7a979b88-8bf9-4426-85e1-7741b24caad2)

Listeye yeni bir cihaz kategorisi eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbbe4dc49-268e-4431-9830-96ec76029e81) (yeni) butonu tıklanarak Cihaz Kategorisi Tanımlama/ Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcc5d713d-e17a-4311-98db-9cc7865ae230)

Cihaz Kategori Tanımlama Yeni Kayıt ekranında Cihaz Kategorisi tanımlama işlemi yapıldığı ekranda Dil Ayarlarında tanımladığımız Cihaz İşlem Raporu alanı da tanımlı olarak gelir. Açılan ekranda tanımlı olan Cihaz İşlem Raporu alanına Rapor Formatları menüsünde yüklünen Raporu seçilerek sağ tıkla/ kopyala komutu ile Cihaz İşlem Raporu alanında sağ tıkla/yapıştır komutu ile yapıştırılır.

1.aşamada SAT\>BSAT\>Konfigürasyon Ayarları\>Rapor Formatları Düzenleme menüsü tıklanarak yüklenen Rapor seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade929cb21-d243-4d85-95f8-0c09b965bd4d)

2\. aşamada SAT\>Cihaz Yönetim Sistemi \>Cihaz Kategorileri Tanımlama menüsünde Yeni butonu ile tanımlanan Cihaz Kategorisi Tanımlama menüsüne gelinir. Açılan ekranda Cihaz işlem Raporu alanına yüklenen Rapor Formatı sağ tıkla/Yapıştır komutu ile yapıştırılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3a368a02-904c-4ab0-8bf9-a08654484395)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd689bd55-2d3a-4f54-96ff-a38239b1f653)

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3045fd34-81bf-4bba-a174-07e6ec3d9ceb) (kaydet) butonu tıklanarak Cihaz Kategori tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6febe77a-512e-46e2-8acc-2455c9c7f6e2)

Cihaz Kategori Bazında Ekleme işlemi yapıldıktan sonra EYS\>Cihaz Yönetim Sistemi/Cihaz Tanımlama işlemi yapılır. Cihaz listesi ekranındaki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade3000131-17a3-4234-829f-2d1553d8b050) (işlem tipleri) butonuyla tanımlanmış işlem tiplerinden biri ya da birkaçı seçilen cihaza atanır. Entegre Yönetim Sistemi/ Cihaz Yönetim Sistemi/ İşlem Gerçekleştirme menüsünde listeye yeni iş emri eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbbe4dc49-268e-4431-9830-96ec76029e81) (yeni) butonu tıklanarak İş emri Listesi/ Yeni Kayıt ekranı görüntülenerek İş Emri kayıt işlemi gerçekleştirilir. Bu işlemlerden sonra Cihaz Kategori Bazında Şablon ekleme işlemi İş emri Listesinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadde7f7714-62f6-4b47-8367-e275024f69f1)(Kalibrasyon Raporu) butonu tıklanarak açılan İşlem Raporu ekranında Ölçüm Değerleri sekmesinde görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaded0e6f3e-96b3-4e15-8e03-c30efad5f9b4)
