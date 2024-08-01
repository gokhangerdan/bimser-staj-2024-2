# Varlık Taşıma Nedir ve Nasıl Yapılır?

## Tanım

Varlıklar tanımlanırken varlıkların bulundukları konumlar sarfyeri ve kısım tanımlarıyla belirtilir. Varlıkların konumları değişikliğe uğrayabilir. Bu nedenle yeni sarfyeri/kısım ve bağlı olduğu yeni varlığı tekrar belirtme gereği duyulabilir.

Varlık kartı içerisinde eğer kullanıcının değiştirme yetkisi var ise varlık özelindeki bilgileri değiştirebilir. Fakat varlıkların lokasyonlarının değişikliğiyle alakalı bir tarihçeye ihtiyaç duyulursa bu işlem yetersiz kalacaktır.

Bu nedenle varlık lokasyonlarının değişiklik işlemlerini kart içerisinden değil, Varlık Taşıma arayüzünden gerçekleştirilmelidir.

Menü > Varlık Yönetimi > Varlık Taşıma


![](https://docsbimser.blob.core.windows.net/imagecontainer/1-6bfeb390-0f15-4e70-af0d-8118ad36f8bc.png)

Bu ekranda görülen tüm veriler varlık ve lokasyon değişikliği bazında görüntülenmektedir. Değişiklik işlemleri de bu şekilde yapılmaktadır.
İşlemler gerçekleştirildiğinde ekran görüntüsünde de görüldüğü gibi, varlık, eski ve yeni kısım/sarfyeri ve bağlı olduğu varlık, kayıt tarihi ve kaydı gerçekleştiren şeklinde bilgiler yer almaktadır.

Kayıt oluşturmak için ekle butonuna tıklayınız.


![](https://docsbimser.blob.core.windows.net/imagecontainer/2-b6db6f85-9b61-403b-aa86-0bb37a23b4ac.png)

## Giriş Yapılacak Alanlar

### Transfer Numarası

Bu alan işlem yapıldıktan sonra otomatik kaldığı sayaçtan itibaren devam edecektir. Giriş yapılmasına gerek yoktur, kartı incelenirken bu alanda numarayı görüntüleyebilmek içindir.

### Varlık Taşıma Türü

Zorunlu değildir, fakat raporlama gereği varlık taşımalarını türlere (Örnek: Varlık Taşıma Nedeni) ayrılabilir. Bu türler Varlık > Tanımlar > Varlık Taşıma Türleri sayfasından tanımlanır ve işlem yaparken de seçilir.

### Bulunduğu Kısım

Zorunlu bilgidir. Eğer Varlık seçtiyseniz otomatik olarak o varlıkta mevcutta kayıtlı olduğu kısım bilgisi otomatik gelir.

### Bağlı Olduğu Varlık

Zorunlu değildir. Her varlığın bağlı olduğu bir varlık bulunmayabilir (Ana varlık olabilir). Varlık seçtikten sonra eğer bağlı olduğu varlık var ise bu bilgi de otomatik getirilecektir.

### Yeni Sahip Varlık

Zorunlu değildir. Taşınacak varlık sadece bir varlığın altında gösterilerek taşınacak ise seçilmelidir. Bu seçim yapıldıktan sonra Yeni Kısım bilgisi de seçilen varlığın bilgilerinden otomatik getirilmiş olur.

### Yeni Kısım

Zorunludur, yeni kısım varlığın işlem sonrasında bulunacağı kısmı gösterir.

### Yeni Gider Merkezi

Zorunlu değildir, daha öncesinde tanımlanmış olan gider merkezini değiştirmek için seçilebilir. Bu tanım varlığın sarfyeri bilgisi değildir.

### İşlemi Yapan

Ekle dediğinizde otomatik olarak kullanıcının eşleştiği kaynaktan getirilir.

### Tarih

Taşıma işleminin tarihi belirtilir.

### Açıklama

Taşıma işleminin detayları bu alanda notlandırılabilir.

### İş Emri

İş emrinde Sökme/Takma sekmesinde bir taşıma yapılabilir. Bu işlem sonucunda iş emri kapandığında taşıma işlemi gerçekleştirilir ve Varlık Taşıma ekranında kaydı oluşur. Bu kaydın içerisinde eğer Sökme/Takma’dan yapılan bir işlem ise hangi iş emrinde gerçekleştiğinin numarası bu alanda gösterilir.

### Özel Kodlar

Varlık Taşıma kodları özelleştirilebilir yedek alanlardır. İsim değişikliği yapılarak ilave giriş alanları oluşturulabilir.

___

Varlık Yönetimi > Raporlar > Varlık Taşıma Raporu içerisinden filtrelendirme yaparak buradaki kayıtlar ile bir rapor çıktısı alınabilmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3-dabb6476-e691-40e9-9388-837bb771b1f1.png)

