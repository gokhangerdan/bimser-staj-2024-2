---
title: 2.1 Process Archive Menüsü
sidebar_position: 10
---

# 2.1 Process Archive Menüsü

İş akışı süreçlerinin, hem akış hem form ekranları arşiv yapısında gösterilmek istenirse Process Archive oluşturulur. Yeni proses arşiv oluşturmak için 1 numaralı alandaki menüye tıkladıktan sonra Add New butonuna tıklanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3a40f411-388f-466e-9db2-ed7ca083652d)

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadc2d0d3d4-f601-4767-88b2-f12708335e5f)

Şekil 28’de, General sekmesinde 2 numaralı alana arşiv adı, 3 numaralı alana raporda görüntülenecek başlık yazılır. Multilanguage Caption alanında ise, sistemde tanımlı tüm diller listelenir. Arşiv başlığı metninin diğer dillerdeki karşılıkları bu alana girilerek arşiv başlığının çoklu dil desteği ile görünmesi sağlanabilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload62c9fdb6-e7d0-4cbb-9b4b-156f0854b74e)

Şekil 29’da, Integration Query sekmesinde proses arşiv için oluşturulan sorgu seçilir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3a994df9-2ddf-4f94-8ff0-b16002dde984)

Şekil 30’da, örnek proses arşiv sorgusu bulunmaktadır. Sorguyu kendi sürecine göre düzenleyebilirsiniz.  
2 numaralı alanda sürece ait raporda görüntülenmek istenilen alanlar, 3 numaralı alanda  form adı yazılmıştır. Eğer sorguya paramtetre eklenecek ise where ifadesinden sonra 4 numaralı alandaki gibi eklenir. Sorguya parametre ekleme işleminin nasıl yapıldığı 1.1.3 Sorgu Parametresi Ekleme başlığı altında anlatılmıştır. 


![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfe4ff990-9c21-4580-9ceb-63efb1e7a620)

Şekil 31’de, Visible Colums sekmesinde raporda görüntülenecek alanlar belirlenir. Yeni alan eklemek için 2 numaralı alandaki ikona, seçili alanı raporda göstermemek için 3 numaralı alandaki ikona, alanların sırasını belirlemek için 4 ve 5 numaralı alandaki ikonlar kullanılır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadd17de21a-9de4-4727-aea2-f97aa41f2133)

Şekil 32’de, alan ekleme butonuna tıkladıktan sonra açılan pencerede görüntülenmek istenilen alan seçildikten sonra OK butonuna tıklanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfadccd2b-6047-4d5f-9f70-debd65d1c354)

Şekil 33’de, Date Filtering sekmesinde hazırlanmış sorguda başlangıç ve bitiş tarihi mevcut ise 2 numaralı alandaki seçenek işaretlenir. Start Date ve Finish Date listelerinde sorguda var olan parametrelerden biri seçilir. Parametrelerin tipleri tarih olmalıdır. Bu iki tarihin varsayılan değerleri burada verilebilir. 
Tarih varsayılan değerleri Relative ve Static olabilir. 

Eğer  Relative varsayılan değer tipi seçilirse günün tarihi veya günü tarihinden ay, gün, yıl cinsinden istenilen kadar öncesi veya sonrası getirtilebilir. 

Eğer Static varsayılan değer tipi seçilirse belirli bir tarih takvimden seçilmelidir. 

Not : Başlangıç tarihi bitiş tarihinden önceki bir tarih olacak şekilde ayarlanmalıdır. Ayrıca eğer arşiv listesinin başlangıçta dolu gelmesi isteniliyorsa ve tarih filtrelemesi kullanılıyorsa bu iki tarih için varsayılan değerler verilmelidir. 


![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadb2a33b7c-5396-480f-a546-bf041f77cbd6)

Şekil 34’te, Query Parameters  sekmesinde seçilen sorgunun parametreleri bulunur. Bu parametrelere varsayılan değerler girilebilir. Varsayılan değer vermek için Use Default Value seçeneği işaretlenir. Parametre tipine uygun varsayılan değer girilir. 
Eğer varsayılan değer girilmişse parametrenin görünüp görünmeyeceği belirtilebilir. Görünmeyen parametreler için hep varsayılan değer kullanılır. Varsayılan değer bir metin bilgisi olabileceği gibi sistemdeki kullanıcının pozisyon bilgisinin özelliklerinden birisi olabilir. Sistem tarafından sunulan varsayılan değerler 3 numaralı alana tıklanarak listelenir.
Gelen ekrandan istenilen özellik seçilir; 

- LogonUser.ID : Kullanıcı kodu 
- LogonUser.Firstname : Kullanıcının adı 
- LogonUser.LastName : Kullanıcının soyadı 
- LogonUser.Email : Kullanıcı elektronik posta adresi 
- LogonUser.Status : Kullanıcı aktiflik durumu (1 : Aktif, 0 : Pasif) 
- LogonUser.Type : Kullanıcı tipi (0: Normal, 1:Özel, 2:Sistem) 
- LogonUser.ImportStatus : Transfer durumu (0:Transfer edilmedi, 1:Transfer edildi)
- LogonUser.Birthdate : Kullanıcının doğum tarihi. 
- LogonUser.EmployementStart : Kullanıcının işe başlama tarihi. 
- LogonUser.EmployementEnd : Kullanıcının işten ayrılma tarihi. 
- LogonUser.Category : Kullanıcının kategorisi (0:Mavi yakalı, 1:Beyaz yakalı). 



- LogonUser.Sex : Kullanıcının cinsiyeti (0:Bayan, 1:Erkek).  
- LogonUser.ManagerUser.default : Kullanıcı yöneticisinin pozisyon kodu. Farklı yönetici profilleri için default yerine ilgili profil adı yazılır.  
- LogonUser.Department.ID : Kullanıcının departman kodu. 
- LogonUser.Department.Description : Kullanıcının departmanının adı.
- LogonUser.Department.ManagerDepartmentID : Kullanıcının departmanının yönetici departmanının kodu. 
- LogonUser.Department.ManagerPositionID : Kullanıcının departmanının yöneticisinin pozisyon kodu. 
- LogonUser.Department.Status : Kullanıcının departmanın durumu (1 : Aktif, 0 : Pasif) 
- LogonUser.Department.Type : Kullanıcının departmanın tipi (0: Normal, 1:Özel, 2:Sistem) 
- LogonUser.Department.ImportStatus : Kullanıcının departmanın transfer durumu (0:Transfer edilmedi, 1:Transfer edildi) 
- LogonUser.Profession.ID : Kullanıcının ünvan kodu. 
- LogonUser.Profession.Description : Kullanıcının ünvan adı. 
- LogonUser.Profession.Status : Kullanıcının ünvanın durumu (1 : Aktif, 0 : Pasif)
- LogonUser.Profession.Type : Kullanıcının ünvanın tipi (0: Normal, 1:Özel, 2:Sistem)
- LogonUser.Profession.ImportStatus : Kullanıcının ünvanın transfer durumu (0:Transfer edilmedi, 1:Transfer edildi)  
- LogonUser. Groups.[GroupName] : Kullanıcı “GroupName” ismindeki grubun içerisinde ise “1” değilse “0” döner.  
- LogonUser.Custom.[PropertyName] : Kullanıcının sonradan tanımlanmış Custom Property özelliklerinden PropertyName ismindeki özelliğinin değerini verir. 

Not : Eğer arşiv listesinin başlangıçta dolu gelmesi isteniliyorsa tüm sorgu parametreleri için varsayılan değerler verilmelidir. 

Not : Sistemdeki kişinin pozisyon bilgilerini varsayılan bilgi olarak kullanarak sadece kişinin doldurduğu bilgileri getirmek mümkündür. Örneğin DOCUMENTS tablosundaki POSITION alanını LogonUser daki ID değeri ile karşılaştırarak sadece kişin doldurduğu belgeleri listelemek mümkündür. 


![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload74a6135d-d26e-4e2a-8789-896db44dd24b)

Şekil 35’te, Field Filtering sekmesinde sorgudan dönen alanlar üzerinde filtreleme yapılmaktadır. Filtreleme yapılmak istenilen alanı listeye eklemek için ekleme butonuna tıklanır. Açılan pencerede alan seçildikten sonra OK butonuna tıklanır. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadebb7cf8c-9dc5-4a52-a225-2f07d14971ff)

Seçilen alan filtrelemeleri için filtreleme tipi ve varsayılan değer girilebilir. Filtreleme tipi, alanın tipine göre değişmektedir.  Alanlara göre filtreleme tipleri ; 
- Metin alanlar için ; 

Text : Yazılan metne göre arama yapar. From Begining seçilirse sadece aranan metin ile başlayan kayıtlar gelir. Contains seçilirse aranan metini içeren kayıtlar gelir. 

List : Bu durumda gelen veriler içinde gruplama yapılır ve bir liste oluşturulur. Contains seçilmişse ve bu listedeki elemanlardan birisi seçilmişse o elemanın olduğu kayıtlar gelir. Not Contains seçilmişse seçili elemanın olmadığı kayıtlar gelir. 

- Nümerik alanlar için ;
```
equal = : Girilen sayıya eşit olan kayıtlar gelir. 
not equal <> : Girilen sayıya eşit olmayan kayıtlar gelir. 
less than < : Girilen sayıdan küçük olan kayıtlar gelir. 
less than or equal <= : Girilen sayıdan küçük ve eşit olan kayıtlar gelir. 
grater than > : Girilen sayıdan büyük olan kayıtlar gelir. 
grater than or equal >= : Girilen sayıdan büyük ve eşit olan kayıtlar gelir. 
between : Girilen değerler arasındaki kayıtlar gelir. 
```

- Tarih alanlar için ;

Tarih alanlar için iki tarih arasında filtrelemesi yapılmaktadır. Tarih alanları için varsayılan değer girilebilir. Tarih varsayılan değerleri Relative ve Static olabilir.Eğer Relative varsayılan değer tipi seçilirse günün tarihi veya günü tarihinden ay, gün, yıl cinsinden istenilen kadar öncesi veya sonrası getirtilebilir. 
Eğer Static varsayılan değer tipi seçilirse belirli bir tarih takvimden seçilmelidir. 

Not : Başlangıç tarihi bitiş tarihinden önceki bir tarih olacak şekilde ayarlanmalıdır. 


![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload6e4cf069-3711-40cc-a742-8338e61454a5)

Forma eklenen dokümanda da arama yapma işlemini aktif etmek için Şekil 37’de, Full-Text Search sekmesinde 2 numaralı alandaki seçenek işaretlenir. 3 numaralı alandan arama yapılması istenilen alanlar işaretlenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload3482ad8d-70e0-4e41-99b5-bfed3278bc13)

- Page Size: Listede her bir sayfadaki kayıt sayısı belirtilebilir. Listenin başlangıçta dolu gelmesi isteniliyorsa Fill On Start seçilmelidir. Liste başlangıçta dolu gelecek ise Date Filtering ve Query Parameters sekmesindeki parametreler için default değerler girilmiş olmalıdır. 

- View Process As Request View : Arşivden açılmak istenen process açan kişinin onayındaysa, bu processi webdeki onay ekranından açılıyormuş gibi açar. Yani arşivden, onayındaki bir formu açan kişi form üzerinde aksiyon butonlarını da görür ve aksiyon alabilir.

- If Not Available View As Process : “View Process As Request View” seçeneği sağlanamadığında hata almadan formu görüntüleyebilmek için kullanılır.

- Use Workflow Permission : Özellik aktif edilirse, arşivden processi açan kişi eğer akıştaysa akıştaki yetkileriyle formu görüntüleyecek demektir.

- ID : Sorguda getirilen süreç numarası (PROCESSID) kolonu bu alanda seçilir. Bu alan sistemdeki bir proses numarasına karşılık gelmektedir. Bu alan genelde LIVEFLOWS tablosundaki ID alanıdır yada süreç numarasını veren başka bir veritabanı tablosu alanıdır. 

ID seçiminin yanında bulunan seçim alanı sadece Process Archive de kullanılmaktadır ve RequestID seçimi içindir. Zorunlu değildir.

- Open From Path : Eğer formlar ID bilgisi ile değil de path bilgisi ile açılmak istenirse bu alan aktif edilir ve Path listesinden, arşiv için seçilen sorgudan dönen ve path değerini barındıran kolon seçimi yapılır.

- Status Icon: Prosesin durum değeridir. Sorgudaki alanlardan birisidir. Metin bir alandır ve bu alana göre listede durum ikonu gözükür. Bu alan bilgisi FLOWSTATUSES tablosunda bulunmaktadır. 
Kullanımı opsiyoneldir. 

- Viewable: Proseslerin görüntülenip görüntülenmeyeceğini belirtir. Görüntülenme yetkilendirmesi dört farklı tipte olmaktadır : 

True : Listedeki tüm prosesler görüntülenebilir. 
  	 	  False : Listedeki prosesler görüntülenemez. 
Not Assigned : Listedeki proseslerin görüntülenmesi menü yöneticisinde belirtilecek. 
Bound : Listedeki proseslerin görüntülenmesi sorgudaki alanlardan birine bağlıdır. Bir alan seçildiğinde ona uygun operatör ile bir karşılaştırma oluşturulur. Sadece bu karşılaştırmanın doğru olduğu kayıtlar görüntülenebilir. Diğerleri görüntülenemez. Bu karşılaştırmada karşılaştırılacak değer sistemde olan kişinin pozisyon bilgilerinden biri olabilir. 

Not : Bound özelliği ile kişinin sadece kendi oluşturduğu prosesleri görüntülemesine izin vermek mümkündür. Sorgudan dönen alanlardan birinde prosesi oluşturan bilgisi olmalıdır ve bu alan viewable da bound alan olarak seçilmelidir ve karşılaştırmada Equal seçilip Value kısmında LogonUser altında ID seçilmelidir. 

- Editable: Proseslerdeki dokümanların güncellenebilme yetkisidir. Viewable yetkisi gibi ayarlanabilir. 

- Deletable: Proseslerdeki silinebilme yetkisidir. Viewable yetkisi gibi ayarlanabilir. 

- Show Event Buttons seçeneğinin bulunduğu alan sadece Process Archive de kullanılmaktadır. Süreçlere fast approve özelliği kazandırmaktadır. İlgili süreçlerin eventlerini Process ve Request id bilgilerini getirecek şekilde ikinci bir sorguya bağlayarak onaylar sayfasındaki gibi onaylama işlemi yapmasına izin vermektedir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadaf6e33dc-393d-4c71-afb8-aafbfb1d971d)

Şekil 39’da, Excel’ e aktarma butonunu aktif etmek için Export sekmesinde 2 numaralı alandaki seçenek işaretlenir.