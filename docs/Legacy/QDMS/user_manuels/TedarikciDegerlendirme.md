---
title: Tedarikçi Değerlendirme
description: Tedarikçi Değerlendirme Yardım Dokümanı
sidebar_position: 52
---

:::tip Bilgi

İlgili konu başlığına sağ tarafta bulunan navigasyon yardımıyla hızlı bir şekilde ulaşabilirsiniz.

:::

**Tedarikçi Değerlendirme Modülü(v.5.24) Kullanıcı Yardım Dokümanı**

Modül Versiyonu: 5.24



**1.GİRİŞ**: Tedarikçi Değerlendirme Modülü, kurumların tedarikçilerin belirlenen kriterlere göre anket yoluyla değerlendirilmesini sağlayan bir modüldür.

**2.AMAÇ**: Bu yardım kılavuzunun amacı; Tedarikçi anketlerin elektronik ortama taşınması, oluşan verilerin saklanması ve analiz edilebilmesini sağlamaktır.

**3.KISALTMALAR**: QDMS: Quality Document Management System, SAT: Sistem Altyapı Tanımlamaları, BSAT: Bimser Sistem Altyapı Tanımlamaları

# **4.TEDARİKÇİ DEĞERLENDİRME MODÜLÜ**

Kurumunuzun tedarikçilerini belirlediğiniz kriterlere göre anketler aracılığıyla değerlendirildiği, Tedarikçi gruplarınızı tanımlayarak, aynı grup içerisinde bulunan tedarikçilerinize aynı anket formatının gönderilmesini, grup tanımlamasının ardından tedarikçilerinizi sisteme kazandırılması, Tedarikçilerinizin kabulü için 3lü, 5li veya şirketinizde bulunan herhangi bir skalayı göre Değerlendirme Kategorisi olarak tanımlanması ve bu kategorilere farklı renkler verilmesi , tedarikçilerinizin kabul durumunu kırmızı, sarı, yeşil gibi renklerle ifade edebilmesini sağlayan modüldür.

## **4.1.Sistem Altyapı Tanımları**

Tedarikçi Değerlendirme Modülünün altyapısını oluşturmak amacıyla gerekli tanımlamaların yapıldığı kısımdır. Yapılan tanımlamalara göre Entegre Yönetim Sistemi menüsünden girişlerde bu veriler kullanılmakta ve görülmektedir. Bu kısımda Değerlendirme Kategorileri, Tedarikçi Anket Şablonları ve Soru Listeleri Tanımlama menüleri bulunmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload442c73a0-6646-4842-8599-5931cb3d4eeb)



### **4.1.1.Tedarikçi Grupları**

**Menü Adı:** SAT/BSAT/Tanımlar/Tedarikçi Grupları

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload06906175-781b-4636-97a3-db46a12fed76)

Tedarikçi gruplarının tanımlandığı menüdür. Örnek verirsek kargo şirketleri, gıda şirketleri. Tedarikçi Değerlendirme Modülü’nde öncelikle tedarikçi gruplarının tanımlanması gerekir. Müşteri ve tedarikçilerimizi tanımlarken bu gruplarla ilişki kuruyoruz. Sonrasında bu grupların önemi tedarikçi anket şablonlarında ortaya çıkacaktır. Her bir grup için farklı sorular yöneltiyoruz. Kargo şirketleri için farklı, gıda şirketleri için farklı ve kırtasiye şirketleri için farklı sorular yöneltiyoruz. Dolayısıyla tek tek soru hazırlamıyor her bir tedarikçi için gruplandırarak bu işlem yapabiliyoruz.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddc0d3c64-6eb2-4d05-886d-e4432cfbb47e)

**Ekranda bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9af778e2-74e8-4897-a0d7-c3c3eb0b30db): Yeni bir tedarikçi grubu tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcbe09a16-c1fe-40ac-ad01-2c686a886a7b): Listede seçili tedarikçi grubu bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload02ef4fc2-ca4a-4ccc-b9aa-0a696c505d9e): Listede seçili tedarikçi grubu bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload05455568-dc58-47e0-9322-dbb9a95d7c99): Mevcut tedarikçi listesini Excel’e aktarır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload52248e0b-a045-4897-8b49-f7144baae605): Kayıtlar filtrelenerek arama yapılabilir.

Tedarikçi Grubu tanımlama ekranına yeni bir tedarikçi grubu eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf44ac841-b81d-4f6c-81b8-a0a3cc22568a) (yeni) butonu tıklanarak Tedarikçi Grubu Tanımlama/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload41817651-760d-40ba-b69a-0cb8a5dfcbf6)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Tanım:** Tedarikçi grubunun ismi girilir.

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload664a3a42-240b-4bba-b56f-7b6c29820438) (kaydet) butonu tıklanarak tedarikçi grubu tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload024dc09a-dad4-49c8-bfcf-b364280b63b1)

### **4.1.2.Müşteri- Tedarikçi Tanımlama**

**Menü Adı:** SAT/BSAT/Tanımlar/Müşteri- Tedarikçi Tanımlama

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddfb6b774-9b83-4281-b1d7-19bb56931f6e)

Sistem Altyapı Tanımlarında müşteri veya tedarikçilerin tanımlamasının yapıldığı menüdür. Tedarikçi Değerlendirme Modülü’nde müşteri-tedarikçi tanımlanmasında tedarikçi gruplarıyla ilişkilendirmek için “Tür” alanında sistemde tanımlı şirket türlerinden tedarikçi seçimi yapılır. Şirket türlerinden tedarikçi seçimi yapıldıktan sonra “Tedarikçi Grupları” adı altında bir alan açılır. Açılan alanda tedarikçi grubu seçimi yapılarak müşteri-tedarikçi tanımlamasında tedarikçi gruplarıyla ilişkilendirme yapılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadef51e418-b8c1-481d-9d89-e3837acdc77e)

**Ekranda bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9af778e2-74e8-4897-a0d7-c3c3eb0b30db): Yeni bir müşteri-tedarikçi tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcbe09a16-c1fe-40ac-ad01-2c686a886a7b): Listede seçili müşteri-tedarikçi bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload02ef4fc2-ca4a-4ccc-b9aa-0a696c505d9e): Listede seçili müşteri-tedarikçi bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload05455568-dc58-47e0-9322-dbb9a95d7c99): Mevcut müşteri-tedarikçi listesini Excel’e aktarır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload52248e0b-a045-4897-8b49-f7144baae605): Kayıtlar filtrelenerek arama yapılabilir.

Müşteri-Tedarikçi tanımlama ekranına yeni bir Müşteri-Tedarikçi eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf44ac841-b81d-4f6c-81b8-a0a3cc22568a) (yeni) butonu tıklanarak Müşteri-Tedarikçi Tanımlama/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload80e1fd9b-deed-4893-b188-6f019585c7ce)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Şirket Kodu:** Tanımlanan şirketin kod bilgisi girilir. Türkçe karakter ve boşluk kullanılmamalıdır. Örnek: “TDS”, ”001”, ”T03”

**Ad:** Tanımlanan şirketin ismi girilir.

**Tür:** Sistemde yer alan şirket türlerinden seçilir. Şirket türleri bireysel, kurumsal ve tedarikçi. (Şirket türlerinin isimlerini değiştirmek veya kullanılmayacak olanları Pasif hale getirmek için BSAT/Konfigürasyon Ayarları/Sabitler menüsüne gidilir. Detaylı bilgi için Sistem Altyapı Tanımları Kullanıcı Yardım Dokümanı incelenmelidir.)

**Tedarikçi Grubu:** Tanımlanan şirketin türünün Tedarikçi seçildiğinde ilişkili olarak açılır. Sistem Altyapı Tanımları/Tanımlar/Tedarikçi Grupları menüsünden tanımlanan tedarikçi grupları listelenir. Listelenen tedarikçi gruplarının seçilebildiği alandır.

**Durum:** Tanımlanan şirketin durum kısmının “Aktif” veya “Pasif” olarak seçilir. Tanımlanan Müşteri ya da Tedarikçi durumu “Aktif” seçilmelidir. Daha öncesinde kullanılmış ancak kullanılmayacak olan müşteri ya da tedarikçiler için silme işlemi yapılmamalıdır, ilgili kaydı kaydı güncelleyip durumu “Pasif” seçilmelidir.

**İş Yeri Kodu:** Tanımlanan şirketin iş yeri kodu girilir. Türkçe karakter ve boşluk kullanılmamalıdır. Örnek: “TDS”, ”001”, ”T03”

**Adres:** Tanımlanan şirketin bulunduğu adres bilgisinin girilir.

**Şehir:** Tanımlanan şirketin bulunduğu şehrin bilgisi girilir.

**Ülke:** Tanımlanan şirketin bulunduğu ülke bilgisinin girilir.

**Telefon:** Tanımlanan şirketin telefon numarası girilir.

**Cep Telefonu:** Tanımlanan şirketin cep telefon numarası girilir.

**Fax:** Tanımlanan şirketin faks numarası bilgisi girilir.

**Sorumlu:** Tanımlanan şirket sorumlusunun isim ve soy isimi girilir.

**E-Posta:** Tanımlanan şirketin E-posta bilgisi girilir.

**Dil:** Tanımlanan şirketin dili sistemde tanımlı dil seçeneklerinden seçilir.

**Açıklama:** Tanımlanan şirket ile ilgili detay bilgisi girilir.

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload664a3a42-240b-4bba-b56f-7b6c29820438) (kaydet) butonu tıklanarak müşteri-tedarikçi tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0c9666f0-2f5e-4488-803a-bbe1253ad647)

### **4.1.3.Değerlendirme Kategorileri**

**Menü Adı:** Sistem Altyapı Tanımları/Tedarikçi Değerlendirme/Değerlendirme Kategorileri

Tedarikçilerin değerlendirmesinin yapıldığı menüdür. Değerlendirme aşamasında bir sınıflama yapılması zorunluluğu vardır. Firmalara bağlı olarak 3’lü ya da 5’li skalalık değerlendirme kategorileri yapısı tanımlanır. “Çok iyi”, “İyi”, “Orta”, “Kötü” ve “Çok kötü” şeklinde 5’li skalalık değerlendirme kategori yapısı örneği verilebilir. Değerlendirme Kategorilerinde “Kabul edilebilir mi?”, “Şartlı kabul edilebilir mi?” ya da “Kabul edilemez” 3’lü skalalık bir değerlendirme kategori yapısı da tanımlanabilir. Genelde kullanılan 3’lü skalalık değerlendirme kategori yapısıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload96cfc77a-68ad-4a4f-8159-e2a9e4f6b358)

**Ekranda bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9af778e2-74e8-4897-a0d7-c3c3eb0b30db): Yeni bir değerlendirme kategorisi tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcbe09a16-c1fe-40ac-ad01-2c686a886a7b): Listede seçili değerlendirme kategorileri bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload02ef4fc2-ca4a-4ccc-b9aa-0a696c505d9e): Listede seçili değerlendirme kategorileri bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload05455568-dc58-47e0-9322-dbb9a95d7c99): Mevcut değerlendirme kategorileri listesini Excel’e aktarır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload52248e0b-a045-4897-8b49-f7144baae605): Kayıtlar filtrelenerek arama yapılabilir.

Değerlendirme kategorileri tanımlama ekranına yeni bir değerlendirme kategorisi eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf44ac841-b81d-4f6c-81b8-a0a3cc22568a) (Yeni) butonu tıklanarak Değerlendirme Kategorileri Tanımlama/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload87616664-cf92-4c1d-b255-73388bf5f951)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Renk:** Puanı, değerlendirme kategorisi ile ilişkilendirip alacağı rengi seçilebilir. Değerlendirme neticesinde ilgili tanım ilişkili renk ile gösterilir. Örnek, “Kabul edilemez“ için kırmızı, “Kabul edilebilir” için sarı.

**Tanım:** Tanımlanan değerlendirme kategorisinin adı girilir.

**Alt Limit:** Değerlendirme kategorisi için belirlenen puan aralığına (10 veya 100’lük skalaya göre) alt limit için verilen değer girilir.

**Alt Limit Aralık İçinde:** Değerlendirme kategorisi için belirlenen puan aralığına alt limit için verilen değer dahil edilmek isteniyorsa ilgili check box işaretlenmelidir.

**Üst Limit:** Puanın (10 veya 100 lük skalaya göre) üst limit bilgisi girilir.

**Üst Limit Aralık içinde:** Puanın üst limit aralık içinde ise ilgili işaret check box işaretlenmelidir.

**Kabul Edilebilir mi?:** “Kabul edilebilir mi?” sorusunun ilgili seçeneklerden seçilir. tedarikçinin teğerlendirme kategorisi sonucunda kabul edilebilirliğini belirler.

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload664a3a42-240b-4bba-b56f-7b6c29820438) (kaydet) butonu tıklanarak değerlendirme kategorisi tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload0770d1b5-5b69-4d06-a872-b8075bc15b46)

### **4.1.4.Soru Listesi Tanımlama**

**Menü Adı:** Sistem Altyapı Tanımları/Tedarikçi Değerlendirme / Soru Listesi Tanımlama

Tedarikçi Değerlendirme Modülü’nde soru listelerinin oluşturulduğu ve ilgili soru listelerine ait soruların tanımlandığı menüdür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload81e5202c-41bb-4c36-9084-82e450b2597a)

**Ekranda bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9af778e2-74e8-4897-a0d7-c3c3eb0b30db): Yeni bir soru listesi tanımlanır.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcbe09a16-c1fe-40ac-ad01-2c686a886a7b): Seçili soru listesi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload02ef4fc2-ca4a-4ccc-b9aa-0a696c505d9e): Seçili soru listesi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd5b9c76c-7033-4876-96b4-ea4220cdbc8f): Seçili soru listesine ait sorular oluşturulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload67b8a82d-545e-4f0e-b7e8-8abe7a588e5a): Seçili soru kopyalanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload05455568-dc58-47e0-9322-dbb9a95d7c99): Mevcut soru listesini Excel’e aktarır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload52248e0b-a045-4897-8b49-f7144baae605): Kayıtlar filtrelenerek arama yapılabilir.

Yeni bir soru listesi eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf44ac841-b81d-4f6c-81b8-a0a3cc22568a) (yeni) butonu tıklanarak Soru Listesi Tanımlama/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd04a02a8-ae4b-472b-88a1-6636bd84ed83)

**Soru Listesi Tanımı:** Soru listesinin adı girilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5e56ab7f-477e-4283-a555-58df1e62772e)

Gerekli alan doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload664a3a42-240b-4bba-b56f-7b6c29820438) (kaydet) butonu tıklanarak soru listesi tanımlama işlemi gerçekleştirilir.

Soru listesi tanımlama işleminden sonra soru listesi seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd5b9c76c-7033-4876-96b4-ea4220cdbc8f) (sorular) butonu tıklanarak anket soruları oluşturulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade73bbf31-a98d-46a4-9621-9c69479877a4)

**Ekranda bulunan butonlar yardımıyla;**

**![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload61794319-1e32-4567-8aef-1a14ab7211bf): Geri Butonu:** Bir önceki sayfaya geçişi sağlar.

**![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb398365c-31b1-4c6d-9df0-f687bcf87957): Yazdır Butonu:** Soruları yazdırmayı sağlar.

**![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb489f28f-878c-4d6e-9cab-d2b360ef0def): Başlık Ekle Butonu:** Anketi bölümlendirerek başlık eklemek istenilirse bu buton kullanılır. Her başlıktan sonraki sorunun numarası 1 olarak gelir. Butona tıklandığında açılan sayfa aşağıdaki gibidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6de8fe6a-6e0c-4235-8c86-a012e7987240)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddce92a70-aca3-4086-bd0d-a8a58a74974b) : **Bilgi Girişi Ekle Butonu:** Anketi dolduran kişilere, metin tipli yanıt alanı sağlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1d07a6e7-df90-4092-8552-5b941ff469d9)

**Soru Metni:** Sorulacak soru metni, Türkçe alana yazılır. Diğer dillerde kullanım olması durumunda ilgili dillerin olduğu alana sorulacak soru girilir.

**Satır Sayısı:** Satır sayısı, metnin uzunluğunu belirlemek için kullanılır. 0 veya 1 olması durumunda cevap verilecek alan tek satır olarak görülür.

Sorunun cevap verme zorunluluğu bu alandan belirlenir. Cevap zorunluluğu var ise soru cevaplanmadığında kaydetmeye izin verilmez, uyarı mesajı verir.

**İlişkili Soru/Seçenek:** Tanımlanan soru, soru listesinde yer alan başka bir soru seçeneği ile ilişkiliyse bu alanda seçilir. Bu sayede seçeneğe bağlı tanımlanan sorunun görüntülenmesi sağlanır.

**![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfe72cce0-348e-4b82-a1d8-7c8883dcb7c4): Seçenek Ekle Butonu:** Seçenekli soru tipi eklenmesini sağlar. Seçenekler çoklu seçmeli veya puanlı da yapılabilir. Puanlı seçenekler için de hesaplama yöntemi belirlenmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8737882c-bc6e-4c09-b1d8-cc438e6cb75c)![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploaddbe6cd0a-dd5c-4a24-8aac-c73b45cfcaf1)

**Soru Metni:** Sorulacak soru metni, Türkçe alana yazılır. Diğer dillerde kullanım olması durumunda ilgili dillerin olduğu alana sorulacak soru girilir.

**Seçenekler:** Tanımlanan soruya ait seçenekler girilir.

**Seçenek-Puan:** Eğer puanlı seçenekli bir soru ise tanımlanan seçeneklere ait değerler girilir. Sorunun cevap verme zorunluluğu bu alandan belirlenir. Cevap zorunluluğu var ise soru cevaplanmadığında kaydetmeye izin verilmez, uyarı mesajı verir. Soruya ait seçenekler için tekli veya çoklu seçim yöntemi belirlenir. Soruya ait seçeneklerin tek satırda veya alt alta listelenmesi için seçeneklerden tek satırlı veya çok satırlı seçilir.

**Hesaplama Yöntemi:** Puanlı seçenekli tanımlanan sorular için birden fazla seçilebilir olan durumlarda hesaplama yöntemi seçilmelidir.

**Ağırlıklı Puan:** Öncelikle tanımlanan sorunun puanlı olması gerekir. Sorular arasında ağırlık farkı var ise sayısal değer yazılır. Sistem yazılan değer ile seçeneğin puanını çarparak sorunun puanını oluşturur.

**İlişkili Soru/Seçenek:** Tanımlanan soru, soru listesinde yer alan başka bir soru seçeneği ile ilişkili ise bu alanda seçilir. Bu sayede seçeneğe bağlı tanımlanan sorunun görüntülenmesi sağlanır.

**![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload898a0863-d10d-477d-b618-09b9abdb6b94): Sıralama Ekle Butonu:** Sıralama yapılması istenen seçenekler için kullanılan soru tipidir. Kişiler soruya ait seçenekleri tercihe göre sıralamasını yapar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload487f99cb-b6d4-4021-9716-ca9f9115fc42)![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf0c1a23e-ccc2-4f3e-9241-de72cf25bee6)

**Soru Metni:** Sorulacak soru metni, Türkçe alana yazılır. Diğer dillerde kullanım olması durumunda ilgili dillerin olduğu alana sorulacak soru girilir.

**Seçenekler:** Tanımlanan soruya ait seçenekler girilir.

**İlişkili Soru/Seçenek:** Tanımlanan soru, soru listesinde yer alan başka bir soru seçeneği ile ilişkili ise bu alanda seçilir. Bu sayede seçeneğe bağlı tanımlanan sorunun görüntülenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7288730a-5c1b-44b1-ab40-3c002cdb26a6): **Çoklu Seçim Listesi Ekle Butonu:** Oluşturmak istenilen soruda çok fazla seçenek mevcut ise ve bunların işaret listesi gibi seçilmesi gerekiyor ise, çoklu seçim listesi tipinde soru eklenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload451c7e5b-ae14-466b-b709-84ab719917e5)![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload61245573-76e6-483e-80d4-ee86e21bfbb6)

**Soru Metni:** Sorulacak soru metni, Türkçe alana yazılır. Diğer dillerde kullanım olması durumunda ilgili dillerin olduğu alana sorulacak soru girilir.

**Seçenekler:** Tanımlanan soruya ait seçenekler girilir.

**Seçenek-Puan:** Eğer puanlı seçenekli bir soru ise tanımlanan seçeneklere ait değerler girilir. Sorunun cevap verme zorunluluğu bu alandan belirlenir. Cevap zorunluluğu var ise soru cevaplanmadığında kaydetmeye izin verilmez, uyarı mesajı verir.

**Min/Max Seçim** Sayısı: Soruya ait seçeneklerden en az ve en çok seçilmesi istenen seçenek adedi sayısal yazılır. Örnek min alanına 2 girilirse kişiler en az iki seçenek seçmesi gerekir.

**Hesaplama Yöntemi:** Puanlı seçenekli tanımlanan sorular için birden fazla seçilebilir olan durumlarda hesaplama yöntemi seçilmelidir.

**Ağırlıklı Puan:** Öncelikle tanımlanan sorunun puanlı olması gerekir. Sorular arasında ağırlık farkı var ise sayısal değer yazılır. Sistem yazılan değer ile seçeneğin puanını çarparak sorunun puanını oluşturur.

**İlişkili Soru/Seçenek:** Tanımlanan soru, soru listesinde yer alan başka bir soru seçeneği ile ilişkili ise bu alanda seçilir. Bu sayede seçeneğe bağlı tanımlanan sorunun görüntülenmesi sağlanır.

**![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload7cdfbf20-84fe-4fe4-a730-d8cb3a9820db): Açılır Liste Ekle Butonu:** Seçenekli sorular için kullanılan soru tipidir. Soruya ait seçeneklerin listeden seçilebilmesini sağlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb473f1bd-c384-4108-92f7-9d5ec2e25e6e)![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload61245573-76e6-483e-80d4-ee86e21bfbb6)

**Soru Metni:** Sorulacak soru metni, Türkçe alana yazılır. Diğer dillerde kullanım olması durumunda ilgili dillerin olduğu alana sorulacak soru girilir.

**Seçenekler:** Tanımlanan soruya ait seçenekler girilir.

**Seçenek-Puan:** Eğer puanlı seçenekli bir soru ise tanımlanan seçeneklere ait değerler girilir. Sorunun cevap verme zorunluluğu bu alandan belirlenir. Cevap zorunluluğu var ise soru cevaplanmadığında kaydetmeye izin verilmez, uyarı mesajı verir.

**Min/Max Seçim** Sayısı: Soruya ait seçeneklerden en az ve en çok seçilmesi istenen seçenek adedi sayısal yazılır. Örnek min alanına 2 girilirse kişiler en az iki seçenek seçmesi gerekir.

**Hesaplama Yöntemi:** Puanlı seçenekli tanımlanan sorular için birden fazla seçilebilir olan durumlarda hesaplama yöntemi seçilmelidir.

**Ağırlıklı Puan:** Öncelikle tanımlanan sorunun puanlı olması gerekir. Sorular arasında ağırlık farkı var ise sayısal değer yazılır. Sistem yazılan değer ile seçeneğin puanını çarparak sorunun puanını oluşturur.

**İlişkili Soru/Seçenek:** Tanımlanan soru, soru listesinde yer alan başka bir soru seçeneği ile ilişkili ise bu alanda seçilir. Bu sayede seçeneğe bağlı tanımlanan sorunun görüntülenmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadeaac8631-e097-4ded-bac5-18d4d8241957)**: Ön Tanımlı Seçim Ekle Butonu:** Departman, müşteri, personel veya ürün seçimi için kullanılan soru tipidir. Seçim tipine göre sistem seçenekli soru oluşturmaktadır. Örnek departman seçili soru tanımlaması yapıldğında seçenek olarak departman listesi görüntülenmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload1b64a324-24e8-412d-81cc-9e0d0bcef2a6)

**Soru Metni:** Sorulacak soru metni, Türkçe alana yazılır. Diğer dillerde kullanım olması durumunda ilgili dillerin olduğu alana sorulacak soru girilir. Cevap zorunluluğu var ise soru cevaplanmadığında kaydetmeye izin verilmez, uyarı mesajı verir.

**İlişkili Soru/Seçenek:** Tanımlanan soru, soru listesinde yer alan başka bir soru seçeneği ile ilişkili ise bu alanda seçilir. Bu sayede seçeneğe bağlı tanımlanan sorunun görüntülenmesi sağlanır.

**Seçim Tipi**: Tanımlanan sorunun tipi belirlenir. Listeden departman, personel, müşteri veya ürün seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload30618e5a-bbd9-4f72-8393-a39e879b8018)**: Tarih Ekle Butonu:** Tarih tipli soru tanımlaması için kullanılır. Tanımlanan alanda kişiler takvimden istenilen tarihi seçer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb8a7c807-7b65-4743-9197-11800a3f8752)

**Soru Metni:** Sorulacak soru metni, Türkçe alana yazılır. Diğer dillerde kullanım olması durumunda ilgili dillerin olduğu alana sorulacak soru girilir. Cevap zorunluluğu var ise soru cevaplanmadığında kaydetmeye izin verilmez, uyarı mesajı verir.

**İlişkili Soru/Seçenek:** Tanımlanan soru, soru listesinde yer alan başka bir soru seçeneği ile ilişkili ise bu alanda seçilir. Bu sayede seçeneğe bağlı tanımlanan sorunun görüntülenmesi sağlanır.

Soru tanımlamaları yapılarak anket oluşturulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadea729ed8-7b73-4f27-8e3c-3444dd186e65)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade05f51db-c2e9-4bca-b10a-d0c88aec4e68)

### **4.1.5.Tedarikçi Anket Şablonları**

**Menü Adı:** Sistem Altyapı Tanımları/ Tedarikçi Değerlendirme /Tedarikçi Anket Şablonları

Tedarikçi anket şablonlarının tanımlandığı menüdür. Açılan sayfada tanımlanan tedarikçi grupları listelenir. Tedarikçi değerlendirmesi, ilgili tedarikçi grubu için oluşturulan anket şablonu üzerinden yapılmaktadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb412e85a-6dd0-47b4-aeee-61cefd666e49)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload450f37f9-edb1-4b85-b2e3-87bcabbf9e0a): Listede seçili tedarikçi grubu için anket şablonu oluşturulur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload52248e0b-a045-4897-8b49-f7144baae605): Kayıtlar filtrelenerek arama yapılabilir.

Açılan ekranda listelen tedarikçi grubu seçilerek ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload450f37f9-edb1-4b85-b2e3-87bcabbf9e0a) (Anket şablonu oluştur) butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload238c9e60-adac-461a-9e1a-ab62d9d309aa)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Periyodik mi:** Anket şablonu periyodik değil ise “Hayır” seçilir, belirli periyotlarla tekrarlanması istenirse “Evet” seçilmelidir.

**Süre (Ay):** Periyodik olarak yapılması istenen anketler için ay bazında süre girilir. Örnek 3 gibi. Bu sayede sistem 3 ay aralıkla anketi tekrar açar.

**Ön Bildirim Süresi(Gün):** Anket şablonun doldurulması için kaç gün önceden bilgilendirme yapılacak bilgisi girilir.

**Başlangıç Tarihi:** Anket şablonu periyodikse periyodik başlangıç tarihi bilgisi girilir.

**Yetkili Kullanıcı Grupları:** Anket şablonu üzerinde yeni anket oluşturma veya düzenleme yetkisi olan kullanıcı grupları seçilir.

**Açıklama:** Seçilen şablon hakkında eğer varsa açıklama girilir.

**Ekranda bulunan butonlar yardımıyla;**

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload9af778e2-74e8-4897-a0d7-c3c3eb0b30db): Yeni bir onaycı eklenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcbe09a16-c1fe-40ac-ad01-2c686a886a7b): Listede seçili onaycı bilgisi güncellenir.

![Untitled1](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload02ef4fc2-ca4a-4ccc-b9aa-0a696c505d9e): Listede seçili onaycı bilgisi silinir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload664a3a42-240b-4bba-b56f-7b6c29820438): Anket şablonu kayıt işlemi gerçekleştirilir.

Tedarikçi anket şablonları menüsünde tedarikçi grupları listelenir. Örneğin kargo şirketleri listeden seçilir. Anket şablonu oluştur butonu tıklanır. Anket şablonu periyodik ise “Evet” periyodik değil ise “Hayır” seçilir. Periyodiklikte “Evet” seçilirse bir aralık belirlenerek buna bağlı olarak bir başlangıç tarihi seçilir. Belirlenen başlangıç tarihinde ilk periyodik anket açılır. Sonrasında da diğer anketleri de sistem otomatik açmaya başlar. Ay bazında açılır. Yetkili kullanıcı grupları alanında yeni bir anket oluşturacağı zaman yetkili olan kişiler oluşturabilirler. Yeni bir anketin oluşturulması görevini yapacak kullanıcı grupları listesinden seçilir. Anketin üzerinde açıklama bilgisi alanında ise detay bilgilendirilmesi yapılır.

Yeni bir onaycı eklemek için ekranın sağ üst köşesindeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf44ac841-b81d-4f6c-81b8-a0a3cc22568a) (Onaycı ekle) butonu tıklanarak Anket Bölümleri Tanımlama/Yeni Kayıt ekranı görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaee1cb10-020e-4998-8606-c9dfe8b0039a)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Soru Listesi:** SAT/Tedarikçi Değerlendirme/Soru Listesi Tanımlama menüsünde oluşturulan soru listelerinden seçim yapılır.

**Onaycı Tipi:** Sistemde tanımlı onaycı tipi listesinden seçilebilir. Personel, pozisyon ve rol seçimi yapılabilir.

**Onaycı:** Onaycı tipi seçimine göre (rol, personel, pozisyon) onaycı listesinden seçilir.

**Seviye:** Onay sıralaması için tanımlanan onaycıların seviyesi yazılır.

**Ağırlık:** Anketin ağırlık oranı belirlenir.

**Doldurma Sonrası Bilgilenecekler:** Doldurma sonrası bilgilenecekler onaycı tanımları listesinden seçilir.

**Onaycı Mesaj Gövdesi:** Sistemde tanımlı onaycı mesaj gövdesi listesinden seçilir.

**Bilgilendirme Mesaj Gövdesi:** Sistemde tanımlı bilgilendirme mesaj gövdesi listesinden seçilir.

**Doldurma Süresi:** Anketin doldurma süresi belirlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadea4240ae-b556-4edf-bc80-6cb8179b8046)

Yeni butonu tıklanarak anket bölümleri tanımlama ekranı görüntülenir. Soru listesi alanında sistemde tanımlanan soru listesi seçilir. Onaycı tipi seçerek personel tipi, rol tipi veya pozisyon tipi kişilere pozisyonlara, rollere, personellere anket görevi düşer. Örneğin “Benim Kargo şirketim şu şekilde değerlendiriliyor. Birinci seviyede onaycıdaki kişiye gidiyor ve ağırlığı %60 ortalama alıyoruz”. Ankette de kendi içinde bir ağırlık var. Anket bölümleri tanımlama ekranında onaya gidecek kişilerde ağırlıklı ortalama yöntemi var. Doldurulduktan sonra bu anketten kimlerin bilgilenecekleri seçilir. Doldurma sonrası bilgilenecekler varsa seçilir. Onaya gönderildikten sonra onaycıya hangi mail gideceği sistemde tanımlı mesaj gövdesi listesinden seçilir. Aynı şekilde bilgilenecekler varsa onlar için de mesaj gövdesi seçilmelidir. (Bunun için sistemde iki ayrı mesaj gövdesi tanımlı olması gerekir. Eğer yok ise veya olan mesaj içeriğinin değiştirilmesi istenirse SAT/BSAT/Tanımlar/Mesaj Gövdesi Tanımlama menüsüne gidilir ve filtreden Tedarikçi Değerlendirme Modülü seçilir.) Sayfanın en altında yer alan doldurma süresi alanında anketin doldurma süresi belirlenir. Gecikme mailleri de anketin doldurma süresine göre belirlenir. (1 nolu parametre değeri “Evet” seçilirse gecikme mailleri gönderilir. Gecikme mailleri gönderilmemesi istenilen amirler için 8 nolu parametre, kullanıcı grupları için 14 nolu parametre veya unvanlar için 15 nolu parametre doldurulmalıdır. Parametre değerlerinde gerekli açıklamalar yer almaktadır.)

Gerekli alanlar doldurulduktan sonra sağ üst köşedeki ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload664a3a42-240b-4bba-b56f-7b6c29820438) (Kaydet) butonu tıklanarak anket bölümleri tanımlama kayıt işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2775c780-5737-4133-ba3d-7efcc02afe77)

Onay için belirlenen veya e-posta ile bilgilendirilecek kişiler için rol tanımlaması yapılır. Tanımlanmak istenen yeni/farklı bir rol olursa BSAT/SAT /Konfigürasyon Ayarları/Rol Tanımlama menüsünden Bimser Destek/Danışmanlık ekibi tarafından yapılır.

## **4.2.Entegre Yönetim Sistemi**

Tedarikçi Değerlendirme Modülü kapsamında Tedarikçi Anketleri tanımlanıp ve Grafiklerin görüntülendiği kısımdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadadec95e1-500b-4498-aeb6-9ab338ba6acc)

### **4.2.1.Tedarikçi Anketleri**

**Menü Adı:** Entegre Yönetim Sistemi/Tedarikçi Değerlendirme/Tedarikçi Anketleri

Tedarikçi anketleri sayfasında tedarikçiler tedarikçi grupları ile ilişkilendirilmiş şekilde listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload188bd17f-5517-4049-81c0-54da0055e729)

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload911119ee-8642-4e58-9cd7-338dfb57f53f): Tedarikçi anketi yayınlanarak akıştaki kişilere doldurulması için gönderilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload61a5ac1b-52d0-485c-88f2-0fae27b7e03d): Değerlendirme kategorisi tanımla sayfasında kabul edilemez olarak tanımlanan kriterdeki anketler için kullanılır. Kabul edilemez anketleri onaya göndermek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf59d5735-999d-470a-84d5-b31429822eff): Görüntüle butonu ile tedarikçi anketleri görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload369fcadd-28c0-40ef-a3ca-47e4dde67d95):Tedarikçi anketi onay tarihçesi bilgisi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaba16902-3e1e-4688-9c09-0fa86b33b904): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbd18721c-f88f-4b6d-a9cf-b75cbcbdd613)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload911119ee-8642-4e58-9cd7-338dfb57f53f)(Yeni) butonu tıklanarak anket yayınlanarak akıştaki kişiye doldurulması için gönderilir. (Tekrar ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload911119ee-8642-4e58-9cd7-338dfb57f53f) yeni butonuna tıklandığında “Yayında olan anket bulunduğu için tekrar üretmezsiniz” şeklinde bilgilendirme mesajı ile karşılaşılır.)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadf9a584ed-f1c9-499d-b8ff-d3857bdec328)

Yayınlanan anket ilgili kişinin bekleyen işlerimde “Doldurulması Gereken Tedarikçi Anketleri” olarak iş düşer. İlgili tedarikçi kodu tıklanarak anket doldurma işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd2efc83c-d535-45b8-8f9b-49957ebbc6ec)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb10be4ec-cfa5-4381-b6a7-df63cbd8fd22)

**Ekrandaki bulunan butonlar yardımıyla;**

![http://qdmsv522.bimser.local/Common/Images/font-size-increase.png](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload54660998-d72b-4513-9429-5a08c0582926): Anketin yazı karakterlerini büyütmek veya küçültmek için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcede267a-631e-466f-8d51-5c4480e175bd): Yazdırma işlemi için yazdır butonu kullanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload532694c1-ddfa-4538-961e-4598e7eb6b3f): Yapılan cevapların kaydedilmesi ve daha sonra ankete devam edilmesi için taslak olarak kaydet butonu kullanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb39842d5-fc62-46fa-8962-4f3bd5a9868d): Soruları cevaplamadan çıkmak istenilirse geri butonu kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload513757ab-8b8e-48c4-ab76-647007d2fb7a): Sorular cevaplama işleminden sonra gönderilmesi için kullanılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaae2a038-dab9-4c7e-8ef7-623681c14ed2)

Akıştaki kişi tedarikçi anketini doldurur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadca99db34-7afe-41bc-b90e-0c826b7dfd2d)

Akıştaki kişi ilgili tedarikçi kodu tıklanarak anket doldurma işlemi gerçekleştirilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade3bb8bcb-35bf-4631-9cf5-5a4668cd1995)

Doldurulduktan sonra anket ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload23a32876-2038-4041-95a8-8ff28f943f9d) (kaydet) botunu tıklanarak kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload5a7366a0-d953-4596-8a9b-01077ffe4524)

Entegre Yönetim Sistemleri/Tedarikçi Değerlendirme/Tedarikçi Anketleri menüsü tıklanır.

Anketin kabul durumu gridde hayır olarak görünür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload90d9b9e2-0c3d-4d16-820a-21b2b09d8753)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb4d78d55-c792-40a6-91e2-0f27462aab7a)(Görüntüle) butonu ile tedarikçi anket listeleri görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc2a43de7-f083-46b6-a43a-5b7b3d6e0b69)

Tedarikçi anket listesinde seçili tedarikçi anket üzerinde ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb4d78d55-c792-40a6-91e2-0f27462aab7a) (görüntüle) butonu tıklanarak anketlerin içeriğini ayrıntılı bir şekilde görüntülenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd8b420dd-c863-4dc2-ab58-954d66933b97)

Tedarikçi Anketin durumun “Onaylı kabul” olması için Kabul edilebilir onayı başlat diye bir onay akışı başlatılır. Üst seviyedeki yönetici pozisyonundaki kişileri görev düşer. O kişi ankete göre kabul edilemiyor ama anketi onaylıyor musunuz diye onaylı kabul şeklinde kabul durumu başlatmak için ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload99bd6e83-9af0-4baf-9ed5-7bac95500033)(Kabul edilebilirlik onayı başlat) butonu tıklanır

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfea4b1d7-5ede-4f40-b25e-d9cb3c6cdaad)

İlgili kişinin bekleyen işlerimde “Kabul Edilebilirlik Onayı” olarak iş düşer.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload740f444f-ce5d-455d-8aa3-d251f8cbec26)

İlgili tedarikçi kodu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadbe958501-0835-4136-9df8-c75e16070d13)

**Ekrandaki bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcd25094d-1bfd-44ec-af2e-7579614508d7): Tedarikçi anketleri görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload369fcadd-28c0-40ef-a3ca-47e4dde67d95):Onay Tarihçesi bilgisi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaba16902-3e1e-4688-9c09-0fa86b33b904): Veriler Excel’ e aktarılabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade230f5ca-1c66-458f-94dd-25ee0d377f71): Tedarikçi anketi reddedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc00ecb50-fe3f-41b2-8021-867774bbf8e9): Tedarikçi anketi onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadcd25094d-1bfd-44ec-af2e-7579614508d7)(Görüntüle ) butonu tıklanarak Tedarikçi Anket Listeleri görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade327fa21-c74c-41ce-bef6-8ba93e6f522a)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc00ecb50-fe3f-41b2-8021-867774bbf8e9)(Onayla) butonu tıklanarak Onay notu bilgisi yazılarak Tedarikçi anketin Kabul edilebilir onayı onaylanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc68c5439-8c9a-467a-ae5e-01ed0d4a5860)

Sistem tarafından “Seçili Kabul edilebilir hale getirilmiştir” uyarı mesajı verilir

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploada2e229a4-2032-4824-9975-b26008f26c98)

Sistemde Tedarikçi Anketin listesinde Tedarikçi Anketin kabul durumu “Onaylı Kabul” olarak görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload2dee55e7-f3d4-48a6-9f44-9e4d90bea130)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload369fcadd-28c0-40ef-a3ca-47e4dde67d95)(Onay Tarihçesi Göster) butonu tıklanarak Tedarikçi Anketin Onay Tarihçe bilgisi görüntülenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload935861f0-9af7-419c-b3df-2f4d0b4d2378)

### **4.2.2.Grafikler**

**Menü Adı**: Entegre Yönetim Sistemi /Tedarikçi Değerlendirme /Grafikler

Tedarikçi Değerlendirme Modülü ile ilgili grafiklerin görüntülendiği kısımdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8036a30f-5a3d-4d12-9a50-b5193e108d28)

#### **4.2.2.1.En Çoklar Analizi**

**Menü Adı**: Entegre Yönetim Sistemi / Tedarikçi Değerlendirme /Grafikler/En Çoklar Analizi

En çoklar analizi grafiğini almak için, grafikler menüsünden en çoklar analizi menüsü tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload91565610-f3ac-4663-8626-8efc80f1e353) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload34f44980-1e44-41c2-a8c0-901e95b8623d)

**Açılan ekranda ilgili alanlar tanımlanır:**

**Grafik Adı**: “En Çoklar Analizi” olarak dolu gelir. İsteğe göre silinip grafiğe yeni isim verilebilir.

**En Çok:** X ekseninde seçilen kritere göre grafikte gösterilmesi istenen en çok değer (sayısal) girilir. 5 değeri otomatik tanımlı gelir. Bu sayede x ekseninde seçilen kritere göre en çok beş değerin görüntülenmesini sağlar.

**X Ekseni:** Oluşturulması istenen grafiğin kriteri seçilir. Listede yer alan kabul durumu, değerlendirme kategorisi, minimum puan veya maksimum puana göre oluşturulur.

**Ana Tema:** Otomatik tanımlı gelir. Listeden istenilen tema seçilerek grafik oluşturulabilir.

**Renk Paleti:** Otomatik tanımlı gelir. Listeden istenilen renk seçilerek grafik oluşturulabilir.

**Grafik Başlığı:** Grafik adı ve x ekseninde seçilen kritere göre grafik başlığı otomatik oluşur. İstenirse üzerinde değişiklik yapılabilir.

**Grafik Eni:** Standart eni 800 olarak tanımlıdır. İsteğe göre değiştirilebilir.

**Grafik Boyutu:** Standart boyutu 600 olarak tanımlıdır. İsteğe göre değiştirilebilir.

**Grafik Tipi:** “PieChart” veya “Bar” şeklinde iki türlü grafik oluşturulabilir. Bar seçeneği kolon şeklinde listeler, piechart seçeneği ise pasta şeklinde grafiği oluşturur.

**Tedarikçi:** Listeden tedarikçi seçimi yapılarak tedarikçiye göre grafik oluşturulmasını sağlar.

**Tedarikçi Grubu:** Listeden tedarikçi grubu seçimi yapılarak tedarikçi grubuna göre grafik oluşturulmasını sağlar.

**Ekranda bulunan butonlar yardımıyla;**

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload34e65b13-9258-4796-8eff-40d5ede1a5a5): Belirlenen özelliklere göre ekrana grafiği çizdirir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload8bbcbca7-ea42-497f-843d-a4ce00c42e65) : İstenen grafiği seçilen format türüne (excel, jpg, pdf, vb.) dönüştürerek dış ortama aktarır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload38a6a37a-7d7e-4233-96f6-e31bddb549d5): Grafik verileri, Excel listesi biçiminde aktarılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload34e65b13-9258-4796-8eff-40d5ede1a5a5)(Grafik Çiz) butonu tıklanarak belirlenen alanlara göre En Çoklar Analizi Grafiği alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploade28a9cfd-1dac-4187-9321-6af260ae381d) ![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload977bab1e-34f7-4da8-9b9c-727e04e8a3bb)
