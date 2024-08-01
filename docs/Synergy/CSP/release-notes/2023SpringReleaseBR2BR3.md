---
sidebar_position: 2332
sidebar_label: "2023 Spring Release BR2-BR3"
custom_edit_url: ""
---



# Bimser Synergy 2023 Spring Release Notes BR2-BR3

*(1 Haziran 2023 - 31 Temmuz 2023)*

## 1. Highlights / New Features

- 50880 - Geliştirme arayüzünde **Datagrid** nesnesi **Datasource** bağlanmadığında **Save**
    **On: Form Save** ve **Row Change** seçenekleri eklenmiştir. **Form Save** özelliğiyle
    **Datagrid’ in** kullanıcı tarafından kaydedilmesi gerekmekte, **Row Change** özelliği ile
    **Datagrid Ekle butonuna tıklanıldığında DocumentID ’ye göre formda anlık**
    **kaydetme işlemi yapılması sağlandı**.
- 48187 - Web arayüzünde **Datagrid** nesnesinde **Datasource** bağlı **olmadığında Save**
    **On: Row Change** seçiliyken Datagrid’de yapılan işlemlere göre **GetRows** , **InsertRows** ,
    **UpdateRow** endpointlerinin **tetiklenmesi** sağlandı. Datasource bağlı Datagrid’lerde
    ise **Editing Settings: Row ve Cell seçenekleri eklendi**.
- 51177 [DR8273] - **IOS** cihazların **mobil arayüzünde** , nesnelerde **zorunlu alanların**
    **uyarı yazısına** ek olarak **Web tarafındaki gibi belirtilme geliştirmesi** yapıldı.
- 51166 [DR8273] - **Android** cihazların **mobil arayüzünde,** nesnelerde **zorunlu**
    **alanların uyarı yazısına** ek olarak **Web tarafındaki gibi belirtilme geliştirmesi** yapıldı.
- 51486 - **IOS** cihazların **mobil arayüzünde** , **Sunucu ekleme** sayfasındaki **Alan Adı** ve
    **Sunucu Yolu** bilgilerinin **"Gelişmiş Seçenekler"** adı altında **açılıp kapanabilir bir alana**
    **taşınması** , girdi yapılan tüm alanlara **çarpı şeklinde silme butonu eklenmesi** ve
    **Sunucu Adresi doldurulduğunda Alan Adı bilgisinin de otomatik olarak**
    **doldurulması** sağlandı.
- 49980 - **IOS** cihazların **mobil arayüzünde** , **Native+** görünümündeki
    **DocumentMetaData** nesnesine **buton ile değer girişi yapılabilmesi** geliştirildi.
- 51259 - **Android** cihazların **mobil arayüzünde** , **sunucu ekleme** sayfasına **Gelişmiş**
    **Ayarlar seçeneğinin eklenmesi** geliştirildi.
- 51244 - **IOS** cihazların **mobil arayüzünde** , **Sunucu Ekle** sayfasında **Sunucu Yolu**
    **alanının otomatik doldurulması** geliştirildi.
- 49672 - **Android** cihazların **mobil arayüzünde** , **Native+** görünümündeki
    **DocumentMetaData** nesnesine **Button ile değer girilebilmesi** geliştirildi.
- 48148 - **IOS** cihazların **mobil arayüzünde** , **Card nesnesi geliştirilmesi** tamamlandı.
- 48139 - **Android** cihazların **mobil arayüzüne, Card nesnesi eklenmesi** geliştirildi.
- 41190 - **Android** ve **IOS** cihazların **mobil arayüzünde** , kullanıcı **Beni Hatırla** özelliği ile
    giriş yaptığında **Kullanıcı Adı alanının otomatik doldurulması** geliştirildi.
- 49979 - **Android** cihazların **mobil arayüzünde, Native+** görünümündeki
    **DocumentMetaData** nesnesine **Button ile değer girilebilmesi için** Web geliştirmesi
    yapıldı.
- 48474 - **Android** cihazların **mobil arayüzünde** , **DataGrid satırlarında resim gösterme**
    **geliştirmesi** yapıldı.


- 49101 - **Android** cihazların **mobil arayüzünde, Native+** görünümündeki **DataGrid**
    nesnesi satırlarına **DoubleClick** özelliği getirilerek **Bilgi alanlarının gösterilmesi**
    sağlandı.


## 2. Improvements

- 51428 - **Android** cihazların **mobil arayüzünde** , **Native+** görünümündeki **Switch** ve
    **ComboBox** nesnelerinin **Background Color özelliğinde düzenlemeler** yapıldı.
- 50244 - **Android** cihazların **mobil arayüzünde, Native+** görünümündeki **Lookup**
    nesnesinde **Sorting Enabled özelliği** değiştirildi.
- 50782 [DR8274] - **Android** cihazların **mobil arayüzünde** , **Native+** görünümündeki
    **Selection Form** 'dan **DataGrid** nesnesine veri eklerken **arama özelliğindeki çarpı** ile
    **formdaki çarpıların karışma hatası** düzeltildi.
- 50163 - **Android** cihazların **mobil arayüzünde** , **İş Akış Yönetimi** sayfasındaki **ikonlar**
    düzeltildi.
- 50783 [DR8274] - **IOS** cihazların **mobil arayüzünde** , **Native+** görünümündeki
    **Selection Form** 'dan **DataGrid'e** veri eklerken **arama özelliğindeki çarpı ile formdaki**
    **çarpının kapanma hatası** düzeltildi.
- 48734 - **Android** cihazların **mobil arayüzünde** , form versiyonuna göre **Enabled** ve
    **Client Enabled** özelliklerine bakılarak **Disabled durumuna karar verilmesi** geliştirildi.
- 47934 - **IOS** cihazların **mobil arayüzünde** , **Native+** görünümündeki **DataGrid**
    nesnelerinde satırlarda bulunan **Actions Button görsellerinde düzenlemeler** yapıldı.
- 47863 - **Android** cihazların **mobil arayüzünde** , formdan geri çıkıldığında **Uygulamalar**
    menüsünün **değişip sıfırlanma hatası** düzeltildi.
- 48286 - **Android** cihazların **mobil arayüzünde** , **sunucudan resim çekme işlemi ile**
    **ilgili düzenleme** yapıldı.
- 48644 - **IOS** cihazların **mobil arayüzünde** , **Native+** görünümündeki **Enabled** ve **Client**
    **Enabled** özelliği **False** olan **ComboBox nesnelerinin görünme hatası** düzeltildi.
- 48802 - **IOS** cihazların **mobil arayüzünde** , **Native+** görünümündeki **Tabs** nesnesinde
    **Tab yüksekliklerinin doğru hesaplanması** geliştirildi.
- 49810 - **Android** cihazların **mobil arayüzünde, Doküman Yönetimi sayfası**
    düzenlendi.
- 49872 - **Android** cihazların **mobil arayüzünde, Native+** görünümündeki **Related**
    **Documents** nesnesindeki **Fotoğraf Çek ikonu** değiştirildi.
- 49944 - **Android** cihazların **mobil arayüzünde** , **Native+** görünümündeki **Related**
    **Documents** nesnesinde **dosya eklenmeme sorunu** düzeltildi.
- 49641 - **Android** cihazların **mobil arayüzünde** , **Uygulamalar** sayfasında gir çık
    yapıldığında **meydana gelen çökme hatası** düzeltildi.
- 49361 - **IOS** cihazların **mobil arayüzünde, Native+** görünümündeki **Card** nesnesi
    **görünümü iyileştirildi**.
- 49068 - **Android** cihazların **mobil arayüzünde, Native+** görünümündeki **Card**
    nesnesinin **öge başlık alanlarının iki satır olarak değiştirilmesi** geliştirildi.
- 49275 - **Android** cihazların **mobil arayüzünde, Native+** görünümündeki **ComboBox**
    **nesnesi verilerine ikon ekleme işlemi** geliştirildi.


## 3. Fixes

### 3.1. Web Arayüzü

#### 3.1.1. Doküman Yönetimi

- 48466 - Web arayüzünde **Doküman Yönetiminde imzalanan bir dosya** , başka bir yere
    kopyalandığında üzerindeki **imzanın kaybolma hatası** düzeltildi.
- 48907 - Web arayüzünde **Doküman Yönetiminde** yeni bir klasör oluşturulmak
    istendiğinde, **sayfa Azerice dilindeyken klasör adının boş gelme hatası** düzeltildi.
- 48918 - Web arayüzü **Azerice** dilindeyken **Doküman Yönetiminde Yeniden Adlandır**
    işlemleri **Türkçe dilinde yapılan değişikliğe göre sonuç verme hatası** düzeltildi.
- 29282 - Web arayüzü **Doküman Yönetiminde** dosyalar açıldıktan sonra **yatay**
    **kaydırma çubuğunun ortadan kalkma ve sayfa ortasında gözükme** hatası düzeltildi.
- 40393 - Web arayüzü **Doküman Yönetiminde Sadece Bahsedilenler Yanıtlayabilir**
    ekranında, bahsedilen kişi haricindeki kişilerin **Yanıtla butonunu görüp kaydolmasa**
    **bile değer girebilme hatası** düzeltildi.
- 42499 - Web arayüzü **Doküman Yönetiminde birden fazla dosyanın silindiği**
    senaryoda **sayfanın hataya düşme** durumu düzeltildi.
- 42718 - Web arayüzü **Doküman Yönetiminde tablo** görünümdeyken **dosyaların**
    **görünmeme** hatası düzeltildi.
- 45503 - Web arayüzü **Doküman Yönetimi** modülünde doküman için oluşturulan
    **ilişkili dosya görünmeme hatası** düzeltildi.
- 46224 - Web arayüzünde **Doküman Yönetimi** modülünde **panoya** eklenen
    dokümanlar için **Tümünü Kaldır** butonundaki **seçenekler** ile **doküman özelindeki**
    **seçenek butonları farklı görünme hatası** düzeltildi.
- 47937 - Web arayüzünde **Doküman Yönetiminde** klasör seçilip **Özellikler** butonuna
    tıklandığında **GetCategory parametresinin 500 dönme hatası** düzeltildi.
- 48058 - Web arayüzü **Doküman Yönetiminde MetaData** içerisinde **farklı proje silme**
    işlemi gerçekleştirirken **ortaya çıkan görsel hata** düzeltildi.
- 48074 - Web arayüzü **Doküman Yönetiminde ilişkili dosyaların görünmeme hatası**
    düzeltildi.
- 46665 [DR7054] - Web arayüzü **Doküman Yönetiminde** dosyalara **Profili Göster**
    denildiğinde, **sistemin tepki vermeme hatası** düzeltildi.
- 48912 - Web arayüzü **Doküman Yönetiminde Azerice gelen maildeki dil hataları**
    düzeltildi.
- 47477 - Web arayüzü **Doküman Yönetiminde Word** dosyasına tıklanıp **Çalışma Başlat**
    denildiğinde **Gözat** seçeneğinin gelmeyip, **doküman versiyonlama işleminin**
    **gerçekleştirilememe** hatası düzeltildi.
- 44648 - Web arayüzü **Doküman Yönetimi** modülünde **klasör** ya da **deponun**
    özelliklerinde yapılan **dosya tipi kısıtlamasının çalışmama** hatası düzeltildi.


- 50983 - Web arayüzü **Doküman Yönetiminde Profil formu** ekranında **MultiLanguage**
    alanındaki **tıklama hatası** düzeltildi.
- 50986 - Web arayüzü **Doküman Yönetiminde Profil formu** ile açılan dosyanın
    **açıklama** ve **yeniden adlandırma** işlemleri esnasında **formun yüklenmeme hatası**
    düzeltildi.
- 50991 - Web arayüzü **Doküman Yönetiminde Profil formu** ekranında **Dosyayı Sil**
    **butonunun görünme hatası** düzeltildi.
- 48089 - Web arayüzü **Doküman Yönetiminde** Gelişmiş Aramada **50'den fazla verinin**
    olduğu aramalarda **Search endpointinin hataya düşme durumu** düzeltildi.
- 48248 [DR7637] - Web arayüzü **Doküman Yönetiminde Dizin** ayarlarında **dosya tipi**
    eklenmek istendiğinde **seçim yapılamadan kapanma hatası** düzeltildi.
- 48764 - Web arayüzü **Doküman Yönetiminde Dizin** ayarlarının **kaydetmeme hatası**
    düzeltildi.
- 51046 - Web arayüzü **Doküman Yönetiminde Gelişmiş Aramada** herhangi bir yer
    butonunun **kapanmama hatası** düzeltildi.
- 51056 - Web arayüzü **Doküman Yönetiminde Profil formu** oluşturma esnasında
    **Silme** ve **Yeni klasör** oluştururken **sayfanın hataya düşme durumu** düzeltildi.
- 51109 - Web arayüzünde **Doküman Yönetimi Profil formunda** form **önizleme** işlemi
    yapılırken **formun yüklenmeme hatası** düzeltildi.
- 51054 - Web arayüzü **Doküman Yönetiminde Profil formu** oluştururken meydana
    gelen **uyarı hatası** düzeltildi.
- 48236 - Web arayüzü **Doküman Yönetiminde PNG-JPG** dosya uzantılarının
    **kategorilendirilememe hatası** düzeltildi.
- 33365 - Web arayüzü **Doküman Yönetiminde ilişkilendirilen Excel** dosyasının **tam**
    **ekran görüntülenmeme hatası** düzeltildi.

#### 3.1.2. İş Akış Yönetimi......................................................................................................................

- 48933 [DR7802] - Web arayüzünde **vekâlet** verirken **İş Akış Yönetiminden**
    menüsünde **Tüm Uygulamalar** yerine, **menü içerisinden uygulama seçilerek** işlem
    yapıldığında **İş Akış Yönetimi menüsünün gözükmeme hatası** düzeltildi.
- 48926 [DR7805] - Web arayüzünde **İş Akış Yönetimi** için **vekâlet** verilip, **İş Akışı ve**
    **uygulamalardan yetki verilen proje akışının devam ettirilememe hatası** düzeltildi.
- 51228 - Web arayüzünde **İş Akış Yönetimi** menüsünde süreçlere ait **Datagrid 'in**
    **açılmama hatası** düzeltildi.


#### 3.1.3. İnsan Kaynakları

- 38185 - Web arayüzünde **İnsan Kaynakları** kısmının **Şirketler** menüsünde **zorunlu**
    **alan uyarısı vermeden kaydedilme hatası** düzeltildi.
- 42810 - Web arayüzü **İnsan Kaynaklarında** , **yeni bir kullanıcı grubu** oluşturma
    ekranındaki **uzun isimlerin Checkbox ile üst üste gelip görüntü bozukluğu** oluşturma
    hatası düzeltildi.
- 42902 - Web arayüzü **İnsan kaynakları** kısmındaki **Kullanıcılar bölümünde Kullanıcı**
    **detay bilgilerini gösteren panel** açıkken başka bir kullanıcıya geçildiğinde, **amir**
    **bilgisinin doğru gösterilmeme hatası** düzeltildi.
- 46604 - Web arayüzünde **İnsan Kaynakları** kısmında **Maaşlar** menüsünde **maaş**
    **tutarının Datagrid'de hatalı gösterilme sorunu** düzeltildi.
- 44819 - Web arayüzünde **İnsan Kaynakları** modülündeki **Şirketler** menüsü Datagrid
    tablosunda **Tehlike Sınıfı, Aktarım Durumu, Durum kolonlarındaki sıralama**
    **seçenekleri** düzeltildi.
- 44847 - Web arayüzünde **İnsan Kaynakları** menüsünün altındaki **Pozisyonlar** ,
    **Şirketler, Maaşlar, Özellik Tanımları** içerisindeki **Özellikler** Datagridlerinde input
    alana veri girildikten sonra **imlecin input alandan çıkma hatası** düzeltildi.
- 50064 - Web arayüzü **İnsan Kaynakları** menüsünde **Kullanıcı Tanımlama** ve
    **Güncelleme** ekranlarındaki **durum ve aktarım durumu** alanlarının **İnteger** değer
    olarak gösterilme hatası düzeltildi.
- 50347 - Web arayüzünde **İnsan Kaynakları** menüsünün **Şirketler Datagrid’ inde**
    **açıklama kolonunun azalan sıralamasındaki hata** düzeltildi.
- 50259 - Web arayüzünde **İnsan Kaynakları** menüsü **Özellik Tanımları** içerisindeki
    **Kullanıcı Özellikleri** sayfasında **Sil** butonunun **üç nokta şeklinde görünme hatası**
    düzeltildi.
- 50366 - Web arayüzünde **İnsan Kaynakları** kısmının **Vardiya** menüsünde var olan bir
    **vardiya kodu tekrar kaydedilmek istendiğinde** alınan hata **'Vardiya zaten var'**
    şeklinde düzeltildi.


#### 3.1.4. Web Ana Sayfa

- 51033 - Web arayüzünde **Datagrid** nesnesi **Datasource** Özellik Görüntüleyicisi altına
    **Save on: Form Save ve Row Change** tipleri eklendi. **Row Change** seçiliyken, eğer
    formun(Dokümanın) **ID** değeri **oluşmadıysa(kaydedilmediyse) uyarı vermekte** ve
    **akış gönderilerek verileri kaydetmesi** sağlandı.
- 46972 [DR7019] - Web arayüzü **Doküman Yönetiminde** dosyalara **Güvenlik**
    sekmesinde **yetki** oluştururken, yetki verilen departman bilgilerinin **Departman Adı**
    değil de **Departman ID bilgisinin görünme hatası** düzeltildi
- 47563 - Web arayüzünde **GetUserDetail** endpointinden dönen ve **themeData**
    parametresiyle aynı işlevi gören **theme parametresi** oluşabilecek hataların önüne
    geçmesi adına **kaldırıldı**.
- 47841 [DR7537] - Web arayüzünde **StartWorkflowWithDocument** 'daki gibi Form
    oluşturabilecek bir endpoint olmadığı için, bu ihtiyacı karşılamak adına
    **SaveFormWithData endpointi** oluşturuldu ve oluşturulan formun **hangi ID numarası**
    ile geldiğini görmek adına **Response parametreleri arasına ek olarak Document ID**
    eklendi.
- 48916 - Web arayüzünde **Azerbaycan diliyle** ortama giriş yapıldığında, **Erişim**
    **anahtarları ve Vekâlet menüsünde oluşan başlık hataları** düzeltildi.
- 46561 [DR7071] - Web arayüzünde **Veri tabanında** ilgili tabloda kullanılan **PositionId**
    olarak kullanılan kolonu, **POSITIONID olarak kullanılarak** hata düzeltildi.
- 48133 - Web arayüzünde, **FormatType** özelliği **Label** olup **EditType** özelliği ise
    **NumberBox** olan **Datagrid kolonuna** yazılan **verilerin sonraki onaycıya gitmeme**
    **hatası** düzeltildi.
- 48369 [DR7660] - Web arayüzünde projede akış ilerletilmek istendiğinde **formun**
    **onaylandıktan sonra görünümün görüntülenmeme hatası** düzeltildi.
- 48408 - Web arayüzünde **DataGrid** nesnesi **Image** kolonuna **eklenen görselin sonraki**
    **onaycıya gitmeme hatası** düzeltildi.
- 49115 [DR7853] - Web arayüzünde nesnelerin **Allow Null** özellikleri **kapalı** iken aynı
    zamanda **Required** özelliği **aktif** olduğunda **zorunlu alan uyarısı verme hatası**
    düzeltildi.
- 36199 - Web arayüzünde **Statik Datagrid** nesnesi **Column Hiding Enabled anahtarı**
    **aktifken Date, Time ve DateTime** kolonlarına **veri yazılmak** istendiğinde **konsola**
    **düşen hata** düzeltildi.
- 39731 - Web arayüzünde **Duyurular** kısmındaki **yazım hataları ve görünüm**
    **bozuklukları** düzeltildi.
- 40648 - Web arayüzünde formda **Client Enabled** özelliği olan **FishBone** nesnesine
    **veri girilebilme** ve **FishBone** nesnesinin **Background color** özelliğinin **çalışmama**
    **hataları** düzeltildi.
- 42476 - Web arayüzünde **Uygulamalar** menüsünün **kaydırma özelliğinin gelmeme**
    **hatası** düzeltildi.


- 43601 - Web arayüzünde **Statik Datagrid Select** kolonunda **Selected** olarak
    işaretlenen veride, **ikon seçimi olduğunda satır kayması yaşanma hatası** düzeltildi.
- 43865 - Web arayüzünde **DataGrid** nesnesi kolonlarında **Summary Types** özelliği
    açıkken boş bir değer olduğunda **minimum veya maksimum değeri bulmama hatası**
    düzeltildi.
- 43920 - Web arayüzünde **Hesabım** kısmının **Vekâlet ve Erişim Anahtarı** ekranında
    **isim ve duruma göre sıralama hatası** düzeltildi.
- 44487 - Web arayüzünde formda **TimePicker** nesnesini açıp **kaydırma çubuğu** ile
    kaydırdığımızda **sayfa boyunca pencerenin kapanmama hatası** düzeltildi.
- 44952 - Web arayüzünde formda **Lookup** nesnesinin **Behavior** kısmından özelliğini
    **ReadOnly** yaptığımız zaman **nesnenin algılama hatası** düzeltildi.
- 44985 - Web arayüzünde formda **FormViewer** nesnesine gömülü olan formda
    **değişiklik yapılamama hatası** düzeltildi.
- 45361 - Web arayüzünde **Aktiviteler Yeni mesaj** kısmının **Gelişmiş** bölümünün **link**
    **ekleme özelliği** kullanıldığında, **daha önce tanımlanmış olan linklerin görülme hatası**
    düzeltildi.
- 45379 - Web arayüzünde formda **Panel** nesnesinin kendisini **ReadOnly** yaptığımızda
    **içindeki nesnelere veri girmeye devam etme hatası** düzeltildi.
- 45405 - Web arayüzünde formda **Tabs** nesnesinin kendisi **ReadOnly** yapıldığında
    **içindeki nesnelere veri girilebilme hatası** düzeltildi.
- 45415 - Web arayüzünde formda **Tabs** nesnesinin kendisi **Enabled** ve **Client Enabled**
    yapıldığı zaman **içindeki nesnelere müdahale edilebilme hatası** düzeltildi.
- 45428 - Web arayüzünde **Duyurular** kısmında **yeni bir duyuru** oluşturulurken link
    eklenmek istendiğinde, **Link alanının üzerinde arama alanı görülme hatası** ile link
    ekleme ekranındaki **Yeni sekmede aç** ve **Ekle butonu İngilizce görülme hatası**
    düzeltildi.
- 45442 - Web arayüzünde **Tüm Duyurular** sayfasından **bir duyuru silinip** tekrar
    Anasayfaya dönüldüğünde **daha önce yayınlanmış duyurunun tekrar açılma hatası**
    düzeltildi.
- 45479 - Web arayüzünde form ekranında **Related Documents** nesnesinde **Doküman**
    **Yönetimi** üzerinden dosya yükleme penceresinde **Tablo** ve **Kart seçimi çerçevesine**
    **tıklanmama hatası** düzeltildi.
- 46034 - Web arayüzünde **Panel1 boyutunda** açılan uygulamanın **Akış Tarihçesini**
    **Göster** dediğimizde **Bilgilendirmeleri Göster onay kutusunun metin alanının dizayn**
    **hatası** düzeltildi.
- 46760 [DR7119] - Web arayüzü **Doküman Yönetiminde Word dosyasına** tıklanıp
    **Çalışma Başlat** denildiğinde, **Gözat** seçeneğinin gelmeyip, **doküman versiyonlama**
    **işleminin gerçekleştirilememe hatası** düzeltildi.
- 47167 [DR7318] - Web arayüzünde formda **Tabs** nesnesi **içerisindeki birden fazla**
    **sekmeye** eklenen ve **Required** özelliği **aktif** nesnelerin **doldurulmadan akışın devam**
    **etme hatası** düzeltildi.


- 47492 - Web arayüzünde **Open Selection Form** tipinde **Toolbar Button** ile **Datagride**
    veri eklenen senaryoda **akış gönderilirken alınan hata** düzeltildi.
- 48173 - Web arayüzünde **Aktiviteler** alanında **Gelişmiş Aktivite mesajı** olarak link
    eklendiğinde **linkin açılmama hatası** düzeltildi.
- 48175 - Web arayüzünde **Lookup nesnesinde oluşan hata** düzeltildi.
- 48091 - Web arayüzünde Giriş ekranında **Beni Hatırla** özelliği kullanılarak giriş
    yapıldığında, veri tabanındaki **Security.Token.RememberMeRefreshTokenTTL**
    değerine göre **tarayıcı kapansa da giriş bilgilerinin hatırlanmaya devam etmeme**
    hatası düzeltildi.
- 49677 [DR8008] - Web arayüzü **Akış Tarihçesi** ekranında **Akış Durumu** nesnesinin
    **gizlenmeme hatası** düzeltildi.
- 50054 [DR8108] - Web arayüzünde nesnelerin **CSS özellikleri** ile ilgili bir işlem
    yapıldığında **formun oluşturulmama hatası** düzeltildi.
- 50475 - Web arayüzünde **İlişkili Datagrid** olan **akış gönderildiğinde alınan hata**
    düzeltildi.
- 43516 - Web arayüzünde formda **FileSelector** nesnesinin **Supported Extensions**
    özelliğinde **izin verilen dosyalarla** birlikte **izni verilmemiş dosyayı da seçme hatası**
    düzeltildi.
- 45966 - Web arayüzünde formda **DocumentViewer** nesnesini **Drawer** modunda
    açtığımızda, **pencere boyutunu küçülttüğümüzde panelin sürekli olarak titreme**
    hatası düzeltildi.
- 46243 [DR6875] - Web arayüzünde **ComboBox** nesnesinden tetiklenen **Datagrid**
    select tipli kolona **Parametrik sorgudan verilerin gelmeme hatası** düzeltildi.
- 47092 - Web arayüzünde **Aksiyon Yönetimi** içerisinde **Aksiyon formu** seçilerek açılan
    **kanban** ekranında **son kolonun sabit kalması için gerekli geliştirme** yapıldı.
- 50281 [DR8159] - Web arayüzünde **StartWorkFlowWithDocument API** ile **Lookup**
    nesnesindeki **atama sorunu** düzeltildi.
- 50506 - Web arayüzünde **Uygulama Gezgininde uygunsuz karakter** ile **profil kodu**
    **tanımlanma** hatası düzeltildi.
- 43233 - Web arayüzünde Akış değişkenine **flow cs** tarafında tarafında yapılan işlem
    ile maildeki **Türkçe karakterlerin görünmeme hatası** düzeltildi.
- 46464 [DR6991] - Web arayüzünde form ekranında **Rest sorgu** bağlantısı olan
    **ComboBox** nesnesinde **arama ve yenileme işlemindeki hata** düzeltildi.
- 47653 [DR7453] - Web arayüzünde akış gönderilirken **kullanıcıya giden mailler ortam**
    **diline göre hatalı gelme** durumu düzeltildi.
- 47838 [DR6626] - Web arayüzünde **NumberBox** nesnesinin **Precision** değerine 2
    verilip, **Step** değerine 0,5 verildiğinde, **form derlenirken alınan hata** düzeltildi.
- 49589 [DR7975] - Web arayüzünde **Akış Durdurucu** nesnesiyle akış ilerletilmek
    istendiğinde **dokümanın silinme hatası** düzeltildi.
- 50264 [DR8136] - Web arayüzünde **menü parametresinin akışta okunmama hatası**
    düzeltildi.


- 50265 [DR8129] - Web arayüzünde **Parametrik** formlarda **Selected** kolonlarında **SL**
    **tablosundaki verinin güncellenmeme hatası** düzeltildi.
- 50418 - Web arayüzünde **Vekâlet** işlemlerinde **proje yönetimi yetkisinin kısıtlanması**
    sonucunda **kullanıcının proje silme işlemini yapabilme** hatası düzeltildi.
- 50521 - Web arayüzünde **Akış Tetikleyici** nesnesiyle **akış ilerletilmek** istendiğinde
    meydana gelen **workflowinstance hatası** düzeltildi.
- 50541 [DR8213] - Web arayüzünde **Parametrik** formlarda **Selected kolonlarında SL**
    **tablosundaki verinin güncellenmeme hatası** düzeltildi.
- 50954 - Web arayüzünde **Pozisyon** ataması yapılan **projede akışı ilerletirken**
    karşılaşılan **Object Referans hatası** düzeltildi.
- 51203 - Web arayüzünde **Save on** özelliği **Row Change** olan **Statik DataGrid**
    nesnesinin **image** kolonuna **eklenen görselin gelmeme hatası** düzeltildi.
- 51314 - Web arayüzünde **Process Arşivi** oluşturulan **Datagrid** nesnesinden açılan
    form **onaylanmak istendiğinde alınan hata** düzeltildi.
- 42027 - Web arayüzünde **DocumentViewer** yüklü form açıldığında **sürekli olarak**
    **forma hata gelme sorunu** düzeltildi.
- 42684 - Web arayüzünde mailden gelen **RelatedDocuments** nesnesi için Doküman
    Onayı açıldığında konsolda **GetRelatedDocumentObjects çoklu istek atma sorunu**
    düzeltildi.
- 43742 - Web arayüzünde formda **RelatedDocuments** nesnesi **ReadOnly** olduğunda,
    sol üstteki ikonların imleci değişirken, **Yerel Dosya Sistemi** ve **DM alanlarının**
    **değişmeme** hatası düzeltildi.
- 43849 - Web arayüzünde formda **Scheduler** nesnesinin **Enabled** ve **Client Enabled**
    olmasına rağmen **veri girişi yapılabilme hatası** düzeltildi.
- 44478 [DR4244] - Web arayüzünde **İlişkili form** açılmak istendiğinde o **formun**
    **yüklenmeyip boş gelme hatası** düzeltildi.
- 46664 - Web arayüzünde formda **FileSelector** nesnesinde **Selection Target ‘da** seçili
    klasörü **otomatik olarak direkt açılmayıp** , **en dış klasörden başlama hatası** düzeltildi.
- 48400 - Web arayüzünde **Statik** formlarda **MultiLanguage** ikonuna **tek tıklama** ile
    açılması gerekirken, **çift tıklamayla açılma hatası** düzeltildi.
- 48518 - Web arayüzünde **Giriş** ekranında **Beni Hatırla** özelliği kullanıldığında **Refresh**
    **endpointindeki hata** düzeltildi.
- 49020 - Web arayüzünde **Azerbaycan** dilindeyken **menüden açılan formun başlığının**
    **gelmeme** hatası düzeltildi.
- 49454 - Web arayüzünde **DataGrid Row** ve **Cell** moddayken **Statik Select** kolonunda
    ikonu bulunan veri setleri seçilip kaydedildikten sonra düzenlenirken, **ikon bulunan**
    **verilerin gitme hatası** düzeltildi.
- 49742 - Web arayüzünde **Datagrid Boolean** kolonunda **Show Editor Always** özelliği
    açıkken **kolonda düzenleme yapıldığında konsola atılan hata** düzeltildi.
- 49750 [DR8037] - Web arayüzünde form ekranında **Lookup** nesnesinde **Display**
    **Expression** değeri **uzun String değerler** olduğunda **nesneden taşma hatası** düzeltildi.


- 49922 - Web arayüzünde formda **Lookup** nesnesinde **Text Align** özelliğinden **Center**
    ve **Right** seçimlerinin **nesneye etki etmeme hatası** düzeltildi.
- 49975 - Web arayüzü **Giriş** ekranında **Şifremi Unuttum** butonuna basıldığında **mail**
    **gönderilmeme hatası** düzeltildi.
- 50052 - Web arayüzünde **Giriş** ekranında **Dijital imza** seçerek **giriş yapılamama**
    **hatası** düzeltildi.
- 50237 - Web arayüzü **Uygulama Gezgininden** menülerin **Form** ya da **Akış** alanının
    **boş görülme hatası** düzeltildi.
- 50266 - Web arayüzünde form ekranında **ComboBox** nesnesinde **uzun metin**
    seçimleri yapıldığında **yanındaki nesnelerin üzerine taşma hatası** düzeltildi.
- 50296 - Web arayüzünde içerisinde **Repeater** nesnesi olan form açılırken **ortamın**
    **hata verme sorunu** düzeltildi.
- 50315 - Web arayüzünde form ekranında **Lookup** nesnesinde **Multiple** seçimler
    yapılıp **Tamam** butonuna tıklandıktan sonra **verilerde 'x' işaretinin gözükmeme**
    **hatası** düzeltildi.
- 50328 - Web arayüzünde **Lookup** nesnesinin formun **Client** ve **Server** tarafında **Value**
    ve **Text değerlerinin gelmeme hatası** düzeltildi.
- 50395 - Web arayüzünde form ekranında **Lookup** nesnesinde **Multiple** seçimler
    yapılıp **Tamam** butonuna tıklandığında oluşan **reading 'ToString' hatası** düzeltildi.
- 50429 - Web arayüzünde **birden fazla görünümün** olduğu ve aynı **Lookup** nesnesinin
    bulunduğu formlarda **Lookup açılmak** istendiğinde meydana gelen **konsol hatası**
    düzeltildi.
- 50476 - Web arayüzünde **İlişkili Datagrid** nesnesinden açılan formda **nesneler**
    **arasında fazla boşluk olma hatası** düzeltildi.
- 50495 - Web arayüzünde **Datagrid** nesnesi **sayfa gruplarında gezinirken** ve
    **filtrelerde işlem yaparken oluşan satır kayma** hatası düzeltildi.
- 50608 – Web arayüzünde **GetLoginParameters Request Payload** tarafında
    **DomainAddress'in gönderilmeme** hatası düzeltildi.
- 50724 - Web arayüzünde **App** sürecindeki formda **Lookup** nesnesinde **On Value**
    **Changed cs kodu** varken **Allow Clear** özelliğinin **gidip gelme hatası** düzeltildi.
- 50743 - Web arayüzünde sol menü pinlendiğinde **Tüm Uygulamalar butonunun** yanıt
    vermemesi ve bir form ile akış başlatıldığında **Akış Tarihçesi açıkken tekrar yeni bir**
    **akış başlatılamama hatası** düzeltildi.
- 50744 - Web arayüzünde **üst menüde açılan formlar** ve **uygulamalar** arasında üst
    menüdeki **ileri geri butonları ile geçiş hatası** düzeltildi.
- 51660 - Web arayüzünde **proje içerisindeki butonun farklı uygulamayı tetiklememe**
    hatası düzeltildi.
- 48179 - Web arayüzündeki **Lookup** nesnelerinin bazılarında **"```<```" işaretinin**
    **görünmeme hatası** düzeltildi.
- 48181 - Web arayüzünde **parametre alan Lookup** nesnesinde liste **yenilendiği** zaman
    **ComboBox ‘ta bulunan listede eski veriler gösterilme** hatası düzeltildi.


- 48203 - Web arayüzünde formda **FormViewer** nesnesinin içerisine gömülmüş olan
    formun **kodlu nesneleri** tetiklendiğinde **FormViewer nesnesinin hata verme durumu**
    düzeltildi.
- 37693 [DR3941] - Web arayüzü **Giriş** ekranında **domain** isminin **Configurations**
    **tablosu üzerinden özelleştirilememe** hatası düzeltildi.
- 51221 - Web arayüzünde **form instance** ile **ComboBox** , **ListBox** ve **TagBox**
    nesnelerine **değer atama** işlemi gerçekleştirme esnasında **bazı değerlerin boş gelme**
    **hatası** düzeltildi.
- 51427 - Web arayüzünde, **Time kolonu filtrelerinin çalışmama hatası** düzeltildi.
- 51451 - Web arayüzünde **Datagrid'de bulunmayan** bir veri arama barında
    aratıldığında, ardından Datagrid boş gözükürken **Yeni Satır Ekle butonuyla**
    Datagrid'de **filtre yapılmadan** olan **bir verinin ID değeri ile yeni bir veri eklenebilme**
    hatası düzeltildi.
- 48118 [DR7561] - Web arayüzünde **Parametreli** formda yer alan **Save on: Row**
    **Change** olan **Datagrid** nesnesiyle **kayıtların birbirini ezme hatası** düzeltildi.
- 50051 - Web arayüzünde formda **NumberBox** nesnesinin belirlenen **Value** değerinin
    **nesne üzerinde gözükmeme hatası** düzeltildi.
- 51034 - Web arayüzünde **Datagrid Save on : Row Change** seçiliyken onaycıya akış
    gönderildikten sonra **satır eklenmek istendiğinde** alınan **Insert Row hatası** düzeltildi.
- 51447 - Web arayüzünde **Datagrid** nesnesi **Save on: Row Change** özelliği aktifken
    **arama alanının çalışmama hatası** düzeltildi.
- 51965 - Web arayüzünde **Datagrid** nesnesi **Save on: Row Change** özelliği aktifken
    **Primary Key** kolonunun **DocumentID** bazında kontrol edilerek **eklenmeme** hatası
    düzeltildi.
- 49403 - Web arayüzünde **Date** , **DateTime** kolonlarında **İnput** alana **veri girişi**
    **yapılırken aratılması** sağlandı.
- 44409 [DR6511] - Web arayüzünde **Atama** nesnesinde **Pozisyon** kullanıcısının
    **amirine atama işlemi yaparken oluşan hata** düzeltildi.
- 51 509 [DR8401] - Web arayüzünde **Sol menü pinlendikten** sonra Tüm Uygulamalar
    butonu ile **Tüm Uygulamalar listelenmesinden** sonra **sayfa yenilendiğinde Tüm**
    **Uygulamalar butonunun yanıt vermeme** hatası düzeltildi.
- 51329 - Web arayüzünde **'Bir şeyler ters gitti'** uyarısındaki **'Ana sayfaya dön'**
    **butonunun çalışmama hatası** düzeltildi.
- 50763 - Web arayüzünde **DataGrid Datasource Type: Aksiyon** seçiliyken oluşturulan
    kolonlarda **nbactionid kolonu boş gelme** hatası düzeltildi.
- 49997 - Web arayüzünde, **IT talep projesini gönderirken alınan hata** düzeltildi.
- 48212 - Web arayüzü formdaki **Drawer** ve **Popover** özelliklerinin kullanıldığı **Lookup**
    nesnelerinde **Sütun Seçici** özelliğinin **sayfa üzerinde** görüntülenmesi gerekirken,
    **sayfa arkasında görünme hatası** düzeltildi.
- 48217 - Web arayüzünde **forma eklenen buton boyutlarının farklı olma hatası**
    düzeltildi.


- 48257 - Web arayüzünde **DataGrid** nesnesi **Image** kolonu **Primary key** olarak
    belirlendiğinde **satıra eklenen görsel kaldırılıp tekrar yüklenince oluşan hata**
    düzeltildi.
- 48289 - Web arayüzünde **Giriş ekranında Qr Code Text’ten** dolayı **Qr Code**
    **okunamama hatası text konumunun değiştirilmesiyle** düzeltildi.
- 50768 - Web arayüzü **Aksiyon Yönetimi** modülünde bir aksiyon açıldığında, gelen
    **kanban ekranında sürükleme işleminin yapılamama** hatası düzeltildi.
- 51990 - Web arayüzünde **DataGrid** nesnesi **Save On: Row Change** seçiliyken **Multi-**
    **Language kolonundaki güncelleme hatası** düzeltildi.
- 50901 - Web arayüzünde **Datagrid** nesnesi **Object** nesnesi **filtrelerinin çalışmama**
    **hatası** düzeltildi.
- 52291 [DR8660] - Web arayüzünde **DataGrid Cell** modundayken, kolonlarda **Ekle** ve
    **Güncelle** işlemleri sırasında **kolon isimlerinde oluşan kayma hatası** düzeltildi.
- 52461 - Web arayüzünde **Datagrid’e aynı anda veri ekleyen iki kullanıcı** olduğunda
    birinin formunda **verilerin tamamı gözükürken** diğerinde **Yenile** butonuna
    **tıklamadan veriler gelmemekte** , bu durumdayken görünen verinin aynısını bir
    kullanıcı silmekte iken diğer kullanıcı **silinen veriyi görmeye devam ettiği için**
    üzerinde işlem yapmak istediğinde alınan hata düzeltildi.


### 3.2. Geliştirme Arayüzü

- 40652 - Geliştirme arayüzünde **Şifremi Unuttum** diyerek **mail** üzerinden **şifre**
    **sıfırlandığında** , **otomatik giriş yaparak tekrar web arayüzüne yönlendirme hatası**
    düzeltildi.
- 42846 [DR6156] - Geliştirme arayüzünde
    **ServiceApi.DocumentManagement.GetDownloadUrl** metoduyla alınan
    **downloadUrl** 'ler çalıştırıldığında **dosyanın kendi ismiyle indirilmeme hatası**
    düzeltildi.
- 46110 [DR6666] - Geliştirme arayüzünde formda yer alan **Datagrid** nesnesi kolonları
    **Visible** özelliği **pasif** olduğunda **PDF'e aktarıldığında gösterilmesi** sağlandı.
- 47971 - Geliştirme arayüzünde **Alt Akış nesnesinden geçen sürecin tekrarlanma**
    **hatası** düzeltildi.
- 47812 [DR7527] - Geliştirme arayüzünde **Datasource** klasörü altında **ProcessItems'ın**
    **oluşmama hatası** düzeltildi.
- 48104 - Geliştirme arayüzünde **Datasource İlişkili ya da Aksiyon Tipinde Kolonları**
    **Üret** dediğimizde, **GetRelationalControls endpointinden** dönen hata düzeltildi.
- 48112 - Geliştirme arayüzünde **projeleri yayınlarken alınan hata** düzeltildi.
- 48130 - Geliştirme arayüzünde **projeleri yayınlarken alınan identifier expected**
    **hatası** düzeltildi.
- 48455 - Geliştirme arayüzünde **Akış Yöneticisinde Rollback işlemi yaparken hata**
    **verme** durumu düzeltildi.
- 48973 - Geliştirme arayüzünde **projede Deploy alınamama hatası** düzeltildi.
- 49011 - Geliştirme arayüzünde **Akışa** eklenen nesnelerde **default** olarak oluşan nesne
    özelliklerinin **Azerice karşılığı bulunmama** ve **Akış Durumu nesnesindeki değerlerin**
    **boş gelme hatası** düzeltildi.
- 49475 [DR7929] - Geliştirme arayüzünde **Form** ekranında bulunan **Lookup** nesnesinin
    **value** değeri, Akış tarafında forma bağlı olan **değişken nesnesinde 0 olarak gözükme**
    **hatası** düzeltildi.
- 49490 [DR7939] - Geliştirme arayüzünde **Akış** tarafında **Service Api ile Lookup**
    nesnesine **Value atama** işleminde hata **formInstance.Controls["Lookup1"].Value =**
    **new List```<Object>```(){1,2};** kullanılarak çözüm sağlandı.
- 49570 - Geliştirme arayüzünde **Akış** tarafında **Lookup** nesnesinde **Value** atamasında
    **Form.Controls["Lookup1"].Value =**
    **JArray.Parse(Newtonsoft.Json.JsonConvert.SerializeObject(new List```<object>```(){1, 3,**
    **4})); JArray** desteği sağlandı.
- 32923 - Geliştirme arayüzünde **Datasource** klasörü altında **DateTime parametresi**
    içeren sorgunun, formdaki nesnelerde **Datasource** bağlantısında **değer türünde Date**
    **olarak gözükme hatası** düzeltildi.
- 41269 - Geliştirme arayüzünde yeni bir klasör oluştururken İnput kısmında
    **Placeholder** olarak görünen **YENİ KLASOR yazım hatası Klasör Adı olarak yazılarak**
    **hata** düzeltildi.


- 48869 - Geliştirme arayüzünde **default** görünüm **haricindeki diğer görünümlerde**
    **Datasource** seçilmek istendiğinde **Display Expression** ve **Display format alanlarında**
    **değer seçilememe hatası** düzeltildi.
- 42875 - Geliştirme arayüzünde **Hesabım** kısmındaki **Vekâlet ve Erişim Anahtarları**
    bölümünden **Yeni Vekâlet Oluşturma** işleminde kullanıcı listesinde durumu **pasif**
    olan **kullanıcıların listelenme hatası** düzeltildi.
- 43598 [DR6334] - Geliştirme arayüzünde **Akış Tetikleme** nesnesinde **parametre**
    eklerken **Control** tipi seçildiğinde **tarayıcının donma hatası** düzeltildi.
- 44004 - Geliştirme arayüzünde **Akış** nesnelerinde **Object Name** alanına veri girilip boş
    bir alana tıklandığında, **Özellik Görüntüleyicinin Yükleniyor olarak kalma hatası**
    düzeltildi.
- 44083 - Geliştirme arayüzünde Akışa eklenen **Karşılaştırma nesnesi özelliği kullan**
    alanının **İngilizce dilinde olmama hatası** düzeltildi.
- 45703 - Geliştirme arayüzünde formda **Tabs** nesnesi içerisindeki **Section'ların**
    birinden diğerine nesne taşınmak istendiğinde, **nesnenin dışarı atılıp taşınmama**
    **hatası** düzeltildi.
- 47464 [DR7384] - Geliştirme arayüzünde formda bulunan bir **DataGrid** , **PDF'e Aktar**
    **nesnesi** ile **PDF'e** aktarılırken **hangi kolonların aktarılacağının seçilebilmesi** sağlandı
    ve **DataGrid** kolonlarındaki **Disable to Export** ve **Visible** özelliklerinin **birbirinden**
    **bağımsız çalışması sağlanarak hata** düzeltildi.
- 45951 - Geliştirme arayüzünde **Tabs** nesnesini kopyalayıp **başka bir Section** içerisinde
    **yapıştır** dediğimizde, **yapıştırma işlemini yapmama hatası** düzeltildi.
- 47595 - Geliştirme arayüzünde formda **NumberBox** nesnesinin **Step** alanına **virgüllü**
    (double) **sayı girilememe hatası** düzeltildi.
- 47902 - Geliştirme arayüzünde **Continue** , **ContinueWhenErrorOccurred** , **Else** ,
    **NoManager** , **Send, Approve, Reject, Cancel** ve **Timeout** olaylarının **renk hataları**
    düzeltildi.
- 47928 - Geliştirme arayüzü **Akış Özellikleri** ekranında bulunan ve **History** sekmesinin
    altındaki **KeepCancelled & KeepTimeouts** onay kutucukları **ara yüzden** kaldırıldı.
- 47929 - Geliştirme arayüzünde nesnelerdeki **Button Alignment** alanı **boş olarak** gelip
    kaydedilmediği için **EventButtonGroup hatası** düzeltildi.
- 47954 - Geliştirme arayüzünde **Rest** sorgusunun **ValueType** değerinin form tarafına
    **unknown olarak set edilme sorunu** düzeltildi.
- 47958 - Geliştirme arayüzünde filtrelenerek **Akış Yöneticisinden** görüntülenen
    projeleri **Delete'e göre OrderBy** olacak şekilde **sıralanmak istendiğinde sayfanın**
    **hataya düşmesi** düzeltildi.
- 47972 - Geliştirme arayüzü **Akış Yöneticisinde** üzerinde **ünlem** olan **İstatistikleri**
    **Göster** butonuna tıklandığında **grafik panelinin açılmama hatası** düzeltildi.
- 48025 - Geliştirme arayüzünde **Dosya** menüsünde **Yeni Boş Proje Aç** ekranında
    **dashboard seçiminin görünme hatası** düzeltildi.


- 48085 - Geliştirme arayüzünde **Aksiyon Oluşturucu** nesnesinin **Parameter** alanına
    **Datagrid kolonlarının gelmeme hatası** düzeltildi.
- 48154 - Geliştirme arayüzünde **Form Özelliklerinde Caption** özelliğine veri girişi
    yapılırken, **Caption** kutucuğu **genişleme ve veri girişi için tekrar tıklamanın gerekme**
    **hatası** düzeltildi.
- 44809 [DR6535] - Geliştirme arayüzünde formdaki bir DataGrid **PDF'e Aktar** nesnesi
    kullanılarak **PDF'e aktarıldığında** oluşan tablodaki **tüm hücreler aynı boyutta oluşma**
    **hatası** düzeltildi.
- 49599 [DR7978] - Geliştirme arayüzünde **FormInstance** üzerinden **formdaki bir**
    **DataGrid'e bağlanmama** hatası düzeltildi.
- 48101 [DR7608] - Geliştirme arayüzünde **Start Immediately** olarak başlatılan akışın
    Web arayüzünde **Pozisyon** nesnesine geldiğinde **formun açılmama hatası** düzeltildi.
- 49022 - Geliştirme arayüzünde **Azerbaycan** dilindeyken oluşturulan **Hızlı Arşiv**
    formlarında **Datagrid kolon isimleri** ve **Caption alanının gelmeme** hatası düzeltildi.
- 49669 [DR7998] - Geliştirme arayüzünde **projeyi yayınlama** işleminde **"The given key**
    **'Column2' was not present in the dictionary." hatası** düzeltildi.
- 49670 [DR7994] - Geliştirme arayüzünde **projeyi derleme** işleminde " **The given key**
    **'Panel2' was not present in the dictionary." hatası** düzeltildi.
- 36736 - Geliştirme arayüzünde, DataGrid **Open a Selection Form** tipindeki **Toolbar**
    **Buttonunda Selection Settings** özelliği **aktif** edildiğinde, **Single** ve **Multiple** seçimden
    bağımsız gelen **Show Select All** özelliğinin görünürlüğü **Multiple** seçime bağlanarak
    hata düzeltildi.
- 41280 [DR5725] - Geliştirme arayüzünde **form içe aktarma işlemi** ile form
    aktarıldıktan sonra **Caption** kısmına ait **Multilanguage alanlarının güncellenmeme**
    hatası düzeltildi.
- 45167 - Geliştirme arayüzünde **forma eklenen nesne** ve **onun Mirror nesnesi farklı**
    **Section** içerisindeyse, **nesnede yapılan değişikliğin Mirror nesnesine yansımama**
    hatası düzeltildi.
- 46606 - Geliştirme arayüzünde form ekranında **Lookup** nesnesinde **Columns** özelliği
    içerisinde **DateTimeOffset** değere sahip verinin **date olarak gözükmesi sorunu**
    düzeltildi.
- 50069 [DR8113] - Geliştirme arayüzünde **Datasource** klasörü altında **Oracle**
    **sorgusunda parametre hatası** düzeltildi.
- 49961 - Geliştirme arayüzünde **Akış** tarafında **FormInstance** ile **ListBox.Text**
    **değerinin boş gelme hatası** düzeltildi.
- 50755 - Geliştirme arayüzünde **CheckInCheckout** özelliği **aktif** olduğunda Kullanıcı
    Grubundaki onaycılardan **birinin formu açtığında diğerinin açmasının engelleneme**
    hatası düzeltildi.
- 45513 - Geliştirme arayüzünde **İş Akış Yönetimi Steps** sekmesinde **Pozisyon Grubu**
    **adımının silinme hatası** düzeltildi.


- 46608 - Geliştirme arayüzünde **Akış** tarafında **GeoLocation** özelliği aktif edilen
    **Pozisyon** ve **Pozisyon Grubu** nesnelerinin **Request** bilgilerinde **GeoLocation bilgisinin**
    **kaydedilmeme hatası** düzeltildi.
- 47105 - Geliştirme arayüzünde **Akış** tarafında **Mail Template** içerisine eklenen
    **{{Reason}} değerinin mail içeriğinde gözükmeme** hatası düzeltildi.
- 49461 - Geliştirme arayüzünde **Edit Message Source Switch'i** aktif edilip **Source**
    **Message'a** tıklandığında, **Mail Template alanı açılmama hatası** düzeltildi.
- 49985 [DR8088] - Geliştirme arayüzünde **projeyi derleme** işleminde
    **Sublayers.Builder.BuildProjectAsync hatası** düzeltildi.
- 39447 - Geliştirme arayüzünde **Akış** tarafında **Doküman Oluştur** nesnesinde **Path**
    **Type** özelliklerinin **İngilizce olmaması** düzeltildi.
- 48959 [DR7819] - Geliştirme arayüzünde **Array** tipte **Datasource** bağlı **Selection**
    formda **parametre değişmeme hatası** düzeltildi.
- 49285 - Geliştirme arayüzünde **formdaki nesnelerin kopyalanmama hatası** düzeltildi.
- 49486 [DR7935] - Geliştirme arayüzünde **Build** işlemi sırasında **log yazmama hatası**
    düzeltildi.
- 49749 [DR8036] - Geliştirme arayüzünde **Datagrid** nesnesi **Object** tipli kolonlarına
    **sorgu** bağlandığında, **ortamın donma hatası** düzeltildi.
- 50045 [DR8099] - Geliştirme arayüzünde **Form** üzerinde **gözükmeyen ve nesne**
    **gezgininde gözüken bir nesnenin silinmeme hatası** düzeltildi.
- 50046 [DR8097] - Geliştirme arayüzünde **Dosya Adı** alanında **Kopyala Yapıştır**
    yönteminin **kullanılamama hatası** düzeltildi.
- 50056 - Geliştirme arayüzünde **Statik FishBone** nesnesinin bir ögesine **Dinamik öge**
    **eklemek** istediğimizde **ortamın komple donma hatası** düzeltildi.
- 50240 - Geliştirme arayüzünde formda **kopyalanıp yapıştırılan nesneler silindiğinde**
    veya **formda başka yere taşındığında** alınan hata düzeltildi.
- 50275 - Geliştirme arayüzü **Görünüm Yöneticisinde Görünüm Ekle** butonunun
    **gözükmeme hatası** düzeltildi.
- 50302 [DR8095] - Geliştirme arayüzünde form açıkken **Araç Kutusuna tıklandığında**
    **Akış Araç Kutusunun görüntülenme hatası** düzeltildi.
- 50343 - Geliştirme arayüzü **Görünüm Yöneticisi** ekranı **Default** görünümüne her
    seferinde **çoğaltma işlemi yapıldığında oluşan sıralama hatası** düzeltildi.
- 50344 - Geliştirme arayüzünde **farklı** görünümlerde **Visible** özelliğinin **Tüm**
    **Görünümlere Uygula** dedikten sonra **açılıp kapanma işlevini kaybetme hatası**
    düzeltildi.
- 50358 - Geliştirme arayüzünde **Show Colon Switch'inin Tüm Görünümlere Uygula**
    denildikten sonraki **aktif - pasif durumlarındaki çalışmama hatası** düzeltildi.
- 50363 - Geliştirme ortamı farklı görünümlerde **Horizontal Align - Vertical Align -**
    **Mark Position** özelliklerinin **görünümler arasında değiştirilememe hatası** düzeltildi.


- 50382 - Geliştirme arayüzünde nesnelere **uzun etiket girildiğinde** ve **Ellipsis** özelliği
    açıldığında, Position kısmı **Left ya da Right** yapıldığı zaman **görünümde oluşan**
    **bozukluklar** düzeltildi.
- 50384 - Geliştirme ortamında farklı görünümlerde **Appearance** alanın altındaki
    **Visible, ClientVisible, Enable, ClientEnable** , **Show Characters Column** anahtarlarının
    **True - False** durumlarının **tüm görünümlerde güncellenmeme hatası** düzeltildi.
- 50542 - Geliştirme arayüzünde oluşturulan görünüm **Ctrl - Z** kısayolu ile silinip üst
    menüden **görünüm değişikliği yapılmak istendiğinde oluşan hata** düzeltildi.
- 50853 - Geliştirme arayüzünde **ComboBox** nesnesinde **Datasource** parametre tipi
    **Boolean** olduğu halde **Array gönderilme hatası** düzeltildi.
- 50974 - Geliştirme arayüzünde **DataGrid** nesnesi **Datasource** bağlandıktan sonra
    **Editing Settings mode: Row, Cell ve Batch seçeneklerinin gelmesi** sağlandı.
- 51171 - Geliştirme arayüzünde form üzerindeki **bir nesne silinip** form
    kaydedildiğinde **Özellik Görüntüleyici üzerindeki butonların çalışmama** hatası
    düzeltildi.
- 41022 [DR5600] - Geliştirme arayüzünde **Araçlar** menüsünün **Akış Yöneticisi**
    kısmında **ilgili süreç seçilerek** silindiğinde, Akış Yöneticisi sekmesinin **Geçmiş**
    **menüsünden sürecin silinmeme hatası** düzeltildi.
- 51922 [DR8585] - Geliştirme arayüzünde **İngilizce Giriş** yapılmasına rağmen **Label**
    **değerlerinin Azerice gelme hatası** düzeltildi.
- 51949 - Geliştirme arayüzünde **SAPQuery BAPI Browser'a** tıklandığında **GetTreeInit**
    endpointinin **500 dönme hatası** düzeltildi.
- 49815 - Geliştirme arayüzünde **Özellik Görüntüleyici** üzerindeki **Font** alanında
    **bulunan seçeneklerin eksik çalışma hatası** düzeltildi.
- 52023 - Geliştirme arayüzünde **Akış Yöneticisi** modülünde herhangi bir kritere göre
    **filtreleme yapılmama hatası** düzeltildi.
- 51584 - Geliştirme arayüzünde **VectorMap** nesnesinin **Annotations** özelliğine
    eklenmiş bir öge **silindiğinde ortamın hata verme durumu** düzeltildi.
- 51909 - Geliştirme arayüzünde **SAPQuery BAPI browser** olarak girilip seçim
    yapıldığında **konsol hatası verme durumu** düzeltildi.
- 49817 - Geliştirme arayüzünde **PDF** format nesnesinde **Naming format** alanında
    **kullanılmayan format tiplerinden** kaynaklı oluşan hata ve **değişken nesnesinde**
    belirtilen değer ile **{{Variable1.Value}} PDF Naming** formatı **oluşturulamama hatası**
    düzeltildi.
- 48243 - Geliştirme arayüzünde **DataGrid** kolonlarından seçilen **Icon Source Field** göre
    **Icon Matchers** alanından seçilen ikon **kolon değişse bile kalmaya devam etme** hatası
    düzeltildi.
- 48263 - Geliştirme arayüzünde **Action** klasörü üzerinden **Yeni Aksiyon Durumu**
    **Ekleme** işlemi yapılmak istendiğinde **Yeni Durum** ekranının **sayfa üzerinde**
    **ortalanmama hatası** düzeltildi.


- 48272 - Geliştirme arayüzünde form nesnelerinin **Text** ve **Caption** özelliklerine **veri**
    **girişi yapılırken imlecin çıkma hatası** düzeltildi.
- 48275 - Geliştirme arayüzü **Özellik Görüntüleyicideki** girişlere **hızlı bir şekilde** değer
    girilirken, **girişteki odağın ortadan kalkarak** tekrar **ilgili girişe tıklanma**
    **gereksiniminin oluşma hatası** düzeltildi.
- 48295 - Geliştirme arayüzünde **Akış** tarafında **kaydetme işleminde TimeOut hatası**
    düzeltildi.
- 52402 - Geliştirme arayüzünde **Akış** tarafında **Documents** özelliği bulunan nesnelerde
    **Documents** içerisindeki dokümanlara tıklandığında, **görünüm bilgilerinin değişme**
    **hatası** düzeltildi.


### 3.3. Android

- 44431 - **Android** cihazların **mobil arayüzünde** , **Native+** ve **Webview** görünümündeki
    **TreeView** nesnesinde seçilen **Dinamik** verilerin **bir sonraki kullanıcıya gitmeme hatası**
    düzeltildi.
- 49108 - **Android** cihazların **mobil arayüzünde** , **Native+** görünümündeki **HTMLTextBox**
    nesnesinde **fonksiyonların düzgün kullanılamaması** ve **imlecin gel git yapma** hataları
    düzeltildi.
- 47041 - **Android** cihazların **mobil arayüzünde** , **Webview** görünümündeki **Button** nesnesi
    ile açılan **Open A Form** özelliğindeki formda yer alan **DateRangePicker** nesnesinin
    **ReadOnly gibi davranmama hatası** düzeltildi.
- 44526 - **Android** cihazların **mobil arayüzünde** , **Native+** görünümündeki **Events DataGrid**
    nesnesinde **Yenile butonunun bulunmama** hatası düzeltildi.
- 49705 - **Android** cihazların **mobil arayüzünde** , **Webview** görünümündeki **Arşiv DataGrid**
    nesnesinde, **Start A Process** ile açılan formun **Native** + **görünümünde açılma** hatası
    düzeltildi.
- 49978 - **Android** cihazların **mobil arayüzünde** , **Native+** görünümündeki formda **Button**
    ile **form görünümünün değiştirilememe hatası** düzeltildi.
- 50104 - **Android** cihazların **mobil arayüzünde** , **Native+** görünümündeki **Statik DataGrid**
    nesnesinde **düzenleme işlemi esnasında verilerin gelmeme** hatası düzeltildi.
- 48201 - **Android** cihazların **mobil arayüzünde** , **Native+** görünümündeki **Visible** özelliği
    **False** olan **TextArea** nesnesinin **görünme hatası** düzeltildi.
- 47762 [DR6499] - **Android** cihazların **mobil arayüzünde,** projenin akışında D **oküman**
    **Oluştur** nesnesi olup, akış başlangıcında ise **Start Immediately** özelliği **aktif**
    durumdayken **formun yükleme ekranında kalması** ve **Akış Tarihçesi sayfasının**
    **açılmaması hataları** düzeltildi.
- 51442 - **Android** cihazların **mobil arayüzünde** , **Native+** görünümünde **Required** nesneler
    için **kırmızı çerçeve verilmemesi** ve **uyarı yazısının kutucuk altında çıkmaması** hataları
    düzeltildi.
- 45382 - **Android** cihazların **mobil arayüzünde** , **Native+** durumunda olan **DataGrid**
    nesnesinde **Filtre Disable** durumunda olduğunda **Sorting işleminin yapılamama hatası**
    düzeltildi.
- 51511 - **Android** cihazların **mobil arayüzünde** , **Native+** görünümündeki **OSF DataGrid**
    nesnesinde **Searching Enabled** özelliği **pasif** olmasına rağmen **Search alanının gelme**
    **hatası** düzeltildi.
- 38941 - **Android** cihazların **mobil arayüzünde** , onaya gelen form açılıp süreç devam
    ettirildiğinde **onaylardaki konumunun güncellenmeme** hatası düzeltildi.
- 50272 - **Android** cihazların **mobil arayüzünde** , **Native+** görünümündeki **Related**
    **Documents** nesnesine **bazı formattaki dosyaların yüklenememe hatası** düzeltildi.


### 3.4. IOS

- 44431 - **IOS** cihazların **mobil arayüzünde** , **Native+** ve **Webview** görünümündeki
    **TreeView** nesnesinde seçilen **Dinamik** verilerin **bir sonraki kullanıcıya gitmeme**
    **hatası** düzeltildi.
- 44695 - **IOS** cihazların **mobil arayüzünde** , **Native+** görünümündeki **Lookup**
    nesnesinde **filtreleme yapılamama hatası** düzeltildi.
- 47052 - **IOS** cihazların **mobil arayüzünde** , **Native+** görünümündeki **RadioList** ve ya
    **Button** nesnesi üzerinden **ChildForm** açılmak istendiğinde **iki kere açılma hatası**
    düzeltildi.
- 46623 - **IOS** cihazların **mobil arayüzünde** , **Native+** görünümündeki **Dinamik RadioList**
    nesnesindeki verinin **sonraki kullanıcıda değiştirilememe hatası** düzeltildi.
- 44526 - **IOS** cihazların **mobil arayüzünde** , **Native+** görünümündeki **Events DataGrid**
    nesnesinde **Yenile butonunun bulunmama** hatası düzeltildi.
- 49707 - **IOS** cihazların **mobil arayüzünde** , **Webview** görünümündeki **Iframe**
    nesnesinde **URL gelmeme hatası** düzeltildi.
- 49976 - **IOS** cihazların **mobil arayüzünde** , **Native+** görünümündeki formda **Button** ile
    **form görünümünün değiştirilememe hatası** düzeltildi.
- 47762 [DR6499] - **IOS** cihazların **mobil arayüzünde,** projenin akışında D **oküman**
    **Oluştur** nesnesi olup, akış başlangıcında ise **Start Immediately** özelliği **aktif**
    durumdayken **formun yükleme ekranında kalması** ve **Akış Tarihçesi sayfasının**
    **açılmaması hataları** düzeltildi.
- 51442 - **IOS** cihazların **mobil arayüzünde** , **Native+** görünümünde **Required** nesneler
    için **kırmızı çerçeve verilmemesi** ve **uyarı yazısının kutucuk altında çıkmaması**
    hataları düzeltildi.
- 45382 - **IOS** cihazların **mobil arayüzünde** , **Native+** durumunda olan **DataGrid**
    nesnesinde **Filtre Disable** durumunda olduğunda **Sorting işleminin yapılamama**
    **hatası** düzeltildi.
- 52077 - **IOS** cihazların **mobil arayüzünde** , **Native+** görünümündeki
    **DocumentMetaData** nesnesindeki **butonun küçük görünme hatası** düzeltildi.
- 51483 - **IOS** cihazların **mobil arayüzünde** , **Native+** görünümündeki **DataGrid**
    nesnesinde **Yenile butonu bulunmama** hatası düzeltildi.
- 49419 - **IOS** cihazların **mobil arayüzünde** , **Native+** görünümündeki **Parametrik**
    formda **Date kolonu Primary Key** olan **Row** ve **Cell DataGrid** nesnelerinde **silme**
    **işleminde yükleniyor aşamasında kalma hatası** düzeltildi.
- 38941 - **IOS** cihazların **mobil arayüzünde** , onaya gelen form açılıp süreç devam
    ettirildiğinde **onaylardaki konumunun güncellenmeme** hatası düzeltildi.
- 49145 - **IOS** cihazların **mobil arayüzünde** , **Native+** görünümündeki **ReadOnly**
    özelliğinde olan **ColorPicker** nesnesinde **renk seçimi yapılabilme hatası** düzeltildi.
- 51554 - **IOS** cihazların **mobil arayüzünde** , **Native+** görünümündeki
    **DocumentMetaData** nesnesinin **butonunun gelmeme hatası** düzeltildi.


- 51586 - **IOS** cihazların **mobil arayüzünde** , **Native+** görünümündeki **ReadOnly**
    özelliğinde olan **NumberBox** nesnesinde **değerin negatife çevrilebilme hatası**
    düzeltildi.
- 51612 - **IOS** cihazların **mobil arayüzünde** , **Native+** görünümündeki **Enabled** özelliği
    **Pasif** olan **DateTimePicker** nesnesinde **değişiklik yapılabilme hatası** düzeltildi.
- 52079 - **IOS** cihazların **mobil arayüzünde** , **Native+** görünümündeki **Lookup**
    nesnesinde **Filtering Disabled** özelliğindeyken **Sorting işleminin yapılamama hatası**
    düzeltildi.
- 52407 - **IOS** cihazların **mobil arayüzünde** , **Native+** görünümündeki **SplineChart**
    nesnesinden kaynaklı **meydana gelen çökme hatası** düzeltildi.
- 52280 - **IOS** cihazların **mobil arayüzünde** , **Native+** görünümündeki **Open A Process**
    **DataGrid** nesnesinde **uygulamanın çökme hatası** düzeltildi


## 4. Breaking Changes

1. Projeler **tekrar** yayınlanmalıdır.
2. DataGrid'e **Datasource** bağlayıp **Columns** ürettiğinizde eğer **STATUS** kolonu varsa,
**Columns** özelliklerinden **Kontrol** sekmesine geçerek **Data Definition Language Field Name**
bilgisinin **değiştirilmesi** gerekmektedir. **STATUS** adı **rezerve bir alan** olarak güncellenmiştir.
Bu nedenle var olan projelerde **STATUS** kolonu **Data Definition Language(DDL) Field Name
değiştirmeniz** gerekmektedir.
3. **Service Api instance'ı üretilirken** ;

```
var serviceApi = new ServiceAPI("https://bimser.net/api/web");
veya var serviceApi = new ServiceAPI("dev");
```
```
şeklinde kullanıldığında alınan hatanın çözülmesi için bu kullanımın credential verilen
constructorlardan biriyle değiştirilmesi gerekmektedir.
```
```
public ServiceAPI(LoginWithBasicAuthenticationParameters loginParameters,
string apiUrlOrInstanceName,
LogSeverity logSeverity = LogSeverity.Information,
ITelemetryCollectorHolder telemetryCollectorHolder = null)
```
```
public ServiceAPI(LoginWithTokenAuthenticationParameters loginParameters,
string apiUrlOrInstanceName,
LogSeverity logSeverity = LogSeverity.Information,
ITelemetryCollectorHolder telemetryCollectorHolder = null)
```
```
public ServiceAPI(LoginWithAccessTokenParameters loginParameters,
string apiUrlOrInstanceName,
LogSeverity logSeverity = LogSeverity.Information,
ITelemetryCollectorHolder telemetryCollectorHolder = null)

```

<font size="5"><a href="https://portal.synergynow.io/#/_redirect/7ZwGl6hygNgygP6mh5gITl"  target="_blank"><svg fill="currentColor" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" viewBox="0 0 40 40" style={{verticalAlign: "middle"}}><g><path d="m35.8 8.5q0.6 0.6 1 1.7t0.5 1.9v25.8q0 0.8-0.6 1.5t-1.6 0.6h-30q-0.9 0-1.5-0.6t-0.6-1.5v-35.8q0-0.8 0.6-1.5t1.5-0.6h20q0.9 0 2 0.4t1.7 1.1z m-9.9-5.5v8.4h8.4q-0.3-0.6-0.5-0.9l-7-7q-0.3-0.2-0.9-0.5z m8.5 34.1v-22.8h-9.3q-0.9 0-1.5-0.6t-0.6-1.6v-9.2h-17.1v34.2h28.5z m-11.4-13.2q0.7 0.6 1.8 1.3 1.3-0.2 2.6-0.2 3.3 0 4 1.1 0.4 0.5 0 1.2 0 0 0 0l0 0v0.1q-0.2 0.8-1.6 0.8-1.1 0-2.6-0.4t-2.9-1.2q-4.9 0.5-8.7 1.8-3.4 5.9-5.4 5.9-0.4 0-0.7-0.2l-0.5-0.2q0-0.1-0.1-0.2-0.3-0.2-0.2-0.8 0.2-0.8 1.3-2t2.9-2.1q0.3-0.2 0.5 0.1 0.1 0 0.1 0.1 1.1-1.9 2.4-4.4 1.5-3.1 2.3-5.9-0.5-1.8-0.7-3.5t0.2-2.9q0.2-0.9 0.9-0.9h0.5q0.5 0 0.8 0.4 0.4 0.4 0.2 1.5-0.1 0.1-0.1 0.2 0 0 0 0.1v0.7q0 2.8-0.3 4.3 1.2 3.7 3.3 5.3z m-12.9 9.2q1.2-0.6 3.1-3.5-1.2 0.8-2 1.8t-1.1 1.7z m8.9-20.6q-0.4 1-0.1 3 0.1-0.2 0.2-1 0-0.1 0.1-0.9 0.1-0.1 0.1-0.2 0-0.1 0-0.1t0 0 0 0q0-0.5-0.3-0.8 0 0 0 0v0z m-2.8 14.8q3-1.2 6.4-1.8-0.1 0-0.3-0.2t-0.4-0.3q-1.7-1.5-2.8-4-0.6 2-1.9 4.4-0.7 1.3-1 1.9z m14.4-0.4q-0.5-0.5-3.1-0.5 1.7 0.6 2.8 0.6 0.3 0 0.4 0 0 0-0.1-0.1z"></path></g></svg>PDF Download</a></font>
