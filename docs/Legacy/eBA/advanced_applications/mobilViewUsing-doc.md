# eBA Mobil View Kullanımı
Bu doküman eBA mobil uygulamasında süreç formlarının mobile özel nasıl tasarlanabileceğini anlatmaktadır.

## Kullanım 
eBA Workflow Studioda formumuzun **default** view'ı üzerinden web için görünümünü tasarladıktan sonra bu form görüntüsünün mobil uygulamada farklı bir şekilde gözükebilmesi için bu forma yeni bir **view** daha ekliyoruz.

**Default View Görünümü**

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAMobileView1-9ff76100-7d73-42c9-bb98-50235080278d.png)

Mobil View eklemek için formumuza sağ tıklayıp **Views > New View** seçeneğini kullanıyoruz.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAMobileView2-ad3a5809-8d20-4c08-a61e-08f826de2de8.png)

Ardından açılan popup ekranında view'ın adını giriyoruz, istediğiniz herhangi bir ad verilebilir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAMobileView3-b2fd2bc7-4dc2-4d3b-a3c5-efd940cc3c5f.png)

Bu kısımdan sonra artık bu yeni oluşturduğumuz view'in mobil uygulamada nasıl görüneceğini ayarlıyoruz.

**Mobil View Görünümü**

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAMobileView8-d36b8082-909a-4153-b842-6fc208475ce4.png)

Formumuzun web ve mobil uygulamada nasıl gözükeceğini ayarladık bundan sonra eklemiş olduğumuz **defaultMobile** view'ını **default** view'ın mobil view'ı olarak ayarlamak gerekiyor. Bunu yapabilmek için forma sağ tıklayıp **Form Properties'e** girdikten sonra açılan modal' üzerinde **Views** tabına gidip buradan **default view'ın mobile view değerini** yeni eklediğimiz **defaultMobile** view'ının adıyla değiştiriyoruz.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAMobileView5-a06b8585-d2f5-447c-b1d3-05991674400c.png)
![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAMobileView6-df3ae60b-5258-4928-8194-a62de04a683c.png)

Bu kısmın ardından sürecimizi derleyip web arayüzünden menümüze ekliyoruz. Daha sonra sürecimizin web ve mobil uygulamadaki görünümleri aşağıdaki gibi olacaktır.

**Web**

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAMobileView7-ce26e15d-8a5e-4ead-89d1-def855b2fc3f.png)

**Mobil**

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAMobileView9-afa39e7d-5745-4353-ba05-fa1935446e5b.png)