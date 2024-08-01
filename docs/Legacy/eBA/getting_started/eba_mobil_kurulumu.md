# eBA Mobil Kurulum

eBA uygulamasının kurulu olduğu IIS üzerindeki bulunduğu site tanımına sağ tıklayıp 'Add Application' seçilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/1-ff85bcca-f805-4c8a-8863-014263389593.png)

Alias (eBARestAPI) ve Physical Path bilgilerini eBA'nın kurulu olduğu dizine uygun şekilde girerek Application tanımlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/2-b6ffd22d-763b-4330-bfa3-1f174aaa1167.png)

eBA Configuration Manager'da Advanced sekmesine RestApi key'i ve altına Adress key'i eklenir. eBA uygulamasının erişim adresine uygun olacak şekilde oluşturulmuş olan eBARestAPI adresi tanımlanarak kaydedilir.
Bu adres web arayüzündeki karekod olarak gösterilecek bilgiyi barındıracaktır.


![](https://docsbimser.blob.core.windows.net/imagecontainer/3-7f2437b5-6cb8-48ef-bdcd-9e0279cda975.png)

eBARestAPI klasöründeki web.config dosyasını açarak 3 farklı yer de bulunan adreslerdeki localhost tanımlarını eBA kurulumuna uygun olacak şekilde düzenlenip kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/4-8b3be4cf-bec1-4bb0-bf64-b972aeeeb13e.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/5-acff18ad-12ae-4599-b8f9-1d6d9f27f2e3.png)

eBARestAPI application tanımı üzerinden browse yaparak test edilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/6-333558a4-d1ca-4725-ad85-5bed4bdabc47.png)

Son işlem olarak eBA uygulamasına ait Windows servisini ve barındığı IIS'teki application pool tanımlarını Restart edilir. Bat dosyası ortama uygun olarak hazırlanıp çalıştırılabilir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/7-585cdea2-d091-4825-8966-1cc7517895a8.png)

Kurulum başarıyla gerçekleştiyse web arayüzde 'Mobil Uygulama' butonu yer alır ve tıklayınca barcode gözükecektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/8-72e0232d-f038-42fe-8e7c-6737932bad5b.png)

Mobil uygulama Apple ve Android marketlerden 'Bimser eBA' ismiyle indirilip kurulabilir. Mobil uygulamada ilk kullanımda Sunucu ekleme kısmında 'Karekod Tarama' kullanılarak web arayüzündeki karekod okutularak ekleme yapılır.
Mobil cihazdan eBA uygulamasına erişimin olması gerekmektedir, yoksa hata alınacaktır. Mobil cihazdan eBA sunucusuna erişim bulunuyorsa mobildeki oturum açma sayfasında dil seçeneği görüntülenebilecektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/9-ea47bf75-ac22-4d2a-b436-8fb585823669.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/10-cc467f71-f8c6-47c2-b246-f5836005b38c.png)

