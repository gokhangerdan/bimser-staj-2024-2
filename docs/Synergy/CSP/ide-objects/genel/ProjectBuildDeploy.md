# Proje Derleme ve Yayınlama
Geliştirilen projelerde Client yada Server olaylarında hata olup olmadığını tespit edebilmek ve eğer varsa hatanın hangi olay sırasında, hangi satırda olduğunu yakalayabilmek için projelerin derlenmesi gerekir.

Geliştirilen projelerin çalışan bir uygulama haline gelebilmesi ve uç kullanıcıların kullanımına açılabilmesi için de projelerin başarılı bir şekilde yayınlanması gerekmektedir.

Derleme ve Yayınlama işlemleri geliştirme arayüzünde Menü yapısındaki **Çalıştır** başlığı altından ya da proje üzerinde sağ tıklandığında açılan pencereden gerçekleştirilebilmektedir.

![ustmenuderleyayinla](https://docsbimser.blob.core.windows.net/imagecontainer/%C3%9CstMen%C3%BC%C3%87al%C4%B1%C5%9Ft%C4%B1rDerleYay%C4%B1nla-f61965cc-b3aa-44f1-ad49-c82f77d5f36b.png)


![deploytest](https://docsbimser.blob.core.windows.net/imagecontainer/%C4%B0stemciveSunucuDerleme-13a5785f-cf51-4b91-85f0-7bc2f513ccb4.png)

Proje geliştirme adımları arasında, o ana kadarki geliştirmede herhangi bir hata olup olmadığı, proje derlendiğinde Çıktı paneline düşen işlem detaylarıyla kontrol edilir. 
Sadece Client tarafında yazılan kodlar için bir derleme işlemi yapılmak isteniyorsa **İstemciyi Derle** alanına tıklanır ve çıktı panelinde istemci kodlarında yapılan hatalar listelenir.
![client_hata](https://docsbimser.blob.core.windows.net/imagecontainer/client_hata-c1349391-6dec-4dce-a3fd-51ecc2051574.png)

Sadece Server tarafında yazılan kodlar için bir derleme işlemi yapılmak isteniyorsa **Sunucuyu Derle** alanına tıklanır ve çıktı panelinde hem formun Server tarafında yazılan kodlarda hem de Akış tarafında yazılan C# kodlarında yapılan hatalar listelenir.
![server_hata](https://docsbimser.blob.core.windows.net/imagecontainer/ServerDerlemeHata-d020defc-1962-4a1a-8e63-d4815d28c1a8.png)

**Projeyi Derle** alanına tıklanarak da hem istemci hem de sunucu tarafında yazılan kodlardaki hatalar çıktı panelinde gösterilir.
![proje-derleme-hata](https://docsbimser.blob.core.windows.net/imagecontainer/ProjeyiDerleHATA-bbd14cc4-8f8c-4cb6-a5e5-94cacdf8e304.png)

Derleme çıktısında **“Başarılı”** mesajı göründüğünde, proje, yayınlanmaya hazır bir paket haline gelmiş demektir.
![derleme-basarili](https://docsbimser.blob.core.windows.net/imagecontainer/DerlemeBa%C5%9Far%C4%B1l%C4%B1-3704c459-383e-4459-9a84-8a12f7cbb1a7.png)

Yayınlama işlemi gerçekleştirildiğinde de yine aynı şekilde client ve server tarafındaki hatalar çıktı panelinde listelenir, **"Başarılı"** mesajı göründüğünde ise artık geliştirilen proje kullanıma hazır hale gelmiş olur.
![deploy-error](https://docsbimser.blob.core.windows.net/imagecontainer/DeployClientServerHata-bb6f35fd-dca6-45cd-9926-5cb06fb680cb.png)

![deploy-success](https://docsbimser.blob.core.windows.net/imagecontainer/ProjeDeployBa%C5%9Far%C4%B1l%C4%B1-21198663-278b-456c-abb9-bec1e0c4458b.png)
