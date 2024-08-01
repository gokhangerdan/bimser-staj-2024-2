# Custom Style

Bu geliştirme kullanıcıların eBA arayüzüne müdahale edebilmelerini, görsel açıdan

kendilerine uygun hale getirebilmelerini sağlamaya yardımcı olan bir modüldür. Öncelikle

yapılması gereken Doküman Yönetimi içerisinde "system" klasörü altında "customstyle"

isminde klasör olmalıdır, eğer yoksa oluşturulması gerekmektedir. Bu klasörün içerisinde ise

customstyle.css dosyası olmalıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/1-0d48df2d-e894-4c44-85a8-c13bd29064a0.png)

Değiştirilmek istenen öge’ye F12 veya sağ tıklayıp “**incele**” dedikten sonra seçeceğimiz

class veya id adını kullanarak “new style rule” (sağ alttaki artı işaretine tıklayarak) vererek

css kodları girilebilir. Örneğin arka plan rengini değiştirmek için;

## .**topMenuWrapper** {

background: red;

}

![](https://docsbimser.blob.core.windows.net/imagecontainer/2-b056fd77-52bd-40c4-88e9-9dae2579c398.png)

Yapacağımız değişiklikler bittikten sonra customstyle.css dosyası yeniden

system/customstyle/ dizinine atılması gerekmektedir. Dosya atıldıktan sonra ise eBA

servisleri yeniden başlatılır ve böylece değişiklik yansımış olur.

![](https://docsbimser.blob.core.windows.net/imagecontainer/3-43dc50c6-e396-4c4a-8382-23405a11ea08.png)

Bununla beraber aşağıda bazı css örnekleri bulunmaktadır.

## **Background Rengini Değiştirme:**

.element {

width: 200px;

height: 200px;

background-color: red;

transition: background-color 0.3s ease;

}

.element:hover {

background-color: green;

}

## **Hover ile Display None:**

.item {

width: 100px;

height: 100px;

background-color: blue;

transition: all 0.3s ease;

}

.item:hover {

display: none;

}

## **Image Belirleme**

Bu özellik, bir image elementine istediğimiz bir resmi koymamızı sağlıyor.

.image {

content: url('desktop/uploads/image1.png');

height: 350px;

width: 400px;

margin: 1rem;

}

## **Flexbox (Esnek Kutu Modeli):**

Flexbox, web sayfalarında düzen oluşturmak için kullanılan bir CSS özelliğidir. Elementleri

bir konteyner içinde esnek bir şekilde düzenlemek için kullanılır.

.container {

display: flex;

justify-content: center;

align-items: center;

}

## **Gradient (Renk Geçişleri):**

Gradient, bir elementin arka planında renkler arasında yumuşak bir geçiş oluşturmak için

kullanılır.

.gradient-background {

background: linear-gradient(to right, #ff0000, #00ff00);

}
