# BEAM Kullanıcı Tanımlama

BEAM uygulaması içinde kullanıcı tanımlaması yaparken dikkat edilmesi ve bilinmesi gereken hususlar vardır.

1.Kullanıcı tanımlamasını nereden yapılır?

2.Kullanıcı tanımalası sırasında doldurulması zorunlu olan alanlar ne için istenmektedir?

3.Kullanıcı tanımlamasını herkes yapabilir mi?

4.Kullanıcı tanımlaması sırasında alınan hatalar ve çözümleri.


## 1.Kullanıcı tanımlamasını nereden yapılır?

BEAM sisteminde kullanıcı tanımlasını, kullanıcımız ile login olduktan sonra sırası ile,
Ana Menü>Sistem>Kullanıcılar sayfasından üstte yer alan "+Ekle" sayfasına gelerek yenir bir kullanıcı ekleyebileceğiz. Burada ilgili alanları doldurduktan sonra sağ üstte yer alan "Kaydet" butonuna basarak yeni bir kullanıcı oluşturmuş olacağız.

![](https://docsbimser.blob.core.windows.net/imagecontainer/mupload-7a074cf4-9cf7-4c33-877c-941e3353927c.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/mupload-4994c3eb-3b2c-48c4-9bce-aec6e2a45620.png)

## 2.Kullanıcı tanımalası sırasında doldurulması zorunlu olan alanlar ne için istenmektedir?

BEAM sisteminde kullanıcı tanımlası yaparken Genel Bilgiler sekmesinde karşımıza çıkan 7 adet zorunlu alan bulunmaktadır ve bu 7 alanı doldurmadan kullanıcı tanımlasını tamamlanmasına izin vermeyecektir sistem. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/mupload-1efe3a26-e905-4f27-b857-10962b0d93d6.png)

1- Kullanıcı Durumu: Kullanıcının aktif olarak kullanıldığını gösteren bir durumdur. Yeni kullanıcılar için bu alan otomatik olarak "Kullanımda" olarak gelmektedir.

2- Kullanıcı Kodu: Kullanıcın uyguluma içinde bir nevi kimlik numarası gibi kendisine özel bir kullanıcı koduna sahip olması gerekmektedir. Bu kullanıcı kodu ile login olabilecek uygulamaya.

3- Kullanıcı Adı: Kullanıcının Adı ve Soyadının veya bilinmesi istenilen isminin yazıldığı alandır.

4- Kullanıcı Rol Tipi: Kullanıcılar, Normal Kullanıcılar ve Talep Kullanıcıları olarak 2'ye ayrılırlar. Bu tanımlamalar uygulama Lisansında tutulur ve birbirinden farklı işleyişleri vardır. Burada ilgili kullanıcnın rol tipi seçimi yapılır.

5- Kullanıcı Grubu: Kullanıcıların her biri, bir kullanıcı grubu içerisinde yer almaktadırlar. Burada Kullanıcının hangi kullanıcı grubunda yer alacağının seçimi yapılır

6- Yetkili Olduğu Şirketler: Kullanıcın yetkili olduğu/görev aldığı şirket veya şirketleri belirlemek için ilgili alanda seçim yapılır. Birden fazla şirket seçimi yapılabilir.

7-Şifre Saklama Türü: Kullanıcı oluşturulurken şifre belirlenmişse bu şifrenin nasıl saklanması gerektiğini buradan belirtilmelidir. Her şirketin kendine ait bir şifre saklama türü olabilir.

## 3.Kullanıcı tanımlamasını herkes yapabilir mi?

Bir kullanıcının kullanıcı tanımlamasını yapabilmesi için içerisinde bulunduğu kullanıcı grubunun, kullanıcı eklemesi için yetkisi olması gerekmektedir. Kullanıcı grubunda bu yetki yok ise admin kullanıcısı ile kullanıcı grubuna kullanıcı ekleme yetkisi verilmesi gerekmektedir.

## 4.Kullanıcı tanımlaması sırasında alınan hatalar ve çözümleri.

BEAM sistemi içerisinde kullanıcı tanımlaması yaparken genellikle 2 temel sorun ile karşılaşılır.
4.1. Lisans hatası.
4.2. Kullanıcı Ekle yetkisi bulunmaması.

4.1. Lisans Hatası

![](https://docsbimser.blob.core.windows.net/imagecontainer/mupload-df4d0839-2bf8-478d-929d-ec30f93cd963.png)

BEAM sistemi içerisinde yer alan ve kullanıcı lisanslarını tutan BEAM lisansı içerisinde Lisanslı Kullanıcı sayısı için yer olmalıdır. Bu konuda eğer bir hata alnıyor ise lütfen BEAM Destek birimine konuyu iletiniz.


4.3. Kullanıcı Ekle yetkisi bulunmaması

![](https://docsbimser.blob.core.windows.net/imagecontainer/mupload-4994c3eb-3b2c-48c4-9bce-aec6e2a45620.png)

BEAM uygulaması içerisinde Ana Menü>Sistem>Kullanıcılar sayfasına geldiğinze eğer "+EKLE" butonu görünmüyor ise, içerisinde bulunduğunuz kullanıcı grubunun kullanıcı tanımlama yetkisi olmadığındandır.

Bu yetkiyi tanımlayabilmek için admin kullanıcısı ile Ana Menü>Sistem>Kullanıcı Grupları>Hangi kullanıcı grubuna bu yetki verilecek ise "Değiştir" diyerek solda yer alan Menü yetkileri sekmesinde "Yeni Kayıt Ekleyebilir" yetkisinin işaretli olması gerekmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/mupload-ba985fce-16e5-49e4-977d-d70a80a57ec7.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/mupload-b78fdf5a-f0ad-49bc-b85d-23c70a14b67a.png)