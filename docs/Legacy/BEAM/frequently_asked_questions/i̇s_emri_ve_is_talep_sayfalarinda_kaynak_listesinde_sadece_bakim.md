# İş emri ve iş talep sayfalarında kaynak listesinde sadece bakım personelleri nasıl filtrelendirilir?

bEAM uygulamasında yüklü olan personel (kaynak) kartlarının tamamının bakım personellerinden oluşmadığı durumlar olabilir.
Personel sayfasına kaydedilen kaynak kartları içerisinde satınalma modülü kullanılıyor ise satınalma personeli, zimmet modülü kullanılıyor ise tüm şirket çalışanları, ihtiyaca göre dışarıdan hizmet alınan firma personelleri ya da bir hizmet,araç,tool vb. tanımlar da kaynak olarak eklenebilmektedir.
Bu tür bir durumda baakım modülü içerisinde iş talebi veya iş emri ekranlarında personel seçimi yapılırken bakım çalışmaları ile ilgili olmayan personeller de listelenebilmektedir. 
Bu durumun önüne geçilebilmesi için bakım personellerini diğer personellerden ayırmak gerekmektedir.
Bu işlemi sağlayabilmek için öncelikle Personel Modülü üzerinden Kaynaklar sayfasına ilerlenilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/kaynak%20sayfası%20erişim-3435b6a8-b7f2-4c60-aff5-907992b3b7d8.png)

Bakım personeli olduğu belirtilecek olan personel kartı seçilir ve değiştir butonu ile kaynak kartı içerisine girilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/değiştir-f75b2fbc-7ac2-4c46-b32f-070a17f7efed.png)

Kaynak kartı içerisinde bulunan genel bilgiler sekmesinin sağ alt kısmında yer alan "Bakım Personeli" butonu işaretlenir ve kaydet denilir.
Bakım personeli işaretli olan kaynaklar böylece diğer personellerden ayrılmış olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/bakım%20personeli-3d4fd1a6-3e06-4e8a-9ea4-602ed975d360.png)

Bakım personeli olarak daha önceden işaretlenmiş olan kaynakları tek bir liste halinde görmek istenilirse eğer kaynak sayfası içerisinde bulunan sağ üstteki filtre tabından "Bakım Personeli" filtresi "Evet" olacak şekilde filtrelenip uygula denilirse eğer bu personeller listelenebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/filtre-b9cbb88d-af7f-46df-9fb8-071a2341b5c7.png)

Son kontrol olarak bakım modülündeki personel seçimi yapılan alanlarda sadece bakım personellerin gelmesi için ilgili şirket parametresinin de aktif edilmesi gerekmektedir.
Bu aktif etme işlemi için öncelikle Admin hesabı ile Sistem Yönetimi altında bulunan Şirketler sayfasına ilerlenmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/şirket-f2a44451-fb71-4c80-b1e1-e7eb9b81709f.png)

Ardından ilgili şirket kaydı seçilip değiştir denilerek şirket kartı açılır. Şirket kartı içerisinde sol üstte bulunan parametreler sekmesi üzerinden "(BC259) - Bakım Modülündeki Kaynak Listelerinde, Sadece Bakım Personeli Gösterilsin" parametresi aktif edilmelidir.
İlgili parametre "Bakım Yönetimi Parametreleri" altındaki "Ortak Kullanılan Parametreler" başlığı altında bulunmaktadır. Parametreye aynı zamanda arama labeli üzerinden anahtar kelimeleri yazarak da bulunup ulaşılabilir. Ardından şirket kaydı parametre işaretli bir şekilde kaydedilmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/parametre-e37c0e40-b799-47ca-8f53-c6edd91167a5.png)

