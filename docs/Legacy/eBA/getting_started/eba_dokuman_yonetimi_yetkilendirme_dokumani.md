# eBA Doküman Yönetimi:Yetkilendirme  Dokümanı

## GİRİŞ

eBA Doküman Yönetimi:Yetkilendirme dokümanında; eBA Doküman Yönetiminde kütüphane, dizin ve 
dokümanlar için kullanıcı, departman,pozisyon, unvan, grup rolleri ve bu rollere bağlı yetkilendirme 
işlemlerinin nasıl yapıldığı anlatılmaktadır.

## 1.eBA Doküman Yönetiminde Yetkilendirme İşlemleri

eBA Doküman Yönetiminde Güvenlik penceresi ile ilgili kütüphane, dizin ve dokümanlar üzerinde hangi 
kulanıcıların hangi yetkilere sahip olacağı belirlenebilir. Bunun için rol tanımlaması yapıldıktan sonra bu role 
ait görüntüleme, indirme, yazdırma, değiştirme ve silme yetkilerinden hangilerine izin verileceği belirlenir.

### 1.1 Kullanıcı ve Rolleri Belirleme


Yetkilendirme işlemi için öncelikle kullanıcı ve roller belirlenir. Dokümanda sahip rolü, kullanıcı rolü ve 
departman rolü tanımlama işleminin nasıl yapıldığı anlatılmıştır. Diğer roller için de aynı işlemleri 
uygulayabilirsiniz.
İlgili kütüphane, dizin ve ya doküman seçildikten sonra Şekil 1’de, 2 numaralı alanındaki Güvenlik tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/1-7dcf9012-32a1-49c6-b93c-e0527675eeb7.png)

### 1.1.1 Sahip Rolü Belirleme

Güvenlik penceresinde rol ve yetkiler tanımlanacaktır. Seçili veri tabanının sahibi kullanıcıyı belirlemek için 
Şekil 2’de, Sahip Rolü kategorisi yanındaki Düzenleme ikonuna tıklanır.
Tür alanından kullanıcı, pozisyon,unvan,depertman veya grup rollerinden seçim yapıldıktan sonra ID
alanında seçilen türe ait ID seçimi yapılır. 3 numaralı alandaki butona tıklanarak açılan pencerede seçim 
yapıldıktan sonra Kaydet butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/2-fdc58430-721e-4499-80e2-762ca7ca0c34.png)

Şekil 3’de, açılan pencerede listelenen kullanıcılardan seçim yapılır. İşlemi tamamlamak için Kaydet butonu 
tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3-cc5269c8-1956-400a-b5e3-71e9ff2269b3.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/4-b68ade22-9d6e-4688-8ca1-41e9b5ca82cc.png)

### 1.1.2 Kullanıcı Rolü Belirleme

Kullanıcı bazlı rol tanımlamak için Kullanıcı Rolü kategorisi altına kullanıcı eklenir. Şekil 5’te, ilgili kategori 
yanındaki Ekleme ikonu tıklanır. Açılan yetki penceresinde tür ve kullanıcı kodu seçildikten sonra Kaydet
butonu tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5-5bea6003-81df-4b7c-80d7-981a41faeab9.png)

### 1.1.3 Departman Rolü Belirleme

Belli bir departmanda bulunan kişilere rol tanımlama yapmak için Departman Rolü kategorisi kullanılır. 
Böylece kullanıcıları tek tek tanımlama işlemi ile uğraşılmaz.
Şekil 6’da, Departman Rolü kategorisi yanındaki Ekleme ikonuna tıklanır. 2 numaralı alandaki butona 
tıklanarak departman seçildikten sonra Kaydet butonuna tıklanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/6-b2c24f48-1b82-4ebe-8d79-a92e5f4f55cd.png)

Eklenen departmandaki kullanıcıları görmek için ilgili departman yanındaki 1 numaralı alandaki ikona 
tıklanır. 2 numaralı alanda departmana bağlı kullanıcılar listelenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/7-f562f567-78e0-4f88-9b5f-147e1fb52ecd.png)

### 1.2 Rol Yetkileri

Eklenen kullanıcı ve rollere ait yetkilerin nasıl verileceği ve bu yetkilerin neler olduğu bu bölümde 
anlatılacaktır. 
Yetki verilmek istenilen ilgili rol tıklanır. Sağ tarafta bu role ait hangi izinlerin verileceği seçilir.
Şekil 8’de, İdari İşer departmanına yetki işlemleri için departman tıklanmıştır. 2 numaralı alanda yer alan 
yetkilerden izin durumu işaretlenir. Tam Yetki seçeneğinin İzin Ver/İzin Verme olarak seçilmesi durumunda 
altında yer alan tüm yetkiler için aynı durum seçilmiş olacaktır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/8-d2e15619-3608-49d2-9fcb-d5fa790bb710.png)

Yetkiler; Görüntüleme, İndirme, Yazdırma ve Değiştirme ana başlıkları altında gruplandırılmıştır. Kendi 
altında bulunan yetkiler için hangi işlemin yapılacağını belirtir. Örneğin, Görüntüleme altında yer alan Ek
yetkisi , kullanıcının ekleri görüntüleme iznin olup olmadığını belirler. Görüntüleme için hangi izin durumu 
seçilirse altındakilerde aynı izin durumu ile işaretlenecektir. Eğer tamamı için aynı izin seçilmeyecekse tek tek 
görüntüleme durumu seçilir.
Şekil 9’da, Görüntüleme yetkisi için İzin Ver ve İzin Verme seçenekleri mavi kutucuk ile işaretlenmiş 
durumdadır. Bu durum, görüntüleme altında yer alan yetkiler için hepsinin İzin Ver ve İzin Verme olarak seçili 
olmadığı anlamına gelir. Eğer tüm yetkiler için aynı durum seçilecekse ana başlığın işaretlenmesi yeterlidir. Bu 
durumda kutucuk mavi tik olarak işaretlenecektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/9-71e685eb-62cf-45cb-b1f2-10ecb690c7b1.png)

## 1. Görüntüleme Yetkileri;

✓ Listeleme: Seçili kütüphane, dizin veya doküman için kullanıcının nesneyi listeleme durumudur.


✓ Klasörler: Kütüphane ve dizinler için ilgili nesneye ait klasörleri görüntüleme durumudur.


✓ Dosya: Seçili nesneye ait dokümanları görüntüleme durumudur.


✓ İçerik: Dokümanlara ait eklenen içeriğin görüntülenme durumudur.


✓ Versiyon: Dokümalara ait versiyonların görüntülenme durumudur.


✓ Ek: Dokümana ait eklenen ek dosyaların görüntüleme durumudur.


✓ İlişki: Doküma eklenen ilişkililerin görüntülenme durumudur.


✓ Profil: Dokümana ait eklenen profillerin görüntülenme durumudur.


✓ Dijital İmza: Dokümana ait dijital imzaların görüntülenme durumudur.


✓ Zaman Damgası:Doküman için eklenen zaman damgalarının görüntülenme durumudur.


✓ Gizlilik: Dizin veya dokümanlar için tanımlanan gizlilik türlerinden kullanıcının seçili nesneye ait 
hangi gizlilik türlerini görüntüleyeceği yetkisidir. Gizlilik başlığı altında yer alan Gizli, Tasnif Dışı, 
Hizmete Özel, Özel,Çok Gizli,Kişiye Özel yetkilerinde seçim yapılır.

## 2. İndirme Yetkisi:

Kullanıcının seçili nesne üzerinde indirme yetkisinin olup olmayacağı belirlenir. 
Örneğin, kullanıcıya ilgili dokümanı sadece görüntüleme yetkisi verilip indirme yetkisi verilmek 
istenmiyorsa, İndirme yetkisi durumu İzin Verme olarak işaretlenir.

## 3. Yazdırma Yetkisi:

Kullanıcının dokümanı yazdırma yetkisine sahip olup olmama durumudur.

## 4. Değiştirme Yetkileri;

✓ Düzenleme: Kullanıcının Özellikler, Açıklama, Yeniden Adlandırma, Profil işlemlerinde 
düzenleme yapabilme yetkisidir.


✓ İşlemler: Kullanıcının; Taşıma, Kopyalama, Referans Dosya, Kısayol Oluşturma, Index Yenileme, 
Paylaşım Linki ve Mail Olarak Gönder işlemlerini yapabilme yetkisidir.


✓ Check In Ceheck Out: Kullanıcının dokümanı versiyonlama işlemini yapılabilme yetkisidir.


✓ Yayınlama: Dokümanı yayınlama işlemini yapılabilme yetkisidir.


✓ Doküman Düzenleme: Kullanıcıya doküman üzerinde değişiklik yapma yetkisinin verilmesidir. 


✓ Silme: Dokümana eklenen içerik, versiyon, ek ve ilişkiler ile klasör ve kütüphane üzerinde 
kullanıcınına silme işlemini yapabilme yetkisidir.


✓ Geri Dönüşüm Kutusu: Kullanıcının geri dönüşüm kutusu altında yer alan işlemler için yetki 
durumudur. Görüntüleme, geri dönüşüm kutusunu görüntüleme, Tümünü Görüntüleme, diğer 
kullanıcıların sildiği dokümanları da görüntüleme, Geri Alma&Silme, geri dönüşüm kutusunda 
yer alan dokümanlar üzerinde silme ve geri alma işlemlerini yapabilme yetkisinin verilmesidir.


✓ Yetki Düzenleme: Kullanıcının yapılan bu yetkilendirmeler için iznin olup olmama durumudur

## 5. Ek Açıklama:

Kullanıcının dokümana eklenen ek açıklamalar için altın yer alan işlemler için yetki 
durumudur. Görüntüleme, ek açıklamaları görüntüleme, Düzenleme, ek açıklamalar üzerinde değişiklik 
yapma, Silme, eklenen ek açıklamaları silme işlemlerini yapabilme yetkisinin verilmesidir.

## 6. Yetkileri Üst Dizinden Al Yetkisi;

Yeni bir dizin veya doküman için Güvenlik ayarında bu seçenek varsayılan olarak işaretlidir. Dizin ise 
kütüphane, doküman ise bağlı olduğu dizin yetkilerini alır. Bu seçeneğin işareti kaldırılarak seçili nesneye ait 
kullanıcı ve roller ile izin durumları seçilir.
Şekil 10’da, Yetkileri üst dizinden al seçeneği işaretli olduğu için izin durumu kutucukları sarı işaretlidir. Bu 
seçilen durumun üst dizinden geldiğini belirtir. Şekil 11’deki gibi işaret kaldırılınca izin kutucukları 2 numaralı 
alandaki gibi olacaktır

![](https://docsbimser.blob.core.windows.net/imagecontainer/10-3932581e-024e-4fc0-952a-35cc2c51df7a.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/11-0ecec59b-377e-4f99-bf76-6b193b30f294.png)

Yetkiler üzerinde istenilen izinler verilebilir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/12-df2715c3-61ea-4f85-bb1c-6249b49b41b9.png)

## 7. Sahibi Üst Dizinden Alma Yetkisi; 

Seçili nesnenin bağlı olduğu dizin için tanımlanan sahip rolündeki kullanıcının ilgili nesne içinde aynı kişi 
olması isteniyorsa Şekil 13’te, Sahibi üst dizinden al seçeneği işaretlendikten sonra Kaydet butonuna tıklanır.
Şekil 14’te, nesnenin Güvenlik ayarları açıldığında sahip rolündeki kullanıcının üst dizinin sahip rolü kullanıcısı 
olduğu görünür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/13-d79c6b77-78d7-45cf-8e07-a83d8cbf5566.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/14-03dbc555-e051-4392-bb57-5c0372b4c3ec.png)

## 8. Listeleme Yetkisini Üst Dizinlere Uygulama Yetkisi;

Dizin veya klasör için role bağlı yetki verilirken ilgili nesne kullanıcıda görüntülenmek isteniyor fakat üst 
dizin için Görüntüleme/Listeleme yetkisi yoksa Şekil 15’te, üst dizin için görüntüleme yetkisi verilerek ilgili 
nesne ve üst dizininin kullanıcıda görünmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/15-a87b1c33-e2cc-40ad-bcd2-e3c5ad5523ab.png)