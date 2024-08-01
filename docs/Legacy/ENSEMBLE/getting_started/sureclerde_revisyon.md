# Süreçlerde Revizyon

"Süreçlerde versiyon yönetimini kullan" parametresi aktif olmalıdır.
Versiyon yönetimi özelliğinin kullanımının implementasyon aşamasında kararlaştırılması ve bu kararda değişikiğe gidilmemesi gerekir. 
Bu parametre açık olarak uygulama kullanıldığında, tekrardan kapatılması durumunda veri tutarsızlığı oluşacaktır.
Versiyon Yönetimi özelliği kullanıldığında süreçler sadece taslak halide iken (süreç revizesi yapılırken ya da süreç yeni oluşturulduğunda) düzenlenebilir/değiştirilebilir.
"Versiyon yönetiminin açık olduğu durumda süreç kayıt bakım modunu aktif et" parametresi aktif edildiğinde Süreç Yönetimi Modülü yöneticileri süreçleri yayınlı iken de düzenleyebilir.
Revizyon başlatabilmek için Süreç Yönetimi modülü yöneticisi, Sürecin sahibi, süreci hazırlayan kullanıcı ya da ilgili süreç üzerinde düzenleme yetkisine sahip olunması gerekir.
Yayınlı süreç üzerinde Revizyon başlat seçeneği, ilgili revizyon talebi de seçilebilecek şekilde gerçekleştirilebilir.
Yayınlı süreç revizyon başlatılırsa, yayınlı sürecin birebir kopyası bir üst versiyon numarası ile taslak süreçler arasında düzenleme modunda yerini alır.
Yayınlı sürecin kopyası taslak süreçler arasında yerini aldığında, yayınlı süreç her açıldığında "Bu sürecin revizyonu devam etmektedir" bilgilendirmesi görüntülenebilir.
Revizyonu başlatan kullanıcı, taslak süreçlerde 'revize eden' ve 'bekleyen kullanıcı' olarak gözükür. 
Taslak halindeki bu süreç silinirse revizyondan vazgeçilmiş olacaktır. Aksi taktirde gerekli tüm değişiklikler sağlanıp bu taslak süreç kontrole ve onaya gönderilebilir.
Süreç detayında yer alan Kontrol matrisine göre kontrol aşaması, ardından Onay matrisine göre onay aşaması işleyecektir.
Kontrole gönderildiğinde "Sürecin kontrole gönderildiği kullanıcı süreci düzenleyebilir" parametresi de pasif ise bundan sonra süreçte değişiklik sağlanamaz.
Kontrol aşamasından sonra Onay aşamasına geçecektir. Taslak sürecin onay aşamasında son onaycı onayladığında yayınlı süreçler arasında yerini alır.
Yayınlı sürecin versiyon numarası, o sürecin kaç kez revize edildiğini gösterir.
Daha önceki tüm eski versiyonları bu yeni revizyon numarasına sahip süreç üzerinden görüntülenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/mupload-517a3b02-3a61-48d8-af28-078ffb88288c.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/mupload-881860dc-b458-4580-91ca-5e565e0a25ee.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/mupload-39772a43-9e77-410b-bfcb-899afad62f9c.png)