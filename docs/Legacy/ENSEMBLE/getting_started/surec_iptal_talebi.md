# Süreç iptal talebi

	- Süreç üzerinde silme yetkisinin bulunmadığı kullanıcılar için yayınlı sürecin iptal işlemini talep olarak iletmelerini sağlamaktadır.
	- Bu özellik sadece Versiyon Yönetimi Kullan parametresi aktif iken geçerlidir.
	- Ek olarak 'Süreçlerde İptal Talebi Kullan' parametresinin aktif edilmesi gerekir.
	- Yayınlı süreç için iptal talebi oluşturma seçeneği, süreci görüntüleyebilen tüm kullanıcılarda yer alır.
	- Yayınlı bir süreç için birden fazla iptal talebi oluşturulabilir. 
	- İptal Talebi Süreç sahibine gidecektir. Bu sebeple iptal talebi oluşturulacak sürecin 'Sahibi' bilgisi boş bırakılmamalıdır.
	- Süreç sahibi Kullanıcı grubu seçili iken, gruptaki tüm kullanıcılara iptal talebi gidecektir.
	- İptal talebinin gönderildiği kullanıcıların bekleyen işler sayfasında 'Süreç İptal Talepleri' başlığı altında ilgili süreç listelenir.
	- Sürecin iptal talebinde hangi kullanıcıda beklediği süreç detayındaki 'Süreç Onay Geçmişi' sekmesinden görüntülenebilir.
	- Süreç sahibi kullanıcı grubu iken gruptaki herhangi bir kullanıcının iptal talebini onaylaması yeterlidir.
	- "İptal onayında (Pasife Alma) akış, kontrol matrisine de gitsin mi?" parametresi aktif ise iptal talebi onaylandığında önce kontrol akışı sonra onay akışı gerçekleştirilir.
	- Parametre aktif değilse süreç sahibinin iptal talebini onaylaması sonrasında direkt onay akışını başlatır, onay akışı sürecin onay matrisine göre oluşmaktadır.
	- Süreç onay matrisindeki kullanıcılara matristeki seviyelerine göre sırayla süreç iptal onay görevi düşer.
	- Süreç onay matrisindeki ilk onaycı henüz iptal talebini onaylamadıysa; süreç, iptal onay akışı geri çağrılabilir.
	- Onay matrisindeki ilk onaycı, iptal görevini onayladığında, artık süreç iptal onay akışı geri çağırılamaz.
	- İptal onay akışında onaycıları değiştirme özelliği bulunmamaktadır.
	- Personel Görev Aktarımında Süreç Yönetimi için 'Onaylar' aktarılamamaktadır.
	- İptal edilen süreç Pasif süreçler arasında yerini alır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/mupload-5b353dd8-fcd8-4658-82b7-fdac03bfdbf2.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/mupload-adbeb3bc-a103-4037-b79a-6743adda6d8e.png)