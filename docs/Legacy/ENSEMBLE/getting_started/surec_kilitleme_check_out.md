# Süreç Kilitleme / Check-Out

## Süreci üzerine alma ve serbest bırakma işlemi

Süreç kilitleme özelliği belli bir kullanıcının süreci kilitlemesini ve farklı bir kullanıcının bu süreç üzerinde değişiklik yapmasının önüne geçmesini sağlayan özelliktir.

___

Süreç Yönetimi modülü yöneticisi olarak tanımlı kullanıcılar tüm süreçlerde, süreç kilitleme ve serbest bırakma işlemini, süreç kimde kilitli olursa olsun gerçekleştirebilirler. Otomatik ve/veya Manuel Check-Out fark etmeksizin bu şekildedir.

Yayınlı bir süreç herhangi bir kullanıcı üzerinde kilitli ise, süreç revize yapıldığında taslak durumundaki hali üzerinde kilit olmayacaktır.

Versiyon yönetiminin kullanılmadığı ("Süreçlerde versiyon yönetimini kullan" parametresi pasifken) durumda ve/veya süreçlerde yetkilendirme kullanılmadığı durumda ("Süreç bazında yetkilendirme kullan" parametresi pasifken) da süreç kilitleme aynı işleyişe sahiptir.

___

"Manuel süreç kilitleme(Check-Out) özelliğini kullan" parametresi aktif edilerek süreç üzerinde 'Düzenleme' ve 'Kısıtlı Düzenleme' yetkisi olan kullanıcıların süreci istediği zaman (halihazırda kilitli değilse) üzerine al seçeneği ile kilitleyebilmesine olanak sağlanır. 
Yayınlı süreçler süreç yönetimi modülü yöneticileri dışındaki kullanıcılar tarafından düzenlenemeyeceği için bu durumda üzerine al seçeneği bulunmamaktadır.
Kayıt bakım modu aktif olduğu durumda Yayınlı süreçler üzerinde süreç yönetimi modülü yöneticileri üzerine al seçeneği kullanarak süreçleri kilitleyebilir.

"Otomatik süreç kilitleme(Check-Out) özelliğini kullan" parametresi aktif edilerek süreçte düzenleme butonuna basıldığında o kullanıcı üzerinde süreç otomatik kilitlenecektir.

"Otomatik süreç kilitleme(Check-Out) özelliğini kullan" ve "Manuel süreç kilitleme(Check-Out) özelliğini kullan" parametrelerinin ikisinin de aktif olduğu durumda süreçler herhangi bir zamanda kilitli olup olmadığı göz önünde bulundurularak kilitlenebileceği ve serbest bırakılabileceği gibi süreç düzenleme butonuna basıldığında da otomatik süreç düzenleyen kullanıcı üzerinde kilitlenecektir.

___

![](https://docsbimser.blob.core.windows.net/imagecontainer/Check-Out%20parametreleri-7b1d9f94-ff59-4f57-8b91-34d3692c1c00.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/Süreç%20Kilidi%20Bilgilendirmesi-d2cd0705-22dd-43b0-8ce5-a491d2a04aeb.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/Süreci%20üzerine%20alma%20işlemi-eb81534a-d06d-473d-a7e6-c57ee80cd235.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/Süreci%20serbest%20bırakma%20işlemi-9641e6fb-faec-416c-8bd5-7317c06c969c.png)