# SSL SERTİFİKASI AKTİF ETMEK İÇİN İŞLEM ADIMLARI

## Müşteriden beklenen işlemler:

1.	SSL Sertifakasını temin etmeleri.
2.	SSL Sertifikasını sunucuda IIS’e yüklenmesi.
3.	DNS tanımlarınının yapılması ve IP yönlendirmeleri.
4.	Domain adresini  Bimsere iletilmesi.


## Bimserin yapması gereken işlemler:

1.	SSL Sertifikası IIS’e yüklendiğini Server Certificate den kontrol etmek.

![](https://docsbimser.blob.core.windows.net/imagecontainer/IIS-b6f50ed5-97fa-4129-ba89-9702afc48dc9.png)

2.	SSL aktif edebilmek için aşağıdaki görselde görüldüğü üzere Default Web Site gelip Edit Site dan Bindings’e tıkalayıp açılan pencereden add butonuna tıkladıktan sonra Type checkboxsından https’i seçemeniz gerekmektedir. Host name yazan Textbox’a müşterimizin bize ilettiği Domain adresini yazılmadı gerekmektedir ve sonrasında SSL certificate kısmından müşterinin yüklemiş olduğu SSL Sertifikası seçilmelidir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/IIS2-bcb66b84-e5d6-4c1d-96ef-b70d0968e1e7.png)

3.	Aşağıdaki görselde 2 adresinde https olarak düzenlenmesi gerekmektedir. Örnek olması gerekirse
https://....................  -  https://..................../eba.net  boş bırakılan yere yukarıda IIS’te host name kısmına yazmış olduğumuz müşterimizin bize ilettiği domain adresi gelmektedir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAConfıgurationEditör-c4708127-5d06-4059-9d7e-e994ac7f4f6f.png)

Aşağa ilettiğimiz görsellerde de adresler https ile yazılmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBACONFİG-e2c0832f-8184-473f-84f6-ea8e5773ed29.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBACon-a905f72e-cdc4-4658-9535-794dfc26d3b7.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/ebaHTTPS-9168df76-7673-4c15-8f39-6dd454700d15.png)

4.	Müşterimizin mobil modülüde var ise aşağıda ilettiğim görseldeki adresinde değişmesi gerekmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAhttpsaktif-fb8915ed-1ab4-4b7d-a6d4-6ead01ef640d.png)

5.	Müşterimizin Viewer’ı var ise BimserViewer içindeki web.config dosyasının ve BimserViewer’ın içinde service klasörü altındaki web.configin SSL’li web configlerle değişmesi gerekmektedir. Sonrasında ise bu web.condiflerin içindeki adreslerin düzenlenmesi gerekmektedir.

