# Client-Side(İstemci Tarafı) Kodlama
Client-Side kodlama, web geliştirme sürecinde kullanılan bir terimdir. İstemci tarafı, web tarayıcısında çalışan ve kullanıcının cihazında gerçekleşen kodlama ve işlemleri ifade eder. İstemci tarafı kodu, web tarayıcısında çalışan JavaScript, HTML ve CSS gibi web teknolojileri kullanılarak oluşturulur.

Client-Side kodlama sürecinde, web sayfalarının yapısını tanımlamak için HTML kullanılır. Bu şekilde, kullanıcı arayüzünün temel yapısı oluşturulur. Ardından, CSS kullanılarak web sayfalarının görünümü düzenlenir ve biçimlendirilir. CSS, HTML ile birlikte kullanılarak sayfaların tasarımını özelleştirmeye ve görsel olarak etkileyici hale getirmeye olanak tanır.

JavaScript ise istemci tarafında çalışan bir programlama dilidir. Bu dil, etkileşimli web sayfaları oluşturmak, veri doğrulaması yapmak, animasyonlar oluşturmak ve kullanıcı etkileşimlerini yönetmek için kullanılır.
-     Not : TypeScript, JavaScript'in geliştirilmiş bir versiyonudur ve (OOP) Nesneye Dayalı Programlama yapmaya olanak sağlamaktadır. İstemci tarafında JavaScript komutlarının kullanmasında herhangi bir engel bulunmamaktadır.

Client tarafında gerçekleştirilen işlemler için sunucuya sürekli olarak taleplerde bulunmayı gerektirmez. Bu da kullanıcı deneyimini hızlandırır ve sunucu yükünü azaltır. İstemci tarafı kodlama, kullanıcıların web tarayıcılarında işlem yapabilmesini sağlar ve sunucu tarafında gerçekleştirilen işlemleri minimuma indirir.

## Form'lar için Client-Side Kodlama
-   ![](https://docsbimser.blob.core.windows.net/imagecontainer/client-870fab56-b75d-45c0-abff-6fd9108f6e65.png)
1.  Client-Side kodlama yapılacak Form kırılımı açılır.
2.  Client kırılımı açılır.
3.  Yapılacak geliştirme türüne göre .css dosyası veya .ts dosyaları seçilir.
*  ![](https://docsbimser.blob.core.windows.net/imagecontainer/client-c4d9cb9c-d133-4243-84bf-373ae9d2dd04.png)

    *   ## CSS
        *   Form nesnelerine css tanımlanabilmesi için ilgili form'un css dosyasının içeriğine CSS komutları yazılır.
        -     Not1 : CSS'ler tanımlanırken class olarak tanımlanıp, nesneye buna göre atanmalıdır. Element'lere verilen özellikler tüm sistemi etkileyecektir.
        -     Not2 : CSS'ler !important denilerek baskılanmalıdır. Tanımlanan özellikler bir üst div'den alttaki nesneye doğru geleceği için, important denmemesi kendi özelliklerini kullanmaya devam edeceği anlamına gelmektedir.
        - Örnek bir CSS bloğu ve özelliğin nesneye tanımlanması
        ```css
            .myCssClass{
                border: none !important;
                color: aquamarine !important;
                font-size: x-small !important;
                font-family: 'Courier New', Courier, monospace !important;
            }        
        ```
        - Nesnenin Özelliklerinden, Appearance'in altında yer alan ClassName özelliğine, tanımlanmış CSS class name'i verilerek, nesnenin style özelliklerinin, tanımlanan özelliklerden beslenmesi sağlanır.

        - ![](https://docsbimser.blob.core.windows.net/imagecontainer/css-c621e0c3-a163-4051-8daa-2781fa63353c.png)

    * ## TypeScript
        * Kullanıcıların istemci bazında belirli komut kümelerini çalıştırmaya yarayan bir dildir.
        * Örnek bir TypeScript kodu ile bir Synergy nesnesine değer atanması
        ```TypeScript
            async setTextBox1(value:string){
                var firstName = this.session.User.FirstName;
                var lastName = this.session.User.LastName;
                var fullName = firstName + " " + lastName;
                this.tbxFullName.text = fullName;
            }
        ```
        
        

