# Depo
Depolar, belgelerin tutulduğu kök dizinler olarak nitelendirilir. Klasörler ve belgeler Depolar altında oluşturulur.
Bir depo üzerinde işlem yapılması istenildiği durumda ilgili işlemlerin görüntülenebilmesi için deponun üzerine gelinir ve sağ tarafında çıkan yuvarlak _seçim alanı_ seçilir veya  _sağ tıklayarak açılan pencerede_ de nesne üzerinde yapılabilecek işlemler görüntülenir. Aynı zamanda birden fazla nesne üzerinde değişiklik yapmak istenildiği durumda; seçimi istenilen depoların sağ tarafındaki yuvarlak seçim alanlarını işaretlenir ve birden fazla deponun seçimi yapılır. Toplu şekilde yapılabilecek işlemler, seçimlere göre filtrelenir ve değişiklikler işlemler alanından veya sağ tıklayarak açılan pencereden yapılır.

![depo](https://docsbimser.blob.core.windows.net/imagecontainer/Depo-a7387fec-0d3b-4600-966b-bc2b03fc9096.png)

- **Yeni**:

   - **Yeni Depo**: Yeni bir depo oluşturmayı sağlar. Yeni depo sadece  _Başlangıç_  dizininde oluşturulabilir. Açılan pencerede oluşturulacak Deponun Adı ve Açıklaması sistemde mevcut dillerde her biri için özel olarak tanımlanabilmektedir.
   ![YeniDepo](https://docsbimser.blob.core.windows.net/imagecontainer/YeniDepo-a4c38d94-ccdb-43ad-9d42-3d2577862e1f.png)

-   **Aç**:
    -   **Özellikler**: Nesne bazlı başlıklar değişken olsa da nesne hakkında _Genel, MetaData, Dizin Ayarları, Yeni Dosya_ başlıkları altında nesne ile ilgili bilgilerin sunulduğu ve ayarlandığı bir alandır.
        -   **Genel**: İlgili depoya ait **Etiketler** tanımlanabilir ve bu etiketler aracılığıyla istenilen etiketteki nesneler filtrelenerek arama sağlanabilir. Tablo görünümünde etikete göre filtreleme yapılabilir.
            -   **İzin Verilen Dosya Tipleri**: Listenen tiplerdeki dosyalardan seçim yapılarak ilgili depoya eklenebilecek dosyalar sınırlandırılabilir.
            - **Maksimum Dosya Boyutu**: Depoya eklenecek dosyaların herbiri için maksimum dosya boyutunun ayarlandığı alandır.
  ![depogenel](https://docsbimser.blob.core.windows.net/imagecontainer/DepoGenel-b2ed4800-2a58-4229-bdf0-017c803abeba.png)
 
        -  **MetaData**: Depoya herhangi bir klasör ya da dosya ekleneceği zaman istenen profil formunun tanımlandığı alandır.
           - **Profiller**: Tabloda bulunan **+** butonuna tıklanarak bir profil formunun eklendiği alandır. Proje seçimi yapıldıktan sonra ilgili projede bulunan Metadata tipli formlardan biri seçilir. Eğer bir profil formu doldurulması zorunlu olacaksa **Gerekli** alanı aktif edilir. **Tip** alanından da dosya, klasör ya da her iki nesne için de ekleme yapılacağı zaman profil formu açılması sağlanmış olur.
            - **Alanlar**: Seçilen Formdaki alanlardan hangilerinin ilgili deponun tablo görünümünde, bir kolon olarak oluşturulacağının seçildiği alandır.
 ![depoMetadata](https://docsbimser.blob.core.windows.net/imagecontainer/DepoMetaData-af7d33c8-b3aa-4d1d-b6c2-28172373674f.png)
Depoya bir dosya eklenmek istediğinde eklenen dosya seçimi yapılır ve MetaData alanından belirlenen profil formu doldurularak kaydedilmesi sağlanır.
![profilformueklerken](https://docsbimser.blob.core.windows.net/imagecontainer/DepoProfilFormuEklerken-268af26e-b57c-431c-9099-dea272382e37.png)

             Profil formunda seçilen alanlar, profil formu eklenen deponun **Tablo Görünümü** modunda görünür olur. Bu sayede klasör ya da dosyalara eklenen profil formu alanları görüntülenebilmiş olur ve bu alanlar üzerinden filtreleme yapılabilir. ![alanlar](https://docsbimser.blob.core.windows.net/imagecontainer/tablogorunumualanlar-8a67d321-4e99-43c0-85d1-9b5d24702782.png)

        -   **Dizin Ayarları**:  Csp Döküman Yönetimi, sizlere dosyalarınız üzerinden ocr yapmaya olanak tanıyor. Depo ya da klasörünüzün Dizin Ayarları menüsünden ayarlama yaparak, yüklediğiniz dosyaların içeriğini düz yazı olarak alabilir ve sisteme kaydebilirsiniz. Ardından Döküman Yönetimi arama ekranından tüm metin arama işlemi gerçekleştirebilirsiniz. Dosyanız içinde bulunan tek bir ibareyi aratarak, ilgili ibarenin içinde geçtiği tüm dosyalara erişebilirsiniz.
 Dizin ayarları menüsünden öncelikle varsa Üst Dizinden Al kutucuğunun işaretini kaldırmanız gerekiyor. (Üst Dizinden Al işaretinin ne olduğuna sayfa sonunda değineceğiz.) "Dosya Tipi" kısmından hangi dosya tiplerinde tüm metin arama yapmak isterseniz seçmelisiniz. İşlemci yapılandırmasından da hangi işlemciyi(OCR engine) kullanmak isterseniz seçmelisiniz. Ardından Ok butonuna tıklayın. Birden fazla kayıt girebilirsiniz.
 Not: OCR Engine yapılandırması için kurulum ve DB konfigürasyonlarının yapılması gerekmektedir.
 Ocr işlemi ile beraber yüklenen dosyalara otomatik yapay zeka destekli kategori belirleme işlemi de yapılmaktadır.
 Not: MetaData ve Dizin Ayarları menüleri üzerindeki işlemleriniz varsayılan olarak alt dizinlerde de geçerlidir. "Üst Dizinden Al" sayesinden alt dizinlerde bu ayarlamalarınızı tekrar yapma zahmetine girmenize gerek yoktur. Alt dizinlerde farklı ayar yapmak isterseniz "Üst Dizinden Al" kutucuğunun işaretini kaldırmanız yeterlidir.![dizinAyarlari](https://docsbimser.blob.core.windows.net/imagecontainer/DizinAyarlari-de26f104-05a8-43af-94d5-f85ebc8b145b.png)
![dizinIslemci](https://docsbimser.blob.core.windows.net/imagecontainer/DizinAyarlari%C4%B0slemci-7129d12f-f839-4793-8267-82ac55281119.png)
           -   **Yeni Dosya**: Depo'ya yeni bir dosya eklendiğinde otomatik olarak başlaması gereken bir sürecin tanımlandığı alandır. Proje ve Akış seçilir, seçilen akış dosya eklendiğinde otomatik olarak başlamış olur. Not: Akışınızın aşağıdaki değişkenlere sahip olması gerekmektedir.
			```StartedFrom (string),  CreatedFileId (long), CreatedFilePath (string)```
			
				![DepoYeniDosya](https://docsbimser.blob.core.windows.net/imagecontainer/DepoYeniDosya-e7c059ec-8e3b-4122-a53c-64854ee6a484.png)

        -  **Ayrıntılar**:  Depoda bulunan dosya, klasör ve içerik sayısının sunulduğu alandır. Hesapla butonuna tıklandığında da deponun toplam boyutu hesaplanmaktadır. 	
![depoAyrintilar](https://docsbimser.blob.core.windows.net/imagecontainer/DepoAyr%C4%B1nt%C4%B1lar-edfbc83d-a48d-4fe9-b09c-dcdd8f8d2d32.png)

    -   **Güvenlik**: Depo özelinde görüntülenme, indirme, yazdırma gibi çeşitli yetkileri organizasyon içerisindeki kişilere (kullanıcılar,kullanıcı grupları, güvenlik grupları vb. gibi)  özel olarak tanımlama yapılabilmesini sağlayan bir güvenlik sekmesidir. 
Sol taraftaki arama çubuğuna nesneye bağlanacak grup yazılır ve seçilir. Seçilen grup için Nesne üzerinde görüntüleme, düzenleme kırılımları ve tüm alt kırılımlarındaki yetkiler, **_Grubu Nesneye Bağla_** butonuna tıklanarak tanımlanmış olur. Daha sonra yapılan değişiklikler, **_Değişiklikleri Kaydet_** butonuna tıklanarak kaydedilmiş olur.
![depoGuvenlik](https://docsbimser.blob.core.windows.net/imagecontainer/DepoGuvenlik-519c09f3-7365-496f-a594-8e6acb578554.png)
 
     -   **Profili Göster**: Depo üzerinde tanımlanmış bir profil formu varsa buradan açılır ve düzenlenir.
    -   **Aktiviteler**: Kullanıcıların nesne üzerinde bir mesaj yayınlamasını ve yayınladıkları mesajları veya nesne üzerinde yaptıkları işlemleri görüntülenmesini sağlayan bir panel ekranı getirir.
    ![depoAktiviteler](https://docsbimser.blob.core.windows.net/imagecontainer/DepoAktiviteler-be157293-27f6-4f54-9a68-e498c73303e4.png)

- **İşlemler**:
   - **Favorilere Ekle**: Bu butona tıklanarak kullanıcının ilgili depoyu favorilerine ekleyebimesi sağlanır. Favorilere sol tarafta bulunan kırılım üzerinden erişilebilir.
   ![favorilereekle](https://docsbimser.blob.core.windows.net/imagecontainer/favorilerekle-40756f98-c6eb-4d8d-9441-d9cc609d85aa.png) 

  - **İndeklemeyi Yenile**: Seçilen Depo için yeniden bir indeksleme başlatılır ve indeks raporunda ilgili deponun bilgileri güncellenmiş olur.
  - **Yeniden Adlandır**: Seçilen Deponun isminin değiştirildiği alandır.
  - **Sil**: Seçilen depoların silinmesini sağlayan özelliktir. Bu butona tıklandığında güvenlik amacıyla işlemi yapan kullanıcının depo adını girerek işlemi gerçekleştirmesi beklenir. 
![](https://docsbimser.blob.core.windows.net/imagecontainer/DepoSil-eb340979-e4fb-498a-9642-d8106e260637.png)
