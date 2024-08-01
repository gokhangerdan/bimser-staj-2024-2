# Yetki Matrisi

Yetki Matrisi

Süreç yönetimi modülünde, modül yöneticisi olmayan kullanıcıların her bir süreç için hangi yetkilere sahip olacağının belirlenmesini sağlar.

Sadece "Süreç bazında yetkilendirme kullan" parametresi aktif iken süreç detaylarında bu sekme görüntülenir, aksi halde tüm süreçlerde tüm kullanıcılar tam yetkili olacaktır.

Süreç detayındaki Yetki Matrisi sekmesinde Yetki matrisi Ekle butonuyla Kullanıcı, Pozisyon ve Kullanıcı Grubu türlerinde ekleme yapılabilir. 

Script ekle butonuyla da yetki matrisine sql script'i eklemek mümkündür, sql script hazırlanırken ensemble destek ekibinden yardım alınabilir.

Yetki Matrise eklenen tanımlar üzerinde görme, değiştirme, silme, yazdırma, modelleme ve kısıtlı düzenleme seçenekleri bulunmaktadır.

Bu seçeneklerin her biri ilgili tanım üzerinde yer alan kullanı(lar)ın mevcut süreç üzerinde hangi yetkilere sahip olacağını belirlemek içindir, aşağıda her bir yetkinin açıklaması yer almaktadır.

Süreç yönetimi modül yöneticisi olarak tanımlı bir kullanıcının yetki matrisine eklenmesine gerek yoktur, eklenmesi de sorun oluşturmayacaktır.

Matrisin kaydedilmesi kapsamında üç seçenek yer alır, varsayılan olarak hiçbiri seçili olacaktır. Bunun yanında 'Matrisi alt süreçlere ekle' ve 'Matrisi alt süreçlere uygula' seçenekleri yer alır.

'Matrisi alt süreçlere ekle' seçeneği seçilerek süreç kaydedildiğinde; Bu sürecin tüm alt süreçlerine bu sürecin yetki matrisi eklenir, alt süreçlerin mevcut yetki matrisleri değişmeden bu süreçteki matris eklenmiş olacaktır.

'Matrisi alt süreçlere uygula' seçeneği seçilerek süreç kaydedildiğinde; Bu sürecin yetki matrisi ile bu sürece ait tüm alt süreçler bu sürecin birebir ayısı olan yetki matrisine sahip olacaktır.

'Matrisi alt süreçlere ekle' ve 'Matrisi alt süreçlere uygula' seçenekleri, sadece alt süreçlerde düzenleme yetkisi olunduğu süreçlerde uygulanacaktır.

___

![](https://docsbimser.blob.core.windows.net/imagecontainer/Süreç%20bazında%20yetkilendirme%20kullan%20parametresi-ec0c0b96-43b7-4d80-a184-5a9a891f5c5a.png)

___

![](https://docsbimser.blob.core.windows.net/imagecontainer/Süreç%20Detayı%20Yetki%20Matrisi%20Sekmesi-2e792b32-1e3e-42b2-8eb8-d356486382e1.png)