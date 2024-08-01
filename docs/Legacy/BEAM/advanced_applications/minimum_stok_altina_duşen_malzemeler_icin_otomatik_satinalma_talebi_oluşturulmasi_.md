# Minimum Stok Altına Düşen Malzemeler İçin Otomatik Satınalma Talebi Açılması   

Web uygulama arayüzünden Sistem parametreleri ayarlanır. Yalnız TCMB ‘den alınan kur değerleri de bu servisten çalıştığı için iki metodunda ınterval değeri aynı olmalıdır.  ( ExchangeRateUpdate.Item1.Interval ve  ItemPurchaseRequest.Item.Interval)
 
Satınalma -> Tanımlar -> Belge Türleri, Masraf Türleri ve Temin sürelerinde varsayılan değer atılmalıdır. Satınalma Talebi oluşturulurken bu alanların dolu olması gerekmektedir.
 
Otomatik Satınalma Talebi oluşmasında  kendi içinde bir algoritması var, açık satınalma taleplerini siparişleri de hesaba katıp güncel ambar miktarına göre hesaplama yapıp hesaplanan miktar;  min. stok miktarından düşükse max. miktara ulaşacak şekilde talep oluşturuyor.
 
örnk. Malzemenin bir ambarda ambar parametresi min. 5 adet max 10 adet  olarak girilsin. Güncel ambar miktarı da  3 , aktif satınalam talebi de yok 
​
Bu durumda; ambardaki miktar min stoktan düşük olduğu için 5(min) > 3(güncel) =>  7 adet (10(max.)- 3 (güncel ambar miktarı ))  satınalma talebi oluşturuyor .Sistemde akış varsa ve akışta bu durum için bir düzneleme yapılmdıysa mevcut akış kullanılıyor. 
Aktif ettiğinizde bütün malzemeler için otomatik satınalmayı tek talepte oluşturabiliyor. Satınalma oluşacak malzeme eğerki sistemde kullanım dışı bir malzeme ise satınalma talebi oluşmuyor . Min miktar altında kalana malzemeler kullanımda olmak zorundadır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/clip_image001.png-612b7a5e-10df-4cd9-90e2-467b04a8eefe.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/clip_image002.png-fdd4e35f-7504-4f58-964d-6b145a18ec47.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/clip_image003.png-f2e4c716-dc87-4d93-9071-31f290a4c0a7.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/clip_image004.png-e2b7e32d-08e2-40e9-8bb3-31a681667aab.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/clip_image005.png-94cec5c2-e462-4d8e-8726-2cb779bc9945.png)

Sonrasında sunucudaki BOYSWEB2Agent servisi çalıştırılır , çalışıyorsa restart edilmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/clip_image006.png-0db0f0c3-e419-426d-b95a-ed26bc429a6c.png)

Sistem parametreleri üzerinden otomatik satınalma oluşturulabilmesi için aşağıdaki parametreler doldurulmaktadır.

ItemPurchaseRequest.Item.Active=True 
Otomatik Satınalma prosedürünü aktif eder.(Pasif etmek için =False)
ItemPurchaseRequest.Item.EbaUserCode	admin
Satınalma talebinde onay var ise akış oluşturabilmesi için yetkili EBA kullanıcı adı
ItemPurchaseRequest.Item.EbaUserPass	****
Yetkili EBA kullanıcısının parolasının girileceği alan
ItemPurchaseRequest.Item.FirmId	100
Otomatik satınalmanın yapılacağı şirket kodu giriş alanı
ItemPurchaseRequest.Item.Interval	1
Otomatik satınalma kontrolünü kaç dakika bir yapılacağının parametresi
ItemPurchaseRequest.Item.ItemGroupTemp	B.AMBARID
ItemPurchaseRequest.Item.Kisimid	6435
Satınalma için belirlenen Kısım'ın Database satırnumarası bilgisi
ItemPurchaseRequest.Item.SarfyeriId	6434
Satınalma için belirlenen Sarfyeri'nin Database satırnumarası bilgisi
ItemPurchaseRequest.Item.UserCode	BOYS
Otomatik Satınalmanın başlatılacağı BEAM kullanıcısı
ItemPurchaseRequest.Item.Description
Otomatik Satınalma içerisindeki not girişi

![](https://docsbimser.blob.core.windows.net/imagecontainer/clip_image008.png-91310e7f-d864-4fb1-b37f-8ed95a514d61.png)

