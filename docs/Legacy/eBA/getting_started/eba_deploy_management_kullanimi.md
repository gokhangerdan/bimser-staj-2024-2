# eBA Deploy Management Nedir?

eBA’da geliştirilen süreçlerin paketini alma ve bu paketleri başka bir ortama taşıma/aktarma ya da yedekleme yapma işleminin yapılabilmesini sağlayan uygulamadır. eBA'nın kurulu olduğu dizindeki Common klasöründe bulunur.

Çözüm ve projelerin yanında Integration Manager'da tanımlı sorguları, Arşiv tanımlarını(Örn: Süreç ve doküman arşiv) ve resim dosyalarının da elde edilmesi mümkündür.

![](https://docsbimser.blob.core.windows.net/imagecontainer/1-%20Deploy%20Management%20Dizini-42a40682-8006-4124-b74b-d6c9278be53c.png)

# eBA Deploy Management Kullanımı

Uygulama çalıştırıldığında 3 farklı seçenek çıkacaktır;
1. Create a new deploy package: Yeni bir eBA paketi oluşturmak için kullanılır.
2. Deploy to server: eBA paket dosyasını eBA uygulamasına almak için kullanılır. 
3. Transfer server to server: Bir eBA uygulamasından başka bir eBA uygulamasına süreçleri taşımak için kullanılır. Örneğin, Test ortamdan Canlı ortama gibi.


![](https://docsbimser.blob.core.windows.net/imagecontainer/2-%20Deploy%20Management%20Arayüzü-d5699b74-7b9a-4144-81b4-d8c7bcfe21fe.png)

## eBA Paketi Oluşturma

"Create a new deploy package" seçeneği seçilerek ilerlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/2-%20Deploy%20Management%20Arayüzü-e354fdf3-a6c5-4125-a5cb-c1123de02b0c.png)

Paketin dışarı aktarılacağı uygulamaya login olunması gerekmektedir, sonrasında işlemlere devam edilebilir. Instance bilgisi seçilerek admin kullanıcı bilgileri ile 'Test Connection' yapılır ve ilerlenerek oturum açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3-%20Deploy%20Management%20Login-a3aedb68-9e12-4b22-aab6-816d6f7cc859.png)

Standart ve Dashboard Transfer olmak üzere iki transfer tipi seçeneği bulunur. Dashboard paketi almak 
için Dashboard Transfer; sorgu, arşiv ve süreçlerin paketini almak için Standart Transfer seçeneği seçilir.

Varsayılan olarak Standart seçili olmaktadır. Oturum açıldıktan sonra bu seçim ekranı gelmediğinde geri gelinerek bu seçimin değiştirilmesi mümkün olacaktır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/4-%20Deploy%20Management%20Transfer%20Tipi%20Seçimi-bdb1bc62-848a-4541-97af-ab6250245cfc.png)

İki transfer tipi için de seçim yapıldıktan sonraki adımlar aynıdır. Pakete alınmak istenen nesneler seçildikten sonra oluşturulan eBA paket dosyası bilgisayara kaydedilir.

Pakete alınmak istenen bağlantı ve sorgular seçilerek ilerlenir. Seçim yapılması zorunlu değildir. Örneğin elde edilmek istenen projede sorgu bulunmuyorsa hiçbir seçim yapılmadan ilerlenir. 

 Not: Projelerin taşınacağı sistemde Integration Manager’da, burada seçilen bağlantıların taşıma işlemi gerçekleştirilmeden önce tanımlanması gerekmektedir. Sorguların tanımlanmasına gerek yoktur. Projelerin aktarılacağı sistemde bağlantıların tanımlanması yeterlidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/5-%20Deploy%20Management%20Bağlantı%20ve%20Sorguların%20seçilmesi-6e8d31d0-5cbf-42a2-b8f1-a1a155cd01df.png)

Pakete alınmak istenen resim dosyaları seçilerek ilerlenir. Seçim yapılması zorunlu değildir. Örneğin elde edilmek istenen projede resim bulunmuyorsa hiçbir seçim yapılmadan ilerlenir. 

Resim dosyaları eBA Doküman Yönetimi içerisindeki "//Root/system/form images" dizinindekiler arasından seçim yapılabilecek şekilde listelenmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/6-%20Deploy%20Management%20Resim%20seçilmesi-0091209c-24ae-449d-b440-911c443649ec.png)

Pakete alınmak istenen süreçler işaretlenerek ilerlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/7-%20Deploy%20Management%20Proje%20ve%20Çözüm%20seçilmesi-f50d4126-c241-48d0-993a-99c38f59f908.png)

Son seçim olarak pakete alınmak istenen arşivler işaretlenerek ilerlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/8-%20Deploy%20Management%20Arşivlerin%20seçilmesi-3a588891-e44b-4238-9a62-7e5c540687f9.png)

Dışarı aktarılmak üzere yapılan seçimlerin özeti gözden geçirilerek ilerlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/9-%20Deploy%20Management%20Önizlemenin%20görüntülenmesi-48293276-2667-45a1-b30a-fe825c152246.png)

Paket içeriğine dair açıklama girilebilir. Bu açıklama paket içeri aktarılırken ilk aşamada görüntülenebilecektir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/10-%20Deploy%20Management%20Not%20Girilmesi%202-bbda3453-be7b-417a-9219-7858a88b4791.png)

Son olarak Start butonuna tıklanmalıdır!

![](https://docsbimser.blob.core.windows.net/imagecontainer/11-%20Deploy%20Management%20Start-78f2f9fc-f0d9-4d17-bbda-725100a07c14.png)

Paket alma işlemi tamamlandıktan sonra 'Save the package' butonu aktif olur. İlgili buton tıklanarak paket bilgisayara kaydedilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/12-%20Deploy%20Management%20Projenin%20kaydedilmesi-42f7c16b-0480-4701-8317-812b2742c93c.png)

Paketin başarılı kaydedildiğine dair bilgi gösterilmektedir. OK butonu ile mesaj kutusu kapatılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/13-%20Deploy%20Management%20Projenin%20kaydedilmesi%20bilgisi.png-b535e535-8a9b-4c26-bff5-d195c4f5a279.png)

Close butonuna tıklanarak uygulama kapatılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/14-%20Deploy%20Management%20Close-a02d9beb-3237-4a58-8cfd-807aab3e1ac1.png)

## eBA Paketini İçeri Alma

Daha önceden Deploy Management uygulamasıyla elde edilmiş paketi istenilen eBA uygulamasına aktarmak için "Deploy to server" seçeneği seçilerek ilerlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/15-%20Deploy%20Management%20Deploy%20to%20server%20seçimi-98384c34-e05c-4bdb-9908-71c4477ca69c.png)

Paketin içeri aktarılacağı uygulamaya login olunması gerekmektedir, sonrasında işlemlere devam edilebilir. Instance bilgisi seçilerek admin kullanıcı bilgileri ile 'Test Connection' yapılır ve ilerlenerek oturum açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/Deploy%20Management%20Login-ccf43b52-5afb-4da6-8e2f-5c750d2e2524.png)

Filename alanının kenarında bulunan ... butonu ile içeri aktarılacak paket dosyasının seçilmesi sağlanır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/16-%20Deploy%20Paket%20Seçilmesi-f5ce9aba-1269-4708-9cdb-26105d3f1867.png)

Seçilen paketi dışarı aktarırken yazılmış olan not bu aşamada görüntülenerek ilerlenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/16-%20Deploy%20Management%20Not%20Görüntüleme-5613ff85-972f-4e7a-9ad3-b5d075451c98.png)

Bağlantı ve sorgular arasından içeri aktarılmak istenenlerin seçimi yapılarak ilerlenir.

Not: Aktarım sadece sorguları içeri aktarırken, aynı isimde bağlantının tanımlı olması gerekir. İçeri aktarım öncesi, aktarımın sağlanacağı eBA uygulamasındaki Integration Manager içerisinde, aktarım paketinde bulunan bağlantı isminin aynısı olacak şekilde tanımlamaların yapılması gerekmektedir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/18-%20Deploy%20Management%20içeri%20sorgu%20aktarma-4328e3aa-607f-421b-ada6-8361c8cdd5a1.png)

Listelenen süreçler arasından içeri aktarılmak istenenler seçilerek ilerlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/20-%20Deploy%20Management%20proje%20aktarma.-e1d14bc0-3699-40a4-873e-099850fffddd.png)

Listenen arşiv tanımlarından içeri aktarılmak istenenler seçilerek ilerlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/21-%20Deploy%20Management%20arşiv%20aktarma-4bfb7ab8-41fd-48ca-acb6-51af036d0408.png)

İçeri aktarılmak üzere yapılan seçimlerin özeti gözden geçirilerek ilerlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/22%20-%20içeri%20aktarılacak%20özet-7d1acba6-ef2d-4b46-95ef-ddd52b474c08.png)

Son olarak Start butonuna tıklanmalıdır!

![](https://docsbimser.blob.core.windows.net/imagecontainer/start-4e8d38cf-f76b-4b70-942c-adbb5f31e9c5.png)

İçeri aktarım yapılan sistemde, aktarılmak istenenlerden halihazırda aynı isimde tanımlama varsa gerekli tercih yapılarak ilerlenir. 

![](https://docsbimser.blob.core.windows.net/imagecontainer/23%20-%20içeri%20aktarılacak%20dublicate-2431b6e3-2c19-4e6a-b171-472bb62166d3.png)

Paket içeri aktarma işlemi tamamlandıktan sonra 'Close' butonu aktif olur. 
Close butonuna tıklanarak uygulama kapatılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/23%20-%20içeri%20aktarılma%20close-e76ea8dd-1ae3-440a-9e88-b71f289bf34d.png)

## Sunucudan Sunucuya eBA Paketini Aktarma

"Transfer server to server" seçeneği seçilerek ilerlenir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/transfer-0e6f00be-7a44-4dc2-8325-99c1ae7f146e.png)

Kaynak ve Hedef eBA uygulamalarına, paketin dışarı aktarıldığı ve içeri aktarılacağı uygulama olmak üzere login olunması gerekmektedir, sonrasında işlemlere devam edilebilir. Instance bilgileri seçilerek admin kullanıcı bilgileri ile 'Test Connection' yapılır ve ilerlenerek oturum açılır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/Transfer%20Connect-29f389a9-93ff-4b1c-a374-7ce2167879ec.png)

Sonraki adımlar eBA Paketini İçeri Alma başlığındaki adımlar ile birebir aynıdır.

