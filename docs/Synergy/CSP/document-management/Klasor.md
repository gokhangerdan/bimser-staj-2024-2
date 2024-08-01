# Klasör
Klasörler, içerisinde dosyaların veya farklı klasörlerin belli bir düzene göre bulunduğu dosyalama ve dizin yapısıdır.
Bir klasör üzerinde işlem yapılması istenildiği durumda ilgili işlemlerin görüntülenebilmesi için klasörün üzerine gelinir ve sağ tarafında çıkan yuvarlak _seçim alanı_ seçilir veya  _sağ tıklayarak açılan pencerede_ de klasör üzerinde yapılabilecek işlemler görüntülenir. Aynı zamanda birden fazla klasör üzerinde değişiklik yapmak istenildiği durumda; seçimi istenilen klasörlerin sağ tarafındaki yuvarlak seçim alanlarını işaretlenir ve birden fazla klasörün seçimi yapılır. Toplu şekilde yapılabilecek işlemler, seçimlere göre filtrelenir ve değişiklikler işlemler alanından veya sağ tıklanarak açılan pencereden yapılır.

![klasor](https://docsbimser.blob.core.windows.net/imagecontainer/Klasor-6241db01-24cc-4ef7-8ac9-6521b2aaa444.png)

- **Yeni**:

   - **Yeni Klasör**: Yeni bir klasör oluşturmayı sağlar. Açılan pencerede oluşturulacak Klasörün Adı ve Açıklaması sistemde mevcut dillerde her biri için özel olarak tanımlanabilmektedir.
   -  **Yeni Dosya**: Klasör üzerine Yeni bir dosya oluşturmayı sağlar. Yeni dosya eklemek için, açılan pencere üzerindeki Göz At kısmından seçim yapılabilir veya yüklenmesi istenen dosyalar bu pencere üzerine sürüklenip bırakılır. Yüklenecek Dosyalar kısmında kullanıcının eklemek istediği dosyalar listelenir. Tamam'a tıklandığı dosya ekleme işlemi gerçekleşmiş olur.
   ![YeniDosya](https://docsbimser.blob.core.windows.net/imagecontainer/KlasorYeniDosya-2b1f7cb0-f99f-4101-a81f-e9e252d4cc09.png)

-   **Aç**:
    -   **Özellikler**: Klasör özellikleri _Genel, MetaData, Dizin Ayarları, Yeni Dosya_ başlıkları altında toplanmaktadır. İlgili klasör ile ilgili özellik tanımları bu panel üzerinden gerçekleştirilir.
        -   **Genel**: İlgili Klasöre ait **Etiketler** tanımlanabilir ve bu etiketler aracılığıyla istenilen etiketteki nesneler filtrelenerek arama sağlanabilir. Tablo görünümünde etikete göre filtreleme yapılabilir.
            -   **İzin Verilen Dosya Tipleri**: Listenen tiplerdeki dosyalardan seçim yapılarak ilgili klasöre eklenebilecek dosyalar sınırlandırılabilir.
            - **Maksimum Dosya Boyutu**: Klasöre eklenecek dosyaların herbiri için maksimum dosya boyutunun ayarlandığı alandır.
  ![depogenel](https://docsbimser.blob.core.windows.net/imagecontainer/DepoGenel-b2ed4800-2a58-4229-bdf0-017c803abeba.png)
 
        -  **MetaData**: Seçilen Klasöre herhangi bir klasör ya da dosya ekleneceği zaman istenen profil formunun tanımlandığı alandır.
	        - **Üst Dizinden Al**: Seçilen klasörün üst dizininde bulunan bir klasörde ya da depoda tanımlı bir profil formu varsa bu formun alt dizine dosya ya da klasör eklerken de tanımlanması gerekiyorsa bu alan aktif olarak kalmalıdır. Varsayılan olarak aktif gelmektedir. Eğer üst dizindeki profil formunun alt dizinde kullanılması istenmiyorsa bu alana pasif hale getirilmelidir.
           - **Profiller**: Tabloda bulunan **+** butonuna tıklanarak bir profil formunun eklendiği alandır. Proje seçimi yapıldıktan sonra ilgili projede bulunan Metadata tipli formlardan biri seçilir. Eğer bir profil formu doldurulması zorunlu olacaksa **Gerekli** alanı aktif edilir. **Tip** alanından da dosya, klasör ya da her iki nesne için de ekleme yapılacağı zaman profil formu açılması sağlanmış olur.
            - **Alanlar**: Seçilen Formdaki alanlardan hangilerinin ilgili klasörün tablo görünümünde, bir kolon olarak oluşturulacağının seçildiği alandır.
 ![depoMetadata](https://docsbimser.blob.core.windows.net/imagecontainer/DepoMetaData-af7d33c8-b3aa-4d1d-b6c2-28172373674f.png)
Klasöre bir dosya eklenmek istediğinde eklenen dosya seçimi yapılır ve MetaData alanından belirlenen profil formu doldurularak kaydedilmesi sağlanır.
![profilformueklerken](https://docsbimser.blob.core.windows.net/imagecontainer/DepoProfilFormuEklerken-268af26e-b57c-431c-9099-dea272382e37.png)

             Profil formunda seçilen alanlar, profil formu eklenen klasörün **Tablo Görünümü** modunda görünür olur. Bu sayede klasör ya da dosyalara eklenen profil formu alanları görüntülenebilmiş olur ve bu alanlar üzerinden filtreleme yapılabilir. ![alanlar](https://docsbimser.blob.core.windows.net/imagecontainer/tablogorunumualanlar-8a67d321-4e99-43c0-85d1-9b5d24702782.png)

        -   **Dizin Ayarları**:  Csp Döküman Yönetimi, sizlere dosyalarınız üzerinden ocr yapmaya olanak tanıyor. Depo ya da klasörünüzün Dizin Ayarları menüsünden ayarlama yaparak, yüklediğiniz dosyaların içeriğini düz yazı olarak alabilir ve sisteme kaydebilirsiniz. Ardından Döküman Yönetimi arama ekranından tüm metin arama işlemi gerçekleştirebilirsiniz. Dosyanız içinde bulunan tek bir ibareyi aratarak, ilgili ibarenin içinde geçtiği tüm dosyalara erişebilirsiniz.
 Dizin ayarları menüsünden öncelikle varsa Üst Dizinden Al kutucuğunun işaretini kaldırmanız gerekiyor. (Üst Dizinden Al işaretinin ne olduğuna sayfa sonunda değineceğiz.) "Dosya Tipi" kısmından hangi dosya tiplerinde tüm metin arama yapmak isterseniz seçmelisiniz. İşlemci yapılandırmasından da hangi işlemciyi(OCR engine) kullanmak isterseniz seçmelisiniz. Ardından Ok butonuna tıklayın. Birden fazla kayıt girebilirsiniz.
 Not: OCR Engine yapılandırması için kurulum ve DB konfigürasyonlarının yapılması gerekmektedir.
 Ocr işlemi ile beraber yüklenen dosyalara otomatik yapay zeka destekli kategori belirleme işlemi de yapılmaktadır.
 Not: MetaData ve Dizin Ayarları menüleri üzerindeki işlemleriniz varsayılan olarak alt dizinlerde de geçerlidir. "Üst Dizinden Al" sayesinden alt dizinlerde bu ayarlamalarınızı tekrar yapma zahmetine girmenize gerek yoktur. Alt dizinlerde farklı ayar yapmak isterseniz "Üst Dizinden Al" kutucuğunun işaretini kaldırmanız yeterlidir.
 ![dizinAyarlari](https://docsbimser.blob.core.windows.net/imagecontainer/DizinAyarlari-de26f104-05a8-43af-94d5-f85ebc8b145b.png)
![dizinIslemci](https://docsbimser.blob.core.windows.net/imagecontainer/DizinAyarlari%C4%B0slemci-7129d12f-f839-4793-8267-82ac55281119.png)
           -   **Yeni Dosya**:  Depo'ya yeni bir dosya eklendiğinde otomatik olarak başlaması gereken bir sürecin tanımlandığı alandır. Proje ve Akış seçilir, seçilen akış dosya eklendiğinde otomatik olarak başlamış olur. Not: Akışınızın aşağıdaki değişkenlere sahip olması gerekmektedir.
			```StartedFrom (string),  CreatedFileId (long), CreatedFilePath (string)```
![DepoYeniDosya](https://docsbimser.blob.core.windows.net/imagecontainer/DepoYeniDosya-e7c059ec-8e3b-4122-a53c-64854ee6a484.png)

        -  **Ayrıntılar**:  Klasörde bulunan dosya, klasör ve içerik sayısının sunulduğu alandır. Hesapla butonuna tıklandığında da klasörün toplam boyutu hesaplanmaktadır. 
![depoAyrintilar](https://docsbimser.blob.core.windows.net/imagecontainer/DepoAyr%C4%B1nt%C4%B1lar-edfbc83d-a48d-4fe9-b09c-dcdd8f8d2d32.png)

    -   **Güvenlik**: Klasör özelinde görüntülenme, indirme, yazdırma gibi çeşitli yetkileri organizasyon içerisindeki kişilere (kullanıcılar,kullanıcı grupları, güvenlik grupları vb. gibi)  özel olarak tanımlama yapılabilmesini sağlayan bir güvenlik sekmesidir. 
Sol taraftaki arama çubuğuna nesneye bağlanacak grup yazılır ve seçilir. Seçilen grup ya da kullanıcının Güvenlik kısmında içerisinde yer aldığı tüm gruplar listelenir. Seçilen grup için Nesne üzerinde görüntüleme, düzenleme kırılımları ve tüm alt kırılımlarındaki yetkiler, **_Grubu Nesneye Bağla_** butonuna tıklanarak tanımlanmış olur. Daha sonra yapılan değişiklikler, **_Değişiklikleri Kaydet_** butonuna tıklanarak kaydedilmiş olur.
![depoGuvenlik](https://docsbimser.blob.core.windows.net/imagecontainer/DepoGuvenlik-519c09f3-7365-496f-a594-8e6acb578554.png)
 
     -   **Profili Göster**: Klasör üzerinde tanımlanmış bir profil formu varsa buradan açılır ve düzenlenir.
    -   **Aktiviteler**: Kullanıcıların nesne üzerinde bir mesaj yayınlamasını ve yayınladıkları mesajları veya nesne üzerinde yaptıkları işlemleri görüntülenmesini sağlayan bir panel ekranı getirir.
    ![klasorAktiviteler](https://docsbimser.blob.core.windows.net/imagecontainer/KlasorAktiviteler-5e2f81fd-af43-48c7-9322-8f9340919627.png)

- **İşlemler**:
   - **Favorilere Ekle**: Bu butona tıklanarak kullanıcının ilgili klasörü favorilerine ekleyebimesi sağlanır. Favorilere sol tarafta bulunan kırılım üzerinden erişilebilir.
   ![favorilereekle](https://docsbimser.blob.core.windows.net/imagecontainer/favorilerekle-40756f98-c6eb-4d8d-9441-d9cc609d85aa.png) 
  - **Taşı**: Seçilen klasörün Doküman Yönetimi üzerinde farklı bir dizine taşınabilmesinin sağlandığı kısımdır.
  ![klasorTasima](https://docsbimser.blob.core.windows.net/imagecontainer/KlasorTasima-cd369369-6017-45c5-a3f2-28489db60908.png)
  - **İndeklemeyi Yenile**: Seçilen Klasör için database seviyesinde yeniden bir indeksleme başlatılır ve indeks raporunda ilgili klasöre ait bilgiler daha hızlı bir şekilde güncellenecektir.
  - **Yeniden Adlandır**: Seçilen Klasörün isminin değiştirildiği alandır.
  - **Sil**: Seçilen klasörlerin silinmesini sağlayan özelliktir. Bu butona tıklandığında güvenlik amacıyla işlemi yapan kullanıcının klasör adını girerek işlemi gerçekleştirmesi beklenir. 
![](https://docsbimser.blob.core.windows.net/imagecontainer/DepoSil-eb340979-e4fb-498a-9642-d8106e260637.png)

- **Paylaş**:
	- **Abonelik**: Seçilen Klasörün içerisinde oluşturulan ve/veya silinen dosyalar ya da klasörler için bir haber alma sistemidir.
	Klasörün adı, yolu, oluşturulma/düzenlenme tarihi, oluşturan kişi ile ilgili bilgilere buradan ulaşılabilir. Belirtilen tarih aralıklarında geçerli olacak bir bildirim seçilir. Bildirim Seçenekleri altında, seçili Klasör içerisinde hangi türde işlemlerde abone kullanıcının bilgilendirileceği seçilir. Herhangi bir dosya ya da klasör oluşturulduğunda ve/veya silindiğinde abone olan kullanıcıyı bilgilendiren bir mail gönderilmesi sağlanır.
	![klasorAbonelik](https://docsbimser.blob.core.windows.net/imagecontainer/KlasorAbonelik-76f4ccf1-7ba3-4244-a74c-5eba28b015d4.png)
