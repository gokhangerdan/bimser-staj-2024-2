---
sidebar_position: 2330
sidebar_label: "2023 Spring Release"
custom_edit_url: ""
---

# Bimser Synergy 2023 Spring Release Notes
*(1 Nisan 2023 - 30 Nisan 2023)*

## 1. Highlights / New Features

- 34105 [DR973] - Form Özellikleri paneline **Check In – Check Out** özelliği eklendi. **Default**
    değeri **pasif** olan bu özellik **aktif** edildiğinde **Timeout** (İşlem için zaman aşımı süresi
    değeri verilir. Default değeri 10 dakikadır) ve **Additional Time** (Timeout süresine ek süre
    verilir. Default değer 5 dakikadır) alanlara dakika bazında **zaman aşımı süre bilgisi** girilir.
    Akışta kullanılan **Pozisyon Grubu** nesnesindeki **kullanıcılardan biri formu açtığında** , **sol**
    **üst köşede geri sayım olarak Timeout süresi görülür**. Süre dolmadan 10 saniye önce
    kullanıcıya **modal olarak süresinin dolmak üzere olduğu** hatırlatır. Kullanıcı işleme
    devam et dediğinde **ek Additional Time alanında belirttiği süre devreye girer** ve form
    üzerinde geri sayım olarak gösterilir. Form açık kaldığı sürece **zaman dolana kadar**
    **Pozisyon Grubundaki diğer kullanıcı formu açamaz**. **İlk kullanıcının süresi dolduğunda**
    ya da **form kapatıldığında ikinci kullanıcının formu açabilmesini sağlayan** bu özellik
    eklendi.
- 43842 - Geliştirme arayüzünde **Akış** tarafında **Flow Events** özelliklerine **"Seçerek Kaldır"**
    **özelliği** eklendi. Bu özellik ile akışta ilgili olayları kullanan nesneler **DataGrid ile**
    **listelenme** ve **istenilen nesnedeki olayın kaldırılma** özellikleri getirildi.
- 43428 - Web arayüzünde **Güvenlik** sekmesinde **Doküman Yönetimi** ayarlarının içerisine
    **İptal** ve **Geçmiş Revizyonlar yetkileri** eklendi.
- 34095 [DR2500] - Web arayüzünde **akış reddetme işlemi** yapıldığında girilen **reddetme**
    nedeninin geliştirme arayüzünde **mail template** içerisinde **{{ProcessId}}** gibi **{{Reason}}**
    yazılarak nedenin **mail template içinde gönderilebilmesi** geliştirildi. **{{Reason}}** alanının
    amacı **akıştaki reddetme nedenine ulaşmaktır**. **Liquid** templatelerinde **{{Reason}}**
    şeklinde erişilebilir.
- 42485 - Geliştirme arayüzünde **Akış yöneticisinde GetProcessLean** endpointine **silinen**
    **akışların tarih bilgisini** tutmak için **Delete Date alanı** eklendi.
- 35277 [DR2887] - Web arayüzünde **İş Akış Yönetiminde Taslaklar** bölümünde taslak
    olarak kaydedilen form veya akışların **kullanıcı arayüzü tarafından silinmesi için Sil**
    **butonu** eklendi.
- 35217 - Geliştirme arayüzünde formda **TreeList** nesnesine **ContextMenu** nesnesinin
    **eklenebilme özelliği** getirildi.
- 38947 - Geliştirme arayüzünde **Akış yöneticisinden filtrelenen** projenin **Steps** sekmesine
    **Rollback (Geri Al) geliştirmesi** eklendi. Bu geliştirme ile beraber **akışın geri alınması**
    sağlandı.
- 16428 - Geliştirme arayüzünde **Datagrid nesnesine Image kolonu** eklendi.
- 43951 - Geliştirme arayüzünde formda **Column** ve **Section Padding özelliğine Top,**
    **Down, Right** ve **Left** değerleri girerek **nesneyi konumlandırma özelliği** getirildi.


- 44141 - Web arayüzünde **DataGrid Start a Process** sonrasında **ProcessId'e ulaşılabilme**
    **özelliği** geliştirildi.
- 44488 - Geliştirme arayüzünde, **DataGrid** nesnesinin **Toolbar Buttons** sekmesinde
    **Project Name, Form Name** ve **Default View** alanlarının **Select** olarak **değiştirilerek**
    **verilerin gelmesi** sağlandı.
- 44569 - Geliştirme arayüzünde Akış tarafında **Continue If Error Occurs** özelliği
    düzenlendi. **Akışta hata olsa da sonraki adıma ilerlemesi** sağlandı.
- 40131 - Geliştirme arayüzü, **Proje Özelliklerinde Otomatik Başlat** özelliği geliştirildi. Bu
    geliştirme ile **Deploy Agent restart** olduğunda, bu seçenek işaretli olan projelerin
    **otomatik başlatılması durumu** geliştirildi.
- 42447 - Geliştirme arayüzünde, formun **css kodlarına yazılanların ön izlemede**
    **gösterilmesi** sağlandı.
- 42900 - Geliştirme arayüzüne **Map** ve **VectorMap** adında iki yeni **vektörel harita ve**
    **normal harita grafik nesneleri** eklendi.


## 2. Improvements

- 29795 - Web arayüzünde **, Vekâlet ve Erişim Anahtarı yeni oluşturma ve düzenleme**
    işlemlerinde oluşan **yetkilerin listelenmesi** ve **yapılan değişikliklerin yansımaması**
    hataları düzeltildi.
- 28742 - Web arayüzünde **Doküman Yönetiminde** depolara girilip, dosya seçilip, paylaşım
    özelliği kullanılırken **mail gönderme** alanına **mail konusu yazılabilmesi** için gerekli
    geliştirme yapıldı.
- 37923 - Web arayüzü **Doküman Yönetiminde** , **bir dosyanın kendisi ile ilişkilendirilmeye**
    çalışıldığında **kullanıcıya uyarı ekranı vermesi** sağlandı.
- 42487 - Geliştirme arayüzünde **Akış Yöneticisinde Objects** sekmesinde, nesnelerin akışta
    çalıştıklarını kontrol eden **CheckStepHasEverWorked endpointi** geliştirildi.
- 34653 - Geliştirme arayüzünde **CreateLink API'nın Body** alanına yeni embeddedView
    parametleri eklenmiştir. Eklenen parametler
    "viewHideInfo" :
    "hideLeftMenu": **false** ,
    "hideBreadcrumbNavigation": **false** ,
    "hideBreadcrumbItems": **false** ,
    "hideAppSearch": **true** ,
    "hideAdminTools": **false** ,
    "hideProfileMenu": **false** ,
    "hideApprovals": **false** ,
    "hideLastVisitedDocuments": **false** ,
    "hideAnnouncements": **false**
- 41409 - Geliştirme arayüzünde nesnelere **Geolocation** adı altında **konum bilgisinin**
    **eklenmesi özelliği** geliştirildi.
- 42533 - Web arayüzündeki, **GetLoginParameters** endpointine **GlobalCss alanı** eklendi.
- 43926 - Web arayüzünde **İş Akış Yönetimi** ve **İnsan Kaynakları Menü Elemanı** için sadece
    **ana kırılım yetkisine değil** , altındaki elemanlardan **birine de yetkisi varsa listede**
    **görülme özelliği** geliştirildi.
- 45125 - Geliştirme arayüzünde **Akış Yöneticisi** menüsünde **bitmiş olan akışlara Rollback**
    **(Geri Alma) yapılmaması** sağlandı.
- 37510 [DR4284] - Geliştirme arayüzünde, **Olaylar** ile tetiklenerek **OpenForm** tipinde
    açılan formun **Editable: false/true** olması sağlandı.
- 2076 - Geliştirme arayüzünde **Senkronize Edici Nesnesi** kullanılarak **bir formdaki**
    **nesnenin başka bir formdaki diğer nesne ile** akışın ilerlediği aşamada, **aynı değeri**
    **döndürmesi durumu** geliştirildi.
- 22453 - Geliştirme arayüzünde Akış Yöneticisinde **GetProcessLean** ve **GetProcess**
    sorgularında **Paging düzenlemesi** ile **GetProcessLean endpointine PackageVersion** ve
    **Count bilgisi** eklendi ve **Rollback (Geri Alma)** işleminde **ilk ve son süreç için engelleme**
    işlemleri geliştirildi.


- 35026 - Geliştirme arayüzünde, **Events** ile tetiklenerek **OpenForm** tipinde açılan formun
    **Editable** bilgisinin **GetFormInfoById** isteğinin **payload** kısmında **gösterilmeme hatası**
    giderildi.
- 22359 - Geliştirme arayüzünde **Akış** tarafında **süreci Başlatan/Onaylayan** kişi ile ilgili
    bilgilerin **(Geo koordinatlarının)** geliştirmesi yapıldı.
- 38049 - **Service Api** ile ilerletilen akışta, ilerletilmek istenilen butonun **Visible değeri**
    **False** olduğunda **akışın ilerletilebilmesi** sağlandı.
- 38275 - Geliştirme arayüzünde **Akış Özelliklerinde Events** içerisinde **Enabled işlemi**
    düzenlendi.
- 38592 - Geliştirme arayüzünde **Akış Yöneticisindeki** verilerin listelenmesi **filtre alanına**
    **Toolbar Sorting özelliği** geliştirildi.
- 40911 - Geliştirme arayüzünde **Akış Yöneticisinde Versiyonlama geliştirmesi** yapıldı.
- 42501 - Web arayüzünde **Akış Yöneticisinde** ilgili akışa ait adımların sayısı **GetProcess**
    **Steps** endpointine **Count özelliği** olarak eklendi.
- 43681 - Geliştirme arayüzünde **Akış yöneticisinde GetProcessLean** endpointine **Flow Id**
    eklendi.
- 42874 - Geliştirme arayüzünde Akış tarafında **Process Creator, ProcessStartDate,**
    **RequestId, Request Date, ProcessStatusNo, ProcessStatus** bilgilerinin **Template**
    eklenmesi geliştirildi.
- 42912 - Geliştirme arayüzünde **sunucu olayları içerisinde** kullanılmak üzere aşağıdaki
    **metotlar** geliştirildi.
    public **bool** GetValueAsBool(string key)
    public **byte** GetValueAsByte(string key)
    public **sbyte** GetValueAsSbyte(string key)
    public **char** GetValueAsChar(string key)
    public **decimal** GetValueAsDecimal(string key)
    public **double** GetValueAsDouble(string key)
    public **float** GetValueAsFloat(string key)
    public **int** GetValueAsInt(string key)
    public **uint** GetValueAsUint(string key)
    public **long** GetValueAsLong(string key)
    public **ulong** GetValueAsUlong(string key)
    public **short** GetValueAsShort(string key)
    public **ushort** GetValueAsUshort(string key)
    public **string** GetValueAsString(string key)
    public **DateTime** GetValueAsDateTime(string key)
    public **TimeSpan** GetValueAsTimeSpan(string key)
    public **DateTimeOffset** GetValueAsDateTimeOffset(string key)
    public T GetValueJsonAsType```<T>```(string key)
- 42915 – **Database** tarafında **MAILS** tablosuna, **mailin gönderildiği İş akışına** ait bilgilerin
    **kaydedilmesi** sağlandı.


- 42923 - Web arayüzünde akış gönderilen kullanıcıya gelen **mail şablonu Proje Adı - Flow**
    **Adı** şeklindeyken bu şablon **Proje Adı** olacak şekilde geliştirildi.
- 45184 - Web arayüzünde **WorkFlowManager** hata mesajlarında **"Request failed."** vb
    **hata mesajları** yerine, **fail** olan **request'in response modelinde** bulunan hata mesajının
    fırlatılması sağlandı. **Request failed hata mesajlarında ID bilgisi** gösterildi.
- 45290 - **Son kullanıcının** aldığı **hata** mesajlarının daha anlamlı olması için **StopWith** ile
    **akışı sonlandırma Implemantasyonu** geliştirildi.
- 37828 - Geliştirme arayüzünde formda **DocumentViewer** nesnesinin **File Settings** başlığı
    altına **Show On geliştirmesi** yapılmıştır. Bu özellik altında **Panel, Modal** ve **Drawer**
    seçenekleri bulunmaktadır. Bu seçenekler sayesinde **DocumentViewer nesnesi** içerisine
    **yüklenmiş olan dosyalarla ilgili çeşitli işlemler** yapılabilmektedir.
- 34467 - Geliştirme arayüzünde, **Rest** sorgusu bağlı **DataGrid** kolonlarında **EditType** :
    **ComboBox** kolonuna **rest sorgusu bağlarken sorguda alan seçimi yapılması** sağlandı.
- 16622 - Web arayüzü **Doküman Yönetiminde çoklu dosya ve klasör silinmek**
    istendiğinde, **dosya sayısının görüntülenmesi** sağlandı.
- 21181 - Web arayüzünde **Uygulama Gezgini açıkken arka planın tıklanabilir olmaması**
    sağlandı.
- 37996 - Geliştirme arayüzünde **Çözüm Gezgini alanında** iyileştirmeler yapıldı.
- 38355 - Geliştirme arayüzünde **Akış Yöneticisinde Step** ve **Object** alanlarına **Flow nesne**
    **ikonları** eklendi.
- 38570 - Web arayüzünde **svg ikonlarına URL adresiyle erişilebilme** özelliği geliştirildi.
- 38040 - Geliştirme arayüzünde **fokus metodu 4 farklı şekilde** çalıştırılabilmesi sağlandı.
    Bu metotlar sadece **Client** tarafında olmalıdır. Örnek kullanımları şu şekildedir:
    - this.TimePicker1.focus({cursor:"start"})
    - this.TimePicker1.focus({cursor:"end"})
    - this.TimePicker1.focus({cursor:"all"})
    - this.TimePicker1.focus({preventScroll:true})
    Metot argümanları **nesneye göre değişkenlik** gösterebilir. İstenilen **tüm değişiklikler**
    **Web arayüzünde gözlemlenebilir**.
- 38302 - Geliştirme arayüzünde Akış yöneticisinde **Steps** sekmesine ve **Tarih filtre**
    alanlarına **ikonlar, Status filtre** alanının **dil seçimine** göre gelmesi, **Tarih** filtresinde ilgili
    günün tarihinden sonrasında **Disabled** durumda olması eklendi.
- 40199 - Geliştirme arayüzünde **Akış Yöneticisinde Package sürüm bilgisinin gösterilmesi**
    sağlandı.
- 40760 - Geliştirme arayüzünde **Akış yöneticisinin filtrele** ekranında **Projects** alanına
    **Yenile butonu** eklendi.
- 39291 - Web arayüzü **Doküman Yönetiminde** klasör ve dosyalara tıklandığı **zaman üst**
    **menüdeki** işlemlerdeki gibi **hızlı çalışması** için değerlerin bu **onTopBarMenuPreparing**
    **metot ile karşılanması** sağlandı.
- 42477 - Web arayüzünde akıştaki kullanıcı **bir başka kullanıcıya vekalet vermiş** ise; **akışa**
    **ait onay mailinin vekaleti** alan kullanıcıya gönderilmesi ve bu mail üzerinden **onaylama**
    **işleminin yapılabilmesi** özelliği geliştirildi.


- 42484 - Geliştirme arayüzünde **Akış yöneticisinde bitirilmiş** veya **silinmiş** olan akışların
    nesnelerinde **değişiklik yapılamaması** geliştirildi.
- 42511 - Web arayüzünde **İş Akış Yönetimindeki DataGrid** üzerinde **Style Düzenleme**
    özelliği, **Column Chooser** ve **Column Resizeable** özellikleri eklenerek **Searchbar** özelliği
    geliştirildi.
- 35375 - Web arayüzünde **Akış** formunda **değişiklikler** yapıldıktan sonra, **Kaydet**
    **butonuna** basıldığında kullanıcıya **'Kayıt Başarılı' uyarısı getirilmesi** sağlandı.
- 42486 - Geliştirme arayüzünde **Akış Yöneticisinde Objects** alanında devam eden
    akışlarda **tamamlanmış adımlar üzerinde** , **silinmiş** veya **tamamlanmış akışlarda**
    **düzenleme yapılması** engellendi.
- 43777 - Geliştirme arayüzünde **Mail Gönder** nesnesi **, PDF'e Aktar** nesnesi, **Senkronize**
    **Edici** nesnelerindeki **Continue if Error Occur** özelliğinin altına **errorOptions**
    parametrelerinin eklenmesi sağlandı.
    "errorOptions": {
    "resumeOnError": true,
    "errorDescriptionObject": {
    "key": "5ef8eb6a- 4548 - 769d-b698-2b5aded9ce5a",
    "name": "Variable1",
    "typeCode": 30
    }
    }
- 43778 - Geliştirme arayüzünde **Atama** nesnesine **TargetObject değerlerinin eklenmesi**
    sağlandı.
    "targetObject": {
    "key": "a40d52c6-9bf1-b38c- 2631 - 1433d170506f",
    "name": "Position1",
    "typeCode": 15
    }
- 43790 - IDE arayüzünde **Akış Yöneticisi** menüsünde, **Filtreleme** alanına **Flows filtresinin**
    **eklenmesi** sağlandı.
- 43767 - Web arayüzü **Doküman Yönetiminde birden fazla dosyanın silindiği zaman** ,
    sayfanın hataya düşmesini engelleyen **endpoint** geliştirildi.
- 42578 - **Studio - Auto Start On Startup** özelliğinin **UpdateProject endpointine eklenme**
    geliştirmesi yapıldı.
- 43640 - Geliştirme arayüzünde Akış tarafında " **Hata Oluştuğunda Devam Et** " özelliği
    bulunan nesnelerde bu özellik seçildiğinde oluşan **Json'ında ErrorOptions propertysi**
    eklendi.
- 45289 - **Son kullanıcının** aldığı **hata** mesajlarının daha anlamlı olması için **StopWith**
    **mesaj gösterimi Implemantasyonu** geliştirildi.
- 22385 - Web arayüzü **Doküman Yönetiminde** makine öğrenmesi kullanılarak **ve text**
    **dosyalarının içeriği** okunarak **otomatik bir kategori belirlenmesi** özelliği geliştirildi.


- 4389 - Geliştirme arayüzünde, **DataGrid** nesnesine **DataType** : **veri tabanı** , **formatType:**
    **görünüm** , **editorType: düzenleme** modunda kolonların nasıl görüneceğine karar verilir.
    **DataType** kısmında bu kolonlar, **String, Boolean, Decimal, Date, Date-Time, Time,**
    **Object** olarak listenir.
    **EditorType** kısmında bu kolonlar, **TextBox, Checkbox, NumberBox, Datepicker,**
    **DateTimePicker, TimePicker, Select** olarak listelenir.
    Kolon kırılımına eklenen yeni proplar şu şekilde,

```
Control > EditControl olarak name değişikliği yapıldı.
CellType prop kaldırıldı. EditType prop eklendi.
```
```
ML Cell;
```

- 40679 - Web arayüzü **Dashboard** ekranındaki sorguların hazırlanıp **Ana sayfa ile**
    **senkronize çalışması durumu** sağlandı.
- 44942 - Web arayüzü **Dashboard** ekranında **kullanıcı bazında sorguların görünüp**
    **kullanıcıya göre değişme** özelliği geliştirildi.
- 41358 - Web arayüzü **Dashboard** ekranındaki sorguların hazırlanıp **Ana sayfa ile**
    **senkronize çalışması durumu** sağlandı.
- 38544 - Web arayüzü **Dashboard** ekranında **Son Kullanılan Uygulamalar** , **Bekleyen**
    **Onaylar, Başlattığım İşler, Devam Eden İşler, Bilgilendirmeler, Süreçler ve Süreç**
    **Detayları** ekranları geliştirildi.
- 43305 – Database’de **Configurations** tablosunda **Security.IndefiniteAccessToken**
    parametresinin değeri **true** olduğunda **Erişim anahtarının süresi verilebilmesi**
    geliştirmesi yapıldı.
- 43783 - Geliştirme arayüzünde **Datagrid** nesnesi **Column Fixing Enabled** özelliği **aktif**
    edildiğinde, formdaki kolonlara sağ tıklayarak **sola ve sağa kolonun sabitlenmesi** veya
    **Çöz seçeneği ile sabitlenen kolon eski haline geri getirilebilmesi** sağlandı.
- 37286 - Web arayüzünde formdaki nesnelere **bir değer girilip** akış bitirildikten sonra,
    **girilen metin ile başlangıç sayfasındaki arama alanından girilen metin ile formu**
    **bulabilme özelliği** geliştirildi.


## 3. Fixes

### 3.1. Web Arayüzü

#### 3.1.1. Doküman Yönetimi

- 44639 - Web arayüzünde **Doküman Yönetiminde** depo ve klasör için **Özellikler**
    alanında **maksimum dosya boyutunun negatif değer olarak verilebilme hatası**
    düzeltildi.

#### 3.1.2. İş Akış Yönetimi

- 44629 - Web arayüzünde **İş Akış Yönetimi** menülerindeki **panellerde yazan "0" yazısı**
    kaldırıldı.
- 41335 - Web arayüzünde **İş Akış Yönetimi** kısmında bulunan **Geçmiş Onaylar**
    sekmesindeki açılan Datagrid'de kayıt seçildiğinde, **açılan panelde filtrenin bulunma**
    **hatası** düzeltildi.

#### 3.1.3. No [İnsan Kaynakları]


#### 3.1.4. Web Ana Sayfa

- 44232 - Web arayüzünde **Giriş ekranında Şifremi Unuttum butonuna** tıklandığında,
    **kullanıcı adı yazılarak Şifre Hatırlatma mailinin gönderilememe** hatası düzeltildi.
- 44769 - Web arayüzünde, **GetDeployAgents endpointinde oluşan hata** düzeltildi.
- 41728 [DR5832] - Web arayüzünde formda **Ribbon** nesnesinde **Text** ve **Custom** tipli
    ögelerinde bulunan **Disabled özelliğinin çalışmama hatası** düzeltildi.
- 41973 - Web arayüzünde **DataGrid Cell mode** seçiliyken, satır ekledikten sonra
    **hemen tekrar satır eklemek istendiğinde oluşan hata** düzeltildi.
- 42861 [DR5982] - Web arayüzünde **Datagrid** nesnesi **Cell** moddayken, veri
    eklendiğinde **alt alta olan iki DataGrid’deki imleç hatası** düzeltildi.
- 43005 - Web arayüzünde formda **ReadOnly** özelliği açık olan **Dropdown,**
    **FileSelector, TabMenu, RelatedDocuments, FishBone** ve **Transfer** nesnelerinin
    üzerine gelindiğinde **çarpı imlecinin gelme hatası** düzeltildi.
- 44654 - Web arayüzünde **Giriş ekranında Reading Style hataları** düzeltildi.
- 44765 - Web arayüzünde **Datagrid yapısı** bulunan alanlarda **konsola düşen hata**
    düzeltildi.
- 44474 - Web arayüzünde içerisine **başka bir projeden form eklenmiş olan Repeater**
    **nesnesinin açılmama** hatası düzeltildi.
- 44907 - Web arayüzünde **Statik Datagrid düzenleme işlemi sonraki onaycıya**
    **gitmeme hatası** düzeltildi.
- 40132 - Web arayüzünde **Yönetim Araçları** içerisinde yer alan **Görev Yönetimi kolon**
    **başlıklarının** hem **Türkçe** hem de **İngilizce yazma hatası** düzeltildi.
- 45270 - Geliştirme arayüzünde Form Özelliklerinin **Toolbar Buttons** kısmından
    " **Yazdır** " butonunun özelliklerinden **IsServerPrint'i** etkileştirip, **View** seçtikten sonra
    **web arayüzünde "Yazdır" butonuna tıklayınca** hata alma sorunu düzeltildi.
- 45515 - Web arayüzünde, **Aktif** listedeki **Vekâlet** seçilip **geri çek** butonuna
    basıldığında **Vekâlet Geri Çekilmiyor** hatası **, Pasif** listedeki vekâlet seçilip **Kaldır**
    butonuna basıldığında **vekâletin kaldırıldığı mesajı alınıyor** fakat **listede hala kalma**
    **hatası** ile **Yeni Vekâlet ve Erişim Anahtarı** için bilgiler eklenip **Tamam** butonuna
    basıldığında **işleme devam edilmeme hatası** düzeltildi.
- 38820 [DR4835] - Web arayüzünde **Pozisyon Grubundaki kişiler** onayladıktan sonra,
    onaylamayan kullanıcıların **istekleri ve bağlantıları siliniyor** fakat hata alındığı zaman
    **mevcut istekler silinmemekle** beraber, **Timeout işlemi** ile akış geri döndürüldüğünde
    **sadece onayların değil bağlantıların da silinme hatası** düzeltildi.
- 40622 [DR5376] - Web arayüzünde **Akış** tarafında **Pozisyon** nesnesinde **süreç**
    **ilerleme hatası** düzeltildi.
- 44055 - Web arayüzünde forma ait **Client Visible** bilgisi, **bir seçim yapılmamış** ve
    **Default değeri True** olmasına rağmen, **runtime** tarafında **False olarak gelme hatası**
    düzeltildi.
- 44915 - Web arayüzünde formda **FileSelector** nesnesini **bir sonraki onaycıya**
    **göndermek** istediğimizde **ortam hata verme sorunu** düzeltildi.


- 45366 - Web arayüzünde **Hızlı Arşiv DataGrid** nesnesinde **View** butonunun
    **görünmeme hatası** düzeltildi.
- 45580 - Web arayüzünde formda **Akış** başladıktan sonra **Onay** aşamasında
    **gerçekleşen hata** düzeltildi.
- 39270 [DR5025] - Web arayüzünde form ekranında **hata mesajı** ekrana gelip
    kapatıldığında, **form ekranında tekrar işlem yapılamama hatası** düzeltildi.
- 39398 - Web arayüzünde **Uygulama dili Türkçe** iken, formdaki **dokümanlar ve akış**
    **özellikleri** içerisindeki başlıkların **Türkçe yazmama hatası** düzeltildi.
- 39674 - Web arayüzünde **Lookup** nesnesinde **Filtreleri Temizle** işleminden sonra
    verilere tıklandığında **yükleme aşamasında gözükme hatası** düzeltildi.
- 39797 - Web arayüzünde **OSF ile doldurulan Datagrid’de** filtreleme işlemi yaparken
    **büyük i harfi ve küçük i harfi ile arama işleminde oluşan farklılık (hata)** düzeltildi.
- 39842 - Web arayüzünde formda **FishBone** nesnesindeki kullanıcı seçimleri **sonraki**
    **onaycıya gitmeme** ve Nesneye veri girildiğinde **, Kaydet butonuna basılıp formu**
    **kapatıp tekrar açtığımızda kaydettiğimiz verilerin gelmeme hatası** düzeltildi.
- 40169 - Web arayüzünde **Görev Yönetimi** menüsünde listelenen **kayıtlarından**
    **birinin detayı açık** olduğunda, **farklı bir akış listelendiğinde detayın açık kalma**
    **hatası** düzeltildi.
- 40357 - Web arayüzünde formda **DocumentViewer** nesnesinde **Allow Edit** başlığı
    altında **Drawer** özelliğindeki açılan pencerede **, nesne içine eklenen dosyanın**
    **başlığının sürekli hareket etme hatası** düzeltildi.
- 40555 - Web arayüzünde form üzerinde bulunan **Aktiviteler** panelinde öne çıkan
    **Checkbox kutucuğunun görülme hatası** düzeltildi.
- 40991 - Web arayüzünde **Giriş** ekranında **Kullanıcı Adı** ve **Şifre** alanları **Edge** ve
    **Chrome tarayıcılarında farklı görünme hatası** düzeltildi.
- 41729 [DR5819] - Web arayüzünde formda **Datagrid** içerisindeki **ComboBox**
    nesnesinin **dışına tıklamadan** nesne açıkken içine tıklandığında, **sürekli olarak**
    **kapanma hatası** düzeltildi.
- 39029 - Web arayüzünde formda **Ribbon** nesnesinin **ReadOnly** özelliği **açıkken** nesne
    içerisindeki **ögelerin aktif olarak çalışma hatası** düzeltildi.
- 40613 - Web arayüzünde **Güvenlik** sekmesinde **herhangi bir güvenlik grubuna**
    eklenmek istenen **yeni** kullanıcıyı, sistemde aratırken **birden fazla seçeneğin çıkması**
    durumunda **kaymama ve diğer seçeneklerin görünmeme** hatası düzeltildi.
- 43235 [DR6238] - Web arayüzünde, **Open A Selection** formun tipi **Panel** olup **boyutu**
    **2 veya 3** olduğunda, **form taslak olarak kaydedilmek istendiğinde** hata alınma
    sorunu düzeltildi.
- 44873 - Web arayüzünde formdaki nesneye Geliştirme arayüzü tarafında **Olaylar**
    sekmesinden **bir etkinlik** eklendiği zaman bu durumun **nesneye yansımama hatası**
    düzeltildi.
- 44891 - Web arayüzünde **DataGrid’deki Statik: Row & Cell** - **Satırların hiza hatası**
    düzeltildi.


- 44972 - Web arayüzünde **Güvenlik Ayarları** sayfasında **büyük harf** ile yazılan
    kelimenin **küçük harfe dönüşmesi** ve **arama sonucu boş gelme hatası** ile **aranan**
    **dışında veri getirme hatası** düzeltildi.
- 44990 - Web arayüzünde **ComboBox** ve **LookUp** ile tetiklenen **DataGrid'e verilerin**
    **gelmemesi** ve **ilişkili** olarak oluşturulan **Datagrid’de** form doldurulup kayıt edildikten
    sonra **Datagrid’in dolmama hatası** düzeltildi.


### 3.2. Geliştirme Arayüzü

- 42121 - Geliştirme arayüzünde **DataGrid** nesnesi **Filtering Settings** özelliği altındaki
    **Row Filter Enabled** ve **Show Operation Chooser** özelliği **aktif** edildiğinde **forma**
    **yansımama hatası** düzeltildi.
- 42815 - Geliştirme arayüzünde formda **HTMLTextBox** nesnesinin **Placeholder** özelliği
    girilirken **ekran üzerindeki nesnenin titreme hatası** düzeltildi.
- 43705 - Geliştirme arayüzünde formda **Statik Treeselect** nesnesine **öge ekleme**
    **alanına isim girerken** ve **Tab** nesnesine **öge eklerken Key alanına** veri girişinde, **her**
    **girişten sonra ilgili alana tıklama hatası** düzeltildi.
- 44058 - Geliştirme arayüzünde **Çözüm Gezgini** üzerindeki **forma** , **yeni form**
    **eklenememe hatası** düzeltildi.
- 44178 - Geliştirme arayüzünde formda nesneler olmasına rağmen **Type script**
    dosyalarının **kod kısmına** yazılan **nesne adlarının altının kırmızı çizilmesi** ve
    **metotların gözükmeme hatası** düzeltildi.
- 44242 - Geliştirme arayüzünde **Akış** tarafında **Service Api** ile **Datagrid ComboBox**
    alanına **atama** işleminde, form ekranında Datagrid nesnesinde **Columns DataType:**
    **Object** ve **EditType: ComboBox** seçilerek, **Text** değerinin de **Value ile aynı olma**
    **hatası** düzeltildi.
- 38873 - Geliştirme arayüzünde **Akış** yöneticisinde **Objects** alanında **Karşılaştırma**
    nesnesinde **Comparison value değerinin boş gelme hatası** düzeltildi.
- 42524 - Geliştirme arayüzünde **Akış** tarafında **Group** nesnesinin **performans hatası**
    düzeltildi.
- 44003 - Geliştirme arayüzünde **Akış** yöneticisinde **Objects** alanında **Doküman Oluştur**
    nesnesinin **Project** bilgilerinin **boş gelme hatası** düzeltildi.
- 44174 - Geliştirme arayüzünde **Akış** yöneticisinde **GetWorkflowDataByProcessId**
    **response** modelinde **Steps** kaldırıldı.
- 44499 [DR6541] - Geliştirme arayüzünde **ServiceAPI** ile **Rest** tipindeki **Datasource** için
    **parametre gönderme hatası** düzeltildi.
- 44513 - Geliştirme arayüzünde **Akış** tarafında **Doküman Oluştur** nesnesinde **Create**
    **New Form** seçeneğinde **Project** , **Form, View, Panel Size** özelliklerinin
    **güncellenmeme hatası** düzeltildi.
- 44599 [DR6559] - Geliştirme arayüzünde **Datasource** sorgusunda
    **ProjectFormStatuses** tablosunun **Suspended hatası** düzeltildi.
- 44914 [DR6626] - Geliştirme arayüzünde formda **NumberBox** nesnesinde **Precision**
    ve ya **Step** değerine **virgüllü sayı girişi** örneğin 2.5 veya 5.6 gibi değerler girdikten
    sonra **Build işlemi sırasında hata alınma sorunu** düzeltildi.
- 45133 - Geliştirme arayüzünde **Akış** tarafında **IMembersUserGroups** modeli
    düzenlendi.
- 45147 - Geliştirme arayüzünde **Akış** tarafının özelliklerinde **mesaj olan nesnelerde**
    **MessageOptions'da Attachments** özelliklerine **Key** ve **Path** özellikleri eklendi.


- 45252 - Geliştirme arayüzünde **Akış** yöneticisinde **İstatistikleri Göster** işleminde
    **GetProcessStepsWithStatistics endpointi** düzenlendi.
- 45502 - Geliştirme arayüzünde **Akış** yöneticisinde **Steps** alanında **İstatistikleri Göster**
    **işaretlendiğinde çıkan hata mesajı** giderildi.
- 34555 - Geliştirme arayüzünde form ekranında **Lookup** , **TreeSelect** , **TreeView**
    nesnelerinde **Datasource değişikliği** yapıldığında **Display Expression** ve **Display**
    **Format alanlarının temizlenmeme hatası** düzeltildi.
- 39765 - Geliştirme arayüzünde **Kural Yöneticisi** kısmındaki **Seçim ile Değer Atama**
    özelliğinde eylem üzerinde **hedef seçiminin hatalı gösterilmesi** , **sık kullanılan**
    **seçiminde göre değişmesi hatası** düzeltildi.
- 39792 - Geliştirme arayüzünde **FishBone** nesnesine ögeler girildiğinde **, form üzerinde**
    **öge adlarının gözükmeme hatası** düzeltildi.
- 39896 - Geliştirme arayüzünde formda **Panel** nesnesinin **Title Font** özelliğindeki **Font**
    **Size değeri** arttırılmak istendiğinde **mevcut olan rakam üzerinden devam etmeyip 1**
    **(bir)'den başlama hatası** düzeltildi.
- 41299 [DR5726] - Geliştirme arayüzünde **yeni form import** edildiğinde **eski formun**
    özelliklerinin **Özellik Görüntüleyicide kalma hatası** düzeltildi.
- 41740 [DR5859] - Geliştirme arayüzünde formun **Yerelleştirme** kısmında yapılan
    **değişiklikler** sonrasında **Kaydet** denildikten sonra **yaşanılan çökme hatası** düzeltildi.
- 41907 - Geliştirme arayüzünde Akışta **Pozisyon Grubu** nesnesine Kullanıcı Grubu
    listesinde **Arama işlemi bütün sayfalar için yapılmaması** , **Büyük harf için arama**
    **yapılamaması** , **Listenin kod kolonu Kullanıcı Grup kodunu karşılamama hataları**
    düzeltildi.
- 43739 - Geliştirme arayüzünde **Akış** üzerinde **Akış kontrol** özelliği **aktif** edilen
    **Pozisyon nesnesinin Web arayüzünde tekrar onaya gelme** hatası düzeltildi.
- 44405 - Geliştirme arayüzünde **Akış** tarafında **Atama** nesnesinde **"Continue If Error**
    **Occurs"** özelliği kapatıldığında, **Continue linkinin silinmesi** ve
    **ContinueWhenErrorOccurred linkinin çizilebilme** hatası düzeltildi.
- 44407 - Geliştirme arayüzünde **Akış** tarafında **Alt Akış Çağırma** nesnesinde **Alt Akış**
    **Başlama** ve **Alt Akış Bitiş** nesnelerinin **seçim yapılamama** ve **zorunlu olmama** hatası
    düzeltildi.
- 44410 - Geliştirme arayüzünde **Akış** özelliklerinde **"Use No Manager If User's**
    **Manager Does Not Exist"** özelliği **false** yapıldığında, **No Manager** linki tanımlı olan
    nesnelerden **silinmeme** hatası düzeltildi.


### 3.3. Android

- 33266 - **Android** cihazların mobil arayüzünde **Native+** görünümündeki **DataGrid**
    nesnesinde **ProcessID, RequestID, DocumentID** ve **Oluşturma Tarihi** alanlarında
    **filtreleme işleminin çalışmama hatası** düzeltildi.
- 42850 - **Android** cihazların mobil arayüzünde, **Native+** görünümünde **StartAProcess**
    **formunun açılmama hatası** düzeltildi.
- 43887 - **Android** cihazların mobil arayüzünde, **Native+** görünümündeki **Lookup**
    nesnesinde **Current Page** özelliğinin **çalışmama hatası** düzeltildi.
- 44584 - **Android** cihazların mobil arayüzünde, **Native+** görünümündeki **Lookup**
    nesnesinde **PageSize özelliğinin çalışmama** hatası düzeltildi.
- 44492 - **Android** cihazların mobil arayüzünde, **Native+** görünümündeki **Arşiv**
    **OpenAForm** olarak açılan formdaki nesnelerde **Clear işlemlerinin yapılma hatası**
    düzeltildi.
- 44993 [DR6683] - **Android** cihazların mobil arayüzünde **Native+** görünümünde
    **Datasource alan Dinamik nesneler** , **Run At Server** olarak çalıştığında **verilerin**
    **nesneye gelmeme** ve **yükleme ekranında kalma** hatası düzeltildi.

### 3.4. IOS

- 38660 - **IOS** cihazların mobil arayüzünde, **RadioList** değerine göre **Panel** nesnesinin
    **Visible** koşulunun sağlandığı ve **Panel** nesnesinin içerisinde **ilişkili bir Datagrid’in**
    bulunduğu formda **Toolbar Button** üzerinden **Create A Form** ile **ChildForm**
    açıldığında ve geri ana forma dönüldüğünde **RadioList nesnesindeki değerin**
    **değiştirilememe hatası** düzeltildi.
- 43048 [DR6206] - **IOS** cihazların mobil arayüzünde, **Datagrid** üzerinden **Open A**
    **Selection** ile **Parametrik forma** veri eklemek için ilgili kullanıcıları seçtikten sonra,
    **Parametrik tabloda olan eski verilerin Caption alanının boş gelme hatası** düzeltildi.
- 42850 - **IOS** cihazların mobil arayüzünde, **Native+** görünümünde **StartAProcess**
    başlatılıp süreç ilerletildiğinde **ana formdan çıkma hatası** düzeltildi.
- 44584 - **IOS** cihazların mobil arayüzünde, **Native+** görünümündeki **Lookup**
    nesnesinde **PageSize özelliğinin çalışmama** hatası düzeltildi.
- 44492 - **IOS** cihazların mobil arayüzünde, **Native+** görünümündeki **Arşiv OpenAForm**
    olarak açılan formdaki nesnelerde **Clear işlemlerinin yapılma hatası** düzeltildi.


## 4. Breaking Changes

1. Projeler **tekrar** yayınlanmalıdır.
2. **Service Api instance'ı üretilirken** ;

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

<font size="5"><a href="https://portal.synergynow.io/#/_redirect/poGxV7KbC6fKbgY8YuBdgf"  target="_blank"><svg fill="currentColor" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" viewBox="0 0 40 40" style={{verticalAlign: "middle"}}><g><path d="m35.8 8.5q0.6 0.6 1 1.7t0.5 1.9v25.8q0 0.8-0.6 1.5t-1.6 0.6h-30q-0.9 0-1.5-0.6t-0.6-1.5v-35.8q0-0.8 0.6-1.5t1.5-0.6h20q0.9 0 2 0.4t1.7 1.1z m-9.9-5.5v8.4h8.4q-0.3-0.6-0.5-0.9l-7-7q-0.3-0.2-0.9-0.5z m8.5 34.1v-22.8h-9.3q-0.9 0-1.5-0.6t-0.6-1.6v-9.2h-17.1v34.2h28.5z m-11.4-13.2q0.7 0.6 1.8 1.3 1.3-0.2 2.6-0.2 3.3 0 4 1.1 0.4 0.5 0 1.2 0 0 0 0l0 0v0.1q-0.2 0.8-1.6 0.8-1.1 0-2.6-0.4t-2.9-1.2q-4.9 0.5-8.7 1.8-3.4 5.9-5.4 5.9-0.4 0-0.7-0.2l-0.5-0.2q0-0.1-0.1-0.2-0.3-0.2-0.2-0.8 0.2-0.8 1.3-2t2.9-2.1q0.3-0.2 0.5 0.1 0.1 0 0.1 0.1 1.1-1.9 2.4-4.4 1.5-3.1 2.3-5.9-0.5-1.8-0.7-3.5t0.2-2.9q0.2-0.9 0.9-0.9h0.5q0.5 0 0.8 0.4 0.4 0.4 0.2 1.5-0.1 0.1-0.1 0.2 0 0 0 0.1v0.7q0 2.8-0.3 4.3 1.2 3.7 3.3 5.3z m-12.9 9.2q1.2-0.6 3.1-3.5-1.2 0.8-2 1.8t-1.1 1.7z m8.9-20.6q-0.4 1-0.1 3 0.1-0.2 0.2-1 0-0.1 0.1-0.9 0.1-0.1 0.1-0.2 0-0.1 0-0.1t0 0 0 0q0-0.5-0.3-0.8 0 0 0 0v0z m-2.8 14.8q3-1.2 6.4-1.8-0.1 0-0.3-0.2t-0.4-0.3q-1.7-1.5-2.8-4-0.6 2-1.9 4.4-0.7 1.3-1 1.9z m14.4-0.4q-0.5-0.5-3.1-0.5 1.7 0.6 2.8 0.6 0.3 0 0.4 0 0 0-0.1-0.1z"></path></g></svg>PDF Download</a></font>
