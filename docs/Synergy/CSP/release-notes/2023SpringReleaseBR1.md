---
sidebar_position: 2331
sidebar_label: "2023 Spring Release BR1"
custom_edit_url: ""
---


# Bimser Synergy 2023 Spring Release Notes BR1
*(1 Mayıs 2023 - 31 Mayıs 2023)*

## 1. No [Highlights / New Features]

## 2. No [Improvements]


## 3. Fixes

### 3.1. Web Arayüzü

#### 3.1.1. Doküman Yönetimi

- 47085 [DR7084] - Web arayüzünde **Doküman Yönetiminde** paylaşılan içerik dilinin
    **Türkçe** olmasına rağmen, **gelen mailin İngilizce olma hatası** düzeltildi.
- 47478 - Web arayüzünde **Doküman Yönetiminde docx** ve **xlsx** dosyalarının
    dizinlenmediği için **kategori oluşturulmama hatası** düzeltildi.
- 38679 - Web arayüzünde **Doküman Yönetiminde MetaData ‘da veri seçilirken**
    oluşan konsol hatası düzeltildi.
- 43114 - Web arayüzü **Doküman Yönetimi** içerisinde **Tüm depolar** bölümünün **Arama**
    kısmında **Aranan deponun** içerisine girildiğinde, **arama alanının açık kalma hatası**
    düzeltildi.
- 45538 - Web arayüzünde **Doküman Yönetiminde Doküman İmzası** oluşturulduktan
    sonra **İmzayı İndir** butonuna **tıklandığında oluşan konsol hatası** düzeltildi.
- 45566 - Web arayüzü **Doküman Yönetiminde** son kullanılan bazı dokümanların **Tarih**
    alanında **Invalid Date şeklinde gözükme hatası** düzeltildi.

#### 3.1.2. İş Akış Yönetimi

- 46432 [DR6993]- Web arayüzünde **İş Akış Yönetimi** kısmında yer alan **Taslaklar**
    içerisinde, **Taslak sürecin görüntülenememe hatası** düzeltildi.

#### 3.1.3. İnsan Kaynakları

- 38287 - Web arayüzünde **İnsan Kaynakları** kısmında **Yeni Kullanıcı** oluştururken yeni
    pencere açıldığında, **pencere boyutu** hareket ederken **Kaydet** butonunun **titreme ve**
    **kaybolma hatası** düzeltildi.
- 46078 [DR6939] - Web arayüzünde **İnsan kaynakları** kısmının **Mesai** menüsünde
    **Mesai adının boşluk karakteri kullanılarak yazılamama** hatası düzeltildi.


#### 3.1.4. Web Ana Sayfa

- 9047 - Web arayüzünde **Elektronik İmza** işlemi sonrasında **DocuSing** alanında, **imza**
    **bilgisinin gösterilmesi ile ilgili hata** düzeltildi.
- 39748 - Web arayüzünde Form seçeneğinde **listenin boş gelme hatası** ve **Search**
    işlemi yapılırken **herhangi bir veri dönmeyip 500 hatası verme durumu** düzeltildi.
- 46727 - Web arayüzünde **Dashboard** ekranındaki **Devam Eden İşler** , **Bilgilendirmeler** ,
    **Bekleyen Onaylar** ve **Başlattığım İşler** gibi kutucuklara tıklandığında, **Süreçler**
    ekranına **verilerin gelmeme ve sorguların silinme hatası** düzeltildi.
- 46918 [DR7001] - Web arayüzünde formda **NumberBox** nesnesinin **Precision**
    özelliğine **boş değer atandığında** , projenin **formun açılması sırasında** hatalar
    meydana gelme sorunu düzeltildi.
- 46937 [DR7218] - Web arayüzünde **Akış Durumu** nesnesinde, **ShowInFlowHistory**
    seçeneğinin **json data** içerisinde **boş olarak gelmesi** ve süreçler ilerletilmek
    istendiğinde **update flow status hatası alınma** sorunları düzeltildi.
- 47878 - Web arayüzünde, **Datagrid** nesneleri olan **formları gönderirken alınan hata**
    düzeltildi.
- 37768 [DR4440] - Web arayüzünde Uygulama Gezgininden **Düğüm İşlem Türü**
    kısmından **"Dış bağlantı"** ve Dış Bağlantı Açma tipini " **Yeni sekmede"** yapıldığında
    **ortamın hata verme sorunu** düzetildi.
- 37943 - Web arayüzünde **Aktiviteler** kısmının **Gelişmiş Mesaj** özelliğinde **“!”** işareti
    kullanılarak **süreç ilişkilendirilememe hatası** ve **TextBox** modunda **mesaj içeriği**
    oluşturulduktan sonra **HtmlText** moduna geçildiğinde oluşturulan **mesaj içeriği**
    **silinme hatası** düzeltildi.
- 41760 - Web arayüzünde formda **Dinamik ListBox** nesnesinde **Arama** işlemi yapılıp
    öge seçildikten sonra **Arama barından çıkıldığında** , nesne içerisindeki **verilerin yer**
    **değiştirme hatası** düzeltildi.
- 43836 - Web arayüzünde formda **Modal** özelliğinde açılan bir akış başlatıldıktan
    sonra **Akış Tarihçesini Göster** butonunun **Tarihçeyi Modal panelin arkasında açma**
    **hatası** düzeltildi.
- 43857 - Web arayüzünde formda **Display Mode** özelliği **icon** olan **Dropdown**
    nesnelerinde **veri gözükmeme hatası** düzeltildi.
- 44254 - Web arayüzünde **Güvenlik** modulünde **butonların düzensiz görülme hatası**
    düzeltildi.
- 45336 - Web arayüzünde **Aktiviteler** alanında **Gelişmiş Aktivite** mesajında
    oluşturulan linkin **Yeni Sekmede Aç özelliğinin çalışmama hatası** düzeltildi.
- 45449 - Web arayüzünde formda **Statik Multiple Treeview** nesnesinin **Show Search**
    özelliğiyle **arama yapıp seçim yaptığımızda** , **bir önceki seçimi silme hatası** düzeltildi.
- 45526 - Web arayüzünde **Yerelleştirme** bölümünde ortam dili **Türkçe** olduğunda ve
    **nesnenin Türkçe etiketleri boş bırakıldığında** onun yerine **İngilizce etiketlerin**
    **gelmeme** hatası düzeltildi.


- 45605 - Web arayüzünde formda **InputGroup** nesnesi **ReadOnly** olmasına rağmen
    içindeki **nesnelere müdahale edilebilme hatası** düzeltildi.
- 45857 - Web arayüzündeki formun, Geliştirme arayüzündeki **Form Özellikleri**
    kısmında **Check-in Check-out Enabled** özelliği **Kapalı** olduğunda **akış ilerlememe**
    **hatası** düzeltildi.
- 46081 [DR6779] - Web arayüzünde formda **DateTimePicker** nesnesinin etkinliklerini
    **temizlemek** için **Text** ve **Value** özelliklerini girdiğimizde, **nesne içeriğinin**
    **temizlenmeme hatası** düzeltildi.
- 46580 - Web arayüzünde **Akış Tarihçesinin** açılıp kapanırken meydana gelen
    **animasyondaki kayma hatası** düzeltildi.
- 46589 - Web arayüzünde **Check-In** ve **Check-Out** kullanılan senaryolarda, **formun**
    **kapanmasına** rağmen **formun Check-Out'a düşmeme hatası** düzeltildi.
- 46599 - Web arayüzünde **Menü** üzerindeki **pinleme** butonunun **çalışmama hatası**
    düzeltildi.
- 46603 - Web arayüzü **Uygulama Gezgininin** menüsünde **daha önce tanımlı menüler**
    **Düzenle** butonu ile açıldığında **Düğüm İşlem Türünün boş gelme hatası** düzeltildi.
- 44911 - Web arayüzünde **DataGrid** nesnesi **Excel'e** aktarılırken **birden fazla indirme**
    hatası düzeltildi.
- 44971 - Web arayüzünde **Datagrid'e** eklenen **MultiLanguage** kolonu **Primary Key**
    olduğu zaman **, yazılan verinin kaydedilmeme hatası** düzeltildi.
- 44973 - Web arayüzünde **Statik Datagrid** nesnesi **TimePicker** kolonu **Primary Key**
    olarak işaretlendiğinde, **akışı gönderirken yaşanan hata** düzeltildi.
- 46744 - Web arayüzünde **Flow History** endpointinde **Items** değeri **boş geldiği için**
    oluşan hata düzeltildi.
- 46778 - Web arayüzünde **Ana Sayfada** sol menü **pinlendiğinde** , **Son Kullanılan**
    **Dokümanlar** alanında **doküman isimlerinin tasarım hatası** düzeltildi.
- 46859 - Web arayüzü **Dashboard** ekranında süreçlerdeki **uzun isimleri sayfada**
    **düzgün görünmeme** hatası düzeltildi.
- 46867 - Web arayüzünde **Devam Eden İşlere** tıklanıp **Süreçler** alanından bir süreç
    seçilmek istendiğinde, **süreç detayında herhangi bir veri görünmeyip** sayfada oluşan
    **konsol hatası** düzeltildi.
- 46871 - Web arayüzünde aynı isimdeki süreçler **farklı bir sürece tıklanmadığı** zaman
    **seçilememe hatası** düzeltildi.
- 46895 - Web arayüzünde bir süreç **seçilip onaylandıktan sonra** konsolda ortaya çıkan
    **panelType hatası** düzeltildi.
- 46906 - Web arayüzünde **Duyurular** sekmesinde **Başlangıçta Göster** olarak
    işaretlenip **yeni bir duyuru eklenince** , **Başlangıçta Göster** olarak işaretlenen bütün
    duyuruların **modal içerisinde görünmeme hatası** düzeltildi.
- 46977 - Web arayüzünde bir akış başlatıldığında ya da bitirildiğinde **Dashboard**
    ekranındaki verilerin **Yenile butonu kullanılarak güncellenmemesi** hatası düzeltildi.


- 47006 - Web arayüzünde **Uygulamalar Menüsü** sabitlendikten sonra **Kullanıcı**
    **Ayarları** sekmesinin **kapanmama** hatası düzeltildi.
- 47070 - **Control Project** ekranından sonra " **Yeni Proje Olarak Aktar** " seçeneği seçilip
    proje adı değiştirilirse **Analyze** endpointine **değiştirilmiş hali gönderilmeme hatası**
    düzeltildi. **Control Project** ekranından sonra " **Yeni Proje Olarak Aktar** " seçeneği
    seçildiğinde **dmpath** seçilmezse de **Analyze** ekranına **devam etme hatası** düzeltildi.
    **Source** ekranından **Target** ekranına geçtikten sonra geri gelip tekrar **Target'a** geçilirse
    **yeniden istek atmama hatası** düzletildi. **Proje Form eşleme** ekranında eğer **Source**
    ekranında **görünüm boş ise Matched View de boş** bırakılabiliyor. **Üç nokta ikonları**
    **Hover** edildiğinde **Cell'in yüksekliğini kaplamama hatası** düzeltildi.
- 47228 - Web arayüzü **Hesabım** kısmında **Vekâlet ve Erişim Anahtarı** sayfalarının
    **Loading durumuna kalma hatası** düzeltildi.
- 47433 - Web arayüzünde **Aktiviteler** kısmında **Gelişmiş** seçeneği işaretlenip **"Herkes**
    **Yanıtlayabilir"** penceresi açıldığında gelen **lisans uyarısı hatası** düzeltildi.
- 47708 [DR7477] - Web arayüzünde, **Client** tarafına yazılan kod ile **Datagrid'e ekleme**
    yapılarak **satır düzenlenmek istendiğinde oluşan hata** düzeltildi.
- 47207 [DR7329] - Web arayüzünde **Refresh Token hatası** düzeltildi.
- 45834 - Web arayüzünde **AksiyonCAPA** sayfasında **Yönlendir** ve **İptal** butonlarında
    açılan formlara **Kaydet denildiğinde oluşan hata** düzeltildi.
- 47213 [DR7331] - Web arayüzünde akış ilerletilirken
    **Bimser.CSP.Workflow.Runtime.Steps.FlowGroup.ExecuteNextStep** hatası düzeltildi.
- 48551 - Web arayüzünde **Masraf Beyan formuna** girildiğinde;
    **Masraf Beyan** formunda bir **masraf kayıt edilip** , **onaydaki diğer kullanıcıya**
    gönderilmektedir. Diğer kullanıcı gelen formu açtığında **ilk kullanıcıdan gelen masraf**
    **Datagrid'de** görünmemektedir. **Datagrid’de birden fazla Ekle Toolbar butonu**
    gelmektedir ve **İkinci onaycıda masraf eklenmek** istendiğinde **Networkte kayıt işlemi**
    görünürken, **Datagrid'de kaydedilen veri görünmeme** hataları düzeltildi.


### 3.2. Geliştirme Arayüzü

- 40652 - Geliştirme arayüzünde **Şifremi Unuttum** diyerek mail üzerinden **şifre**
    **sıfırlandığında** , giriş yaparak **tekrar web arayüzüne yönlendirme hatası** düzeltildi.
- 44992 - Geliştirme arayüzünde **Dinamik DataGrid** nesnesi **Form .cs** yazılan **reload**
    **kodunun arayüze yansımama hatası** düzeltildi.
- 45953 - Geliştirme arayüzünde **Araçlar** sekmesinde **Aksiyon Durum Yöneticisi**
    ekranının **boş olarak açılma hatası** düzeltildi.
- 46862 - Geliştirme arayüzünde, formda **alt akışa düşmesi gereken akışın düşmeme**
    hatası düzeltildi.
- 47019 - Geliştirme arayüzünde **Form Indexle** tuşuna basarak **Dizinleme** ekranında
    **formu kaydedip** , Web arayüzünde formu açtıktan sonra **Kaydet işlemi** yaptığımızda
    hata alma sorunu düzeltildi.
- 47202 - Geliştirme ortamında **projeler yayınlanırken alınan hata** düzeltildi.
- 47396 - Geliştirme arayüzünde **Datasource** içindeki **json** dosyalarına
    **ConnectionName değerlerinin gelmeme hatası** düzeltildi.
- 47571 - Geliştirme arayüzü Akış Yöneticisinde, **GetProcessLean** endpointine
    **DeleteDate** alanı parametresi eklenerek **görünen akışlardaki sıralama hatası**
    düzeltildi.
- 40733 [DR5392] - Geliştirme arayüzünde **Form Özellikleri** üzerinden **Variables** değeri
    **sıfırlandığında** , değer kısmında sıfırlanan özellik **null** olarak yazdığı için **projenin**
    **açılırken hata verme** sorunu düzeltildi.
- 44948 - Geliştirme arayüzünde **TextBox** nesnesindeki **Değer Atayın** işleminden sonra
    seçim yapıldığı zaman, **konsol ekranına düşen hata ve hiçbir alana tıklanamama**
    **hatası** düzeltildi.
- 45156 - Geliştirme arayüzünde **Akış** tarafının **Coding** alanında ve Form tarafının
    **Appearance** ile Nesne Özelliklerinde **MaxLength** kısmına **eksi değer girilme hatası**
    düzeltildi.
- 45210 - Geliştirme arayüzünde **Datagrid** kolonları eklendiğinde **DataType** özelliğinin
    **değiştirilebilme hatası** düzeltildi.
- 45370 - Geliştirme arayüzünde **Akış** tarafında **Pozisyon Grubu** nesnesinde **Kullanıcı**
    **Gruplarında arama işlemi yapılırken alınan hata** düzeltildi.
- 45491 - Geliştirme arayüzünde **Akış Yöneticisi** içerisindeki **Filtrele** panelinde yer alan
    **Temizle** butonuna tıklanıldığında, **panelin kapanma hatası** düzeltildi.
- 45496 - Geliştirme arayüzünde **Akış Yöneticisinde Show Deleted filtresi** " **Include**
    **Deleted** " olarak **değiştirildi** ve bu alanda yer alan **Delete butonu pasif işlemi**
    tamamlandı. **Silinen akışların listede ilk başta gösterilmeme hatası** düzeltildi.
- 45546 - Geliştirme arayüzünde **Akış** tarafında **PDF Aktar** nesnesinde **özelliklere**
    **tıklandığında konsolda oluşan hata** düzeltildi.
- 45571 - Geliştirme arayüzünde **InputGroup** nesnesini forma **Kopyala Yapıştır**
    **yapılamama hatası** düzeltildi.


- 45622 - Geliştirme arayüzünde **Header** nesnesinin **Text** özelliğinin **Font Size** değerini
    **arttırmak** istendiğinde, ilk yazılan font boyutunun **belirlenen değerden başlaması**
    **yerine sıfırdan başlama hatası** düzeltildi.
- 45716 - Geliştirme arayüzünde **Kural Yöneticisinde** eklenen koşulların **'Seçiniz'** olarak
    **görülme hatası** düzeltildi.
- 45841 - Geliştirme arayüzünde **NumberBox** nesnesinin **Precision** özelliğine **virgüllü**
    **basamak** girilmesinden kaynaklı oluşan hata düzeltildi.
- 45887 - Web arayüzünde **Check-in Check-out** özelliği **Açık** olan bir form **üzerinde ilgili**
    **kullanıcı tarafından açıksa** , diğer kullanıcı tarafından **aynı form açılmak istendiğinde**
    **uyarı mesajı gelme** kontrolü eklendi.
- 45902 - Web arayüzünde **Open Selection Form Toolbar butonu** ile veri eklenen
    **Datagrid'de Düzenleme** işleminden sonra çıkan hata düzeltildi.
- 46242 [DR6947] - Geliştirme arayüzünde formda **Chart** nesnesine sayısal içerikli **Rest**
    **sorgusu** bağlandığında, **Chart Items** tarafında **Argument Field** ve **Value Field**
    **alanlarının boş gelme hatası** düzeltildi.
- 46252 - Geliştirme arayüzünde **Aksiyon Durum Yöneticisi** ekranında **yeni ekleme**
    işlemi yapılırken **boş bırakılıp Tamam** butonuna tıklandığında **hata mesajı**
    **verilmemesi** , **Yeni Aksiyon Durum Yöneticisi penceresinin hizalanma** hataları
    düzeltildi.
- 46511 [DR7008] - Geliştirme arayüzünde **DataGrid** nesnesi **Boolean** kolonunun **Icon**
    **source field** alanından ilgili kolon seçilerek, **Icon Matchers** özelliğinden **ikon**
    **eklendiğinde gözükmeme hatası** düzeltildi.
- 46156 - Geliştirme arayüzünde **Karşılaştırma** nesnesinde **Sonuç** kısmındaki
    **değerlerin sıfırlanmama hatası** düzeltildi.
- 46922 [DR7118] - Geliştirme arayüzünde Akış tarafında **PDF 'e Aktar** nesnesinde
    **Export Page Header** ’de **Footer’ı** revize edildiğinde, **Type** görsel seçildiğinde **Content**
    **alanının seçilememe hatası** düzeltildi.
- 47189 - Geliştirme arayüzü Akış Yöneticisinde **icon.Enabled = showStatistics**
    edildiğinde **istatistiklerin sayfada görünmeme hatası** düzeltildi.
- 47379 - Geliştirme arayüzü **Proje Yönetimi** içeri alma işleminde açılan **Import Project**
    ekranının **bağlantı** sekmesinde **bağlantı isimlerinin görülmeme hatası** düzeltildi.
- 47471 - Geliştirme arayüzünde **Akış** tarafında **Alt Akış Çağırma** nesnesinde **geri**
    **dönüş değeri linkleme sorunu** düzeltildi.
- 47537 - Geliştirme arayüzünde **Akış** tarafında **Pozisyon Grubu** nesnesinde **Empty**
    **Group Event** ve **Conflict State Event Validasyon sorunu** düzeltildi.
- 47546 - Geliştirme arayüzünde **Form Özelliklerinde Form Type Görünüm formu**
    seçildiğinde, Web arayüzünde **Uygulama Gezgininde Düğüm İşlem Tipi** kısmında **Bir**
    **Form Doldur** seçildiğinde **ilgili formun gelmeme hatası** düzeltildi.
- 47654 [DR7445] - Geliştirme arayüzünde forma eklenmiş **TextBox** nesnesinin **Name**
    alanın " **View** " yazıldığında **ortamın hata verme sorunu** düzeltildi.


- 45626 - Geliştirme arayüzünde formda **TextBox** nesnesine **değer atandığı zaman** ,
    **formun ve arayüzün donma hatası** düzeltildi.
- 40885 [DR5544]- Geliştirme arayüzünde form ekranında **Datasource** bağlantısı olan
    ve **birbirine bağlı ComboBox** nesnelerinde, Akış tarafında **Service Api** ile
    ayarlandığında **Web arayüzüne yansımama hatası formInstance.Reload(); yardımcı**
    **metodu** eklenerek düzeltildi.
- 46676 - Geliştirme arayüzünde **EntityUniqueIdTemplates** projesinde **deploy alma**
    **esnasında** oluşan hata düzeltildi.


### 3.3. Android

- 44468 [DR6536] - **Android** cihazların mobil arayüzünde, form üzerinde **Radio**
    nesnesinin **sunucu** tarafında **OnValueChanged** etkinliğine göre **ActiveView**
    değiştirildiğinde **ClientVisible False** olan **Label nesnelerinin gözükme hatası**
    düzeltildi.
- 46953 - **Android** cihazların mobil arayüzünde, **Native+** görünümündeki **OSF DataGrid**
    nesnesinde seçimlerin **nesneye yansımama hatası** düzeltildi.
- 38683 - **Android** cihazların mobil arayüzünde, **Webview** görünümündeki **OSF**
    **DataGrid** formunda **Editing Settings False** özelliğinde olan nesneye **veri ekleme**
    **esnasında hata mesajı** çıkma sorunu düzeltildi.
- 46174 [DR6954] - **Android** cihazların mobil arayüzünde, nesnelerin **cs tarafında**
    **OnValueChanged** olayında **ActiveView alanı değiştirildiğinde** , formda olan
    **UserMetaData** nesnelerinin **ActiveView** değiştiği için **yükleniyor aşamasında kalma**
    hatası düzeltildi.
- 47043 - **Android** cihazların mobil arayüzünde, **Webview** görünümündeki **OSF**
    **DataGrid** nesnesinde **seçimlerin nesneye yansımama hatası** düzeltildi.
- 46075 [DR6926] - **Android** cihazların mobil arayüzünde, **Native+** görünümündeki
    **DataGrid** nesnesinde yer alan **birinci Select tipli Column** nesnesinden **ikinci Select**
    **tipli Column** nesnesine **veri gelmeme hatası** düzeltildi.

### 3.4. IOS

- 44468 [DR6536] - **IOS** cihazların mobil arayüzünde, form üzerinde **Radio** nesnesinin
    **sunucu** tarafında **OnValueChanged** etkinliğine göre **ActiveView** değiştirildiğinde
    **ClientVisible False** olan **Label nesnelerinin gözükme hatası** düzeltildi.
- 47302 - **IOS** cihazların mobil arayüzünde, **Native+** görünümündeki formda **Deploy**
    mesajı geldiğinde ve **Deploy** mesajının **Tamam** butonuna tıklandığında **formun**
    **kapanmama hatası** düzeltildi.
- 46174 [DR6954] - **IOS** cihazların mobil arayüzünde, nesnelerin **cs tarafında**
    **OnValueChanged** olayında **ActiveView alanı değiştirildiğinde** , formda olan
    **UserMetaData** nesnelerinin **ActiveView** değiştiği için **yükleniyor aşamasında kalma**
    hatası düzeltildi.
- 46952 - **IOS** cihazların mobil arayüzünde, **Native+** görünümündeki **OSF DataGrid**
    nesnesinde **seçimlerin nesneye yansımama hatası** düzeltildi.
- 46075 [DR6926] - **IOS** cihazların mobil arayüzünde, **Native+** görünümündeki
    **DataGrid** nesnesinde yer alan **birinci Select tipli Column** nesnesinden **ikinci Select**
    **tipli Column** nesnesine **veri gelmeme hatası** düzeltildi.


## 4. Breaking Changes

1. .ts versiyonumuz 3.3.4 den 4.9.4 e güncellenmiştir. Metodların ts'in yeni versiyonuna göre revize edilip projeler **tekrar** yayınlanmalıdır.
2. DataGrid'e Datasource bağlayıp Columns ürettiğinizde eğer STATUS kolonu varsa,
Columns özelliklerinden Kontrol sekmesine geçerek Data Definition Language Field Name
bilgisinin değiştirilmesi gerekmektedir. STATUS adı rezerve bir alan olarak güncellenmiştir. Bu
nedenle var olan projelerde STATUS kolonu Data Definition Language(DDL) Field Name
değiştirmeniz gerekmektedir.
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
.
```

<font size="5"><a href="https://portal.synergynow.io/#/_redirect/OeWDbBRlEygs2lII289sij"  target="_blank"><svg fill="currentColor" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" viewBox="0 0 40 40" style={{verticalAlign: "middle"}}><g><path d="m35.8 8.5q0.6 0.6 1 1.7t0.5 1.9v25.8q0 0.8-0.6 1.5t-1.6 0.6h-30q-0.9 0-1.5-0.6t-0.6-1.5v-35.8q0-0.8 0.6-1.5t1.5-0.6h20q0.9 0 2 0.4t1.7 1.1z m-9.9-5.5v8.4h8.4q-0.3-0.6-0.5-0.9l-7-7q-0.3-0.2-0.9-0.5z m8.5 34.1v-22.8h-9.3q-0.9 0-1.5-0.6t-0.6-1.6v-9.2h-17.1v34.2h28.5z m-11.4-13.2q0.7 0.6 1.8 1.3 1.3-0.2 2.6-0.2 3.3 0 4 1.1 0.4 0.5 0 1.2 0 0 0 0l0 0v0.1q-0.2 0.8-1.6 0.8-1.1 0-2.6-0.4t-2.9-1.2q-4.9 0.5-8.7 1.8-3.4 5.9-5.4 5.9-0.4 0-0.7-0.2l-0.5-0.2q0-0.1-0.1-0.2-0.3-0.2-0.2-0.8 0.2-0.8 1.3-2t2.9-2.1q0.3-0.2 0.5 0.1 0.1 0 0.1 0.1 1.1-1.9 2.4-4.4 1.5-3.1 2.3-5.9-0.5-1.8-0.7-3.5t0.2-2.9q0.2-0.9 0.9-0.9h0.5q0.5 0 0.8 0.4 0.4 0.4 0.2 1.5-0.1 0.1-0.1 0.2 0 0 0 0.1v0.7q0 2.8-0.3 4.3 1.2 3.7 3.3 5.3z m-12.9 9.2q1.2-0.6 3.1-3.5-1.2 0.8-2 1.8t-1.1 1.7z m8.9-20.6q-0.4 1-0.1 3 0.1-0.2 0.2-1 0-0.1 0.1-0.9 0.1-0.1 0.1-0.2 0-0.1 0-0.1t0 0 0 0q0-0.5-0.3-0.8 0 0 0 0v0z m-2.8 14.8q3-1.2 6.4-1.8-0.1 0-0.3-0.2t-0.4-0.3q-1.7-1.5-2.8-4-0.6 2-1.9 4.4-0.7 1.3-1 1.9z m14.4-0.4q-0.5-0.5-3.1-0.5 1.7 0.6 2.8 0.6 0.3 0 0.4 0 0 0-0.1-0.1z"></path></g></svg>PDF Download</a></font>
