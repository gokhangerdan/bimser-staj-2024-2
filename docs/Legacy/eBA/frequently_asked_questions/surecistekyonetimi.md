# Süreç İstek Yönetimi Kullanım Dokümanı

Bir kişinin onayında bekleyen süreçleri başka bir kişiye aktarmak için “Süreç İstek Yönetimi” alanı kullanılır. 
İlgili akışı başka bir personele aktarabilmek adına yetkili  kullanıcı web arayüzünde
“İş Akış Yönetimi” başlığı altındaki “Süreç İstek Yönetimi” menüsünü göreceklerdir.

Not:
Süreç istek yönetimi yetkisi için eBASysteamManager>Authorization Manager>Yetkiler >Web kırılımının altından 
WebProcessRequestManagementAdmin yetkisinin verilmesi gerekmektedir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/isakis1-c8ec69b5-422b-4f39-a276-418b0ebdf86a.png)

Süreç Yönetimi menüsüne tıklandığında yan panele, hangi kullanıcının üzerindeki hangi bekleyen işleri aktaracağının seçilebileceği bir ekran gelir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/isakisi2-bbb346dc-0713-4581-bab1-96926e954872.png)

Kullanıcı ve Pozisyon seçenekleri, iş akışlarında kişilere user bazlı mı pozisyon bazlı mı düşen onayların listelenmesini istediklerinin seçeneğini sunar.
 eBA'da kişilere user bazlı veya pozisyon bazlı akışlar düşürülebilir.
 Bizim oluşturduğumuz süreçlerde onaylar user bazlı kişilere aktarıldığından bu ekranda Kullanıcı seçeneği işaretli kalacaktır.

Sadece Pasif Kullanıcıları Getir seçeneği, işten çıkan ve pasife düşen kullanıcıların üzerinde bekleyen onayları başka birine aktarmak için kullanılır. 
Eğer üzerindeki onayın başka personele aktarılacağı kişi pasif değilse bu seçenekteki seçim kaldırılarak, onayındaki işin aktarılmak istendiği kullanıcı browse butonuna tıklanıp seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/isakisi3-f15c5f3d-723f-4201-92a6-99184e194709.png)


	Kullanıcı seçim listesinde, onayında bekleyen akış olan tüm personeller listelenmektedir.
 Aktarım yapacak kişi ilgili personeli bu listeden seçer.
Personel seçildikten sonra aşağıdaki “Süreçler” comboboxına seçilen kişinin onayında ne kadar süreç bekliyorsa bu süreçler listelenir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/isakis4-3766d020-dfeb-4cbe-a586-f11f05592507.png)

	Aktarım yapacak kişi, hangi sürecin akış kaydını aktaracaksa ilgili süreç adını buradan seçer ve yukarıdaki “Tamam” butonuna basar.

Tamam butonuna basıldığında yan panelde, seçilen kullanıcının üzerinde bekleyen seçilen sürece ait akış kayıtlarının listesi açılır. Kişi buradan atamak istediği süreç ya da süreçleri işaretleyerek yukarıda bulunan “İstekleri Ata” butonuna tıklar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/isakis6-5a5bfab3-60a1-4cdc-9ebe-1a9c961d720b.png)

İstekleri Ata butonuna tıklandığında yan panelde, isteklerin kime atanacağının seçildiği bir ekran gelir. Burada da atamalar kullanıcı bazlı ya da pozisyon bazlı kişi ya da pozisyonlara atanabilir. 
Sizin süreç yapınıza göre istekler kullanıcı bazlı atanacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/isakis7-a552d8ff-69b8-4102-8212-41cff3ab6c80.png)

İstekleri ata ekranında da Kullanıcı seçeneği işaretliyken browse denerek, süreçlerin atanacağı personel seçilir ve ardından “Tamam” butonuna basılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/isakis8-13765364-1138-45f7-bf52-7f9933dcd4b8.png)

Böylece seçilen süreç ya da süreçler ilgili personele aktarılmış olur. Kendisine süreç atanan personel ise onaylar ekranından bu süreci görüp ilerletebilir.

