# Windows Kurulumu
Bu makale ile birlikte Bimser Synergy Capture uygulamasını bilgisayarınıza nasıl kurabileceğinizi öğreniyor olacaksınız.

## Gereksinimler
Bimser Synergy Capture uygulamasının geliştirme aşamasında, siz değerli müşterilerimizin olabildiğince kolay bir kurulum yapabilmesi için ekstra çaba sarf ettik. Bundan dolayı uygulamayı kurmak veya kullanmak için ekstra bir kurulum yapmanıza gerek yoktur. Yalnız, uygulamamız ile birlikte **ABBYY FineReader Engine**'i kullanma gayesindeyseniz sizden almamız gereken bir adet bilgi var.
1. ABBYY FineReader Engine DLL klasörü
    > **NOT:** Bu klasörün **FREngine.dll** dosyasını içermesi gerekmektedir.

Bu bilgiyi nereye gireceğiniz konusuna makalenin devamında değiniyor olacağız. Şimdilik bu bilgiye erişmeniz yeterli olacaktır.

## Capture'ın Kullanıcı Bazında Aktif Edilmesi
Aşağıda yer alan adımları izleyerek Capture kullanımını aktif edebilirsiniz.

1. Arayüzün sağ üstünde bulunan "Yönetim Araçları" butonuna basın.

  <img src="https://docsbimser.blob.core.windows.net/imagecontainer/asd-7b2ccc13-fa94-48a6-b074-c10c0e494b09.png" style={{padding: "8px", border: "1px solid #DADDE1", backgroundColor: "#cccccc"}} />
2. "Güvenlik" butonuna basın.

  <img src="https://docsbimser.blob.core.windows.net/imagecontainer/aa-661c2eaa-f4b5-46df-9417-4e4102a1fc7f.png" style={{padding: "8px", border: "1px solid #DADDE1", backgroundColor: "#cccccc"}} />
3. Üst tarafta izinler tabına gelip soldan istediğiniz kullanıcı grubunu seçin.

  <img src="https://docsbimser.blob.core.windows.net/imagecontainer/a-49a4f03b-1f1e-4ad2-bed7-de403c5eafa2.png" style={{padding: "8px", border: "1px solid #DADDE1", backgroundColor: "#cccccc"}} />
4. Sırasıyla "Döküman Yönetim Sistemi" ve "Capture" alanlarını genişletin.
  
  <img src="https://docsbimser.blob.core.windows.net/imagecontainer/asd-043aa67c-a265-4cad-a3a9-bae95d0d53de.png" style={{padding: "8px", border: "1px solid #DADDE1", backgroundColor: "#cccccc"}} />

Açtığınız penceredeki seçenekleri kullanarak gerekli ayarları yapabilirsiniz. Bu ayarı dilediğiniz kullanıcı veya kullanıcı grubu için güncelleyebilirsiniz.


## Synergy Capture Uygulamasının Kurulumu
1. CSP Arayüzü üzerinden **Döküman Yönetimi** modülüne gidin.
2. Taranan verilerin yükleneceği depoya gidin. 
3. Yüklemenin yapılacağı klasörü belirleyin.
4. "Yeni" butonuna basın.

  <img src="https://docsbimser.blob.core.windows.net/imagecontainer/kullanim1-b39bfcce-4ee5-4048-9925-28fc0c72a714.png" style={{padding: "8px", border: "1px solid #DADDE1", backgroundColor: "#cccccc"}} />
5. "Yeni Dosya" butonuna basın.
  
  <img src="https://docsbimser.blob.core.windows.net/imagecontainer/kullanim2-af559fa0-0e05-47e0-8dd1-f3467109d5a3.png" style={{padding: "8px", border: "1px solid #DADDE1", backgroundColor: "#cccccc"}} />
6. "Tara" butonuna basın.
  
  <img src="https://docsbimser.blob.core.windows.net/imagecontainer/kullanim3-fe113232-cde9-4adb-9663-b215ac158a4d.png" style={{padding: "8px", border: "1px solid #DADDE1", backgroundColor: "#cccccc"}} />
7. Karşınıza gelen hata mesajında yer alan bağlantıyı kullanarak uygulamayı indirin.

  <img src="https://docsbimser.blob.core.windows.net/imagecontainer/a-ab6b7718-6db4-4151-a83d-eea667859eaf.png" style={{padding: "8px", border: "1px solid #DADDE1", backgroundColor: "#cccccc"}} />
8. İndirmiş olduğunuz **CaptureInstaller.msi** dosyasını açın ve "İleri" butonuna basın.

    |![](https://docsbimser.blob.core.windows.net/imagecontainer/setup-page-1-6c6bd146-247b-4e96-bd34-809f24a618af.png)|
    |:--:|
    |*Bilgisayarınızdaki boş alanı kontrol ediyor.*|

    |![](https://docsbimser.blob.core.windows.net/imagecontainer/setup-page-2-071d9698-ebba-437b-b49f-582a270ac538.png)|
    |:--:|
    |*Kurulum başlangıç aşaması.*|
9. Lisansı okuyup, kabul edip "İleri" butonuna basın.

    |![](https://docsbimser.blob.core.windows.net/imagecontainer/setup-page-3-e36a06d0-d3da-499a-8838-6cddb4ddf850.png)|
    |:--:|
    |*Kullanım sözleşmesinin kabul aşaması.*|
10. Kurulum klasörünü belirleyip "İleri" butonuna basın.

    |![](https://docsbimser.blob.core.windows.net/imagecontainer/setup-page-4-e96aeffe-8737-4617-8f5f-8bd68a49af49.png)|
    |:--:|
    |*Kurulum yerinin belirlenme aşaması.*|
    > **NOT:** **Bimser Synergy Capture** uygulaması, güvenlik durumlarından ötürü bilgisayarda yer alan her kullanıcı için özel olmalıdır. Bunu sağlamanın yöntemlerinden biri ise kurulum klasörünün konumudur. Kurulum klasörü, kurulumu yaptığınız kullanıcı için ayrılmış klasör içerisinde yer almalıdır. Varsayılan olarak seçilmiş klasör konumu ile devam etmenizi tavsiye ederiz.
11. Kullanılacak olan portu belirleyip "İleri" butonuna basın.

    |![](https://docsbimser.blob.core.windows.net/imagecontainer/setup-page-5-54bc5315-5d1b-45b7-b360-e250b8cee240.png)|
    |:--:|
    |*Uygulamanın kullanacağı portu belirleme aşaması.*|

    |![](https://docsbimser.blob.core.windows.net/imagecontainer/setup-page-6-3b1b2b1a-7d1e-4284-bc64-c888d9440290.png)|
    |:--:|
    |*Manuel port belirleme işlemi.*|
    
    |![](https://docsbimser.blob.core.windows.net/imagecontainer/setup-page-7-1b0c69c0-70a5-4402-be56-c06bf7c0b8a8.png)|
    |:--:|
    |*Belirlenen portun kullanılıyor olması durumu.*|
12. ABBYY kullanım durumunu belirleyip "İleri" butonuna basın.

    |![](https://docsbimser.blob.core.windows.net/imagecontainer/setup-page-8-b7ac35f9-2946-453e-9548-424889b2108e.png)|
    |:--:|
    |*ABBYY FineReader Engine kullanımının belirlenmesi aşaması.*|

    |![](https://docsbimser.blob.core.windows.net/imagecontainer/setup-page-9-e8091e30-c33f-4935-9cfd-519c4fdf6306.png)|
    |:--:|
    |*ABBYY FineReader Engine'e sahipseniz istenen bilgileri girin.*|
    
    |![](https://docsbimser.blob.core.windows.net/imagecontainer/setup-page-10-eb2a9925-7e00-462b-8df0-ff837e76a3cd.png)|
    |:--:|
    |*ABBYY DLL Klasörü bilgisinin yanlış girilmesi durumu.*|
13. "Yükle" butonuna basın.

    |![](https://docsbimser.blob.core.windows.net/imagecontainer/setup-page-12-ce8dfcaf-011a-4142-86d9-abe02f1eabd7.png)|
    |:--:|
    |*Uygulama kurulumunun başlatılma aşaması.*|

Yukarıdaki aşamaları tamamladıktan sonra karşınıza bir yüklenme ekranı gelecek. Bu ekrandaki işlemler birkaç dakika sürebilir. Yüklenme tamamlandıktan sonra pencereyi kapatıp aşağıda yer alan adımlara geçebilirsiniz.

## Kurulum Sonrasında Gerçekleşen Eylemler
Eğer **Bimser Synergy Capture** uygulaması kurulumu başarıyla tamamlandıysa, aşağıdaki eylemler otomatik olarak sizin adınıza gerçekleşir.
### 1. Uygulama Otomatik Olarak Başlatılır
**Bimser Synergy Capture** uygulamasını hemen kullanabilmeniz adına bu işlemi gerçekleştirmekteyiz.
### 2. Masaüstüne ve Arama Menüsüne Kısayollar Eklenir
Uygulamayı kapatıp tekrardan başlatmak istediğinizde zorlanmamanız adına gerekli kısayollar bilgisayarınıza eklenir. Gerek masaüstüne koyduğumuz kısayol üzerinden gerek arama yaparak **Bimser Synergy Capture** uygulamasını başlatabilirsiniz.
### 3. Bilgisayarınızın Başlatma Menüsüne Ekleme Yapılır
Bilgisayarınızı her başlattığınızda **Bimser Synergy Capture** uygulamasını çalıştırma zorunluluğunuzu ortadan kaldırmak adına bu eklemeyi sizin adınıza gerçekleştirmekteyiz.

## Synergy Capture Uygulaması Kurulumunun Doğrulanması
### 1. Uygulamanın Başladığının Kontrol Edilmesi
**Bimser Synergy Capture** uygulaması kurulumdan sonra otomatik olarak başlamış olmalıdır.Bu durumu aşağıdaki adımlarla kontrol edebilirsiniz.
1. Bilgisayarınızın sağ altında yer alan iconları kontrol edin. Bu alanda aşağıdaki gibi bir icon görmeniz gerekmektedir.

    |![](https://docsbimser.blob.core.windows.net/imagecontainer/icon-5a449380-219e-4c4e-bd46-4fa3f1408733.png)|
    |:--:|
    |*Uygulama iconu*|
2. Eğer bu iconu göremediyseniz. Aşağıda işaret ettiğimiz butona basmayı deneyebilirsiniz.

    |![](https://docsbimser.blob.core.windows.net/imagecontainer/setup-page-19-f358258a-bf50-4d1e-8142-be2fad1ee90a.png)|
    |:--:|
    |*Gizli iconların görünmesini sağlar*|
### 2. Yerel API Sunucu Kontrolü
**Bimser Synergy Capture** uygulamasının, sizin yerel bilgisayarınızda çalışmak üzere bir API sunucunu başlatmış olması gerekmektedir. Bu durumu aşağıdaki adımlarla kontrol edebilirsiniz.
1. Aşağıda yer alan formatı kullanarak bir link oluşturup, bu linki tarayıcınızda açın.
    > **Format:** http://localhost:{BELIRLEDIGINIZ_PORT}/scanner/devices

    Örneğin portu varsayılan olarak bıraktıysanız,
    > http://localhost:7112/scanner/devices

    adresini tarayıcınızda açmalısınız.
2. Oluşturmuş olduğunuz linki tarayıcınızda açtığınızda karşınıza aşağıdaki gibi bir ekran gelmelidir.

    ![](https://docsbimser.blob.core.windows.net/imagecontainer/setup-page-18-d7788111-a6d6-4bd4-8e35-c279a4c965bb.png)
    > **NOT:** Bilgisayara takılı olan herhangi bir tarayıcınız yoksa bu sayfa içerisindeki metin "[]" şeklinde olacaktır.
### 3. Regedit Kontrolü (Opsiyonel)
**Bimser Synergy Capture** uygulamasının çalışabilmesi için gerekli olan ayarlar, kurulum aşamasında Registry alanına kayıt edilmektedir. Bu alanların doğru bir şekilde kayıt edilip edilmediği aşağıdaki adımlarla kontrol edilebilir.
1. Windows + R kombinasyonunu kullanarak aşağıdaki pencereyi açın.

    ![](https://docsbimser.blob.core.windows.net/imagecontainer/setup-page-13-ea3a517a-0083-4b03-a8ac-8136b443831b.png)
2. Open kısmına "regedit" yazıp "Ok" butonuna basın.

    ![](https://docsbimser.blob.core.windows.net/imagecontainer/setup-page-14-4727517c-19f6-4e9f-aa63-6bcb71650a96.png)
3. Açılan pencerede yer alan "HKEY_CURRENT_USER" klasörünü açın.

    ![](https://docsbimser.blob.core.windows.net/imagecontainer/setup-page-15-1847b730-ab53-47b5-ae1b-3413f34318ca.png)
4. "Software" klasörünü açın.

    ![](https://docsbimser.blob.core.windows.net/imagecontainer/setup-page-16-cb14ceab-34a9-406f-8ef9-aea5a28ff3d2.png)
5. "BimserSynergy" klasörünü açıp altında yer alan "Capture" klasörüne tıklayın.

    ![](https://docsbimser.blob.core.windows.net/imagecontainer/setup-page-17-210c110c-6278-4f7a-8e7e-3394ae94e739.png)
6. Pencerenin sağında açılan alanların yukarıdaki fotoğraf ile eşleştiğine emin olun.
    > **NOT:** Data sütununda eşleşmeyen alanlar gördüyseniz problem değil. Bu sütun, kurulum aşamasında sağlamış olduğunuz bilgiler ile şekillenmektedir. Dolayısıyla kurulumdan kuruluma değişiklik gösterebilir.