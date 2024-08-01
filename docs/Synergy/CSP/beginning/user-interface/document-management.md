---
sidebar_label: Doküman Yönetimi
sidebar_position: 2
custom_edit_url: ""
---

# **Doküman Yönetimi**

Doküman Yönetimi, dijitalleşmek amacıyla iş dokümanlarını/dosyalarını ve proje/sistem dosyalarını içerisinde depolamak maksadıysa saklamak, gerektiği alanlarda düzenlenmesine ve görüntülenmesine imkan sağlamak için kullanılan bir belge yönetimi sistemidir.

## **Doküman Yönetimi Arayüzü**

Doküman Yönetimine girişin ilk sayfası, **Doküman Yönetimi Ana Ekran**ıdır. Bu alan dosyaları aramak için bir **Arama** alanı da dahil olmak üzere: Son Kullanılan Dokümanlar, Favoriler, Çalışma Alanları, Aktiviteler ve Depoları görüntüleyebilmek için 7 ayrı parçaya ayrılmıştır.

![Doküman Yönetimi Ana Ekranı](https://docsbimser.blob.core.windows.net/imagecontainer/Doküman%20Yönetimi%20Ana%20Ekran-ef45431b-10cc-434a-9bfd-c14891aaeb3b.png)

### **Depolar Arayüzü**

Temel olarak iki tarafa ayrılan bir kafes/tasarım yapısına sahip olan arayüz; 

- **Sol Kısım:** Son Kullanılan Dokümanlar, Favoriler, Çöp Kutusu, Depolar ve bunların alt kırılımların sahip olan bir ağaç yapısı ile karşımıza gelmektedir.

- **Sağ Kısım:** En üstüne bulunan navigasyon alanında seçilen dosya ve/veya doküman üzerinde **yetkiler dahilinde** yapılabilecek işlemlerlerin olduğu bir alan, arama yapılmasını sağlayan bir alan, listeleme tipini değiştirilebileceği bir alan ve son olarak doküman yönetim panelini kapatılabileceği bir alan olarak **işlemler alanı** görüntülenmekte, bir alt kısmında ise doküman yol bilgilerinin görüntülenebileceği bir **navigasyon alanı**, bunların altında kalan kısımda ise bir depo, klasör ve dosyaların bulunduğu bir **dosyalama alanı** bulunmaktadır.

## **Depolar ve Klasörler**

Depolar, belgelerin tutulduğu kök dizinler olarak nitelendirilir. Klasörler ise içine, dosyaların veya kendi içinde de oluşturulacak yeni klasörlerin belli bir düzene göre konulduğu dosyalama ve dizin yapısıdır.

## **İşlemler Alanı**

Bir depo, klasör veya dosya üzerinde işlem yapmak istenildiği durumda ilgili işlemlerin görüntülenebilmesi için nesnenin üzerine gelinir ve sağ tarafında çıkan *yuvarlak seçim alanı* seçilir veya *sağ tıklayarak açılan pencere*de de nesne üzerinde yapılabilecek işlemler görüntülenir. Aynı zamanda birden fazla nesne üzerinde değişiklik yapmak istenildiği durumda; seçimi istenilen nesnelerin sağ tarafında ki yuvarlak seçim alanlarını işaretlenir ve birden fazla seçim yapılır. Toplu şekilde yapılabilecek işlemler, seçimlere göre filtrelenir ve değişiklikler işlemler alanından veya sağ tıklayarak açılan pencereden yapılır.

![Doküman Yönetimi Ekranı](https://docsbimser.blob.core.windows.net/imagecontainer/Doküman%20Yönetimi%20Ekranı-32f28b68-0ba3-4a94-b46a-19e1e23e2c60.png)


- **Yeni**:
    - **Yeni Depo**: Yeni bir depo oluşturmayı sağlar. Yeni depo sadece _Başlangıç_ dizininde oluşturulabilir.
    - **Yeni Klasör**: Yeni bir klasör oluşturmayı sağlar. Yeni klasör sadece _Başlangıç_ dizini **haricinde** oluşturulabilir.
    - **Yeni Dosya**: Yeni bir dosya oluşturmayı sağlar. Yeni dosya sadece _Başlangıç_ dizini **haricinde** oluşturulabilir.

- **Aç**: 
    - **Karşılaştırma**: İki metin dosyasının birbiriyle karşılaştırmasını sağlar, benzerliklerini ve farklılıklarını listeler.
    - **Özellikler**: Nesne bazlı başlıklar değişken olsa da nesne hakkında Genel, MetaData, Dizin Ayarları, Yeni Dosya başlıkları altında nesne ile ilgili bilgilerin sunulduğu ve ayarlandığı bir alandır.
    - **Güvenlik**: Seçili nesne özelinde görüntülenme, indirme, yazdırma gibi çeşitli yetkileri kişilere veya gruplara özel olarak tanımlama yapılabilmesini sağlayan bir güvenlik sekmesidir.
    - **Profili Göster**: Nesne üzerinde tanımlanmış bir profil formu varsa bunu açar. 
    - **Aktiviteler**: Kullanıcıların nesne üzerinde bir mesaj yayınlamasını ve yayınladıkları mesajları veya nesne üzerinde yaptıkları işlemleri görüntülenmesini sağlayan bir panel ekranı getirir.
- **İşlemler**: 
    - **Favorilere Ekle**: Favoriler alanında görüntülenmek üzere nesneyi pinler.
    - **Kopyala**: Seçilen nesneyi çoğaltır.
    - **Taşı**: Seçilen nesneyi başka bir dizine taşır.
    - **İndekslemeyi Yenile**: Aramalarda daha hızlı sonuçlar sağlanabilmesi için içeriği işleyerek sistem hafızasında tutar.
    - **Yeniden Adlandır**: Nesneye yeni bir isim verilmesini sağlar.
    - **Sil**: Nesneyi bulunduğu dizinden siler.
    - **Dijital İmza**: Nesne üzerinde bir dijital imza varsa bunu gösterir ve/veya imzalar.
- **Paylaş**: 
    - **İndir**: Seçili nesneyi bilgisayara indirmek üzere işlem başlatır.
    - **Paylaş**: Seçili dosyayı bağlantı olarak veya mail eki olarak paylaşımını sağlar. Paylaşım olanakları ve sınırları bu alandan düzenlenir. 
    - **Abonelik**: Depolar ve klasörler için oluşturulan ve/veya silinen dosyalar için bir haber alma sistemidir.
- **Rapor**: 
    - **Tarihçe**: Nesne üzerinde yapılan değişikliklere dair geçmişin görüntülenmesi adına bir panel açar.
- **Panoya Ekle**: Farklı depo veya klasörde bulunan, klasörleri veya dosyaları bir havuza toplar; o an bulunulan *-işlem yapılması istenen-* dizine, kopyalama veya taşıma işlemini sağlar. Panoya ekleme yapılabilmesi için klasör veya dosya üzerinde sağ tıklanır ve açılan menüden **Panoye Ekle** butonuna basarak panoya ekleme işlemi yapılır. Panoya bir klasör veya dosya eklendiğinde işlemler alanında **Pano** isimli alan görünür hale gelir. Kopyalanması veya taşınması istenilen klasör, doküman yönetiminde açılır ve işlem alanlarında görünür hale gelmiş olan Pano butonuna tıklanır, açılan listede yapılan seçimler sonucunda belirtilen kopyalama veya taşıma işlemi gerçekleşir.  
- **Kısayol**: Klasör ve dosya için bulunulan dizine bir kısayol nesnesi oluşturulur. Bu nesne görüntülenmeye çalışıldığında doğrudan olarak ana nesne açılır. Kısayol nesnesi, panoya eklenebilir, taşınabilir, kopyalanabilir, yeniden adlandırılabilir veya silinebilir. Bu değişiklikler ana nesneyi etkilemeyecektir. Kısayol nesnesi kullanılarak görüntülenen dosyalar için üzerinde bir değişiklik yapılmak istenildiğinde sistem bu değişikliklere onay vermeyecektir.


