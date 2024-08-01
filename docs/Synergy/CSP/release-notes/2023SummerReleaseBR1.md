---
sidebar_position: 2333
sidebar_label: "2023 Summer Release BR1"
custom_edit_url: ""
---

# Bimser Synergy 2023 Summer Release Notes BR1
*(1 Ağustos 2023 - 30 Eylül 2023)*

## 1. Highlights / New Features

- 53209 - Geliştirme arayüzünde **RelatedDocuments** nesnesinin **Property Inspector'a**
    **Enable OCRData** özelliği eklendi. Aktif edildiğinde, yüklenen dosyanın **OCR verisi**
    **oluşturulup veri tabanına** kayıt edilir.
- 50706 - Geliştirme arayüzünde **CSharp** ve **TypeScript** dosyaları için **Chatgpt**
    kullanarak **kod düzeltme işleminin yapılması** sağlandı.
- 53391 - Geliştirme arayüzünde **ComboBox, TagBox, TreeSelect** nesnelerinin
    **'Yenilemeye Zorla'** butonunun görünürlüğü **Hide Force Refresh Button** ile kontrol
    edilmesi için eklendi.
- 37728 - Geliştirme arayüzünde formun **cs** tarafına yanlış yazılan **kodun doğru halini**
    gösteren **"Kodu Yapılandır" butonu** geldi. **Bozulan kod yapısını düzeltip** formata
    uygun hale getirmek için **"Format" butonu** geldi. **Hatalı olan yeri göstermek** için
    **"Code Check" butonu** geldi. **Kullanılmayan kütüphaneleri gizlemek** için **"Fix Usings"**
    **butonu** geldi.
- 54931 - Colorpicker nesnesine **Show text, Allow Clear, Trigger** , **Format** gibi yeni
    özellikler eklendi. Yeni eklenen bu özelliklerin endpointleri hazırlandı.
- 34093 [DR2629] - Web arayüzünde Form ekranında **RelatedDocuments** nesnesine
    yüklenen **PDF dosyasına Yazdır özelliği** eklendi.
- 54777 - Web arayüzünde, **akış gönderilen kullanıcıya sağ altta bildirim gelmesi**
    sağlandı.
- 56332 - Web arayüzünde **Yönetim Araçları** menüsünün altındaki **Güvenlik** panelinde
    **istenilen proje ya da özelliğe ulaşmayı kolaylaştırmak için filtre özelliği** eklenmiştir.
- 56475 - Geliştirme arayüzünde, formun **css** dosyasına **Datagrid** kolonuna **özel css**
    **özellikleri** ekleyebilmek için, **projectname_formName_datagridname_columnname**
    şeklinde bir **Class yazılarak kolonlara style özelliği** eklendi.

```
Örnek kullanım,
```
```
.ant-modal-wrap .ProjeAdi_FormAdi_DataGrid1_NewColumn2 .ant-modal-content {
```
```
width:800px !important;
height: 200px;
border: 8px solid rgb(245, 6, 6);
}
```
- 54815 - Web arayüzünde **Datagrid nesnesi Tarih kolonlarına Eşittir filtresi** eklendi.


- 54901 - Geliştirme arayüzünde **Colorpicker** nesnesinde **Özellik Görüntüleyici** başlığı
    altına **Show Text, Allow Clear, Trigger (Click - Hover), Format (Rgb - Hex - Hsb)**
    **özellikleri** nesneye eklendi.
- 56214 - Web arayüzünde Ana sayfada bulunan süreç detaylarına **Fast Approval (Hızlı**
    **Onay)** özelliği eklendi.
- 56324 - Geliştirme arayüzünde **RelatedDocuments** nesnesine **Categories** başlığı
    içerisinde **Min. File Count özelliği** eklendi. Bu özellik sayesinde kullanıcının belirlediği
    **Minimum dosya sayısı** altında nesneye yükleme yapıldığında **akış ilerlememekte ve**
    **pop-up uyarısı** vermektedir.


## 2. Improvements

- 52159 - Web arayüzü **Doküman Yönetiminde Abonelik işlemlerindeki kodlar**
    **iyileştirildi**.
- 51350 - Web arayüzünde **Vekalet ve Erişim Anahtarları** kısmında **yeni Vekalet**
    **oluşturma** , oluşturulan Vekalete **yetkiler verip kaldırma ve Vekalet panelinin**
    **arayüzünde iyileştirmeler** yapıldı.
- 52216 - Web arayüzünde **getUserDetail** endpointindeki dönen **canCodeRefactor**
    bilgisi **True** olan kullanıcılarda **{{webinterfacewebapiurl}}/CodeRefactor/CodeRefac**
    endpointine kodu endpointe gönderip mevcut kodun **Refactor edilmiş kod ile**
    **değiştirilmesi** durumu geliştirildi.
    {
    "code" : "var a = 1;",
    "customPrompt" : ""
    }
- 42898 - Geliştirme arayüzünde **birden fazla Build Service çalışılabilme özelliği**
    geliştirildi.
- 52024 - Geliştirme arayüzünde **formun açılması** ve **kaydedilmesinde oluşabilecek**
    **hatalar için** geliştirilme yapıldı.
- 48321 - Web arayüzünde **Beni Hatırla** özelliğini kullanarak **Harici Hesap Yönetimi** ile
    giriş yapıldığında **tarayıcı kapatılıp tekrar açıldığında Oturumun Hatırlanma**
    geliştirmesi yapıldı.
- 50993 - Geliştirme arayüzünde oluşturulan bir **Aksiyon formunun Durum** alanında
    **değişiklik yapılması için geliştirme** yapıldı.
- 53372 - Web arayüzünde **Olay Günlük Görüntüleyici raporunun alınabilmesi için**
    geliştirme yapıldı.
- 42627 - Web arayüzünde **Çoklu Silme işleminde hata dönmemesi için** endpoint
    geliştirildi.
- 50710 - Geliştirme arayüzünde **Yerelleştirme** ekranı ve Form nesnelerindeki
    **Multilanguage** alanlarda çalışmak üzere **Otomatik Çevir** butonuyla **boş değerlerin dil**
    **karşılıkları ile doldurulması** sağlandı.
- 48605 - Geliştirme arayüzünde **Build** alındıktan sonra, **son gelen link** açıldığında **Build**
    **'de yapılan tüm işlerin görüntülenmesi** sağlandı.
- 52115 - Geliştirme arayüzünde **Yerelleştirme** form kapanmadan form üzerindeki
    **Toolbar'a eklenmiş** bir buton ile **Yerelleştirme formunun açılması** sağlandı.
    Güncellemeler yapıldıktan sonra **kaydedilen json veri** form üzerindeki **veriyi**
    **değiştirmesi** sağlandı. Yerelleştirme penceresinin **Panel yerine modal form şeklinde**
    **açılması** sağlandı.
- 54965 - Web arayüzü **Doküman Yönetiminde Profil Form** ile doldurulan
    dokümanların **Tablo görünümünde filtrelenme özelliği** geliştirildi.


- 6361 - Geliştirme arayüzünde **Depo, Klasör** ve **Dosyalara** giriş yapıldığında **aktivite**
    **girişinde yapılma özelliği** geliştirildi.
- 54903 - Web arayüzü **Doküman Yönetiminde Aktivite mesajlarının dile göre gelmesi**
    durumu geliştirildi.
- 55456 - Web arayüzünde Depo ve klasörlerin içerik bilgilerinin hesaplandığı
    **CalculateCounts** ve **CalculateSizes endpointleri** geliştirildi.
- 40654 - Geliştirme arayüzünde deploy alınan projelerin **hangi versiyon ile** ve **hangi**
    **deploy agent üzerinde çalıştığı bilgileri** endpointe eklendi.
- 53742 [DR8904] - Geliştirme arayüzünde **Akış Yöneticisinde** devam eden akışlarda
    **Rollback işlemi** sonrası **değiştirilen özelliklerin akışa yansıması** sağlandı.
- 54471 - Web arayüzünde **Onaylar** listesinde **hızlı onay verebilme** özelliğinin **Backend**
    **parametreleri** geliştirildi.
- 54792 - **Dapper** ile geliştirilmiş **Persistence Provider'ın EFCore'a geçişi** sağlandı.
- 54796 - Web arayüzünde **Datagrid** içinde bulunan **ComboBox** tipli **Dinamik**
    kolonlarına seçeneklerini **Ekleme** veya **Düzenleme** esnasında **üstüne tıklanarak**
    **verilerin gelmesi** sağlandı.
- 48030 - Web arayüzünde formda **UserMetaData** nesnesinde, **Select Metadata Type**
    özelliğinden seçilen **Company** ve **CompanyID özelliklerinin gözükme geliştirmesi**
    yapıldı.
- 27687 [YA24866] - Web arayüzü **Dashboard** ekranında **Onaylar** sayısının ve **listesinin**
    **sayfanın yenilenmesine** ihtiyaç duymadan **direkt ekrana düşme** ve **güncelleme**
    özelliği geliştirildi.
- 22365 - Geliştirme arayüzünde **Akış** tarafında **Events** özelliklerinde aktif edilen **Fast**
    **Approval** özelliği ile **İş Akış Yönetiminde Bekleyen İşler'de** süreç içeriği açılmadan
    kullanıcının listede gösterilecek olay butonları ile **süreci ilerletebilmesini ve istenirse**
    **gösterilecek butonların özelleştirilebilmesini sağlayan geliştirme** yapıldı.
- 42933 - Web arayüzünde **Datagrid** içinde bulunan **ComboBox** tipli **Dinamik**
    kolonlarına seçeneklerini **Ekleme** veya **Düzenleme** esnasında **üstüne tıklanarak**
    **verilerin gelmesi** sağlandı.
- 50708 - Geliştirme arayüzünde formda **.cs** dosyasında yazılan **kodların formatının**
    **bozulması** durumunda, kodların seçilip sağ tıklayıp **"Format Document"** ve ya üst
    bardaki **"Format"** butonuna basılarak tekrar **tüm yazılanların formata uygun hale**
    **getirilmesi** sağlandı.
- 54764 - Web arayüzü **Doküman Yönetiminde** Kolon seçicinin **Local Storage ile**
    **birlikte kayıt edilme özelliği** geliştirildi.
- 54928 - Web arayüzünde **Tema** ayarlarında ve **Menü ekleme** panelindeki **Colorpicker**
    **özellikleri** düzenlendi. Geliştirme arayüzünde formda **Colorpicker** nesnesinin **Menü**
    **Özellikleri ve Ribbon nesnesinin Colorpicker özelliği** yenilendi.
- 55516 - Web arayüzü **Doküman Yönetiminde Profil Form** ile doldurulan
    dokümanların **Tablo görünümünde filtrelenme özelliği** geliştirildi.
- 55134 - Web arayüzü **İnsan Kaynaklarında Kullanıcı Grubuna toplu şekilde Kullanıcı**
    **kaydedilme** özelliği geliştirildi.


- 54804 - Web arayüzünde **İş Akış Yönetimi** menülerinin her biri için panel açıldığında
    **50 adet veri yüklenmesi** , eğer daha fazla veri varsa **kaydırmanın** , en alta gelince
    **GetWorkflowItems endpointinin tetiklenmesi** sağlandı.
- 55457 - Web arayüzü **Doküman Yönetiminde Özellikler** penceresine **Ayrıntılar** adı
    altında **Depo ve Dosya İçeriğini Gösterme çalışması** yapıldı.
- 55509 - Web arayüzü **Doküman Yönetiminde** açılan dosyaların **Panel** isimlerinin
    **büyütülme özelliği** geliştirildi.
- 56307 - Web arayüzü Doküman Yönetiminde **Rapor ve Tarihçe alanlarının**
    **kaldırılması** sağlandı.
- 56327 - Web arayüzünde **İnsan Kaynakları** sekmesinde **Kullanıcılar** panelinde
    **Amirler** kısmında **Tüm Anahtarlar** için **Silme butonu** gelmesi **engellenerek** , anahtarın
    içinde **bir yönetici varsa Silme butonu gelecek şekilde** geliştirme yapıldı.
- 56328 - Geliştirme arayüzünde **UserMetaData** nesnesinin **Select Metadata Type :**
    **Custom** ve **Custom Metadata Field Name: Tarih formatı** olarak seçilen durumda
    Web arayüzünde nesnedeki **Tarih** formatının **İnsan Kaynaklarındaki format ile aynı**
    **olması** sağlandı.
- 56330 - Geliştirme arayüzünde **Akış** tarafında **Variables** alanında **Kontrol Ekleme**
    işleminde **seçilen formdaki nesnelerin sıralı halde listelenmesi** sağlandı.
- 56331 - Geliştirme arayüzünde **Arşiv Datagrid'inde MultiLanguage** kolonlarında
    **uygulamada kullanılan dil** hangisi ise o **dil seçeneğiyle verilerin gelmesi** sağlandı.
- 56473 - Geliştirme arayüzünde **Lookup** nesnesine girilen **Caption** verisinin Web
    arayüzünde **Lookup** nesnesinin **Popover** görünümünde **başlık üzerinde**
    **görüntülenmesi** sağlandı.
- 59971 - Web arayüzünde **Dashboard** ekranında ve **İş Akış Yönetiminde** proje bazlı
    yetkisi olmayan kullanıcılar **akış detaylarına girmek** istediğinde, **hata mesajının**
    **kullanıcıya gösterilme özelliği** geliştirildi.
- 60097 - Web arayüzünde **Giriş işlemlerinde performans iyileştirmeleri** yapıldı.
- 54954 - Web arayüzü **Güvenlik** modülünde **İnsan Kaynakları Yetki Grubu** izinlerinde,
    Görüntüleme izni **"İzin verme"** olarak seçildiğinde, ilgili menünün **(İnsan Kaynakları -**
    **Kullanıcı - Görüntüleme gibi) görünürlüğü** kaldırıldı. **Düzenleme izini sınırlandığında**
    ise kayıt **Kaydet** butonunun **Pasif edilme geliştirmesi** yapıldı.
- 59855 - Geliştirme arayüzünde **form .ts dosyasında Fast Approve** etkinliğinin
    **tetiklenebilmesi** sağlandı.
    await (this as any).fastApprove({
    eventId: 5,
    projectName: " ",
    flowName: " ",
    processId: 123,
    requestId: 456
    });


## 3. Fixes

### 3.1. Web Arayüzü

#### 3.1.1. Doküman Yönetimi

- 10998 - Web arayüzü **Doküman Yönetiminde** dosyalara **Çalışma Başlat** denilip **uzun**
    **veriler** yazıldığında, **özel karakterler** kullanılıp **Yayınla** dendikten sonra meydana
    gelen hata düzeltildi.
- 39320 - Web arayüzü **Doküman Yönetiminde** klasör ve depolar arası gezinirken
    **seçilen dosya ve klasörlerin koordinatlarının temizlenmeme hatası** düzeltildi.
- 51047 - Web arayüzü **Doküman Yönetiminde Gelişmiş aramada Excel'e Aktar** işlemi
    yaparken oluşturulan **Excel'in ID ile gelme hatası** düzeltildi.
- 51082 - Web arayüzü **Doküman Yönetiminde** ilişkilendirilen **dosyalardaki açıklama**
    **alanı hatası** düzeltildi.
- 52094 - Web arayüzü **Doküman Yönetiminde Tablo görünümüne** geçerken oluşan
    **e.localeCompare hatası** düzeltildi.
- 22182 [YA23608] - Web arayüzü **Doküman Yönetiminde docx uzantılı** dosyaların **son**
    **versiyonda görüntülenememe** durumu düzeltildi.
- 48362 - Web arayüzünde **Doküman Yönetimi** üzerinde bir **doküman imzalarken**
    alınan **object object hatası** düzeltildi.
- 53950 - Web arayüzünde **Doküman Yönetimi Tablo** görünümündeyken **, get**
    **repositories endpointinin birden fazla istek atma hatası** düzeltildi.
- 53622 [DR8887] - Web arayüzü **Doküman Yönetiminde Profil form eklendikten**
    sonra **tablo** görünümünde yapılan **filtre ile eklenen dosyanın bulunamama hatası**
    düzeltildi.
- 55508 - Web arayüzü **Doküman Yönetiminde Doküman isminin iki defa görünme**
    **hatası** düzeltildi.
- 55532 [DR9130] - Web arayüzü **Doküman Yönetiminde Profil form gösterme**
    işleminde formdaki **değerlerin dolu gelmeme hatası** düzeltildi.
- 39965 - Web arayüzü **Doküman Yönetiminde Çöp Kutusundan veri silinmek**
    istendiğinde, **anlam karmaşası yaratan uyarı mesajı hatası** düzeltildi.
- 40030 - Web arayüzünde **Doküman Yönetimi** üzerinden klasöre sağ tıklayıp
    **Özellikler** kısmından **Yeni Dosya ekleme** işleminde **proje seçildiğinde gözükmeme**
    hatası düzeltildi.
- 45500 - Web arayüzü **Doküman Yönetiminde** fare ile kaydırarak hareket
    ettirildiğinde, **Düzenle** ve **Sil butonlarının satır dışında görünme hatası** düzeltildi.
- 50493 - Web arayüzü **Doküman Yönetiminde üst menü Favorilere Ekle** esnasında
    **oluşan hata** düzeltildi.
- 53577 [DR8879] - Web arayüzü **Doküman Yönetiminde versiyon numaralarının**
    **gösterilmeme** hatası düzeltildi.
- 48891 - Web arayüzünde **Doküman Yönetiminde** açılan uzantıların **Panel Size**
    değiştirildiğinde **yazıların üst üste gözükme hatası** düzeltildi.


- 52255 - Web arayüzünde **Doküman Yönetiminde** dosya seçim yapılıp seçim
    kaldırılınca, **üst menünün açık kalma hatası** düzeltildi.
- 53583 [DR8875] - Web arayüzü **Doküman Yönetiminde Tablo** görünümünde **Paging**
    sebebiyle **Filtre** işlemiyle **arama işleminin yapılamama hatası** düzeltildi.
- 53946 - Web arayüzünde **Doküman Yönetimi** ve **Panellerdeki hiza ve tasarım**
    **sorunları** düzeltildi.
- 54453 - Web arayüzü **Doküman Yönetiminde içeriklerin kaydedilmeme hatası**
    düzeltildi.
- 55328 - Web arayüzü **Doküman Yönetiminde Word** dosyalarında **Çalışma Başlat**
    denildikten sonra **değişikliklerin kaydedilmeme hatası** düzeltildi.
- 61508 - Web arayüzü **Doküman Yönetiminde docx dosyası** içeriğine, **docx** uzantılı
    **başka içerikler eklendiğinde görüntülenememe hatası** düzeltildi.
- 60727 [DR9512] - Web arayüzünde **Doküman Yönetiminden dosya tipleri kısıtlanan**
    **RelatedDocuments** nesnesinde, **farklı bir dosya türü** eklenmeye çalışıldığında çıkan
    **sistemsel hata mesajının anlaşılır bir dilde olmama hatası** düzeltildi.
- 61114 - Web arayüzü **Doküman Yönetiminde Çöp Kutusunda silinen verilerin**
    **gelmeme hatası** düzeltildi.
- 59843 - Web arayüzü **Doküman Yönetiminde** formda yapılan değişikliklerin **Tablo**
    **görünümüne Güncelleme yapılmama hatası** düzeltildi.
- 61560 - Web arayüzü **Doküman Yönetiminde Profil Form** ile oluşturulmuş formda
    **güncelleme** işleminin **Tablo görünümüne yansımama hatası** düzeltildi.


#### 3.1.2. İş Akış Yönetimi......................................................................................................................

- 41449 - Web arayüzü **İş Akış Yönetimi** modülünde **Geçmiş - Onaylar** alanında **bitiş**
    **tarihine göre filtre yapılamama hatası** düzeltildi.
- 44417 - Web arayüzünde **İş Akış Yönetimi** menüsünde **Geçmiş - Onaylar** ve
    **Oluşturduğum İşler** panel filtrelerinin **başlangıç tarihine göre çalışmama** hatası
    düzeltildi.
- 52422 - Web arayüzünde **İş Akış Yönetimi** modülünde **Geçmiş Onaylar** alanında **Bitiş**
    **tarihine göre filtre yapılamama hatası** düzeltildi.
- 55485 - Web arayüzünde **İş Akış Yönetimi** menüsünde **Datagrid** üzerinde **proje**
    **açılırken oluşan hareket sorunu** düzeltildi.
- 55485 - Web arayüzünde **İş Akış Yönetimi** menüsünde **Datagrid** üzerinde **proje**
    **açılırken oluşan hareket sorunu** düzeltildi.
- 55485 - Web arayüzünde **İş Akış Yönetimi** menüsünde **Datagrid üzerinde proje**
    **açılırken oluşan hareket sorunu** düzeltildi.
- 52253 - Web arayüzü **İş Akış Yönetimi** panelindeki Datagrid'lerde **Tarih** kolonundaki
    **tüm tarihler için "daha eski"** yazma hatası düzeltildi.
- 56366 - Web arayüzünün **İş Akış Yönetiminde Bekleyen İşler sayfasında Fast**
    **Approval** işleminde, **Reddet** işleminde açılan pencere kapatıldığında **sayfanın**
    **yükleniyor durumda kalma hatası** düzeltildi.
- 60052 - Web arayüzünde **İş Akış Yönetimi** , **Görev Yönetimi** ve **Süreç** detaylarındaki
    **Datagrid’lere verilerin gelmeme hatası** düzeltildi.
- 50742 - Web arayüzünde **İş Akış Yönetiminde** süreç açıldığında **form yüklenmeden**
    **onaylandığında alınan konsol hatası** düzeltildi.


#### 3.1.3. İnsan Kaynakları

- 39687 - Web arayüzünde **İnsan Kaynakları** modülünde **Kullanıcı tanımlama**
    ekranında **Sicil Numarası** ve **Vatandaşlık Numarası** alanlarına, aynı şekilde **Şirket**
    **Tanımlama** ekranında **Şirket Sicil Numarası alanına alfabetik değer girilme hatası**
    düzeltildi.
- 50388 - Web arayüzünde **İnsan Kaynakları** modülünde kullanıcıya ait **İşe Başlama** ve
    **İşten Ayrılma Tarihi alanlarının silinememe hatası** düzeltildi.
- 44683 - Web arayüzünde **İnsan Kaynakları** sekmesinde **Panel boyutu minimum**
    olarak işaretlendiğinde, **açılan birden fazla paneldeki tasarım hatası** düzeltildi.
- 50387 - Web arayüzü **İnsan Kaynakları Kullanıcı ekleme** alanında **sabit telefon** ve
    **sabit kişisel telefon numarası** için alan kodunun yazılacağı kısma, **5 rakamı default**
    **olarak gelme hatası** düzeltildi.
- 52207 - Web arayüzünde **İnsan Kaynakları** modülünün **Organizasyon Bakımı**
    alanında **Kayıt Düzenle butonu** ile açıldığında, orta panelden **kayıt silindiğinde**
    **Güncelle panelinin açık kalma hatası** düzeltildi.
- 53686 - Web arayüzünde **İnsan Kaynakları Mesai** menüsünde **Datagrid** üzerindeki
    **faktör kolonundaki sıralama hatası** düzeltildi.
- 54947 - Web arayüzünde **İnsan Kaynakları** kısmının **Kullanıcılar** menüsünde **kullanıcı**
    **kayıtlarının düzenlenememe hatası** düzeltildi.
- 55451 - Web arayüzü **İnsan Kaynaklarında Maaş** menüsünde **Insert işlemi** yaparken,
    aynı kullanıcıya **birden fazla eklenen maaşta Update uç noktasının çalışma hatası**
    düzeltildi.
- 56118 - Web arayüzü **İnsan Kaynaklarında Maaş** menüsünde **aynı kullanıcıya aynı**
    **tarihlerde maaş girilmek** istendiğinde, **uyarı mesajı vermeme** hatası düzeltildi.
- 56251 - Web arayüzünde **İnsan Kaynakları** kısmının içerisindeki herhangi bir bölüme
    girdikten sonra **üstteki sekmeden çarpı ile kapattığımızda ortamın hata verme**
    durumu düzeltildi.
- 44451 - Web arayüzünde **İnsan Kaynakları** kısmının **Özellikler** bölümünde **Kullanıcı**
    **Özellikleri** alanında **zorunlu alan** olarak eklenen bir alanın, **Kullanıcı Tanımlama** ya da
    **Güncelleme** ekranında doldurulmadan **Kaydet** butonunun **aktif olma hatası** ve
    **Doğru / Yanlış** tipindeki **varsayılan değer ile atanmış zorunlu bir alanın değeri**
    değiştiğinde, **zorunlu alan uyarısının alınma hatası** düzeltildi.
- 50301 - Web arayüzünde **İnsan Kaynakları** modülünde **Özellik** tanımlanırken
    **açıklama bilgisinin özellik üzerinde görünmeme hatası** ve **Çoklu dil desteği** ile
    tanımlanan özelliği kullanıldığında **varsayılan değerin görünmeme hatası** düzeltildi.
- 50307 - Web arayüzünde **İnsan Kaynakları Kullanıcı Özelliklerinde** bulunan **Özellik**
    **Taşıma** kolonundaki **Sıralama hatası** ve **Mesailer** Datagrid 'indeki **Silme Kolonu,**
    **Yönetici Anahtarı, Şirket** ve **Vardiya** Datagridlerindeki **Silme kolonu sıralama hatası**
    düzeltildi.


- 50309 - Web arayüzü **İnsan Kaynakları** modülünde **Kullanıcı Tanımlama** ekranında
    **varsayılan değeri olan zorunlu bir alanın** , **varsayılan değeri silinerek kaydedilebilme**
    hatası düzeltildi.
- 50333 - Web arayüzü **İnsan Kaynakları** modülünde **Kullanıcı Grubu güncelleme** ve
    **Pozisyon Güncelleme** işlemlerinde kayıt işleminin gerçekleştiğini belirten **uyarı**
    **mesajının kayıt tamamlandığında gelmeme hatası** düzeltildi.
- 50350 - Web arayüzünde **İnsan Kaynakları Kullanıcı bilgileri** oluşturulurken **pasif**
    olan **Departman, Unvan** ve **Şirketin seçim alanlarında görünme hatası** düzeltildi.
- 52944 - Web arayüzü **İnsan Kaynakları** kısmının **Kullanıcılar** alanında bir kullanıcı
    kaydı açılıp başka bir kullanıcı seçildiğinde, **'Form kaydedilmedi, Kapatmak**
    **istediğinizden emin misiniz'** uyarısına **Hayır** dendiğinde **kullanıcı bilgilerinin ikinci**
    **seçilen kullanıcı bilgilerini gösterme** hatası düzeltildi.
- 53620 - Web arayüzünde **İnsan Kaynakları** modülünde **Kullanıcı bilgileri**
    değiştirildiğinde **Kaydet** butonunun **aktif olmama hatası** düzeltildi.
- 56406 [DR9208] - Web arayüzünde **İnsan Kaynakları Mesailer** sekmesinde **Yeni**
    **Mesai** eklenirken **Mesai** adında **boşluk** kullanıldığında alınan **regexp hatası** düzeltildi.
- 56437 - Web arayüzünde **İnsan Kaynakları** panelinde **Kullanıcı Grupları**
    **düzenlenmeme hatası** düzeltildi.


#### 3.1.4. Web Ana Sayfa

- 52824 - Web arayüzünde **Hesabım** menüsünde **Vekalet ve Erişim Anahtarları**
    kısmında **Vekalet verme** işleminde **proje bazlı vekalet** verildiğinde **kullanıcının**
    **menüye erişememe hatası** düzeltildi.
- 50749 - Web arayüzünde **Aksiyon Yönetimi Kanban** ekranında **Başlangıç tarihine**
    göre **filtreleme yapılamama** hatası düzeltildi.
- 50895 - Web arayüzünde formda **RelatedDocuments** nesnesini **İçe Aktar** deyip
    ortama aktarıldığımızda **"Bilgisayardan Seç"** ve **"Yerel dosya sistemi"** kısımlarının
    **açılmama hatası** düzeltildi.
- 50984 - Web arayüzünde yayınlanmış olan bir **aksiyon formunun Geliştirme arayüzü**
    tarafında **durum** alanındaki **ögeleri değiştirildiğinde formun açılmama hatası**
    düzeltildi.
- 52095 - Web arayüzünde **Parametreli** formda yer alan **Datagrid** nesnesi **Primarykey**
    olarak belirlenen **object: ComboBox** kolonundan **seçim** yapıldığında ve **Datepicker**
    **kolonunda update yapılınca alınan object referans hatası** düzeltildi.
- 52175 - Web arayüzünde **Parametreli** formda yer alan **Datagrid** nesnesi **Columns**
    özelliği **Auto Increment** seçiliyken, **iki veya daha fazla kullanıcı aynı anda veri**
    **ekleme** işlemi yaptığında alınan **Primarykey hatası** düzeltildi.
- 52380 - Web arayüzünde **Datagrid’i Row Change** ve **Decimal** ile **Primary Key** ve **Auto**
    **Increment** olan formda **aynı anda eklenen veriye işlem yapılmak** istendiğinde,
    **veriler aynı ID ile oluştuğu** için **eklenen diğer veriye düzenleme işlemi yapılamama**
    hatası düzeltildi.
- 52203 - Web arayüzünde **Datagrid** nesnesi **Row ve Cell** modundayken
    **String:Numberbox** , **String:Combobox** kolonlarına veri eklendikten sonra
    onaycıdayken yazılan veriler temizlendiğinde, **sonraki onaycıda temizlenen verilerin**
    **hala gelmeye devam etme hatası** düzeltildi.
- 52341 - Web arayüzünde formda **cs** tarafında **Text verisi Transfer nesnesine**
    **yazdırılmama** hatası düzeltildi.
- 52461 - Web arayüzünde, **Datagrid’e aynı anda veri ekleyen iki kullanıcı** olduğunda
    birinin formunda verilerin tamamı gözükürken diğerinde **Yenile** butonuna tıklamadan
    **veriler gelmemekte** , bu durumdayken görünen verinin aynısını **bir kullanıcı**
    **siliyorken** diğer kullanıcı **silinen veriyi görmeye** devam ettiği için **üzerinde işlem**
    **yapmak istediğinde alınan hata** düzeltildi.
- 52495 - Web arayüzünde **Datagrid** nesnesi **Number** kolonu **Auto Increment** olarak
    işaretlendiğinde **akışta verilerin aynı gelme hatası** düzeltildi.
- 52892 - Web arayüzünde form ile birlikte gelen **StartParameters** endpointinde profil
    form ile **ilgili projeye eklenen dosya bilgisinin gelmeme hatası** düzeltildi.
- 53004 - Web arayüzünde **Datagrid** nesnesine veri eklendiğinde alınan **Parameter**
    **Count hatası** düzeltildi.
- 52713 - Web arayüzünde **Datagrid** nesnesinde **ComboBox** kolonu bulunan form
    **onaycıda açılıp** düzenleme yapılmak istendiğinde **seçili gelmeme hatası** düzeltildi.


- 52720 [DR8762] - Web arayüzünde **Datagrid** nesnesinde **ComboBox** kolonu bulunan
    form **onaycıda açılıp** düzenleme yapılmak istendiğinde **seçili gelmeme hatası**
    giderildi.
- 52738 [DR8770] - Web arayüzünde **default** görünümde yazılan **değişiklikler forma**
    **yansırken** aynı nesnenin diğer görünümünde yapılan değişikliklerin **forma**
    **yansımama hatası (SwitchView(viewName)) metodu ile** düzeltildi.
- 38658 - Web arayüzünde **Yeni Duyuru Ekleme** işlemi yapılırken iletilerdeki
    **MultiLanguage** butonuna tıklandığında **ortaya çıkan görüntü hatası** düzeltildi.
- 47837 [DR7539] - Web arayüzünde **Pozisyon Grubundaki** kişilere düşen **süreç**
    **onayının çoklanma hatası** düzeltildi.
- 45480 - Web arayüzünde form ekranında **RelatedDocuments** nesnesinde **önizleme**
    **hatası** giderildi.
- 46159 - Web arayüzünde **Güvenlik Ayarları** menüsünde **Grup Ekle** ve **Yenile**
    butonlarının **Birincil renkte görünmeme hatası** düzeltildi.
- 50160 [DR8119] - Web arayüzünde **Client** tarafında **Client Enabled** ve **ReadOnly**
    özellikleri aktif edilen **Panel** nesnesinin **içindeki nesnelere hala veri girilebilme hatası**
    düzeltildi.
- 50393 - Web arayüzünde form ekranında **Run at server** özelliği **aktif** olan **ListBox**
    nesnesinde **arama yapılmama hatası** düzeltildi.
- 50511 - Web arayüzünde **Left** menüde uygulama ismi uzun senaryolarda **Dropdown**
    **ikonu menü etiketin üzerine gelme hatası** düzeltildi.
- 50877 - Web arayüzünde **Yıllık İzin sürecinde konsola hata düşme** sorunu düzeltildi.
- 50888 - Web arayüzünde **Datasource bağlı olmayan Datagrid** nesnesinde veri
    eklenip kaydedildikten sonra **Ekle, Sil, Düzenle butonlarının nesneye geç yansıma**
    hatası düzeltildi.
- 50988 [DR8320] - Web arayüzünde **Uygulama Gezgininde ikon olan bir menü**
    güncellendiğinde **var olan ikonun silinme hatası** düzeltildi.
- 51149 - Web arayüzünde **Datagrid** nesnesi **Save on: Row Change** seçiliyken
    işlemlerde oluşan yavaşlık hatası düzeltildi.
- 51987 - Web arayüzünde **DataGrid: Statik - Save On: Row Change** üzerinde veri
    eklenmek istendiğinde **uyarı mesajındaki yazım hatası** düzeltildi.
- 52047 - Web arayüzünde **Datagrid** nesnesi **Create a form Toolbar Button** ile açılan
    formda yer alan **Row Change** özelliği **aktif Datagrid'in** veri eklenirken **formun**
    **kendiliğinden kapanma hatası** düzeltildi.
- 52291 [DR8660] - Web arayüzünde **DataGrid Cell** modundayken, kolonlarda **Ekle ve**
    **Güncelle** işlemleri sırasında **kolon isimlerinde oluşan kayma hatası** düzeltildi.
- 52292 [DR8661] - Web arayüzündeki formda **DataGrid cell** modda iken, **Edit Type**
    özelliği **NumberBox** olan kolona değer girildiğinde, eğer kolon özelliği **Show Editor**
    **Always** özelliği de **açık** ise nesnenin her değer girişinde **odağından çıkıp akıcı şekilde**
    **veri girilememe hatası** düzeltildi.
- 52432 - Web arayüzünde **Transfer** nesnesinde **Date** verileri nesneye yansımasına
    rağmen **seçim yapılamama hatası** düzeltildi.


- 52559 - Web arayüzünde **Statik Datagrid cell** modda, **Save on: Row Change**
    seçiliyken **Parametreli** formda **verilerin listelenmeme** ve **Yenile butonu** yerine
    **Hepsini Temizle** butonuna tıklayınca **verilerin listelenme hatası** düzeltildi.
- 52659 [DR8356] - Web arayüzünde açılmış olan formdaki **Lookup** nesnesinde seçim
    yapılıp akış ilerletildikten sonra, **Geliştirme arayüzünde Lookup** nesnesine ait V **alue**
    **Expression değeri** değiştirilip deploy alınıp, **Lookup** nesnesinin içerisinde bulunan
    **formdan seçim yapılınca konsola düşen uyarı mesajları** düzeltildi.
- 52690 - Web arayüzünde **Dashboard** ekranında **GetAllAnnouncementsStartup**
    **endpointinin 500 dönme hatası** düzeltildi.
- 47535 [DR7431] - Web arayüzünde **Dashboard** ekranında **Bekleyen Onaylar**
    alanından bir form onaylandığında **bekleyen onay sayısının değişmeme hatası**
    düzeltildi.
- 51849 [DR8542] - Web arayüzünde **Datagrid** nesnesi **Action Button** aracılığıyla **satır**
    **kopyalanma işlemi** sonrasında nesnenin **Paging yapısının bozulma hatası** düzeltildi.
- 51853 [DR8453] - Web arayüzünde **Datagrid** nesnesi **TextBox** kolonuna **hızlı veri**
    **girişi yapılırken alınan hata** düzeltildi.
- 52721 [DR8766] - Web arayüzündeki formlarda **herhangi bir nesnede Required** alan
    **aktif** edilip, nesneye **veri yazılmadan** form kaydedilmek istendiğinde, **farklı**
    **görünümlerde zorunlu alan uyarısı ve nesneye odaklanmama hatası** düzeltildi.
- 53079 [DR8817] - Web arayüzünde **form instance** ile **Datagride** satır eklendikten
    sonra **Delete butonunun pasif gelme hatası** düzeltildi.
- 53188 [DR8815] - Web arayüzünde form ekranında **Lookup** nesnesinde **seçim yapılıp**
    akış ilerletildiğinde, **diğer onayda text yerine value değerinin gözükme sorunu**
    düzeltildi.
- 46595 - Web arayüzü **Tüm Duyurular Datagrid'inde** bulunan **tarih alanlarının hatalı**
    **filtrelenmesi** düzeltildi.
- 45480 - Web arayüzünde form ekranında **RelatedDocuments** nesnesinde **önizleme**
    **hatası** düzeltildi.
- 47255 - Web arayüzünde **Hesabım** menüsünün altındaki **Tema Ayarları** işlem
    yetkisinin **Kullanıcı Grubu düzenleme yetkisine bağlı olma** hatası düzeltildi.
- 4 2860 [DR5993] - Web arayüzünde akış ilerletilirken **bir sonraki Request** bilgisi
    **oluşamadığı için alınan hata** düzeltildi.
- 43274 [DR6264] - Web arayüzünde Akış tarafında yer alan **Statues** kısmındaki **statü**
    **açıklama** kısmına yazılan **& simgesi (&) içerisinde gösterilme hatası** düzeltildi.
- 50014 - Web arayüzünde formda **UserMetaData** nesnesinin **Custom** olarak ve
    sonrasında da **Company** olarak **seçilmiş değerinin gözükmeme hatası** düzeltildi.
- 53614 - Web arayüzünde **imza seçeneği optional** olan sürecin **elektronik imza**
    **atılmadan sürecin devam edememe** hatası düzeltildi.
- 56408 [DR9204] - Web arayüzünde **Değişken** nesnesinden **Mail Template** gönderilen
    **Türkçe karakterlerin mailde gözükmeme hatası** düzeltildi.
- 55321 - Web arayüzünde akış ilerletilirken alınan **Disposing or disposed unit of work**
    **object can not operate hatası** düzeltildi.


- 54879 - Web arayüzünde akışta **hata oluştuğunda veri tabanına atılan log ‘un**
    **Rollback yapıldığında silinmemesi** sağlandı.
- 54921 - Web arayüzünde formdaki **Datagrid** nesnesi **PDF'e** aktarıldığında **Datagrid'in**
    **ComboBox** kolonunun **value** ve **text değerlerinin basılması** , **Tarih alanlarında da**
    **zaman dilimi bilgisi gösterilmesi** sağlandı.
- 55419 - Web arayüzünde **Datagrid** nesnesi **Save on: Row Change** seçiliyken **yeni veri**
    **eklenmek istendiğinde alınan hata** düzeltildi.
- 55521 [DR9127] - Web arayüzünde form nesnelerinin **PDF'e aktarılma** formatında
    **DocumentMetaData, TimePicker, Lookup, DateTimePicker, DateRangePicker,**
    **ComboBox, ListBox, RadioList** ve **Dropdown** nesnelerinde **meydana gelen hata**
    düzeltildi.
- 55525 [DR9127] - Web arayüzünde form nesnelerinin **PDF'e aktarılma** formatında
    **DocumentMetaData, TimePicker, Lookup, DateTimePicker, DateRangePicker,**
    **ComboBox, ListBox, RadioList** ve **Dropdown** nesnelerinde **meydana gelen hata**
    düzeltildi.
- 55524 [DR9127] - Web arayüzünde form nesnelerinin **PDF'e aktarılma** formatında
    **DocumentMetaData, TimePicker, Lookup, DateTimePicker, DateRangePicker,**
    **ComboBox, ListBox, RadioList** ve **Dropdown** nesnelerinde **meydana gelen hata**
    düzeltildi.
- 56165 - Web arayüzünde **Pozisyon Grubu** kullanıcılarında **Onay / Reddet**
    **işlemlerindeki hata** düzeltildi.
- 56215 - Web arayüzünde form ekranında **Akış Özelliklerinde Olaylar** bilgisinin
    **gözükme hatası** düzeltildi.
- 46607 - Web arayüzünde form ekranında **Parametreli Datasource** bağlantısı olan
    **Lookup** nesnesinde, **kolon araması** yapılırken **input alanından çıkma hatası**
    düzeltildi.
- 47977 - Web arayüzünde bir akış başlatıldığında onaycının **Dashboard** ekranın **kayıt**
    **bilgisinin düşmemesi** , **İş Akış yönetiminde ilgili sürecin açılamama hatası** düzeltildi.
- 48192 - Web arayüzünde formda **DocumentViewer** nesnesinde **Show on**
    panellerinden birini açıp, **Çalışma Başlat** deyip **Yayınla** butonuna tıkladıktan sonra
    gelen pencerede **Kaydet butonunun tepki vermeme hatası** düzeltildi.
- 48422 - Web arayüzünde **Aksiyon Yönetimi** modülünde **Kanban** ekranında **statüler**
    **arası sürükleme işlemi** yapıldığında, **durum bilgisinin İngilizce görünme hatası**
    düzeltildi.
- 50330 - Web arayüzünde form ekranında **TagBox** nesnesinde **uzun metin seçimleri**
    yapıldığında **görüntünün bozulma hatası** düzeltildi.
- 50392 - Web arayüzünde **Hesabım** menüsünün altındaki **Vekalet** işlemleri
    sekmesinde, **Vekalet Başlangıç saatinin geride gösterilme hatası** düzeltildi.
- 50407 - Web arayüzünde aynı kullanıcı için **Tema ayarlarının farklı tarayıcılarda farklı**
    **görünme hatası** düzeltildi.


- 50412 - Web arayüzünde **Vekalet** verilen kullanıcının **Aktiviteler** için **yetki sınırlaması**
    yapıldığında, **Vekalet** kullanıcısının form üzerindeki **Aktiviteler alanının kısıtlanmama**
    hatası düzeltildi.
- 51347 - Web arayüzünde formda **DateTimePicker** nesnesi için belirlenen **Disable**
    **before** ve **Disable after** tarihlerinin **öncesi ve sonrası seçilememe hataları** düzeltildi.
- 51431 - Web arayüzünde **Statik Datagrid** nesnesi **Save on: Row Change** seçiliyken
    **Multilanguage** kolonu filtrelerinin **konsol hatası atması** ve **Object ComboBox**
    **kolonunun filtrelerinin çalışmama** hatası düzeltildi.
- 51860 [DR8434] - Web arayüzü **Güvenlik Yetkilerinde İnsan Kaynakları** menüsündeki
    **Kullanıcı Grubu** ve **Şirket Yöneticileri** menüleri için **yetki sınırlaması** yapıldığında
    **hata mesajlarının tutarsız olma** hatası düzeltildi.
- 52284 - Web arayüzünde **DataGrid** nesnesi olan form açılınca **Panel Size maksimuma**
    **çekildiğinde alınan tasarım hatası** düzeltildi.
- 52819 - Web arayüzünde **bir form açıldığında panel boşluklarının orantısız gelme**
    hatası düzeltildi.
- 53003 - Web arayüzünde **Date** ve **DateTime** kolonu olan **Datagrid'lerde Düzenle** ve
    **Sil butonları gelmeme hatası** düzeltildi.
- 53613 - Web arayüzünde **bir süreç reddedildiğinde** , tekrar onaylayacak onaycının
    **reddeden kullanıcıya ait dokümanları görme hatası** düzeltildi.
- 53619 - Web arayüzünde **süreç** üzerinde **birden fazla onaycının Dijital İmza**
    **kullanamama** hatası düzeltildi.
- 53692 - Web arayüzünde yüklenen **dosyanın linki kopyalanarak** açılmak
    istendiğinde, **sayfanın tarayıcıda 413 hatası verme sorunu** düzeltildi.
- 54389 [DR8981] - Web arayüzünde **Datagrid** nesnesi **Date kolonlarına** seçilen
    **formatın yansımama hatası** düzeltildi.
- 54455 - Web arayüzünde form ekranında **Repeater** nesnesine yüklenmiş olan
    **formdaki görünüm hatası** giderildi.
- 54544 [DR8999] - Web arayüzünde forma eklenmiş nesnelerin **Client Visible** ve **Client**
    **Enabled** özelliğini **kapatınca diğer nesnelerin arasında boşlukların oluşma hatası**
    düzeltildi.
- 54858 - Web arayüzünde **Process arşivi** oluşturulan formun **Datagrid ‘indeki filtre**
    **alanlarına veri yazılmama hatası** düzeltildi.
- 55016 - Web arayüzünde **Datagrid cell** modundayken, **DateTime** kolonlarına veri
    eklendiğinde alınan **DevExpress hatası** düzeltildi.
- 55422 - Web arayüzünde, formda **FishBone** nesnesinin **Sub Reaso** n ögelerinden
    **silme işlemi** yapıldığında **ortamın hata vermesi** düzeltildi.
- 39955 - Web arayüzünde form ekranında **RelatedDocuments** nesnesinde **Doküman**
    **Yönetimi tablo görünümü** üzerinden **dosya seçimi yapıldığında çıkan hata** ve **çift**
    **tıklanarak klasör içeriğine gitmeme hatası** düzeltildi.
- 41537 - Web arayüzünde **açılan bir onayın** ve **son kullanılan dokümanın üst menüde**
    **çoklanma** hatası düzeltildi.


- 44126 - Web arayüzünde **Olay Günlük Görüntüleyici** menüsünde **Excel'e Aktar**
    işleminin **sadece ekrandaki veriyi basma hatası** düzeltildi.
- 44475 - Web arayüzünde formda **FileSelector** nesnesine **JPG dosyası** yüklerken
    **ortamın hata verme sorunu** düzeltildi.
- 44922 [DR6643] - Web arayüzünde **İlişkili Datagrid 'den form açılıp kapatıldığında**
    **Datagrid üzerinde oluşan boşluk** düzeltildi.
- 44994 - Web arayüzünde **Dinamik Rest sorgusuyla** çekilen **alt kırılımı olan** verilerin
    **object object** şeklinde gelmesi ve bu şekilde **Excel’e aktarılma hatası** düzeltildi.
- 45076 - Web arayüzünde formda **Ribbon** nesnesinin olduğu sayfayı genişlettiğimizde
    **nesne üç nokta şeklinde kalmaya devam etme** ve **nesne üzerinde bir tıklama**
    **yapınca genişleme hatası** düzeltildi.
- 45478 - Web arayüzünde form ekranında **RelatedDocuments** nesnesinde **Doküman**
    **Yönetimi** üzerinden **dosya yükleme işleminde** , **tablo** görünümünde klasör içeriğine
    **çift tıklanarak** girilmek istenildiğinde **oluşan görüntü bozukluğu** düzeltildi.
- 47091 - Web arayüzünde **Dashboard** ekranında **Süreç ve Süreç detayları** alanındaki
    kaydırmanın **fare imlecinin dışarıya çıkması** sonucunda tekrar **Süreç ve Süreç detayı**
    **ekranındaki hatalı çalışması** düzeltildi.
- 48244 [DR7560] - Web arayüzünde formda yer alan butonlarla **Dinamik Datagrid**
    nesnesinin **ReadOnly** özelliği **aktif / pasif edildiğinde hatalı çalışması** düzeltildi.
- 49286 - Web arayüzünde **DataGrid** nesnesi **Column Hiding Enabled: True - Text** ve
    **Number** kolonu **Hiding Priority** göre alt menüye geçtiğinde **imleç satırdan sürekli**
    **olarak çıkma hatası** düzeltildi.
- 50510 - Web arayüzünde **DataGrid DateTime** kolonunda saniyelerden dolayı
    **Büyüktür** filtresinin **Büyük Eşit gibi çalışma hatası** düzeltildi.
- 50775 - Web arayüzünde **InputGroup** nesnesi **Enabled** olmasına rağmen **içerisindeki**
    **nesnelere veri girilebilme hatası** düzeltildi.
- 51410 - Web arayüzünde **DataGrid: Statik: Row** - **Save On: Row Change** - **String**
    kolonlarda **eşit değildir filtresinde ortaya çıkan hata** düzeltildi.
- 52237 - Web arayüzünde **Scheduler** nesnesinin **DragDropProvider** ve **EditingState**
    **özelliklerinin hata vermesi ve bu özelliklere sahip nesneleri form üzerinde**
    **açılmama** hatası düzeltildi.
- 52462 - Web arayüzündeki formlarda **butonların yakınlaştırmada kalma hatası**
    düzeltildi.
- 52650 - Web arayüzünde **Multiple** özelliği olan **Lookup** nesnesinde **seçilen**
    **metinlerin tam olarak gözükmeme** hatası düzeltildi.
- 53117 - Web arayüzünde **Görev Yönetimi** modülünde işi yapacak alanında açılan
    Datagrid 'de **ID kolona 10 basamak üzeri veri girilme hatası** düzeltildi.
- 53120 - Web arayüzünde **Dashboard** ekranında **Süreçler** ile **Süreç detayındaki hiza**
    **hatası** ve **bu iki alan boşken ortaya çıkan renk uyumsuzluğu** düzeltildi.
- 53218 - Web arayüzünde **Datagrid** nesnesi **OnRowUpdated** etkinliği tetiklenirken
    **oldRow argümanında yeni datanın gelme hatası** düzeltildi.


- 53318 - Web arayüzünde **Tabs** nesnesi içerisinde bulunan **Datagrid DateTime**
    kolonunun **sortColumn metoduyla çalışmama hatası** düzeltildi.
- 53368 - Web arayüzünde **Güvenlik Ayarları** içerisindeki **Güvenlik Grubu** seçildiğinde
    **üyeler ve üye oldukları sekmelerine geçilememe** hatası düzeltildi.
- 53387 - Web arayüzünde **Dijital İmza ile onaylanan bir sürecin sonraki onaycıya**
    **düşmeme** hatası düzeltildi.
- 53611 - Web arayüzünde **imza** ekranında, Geliştirme arayüzü tarafında **Document**
    alanında belirlenmiş olan **Signature Format bilgisinin görünmeme hatası** düzeltildi.
- 48180 - Web arayüzünde form ekranında **Lookup** nesnesinde **veri olduğu halde**
    tıklandığında **Veri yok mesajını gösterme hatası** düzeltildi.
- 50900 - Web arayüzünde **Datagrid** nesnesi **Image** kolonunun **Excel'e hatalı**
    **aktarılması** düzeltildi.
- 52110 - Web arayüzünde **Parametreli formda** yer alan **Datagrid** 'de
    **object:combobox kolonunda silme işlemi yapılmama** hatası düzeltildi.
- 52119 - Web arayüzünde **Dinamik Datagrid** nesnesi **Column Hiding** özelliği **aktifken**
    **düzenleme** yapılmak istendiğinde **giriş alanlarında oluşan hareket sorunu** düzeltildi.
- 52474 - Web arayüzünde **Datagrid** nesnesi **Save on: Row Change** seçiliyken **birden**
    **fazla kolonda filtre testi yapıldığında alınan konsol hatası** düzeltildi.
- 52513 - Web arayüzünde **Datagrid** nesnesi **DataType: String** olup, **EditType:**
    **NumberBox** olan kolonda **Summary Types** işlemlerinde **ortalama hesabı yanlış**
    **çalışma hatası** düzeltildi.
- 52741 [DR8771] - Web arayüzünde **MacBook'ta Chrome** ve **Safari** tarayıcısında
    **Datagrid ComboBox kolonlarının tepki vermeme** hatası düzeltildi.
- 53046 - Web arayüzünde **Datagrid Action** butonlarından açılan formların **Aktiviteler**
    butonuna tıklanınca **formun arkasında açılma hatası** düzeltildi.
- 53870 [DR8890] - Web arayüzünde **Datagrid** nesnesi **Sorting Enabled Aktif** edilip,
    kolonun **Field name** alanı değiştirilerek **nesnede sıralama yapıldığında oluşan hata**
    düzeltildi.
- 54290 - Web arayüzünde **Datagrid nesnesi DataType: String** ve **Edit Type:**
    **ComboBox** olan kolonda **Value değeri boş** bırakıldığında yazılan **object object hatası**
    giderilerek, boş bırakıldığında **uyarı mesajı** ile **kolonun kaydedilmemesi sağlanarak**
    hata düzeltildi.
- 56013 [DR9160] - Web arayüzünde formun **OnLoad** etkinliğine **yazılan kodlarla** dolan
    **Datagrid** nesnesi, form ilerletildiğine **verilerin listelenmemesi** ve **eklenen verinin**
    **gelmeme** hatası düzeltildi.
- 54370 - Web arayüzü **Hesabım** menüsü **Vekalet ve Erişim Anahtarları** ekranında **Yeni**
    butonuna basıldığında açılan ekranda **olması gereken butonların gözükmeme hatası**
    düzeltildi.
- 56480 - Web arayüzünde **Hesabım** paneli altında **Tema ayarlarındaki Birincil renk**
    seçimi değiştirildiğinde **Önizlemeye yansımama hatası** düzeltildi.


- 56481 - Web arayüzünde **Hesabım** penceresi altında **Vekalet ve Erişim Anahtarları**
    seçeneğinden **Vekalet Oluştur butonu** ile açılan **Vekalet Edecek Kişi** seçim panelinde
    **Tamam** butonunun **Kapat butonu gibi çalışma hatası** düzeltildi.
- 56522 - Web arayüzünde **Uygulama Gezgini Menü Ekle** penceresinde başlık alanı
    **uygulama dili Türkçe** olduğu halde **çoklu dil** seçeneğinde **tekrar Türkçe alanının**
    **gelme** hatası düzeltildi.
- 54946 [DR8909] - Web arayüzünde nesnenin **Ellipsis** özelliği kapalıyken **girilmiş olan**
    **verinin tamamının gözükmeme hatası** düzeltildi.
- 56640 - Web arayüzünde **Görev yönetimi** sayfasında görev transferinden işi yapacak
    **Kullanıcı / Pozisyon seçimi** yapılmadan **Aktar** butonuna tıklanıldığında, **Sunucu**
    **tarafında bir hata oluştu** mesajının yerine **bilgilendirme mesajı gösterilmesi**
    sağlandı.
- 56369 - Web arayüzünde **Fast Approval** özelliği **Aktif** olmayan butonların **Bekleyen**
    **İşler** ekranında **Olaylar alanında gözükme hatası** düzeltildi.
- 56703 - Web arayüzünde **Hesabım** menüsünün **Vekalet ve Erişim Anahtarları**
    alanında **Erişim anahtarları** oluştururken **Bitiş Tarihi seçilememe hatası** düzeltildi.
- 59675 - Web arayüzünde **Form** ekranında **Akış Tarihçesi boş olduğunda diğer**
    **özelliklerin gösterilmeme** hatası düzeltildi.
- 60108 - Web arayüzünde **Görev Yönetimi** panelinde **İşi Yapan Kullanıcılar paneli**
    açıldığında, **kullanıcı seçimi yapılmadığı** halde **Kaydet** butonunun **aktif gelme hatası**
    düzeltildi.
- 53074 - Web arayüzünde **CSP eBA Entegrasyonu** için menüye eklenmiş **eBA 6.**
    **versiyonu** bağlantısına tıklandığında **açılmama hatası** düzeltildi.
- 59866 - Web arayüzünde **Giriş** ekranında **üç defa hatalı giriş** sonrası gelen
    **Doğrulama ekranı hatası** düzeltildi.
- 56623 [DR9283] - Web arayüzünde formda **Scheduler** nesnesinde **Tarih** alanlarının
    **Disable before** ve **Disable after** kısımlarının **çalışmama** hatası düzeltildi.
- 56681 [DR9291] - Web arayüzünde **Columns** özelliği **ReadOnly** olan **Scheduler**
    nesnesinin ilgili kolonuna **veri girilebilme** hatası düzeltildi. **Allow Null** ve **Required**
    özellikleri ise **Control Properties** panelinden **kaldırıldı**.
- 60230 [DR9391] - Web arayüzü **Norm Holding** projesinde **Kural Yöneticisi**
    **onbeforesave** kısmı **boş** olmasına rağmen **formu kaydederken hata alınma sorunu**
    düzeltildi.
- 60705 - Web arayüzünde **birden fazla görünümün** olduğu formda, form içerisinde
    **Client Enabled** özelliği **Pasif** olan nesnenin **kod ile tetiklenmeme hatası** düzeltildi.
- 60957 - Web arayüzü **Norm Holding İlişkili Datagrid** nesnesinde **Düzenle** işleminde
    **Kaydet** butonuna tıklanıldığında, oluşan **object referance hatası** düzeltildi.
- 62163 - Web arayüzünde Form ekranında **Allow Null = False** olduğunda **nesne dolu**
    olsa da **Kaydetme** işleminde **Validasyon hatasına takılma sorunu** düzeltildi.
- 55692 - Web arayüzünde form ekranında **docx, xlsx, txt, Png, Pdf** uzantılarının
    **açılmama hatası** düzeltildi.


- 61441 - Web arayüzünde **FormViewer** nesnesinin içerisinde bulunan **form**
    **açıldığında ortamın hata verme sorunu** düzeltildi.
- 59839 - Web arayüzünde **Vekalet ve Erişim Anahtarları** kısmında **Erişim Anahtarları**
    **Bitiş Tarihi seçilememe ve alınan konsol hatası** düzeltildi.
- 59864 [DR9342] - Web arayüzünde **ToolBar Button** yardımıyla açılan formdaki
    satırları **DataGrid'e** eklerken **onRowInserting** etkinliğiyle **args.cancel = true** diyerek
    **satır ekleme işlemini engellenmeme hatası** düzeltildi.
- 56498 - Web arayüzünde, **Akış** gönderilen kullanıcıya gelen **bildirimden akış**
    **onaylandığında Akış Tarihçesinin boş gelme hatası** düzeltildi.
- 56081 - Web arayüzünde **mailden açılan formun gözükmeme hatası** düzeltildi.
- 60114 - Web arayüzünde **Profil Form** olan **depoya dosya yüklenmek** istendiğinde
    **editingEnabled hatası alınma sorunu** düzeltildi.
- 60808 - Web arayüzünde **formların açılmama hatası** düzeltildi.
- 61159 - Web arayüzü **Doküman Yönetiminde Gelişmiş Arama işlemi** yapılırken
    **GetFolderItems'ın 400 dönme hatası** düzeltildi.
- 62762 [DR9868] - Web arayüzünde **Dinamik DataGrid büyük bir veri kaynağından**
    doldurulurken, sayfalar arasında her seferinde geçişte **veri tabanından çekilmesi**
    yerine **data cach veri olarak tutulması** sağlanarak **Sayfaların yüklenmesinin uzun**
    **sürme hatası** düzeltildi.
- 62970 - Web arayüzünde **FileSelector** nesnesine **Bilgisayardan Dosya seçimi**
    **yapılamama** hatası düzeltildi.
- 63180 - Web arayüzünde **Scheduler** nesnesine **veri eklendiği** zaman, eklenen veriye
    **çift tıklandığında ortamın hata verme sorunu** düzeltildi.
- 62624 [DR9804] - Web arayüzü formda **Buton** ile **nesnelerin Client Visible** özelliğinin
    **Aktif** ve **Pasif olamama hatası** düzeltildi.


### 3.2. Geliştirme Arayüzü

- 52677 - Geliştirme arayüzünde, formda yer alan **Datagrid** nesnesi **PreferredWidth**
    **özelliği** kullanıldığında **json** dosyasında **bu özelliğin gelmeme hatası** düzeltildi.
- 37688 [DR4258] - Geliştirme arayüzünde **Events** alanından **Confirmation özelliği aktif**
    edilip, Web arayüzünde formda **akış ilerletilmek** istendiğinde özelliğin çalışabilmesi
    için **akıştaki nesnelerin kaldırılıp tekrar eklenme hatası** düzeltildi.
- 42970 - Geliştirme arayüzünde **Datasource** içerisinde **ODBC** uzantılı **dosyanın**
    **yeniden adlandırma ve silme işleminde** oluşan hata düzeltildi.
- 45487 - Geliştirme arayüzünde **Akış Yöneticisi** modülünde **filtreleme** işleminin **akış**
    **bilgisine göre yapılamama** hatası düzeltildi.
- 45494 - Geliştirme arayüzünde İş Akış Yönetimi modülünde **Filtre** ekranında **Proje** ve
    **Created after filtresinin çalışmama** hatası düzeltildi.
- 49072 - Geliştirme arayüzünde **yeni** ve **daha önceden oluşturulan** projelerde
    **TableML** sınıfında **Culture alanına ait karakter sayısı** düzenlendi.
- 50269 - Geliştirme arayüzü **Proje Yönetimi Proje Dışa Aktar** işlemi ile dışarı alan
    proje, yine aynı ekrandaki **İçe Aktarma işlemi** ile **Import** edildiğinde **Doküman**
    **Yönetimi dokümanlarının taşınmama** hatası düzeltildi.
- 51766 - Geliştirme arayüzü **Action Form** üzerindeki **Başlangıç Tarihi** ve **Bitiş Tarihi**
    alanları ve **Kullanıcı ata durum** alanlarının aynı **InputGroup nesnesi içinde olmama**
    hatası düzeltildi.
- 47418 - Geliştirme arayüzünde **Proje Yöneticisi İçe Aktar işlemi** için açılan **Import**
    ekranında **Bağlantılar sekme adının doğru yazılmama hatası** düzeltildi.
- 48206 - Geliştirme arayüzünde **proje yayınlama işlemi** sırasında **çıktı** alanında **yeni**
    **bir çıktı satırı** eklendiğinde, **tüm satırların taranma hatası** düzeltildi.
- 50414 [DR8206] - Geliştirme arayüzünde form nesnelerinde **Kopyala Yapıştır**
    **özelliğinin çalışmama hatası** düzeltildi.
- 50800 - Geliştirme arayüzünde **Akış** tarafında **Alt akış çağırma** ve **Alt akış bitiş**
    **nesnelerinin özelliklerinde dil bütünlüğü** sağlandı.
- 51806 - Geliştirme arayüzünde **Header** nesnesi forma sürüklenip bırakıldığında
    **default** olarak **seçili font gözükmemekte** ve **font kutusunun boş gelme hatası**
    düzeltildi.
- 51855 [DR8447] - Geliştirme arayüzünde **Kural Yöneticisi** uygulama zamanı olarak **+5**
    olarak gösterilen etkinlik içeriğinde **eksik etkinlik gösterilmesi** ve **5 üzeri etkinlik**
    **eklenememe** hatası düzeltildi.
- 52183 - Geliştirme arayüzünde **Akış** etkinliğindeki **Confirmation** alanının
    **Multilanguage Başlık özelliği** düzenlendi.
- 52299 - Geliştirme arayüzünde **Akış özellikleri** içerisindeki etkinliklerdeki **${0}** bu
    **görünüm hatası** düzeltildi.
- 52402 - Geliştirme arayüzünde **Akış** tarafında **Documents** özelliği bulunan nesnelerde
    **Documents** içerisindeki dokümanlara tıklandığında **görünüm bilgilerinin değişme**
    **hatası** düzeltildi.


- 52509 - Geliştirme arayüzünde **Akış** tarafında **Variables** özelliği içerisinde **kontrol**
    **ekleme** işleminde **form değişikliği** yapıldığı zaman **Fields listenin temizlenmeme**
    hatası düzeltildi.
- 52801 - Geliştirme arayüzünde forma **Datagrid** sürüklendiğinde ortaya **dbType** hatası
    düzeltildi.
- 44018 - Geliştirme arayüzünde **Akış** tarafında **akış bitişi** nesnesinde **Set Flow Status**
    **as Deleted** özelliği seçilip akış bitirildiğinde, **Akış Tarihçesinde Başladı olarak yazma**
    durumu düzeltildi.
- 45569 - Geliştirme arayüzünde akış üzerindeki **Pozisyon** nesnesi **Sabit kullanıcı** olarak
    seçildiğinde, Web arayüzünde **Görev Yöneticisi** modülünde görev aktarımı sırasında
    **pozisyon bazlı bir aktarım** yapılmak istendiğinde, **listede kullanıcı bazlı onayı olan**
    **süreçlerin listelenme hatası** düzeltildi.
- 51714 - Geliştirme arayüzünde **Flow Variables** alanından eklenen kontrollerde farklı
    formlardan **aynı isimde nesneler eklenip** deploy alındığında çıkan **"An item with the**
    **same key has already been added."** hatası düzeltildi.
- 52468 - Geliştirme arayüzünde aynı projede **aynı anda birden fazla deploy işlemi**
    **başlatıldığında oluşan hata** düzeltildi.
- 54415 [DR8993] - Geliştirme arayüzünde **Datasource** içerisinde bulunan **Delete**
    işlemini **ServiceApi** üzerinden **ExecuteQuery ile çalıştırılamama hatası** düzeltildi.
- 47451 - Geliştirme arayüzünde **Proje Yönetimi** modülünde **İçe Aktarma işlemi**
    yapılırken **Akış alanının boş görünme hatası** düzeltildi.
- 50254 [DR8155] - Geliştirme arayüzünde **NumberBox** nesnesinin **Behavior** özellikleri
    arasında bulunan **Precision değeri 0** olarak atandığında, **Data Definition Language**
    özellikleri arasında bulunan **Size özelliği de 0 olarak atanma hatası** düzeltildi.
- 50550 - Geliştirme arayüzünde **default** görünümlerde **tüm görünümlere uygulama**
    **butonunun görünme hatası** düzeltildi.
- 50767 - Geliştirme arayüzünde **Akış Yöneticisinde silinmiş olan akışlardaki Sil**
    **butonunun pasif olarak gözükmeme** hatası düzeltildi.
- 50795 - Geliştirme arayüzünde **Akış Yöneticisinde Objects** alanında **arama işlemi**
    yapılırken **imlecin input alanından çıkma hatası** düzeltildi.
- 52979 - Geliştirme arayüzünde nesnelerin **başlık bilgisine uzun veri girildiğinde**
    **satırları alt alta gösterme hatası** düzeltildi.
- 53581 [DR8873] - Geliştirme arayüzünde formda **ReportViewer** nesnesi için **Reports**
    dosyası içerisinde **bir nesne silindiği** zaman form üzerinde **ReportViewer nesnesinin**
    **de silinme hatası** düzeltildi.
- 54441 - Geliştirme arayüzünde form ekranına **Map nesnesi eklediğinde**
    **görüntülenmeme sorunu** düzeltildi.
- 54597 - Geliştirme arayüzünde **Bağlantılar** alanında veri girildikten sonra
    " **MultipleActiveResultSets=True;TrustServerCertificate=True;"** parametrelerinin
    **silinme hatası** düzeltildi.
- 54646 - Geliştirme arayüzünde formda **Yerelleştirme** panelinde **filtre** ile **arama işlemi**
    yapılmak istendiğinde **girilen verilerin sayfada gözükmeme hatası** düzeltildi.


- 55246 [DR9086] - Geliştirme arayüzünde **ilişkili DataGrid** nesnesi
    **OPENRELATIONDOCUMENT** kolonundaki **Format Type** ve **Edit Type boş gelme hatası**
    düzeltildi.
- 55473 - Geliştirme arayüzünde **Akış** tarafında **nesnelerin özelliklerinden** erişilen
    **Documents alanındaki tasarım hatası** düzeltildi.
- 55477 - Geliştirme arayüzünde **Datagrid** yapısı olan **kolonlarının görünüm hatası**
    düzeltildi.
- 55624 - Geliştirme arayüzünde **Önizleme** ekranında **DateTimePicker** nesnesinin
    **Value değeri** değiştirildiğinde **sıfırlanma hatası** düzeltildi.
- 55714 - Geliştirme arayüzünde **Akış** tarafında **etkinlik** özelliğine sahip nesnelerde,
    **butonların çoklanma sorunu** düzeltildi.
- 56288 - Geliştirme arayüzünde formdaki ikinci görünümdeyken **Datagrid 'de bir**
    **özellik değiştirildiğinde** , **kolonların çoklanma hatası** düzeltildi.
- 56290 [DR9230] - Geliştirme arayüzünde formdaki ikinci görünümdeyken **Datagrid**
    **'de bir özellik değiştirildiğinde** , **kolonların çoklanma hatası** düzeltildi.
- 38090 - Geliştirme arayüzünde **aynı Datasource** 'un **Dışarı Aktar - İçeri Aktar**
    yapılırken **oluşan hata** düzeltildi.
- 45504 - Geliştirme arayüzünde **İş Akış Yöneticisi object** alanında Datagrid
    filtresindeki **Input alana veri girilirken** , **imlecin dışarı çıkma hatası** düzeltildi.
- 45621 - Geliştirme arayüzünde **forma sağ tıklayınca** açılan **Contextmenu'** nun **diğer**
    **menülerin altında açılma hatası** düzeltildi.
- 46027 - Geliştirme arayüzünde **Akış** tarafında etkinlik içerisinde **Seçerek Kaldır**
    ekranındaki **arama işleminde Input alanından çıkma hatası** düzeltildi.
- 46337 - Geliştirme arayüzünde pozisyonun **Doküman** özelliğinde **Akış** üzerinde **onay**
    **işleminin Dijital imza ile yapılamama hatası** düzeltildi.
- 47415 - Geliştirme arayüzünde **Proje Yönetimi İçe Aktar** işleminde proje adının
    **uygunsuz karakter içerecek şekilde verilebilme hatası** düzeltildi.
- 47447 - Geliştirme arayüzünde **Proje Yönetimi İçe Aktar** işlemindeki **İnsan Kaynakları**
    sekmesinde **eşleşme durumunun null olarak görünme** hatası düzeltildi.
- 47463 - Geliştirme arayüzünde **İçe Aktarma işlemi** sırasında **Kaynak** ve **Hedef**
    sekmeleri arasındaki geçişte **dosya yolu alanının silinme hatası** düzeltildi.
- 50280 - Geliştirme arayüzünde **Transfer** ve **FishBone** nesnelerinin **bölümlerinin**
    **dışına taşarak görünüm bozukluğu oluşturma hatası** düzeltildi.
- 50801 - Geliştirme arayüzünde **Akış** yöneticisinde **Steps** alanında akış ilerletildiğinde
    **Pozisyon** ve **Pozisyon Grubu Description bilgileri boş görünme hatası** düzeltildi.
- 50850 - Geliştirme arayüzünde **Çözüm** içerisine **Aksiyon Formu eklenememe** hatası
    düzeltildi.
- 51129 [DR8325] - Geliştirme arayüzünde **Datasource** klasörü altında **Parametreli**
    **sorguda değişiklik** yapıldığında **Parametre değerinin** ve **türünün silinme hatası**
    düzeltildi.


- 51415 [DR8347] - Geliştirme arayüzünde **Tabs** nesnesi içerisinde **InputGroup**
    nesnesine **başka bir nesne sürüklenip bırakıldığında nesnenin baskılanıp**
    **gözükmeme** hatası düzeltildi.
- 51555 - Geliştirme arayüzünde **Password** nesnesi için **MaxLength özelliğine eksi**
    **değer girilme** hatası düzeltildi.
- 51624 - Geliştirme arayüzünde **Akış yöneticisinde biten akış için Rollback**
    **butonunun aktif olması** ile ilgili hata düzeltildi.
- 52308 - Geliştirme arayüzünde **Etkinlik Özellikleri** değiştirilip akış kapatıldıktan sonra
    tekrar **Etkinlik Özelliklerine** girildiğinde, **yapılan işlemlerin kaydedilmeme hatası**
    düzeltildi.
- 52683 - Geliştirme arayüzünde projede **her deploy sonrası çıktı ekranında deploy**
    **geçmişinin bulunma hatası** düzeltildi**.**
- 53286 - Geliştirme arayüzünde **Akış** tarafında **Flow Variables** alanındaki **kontrol**
    **ekleme** işleminde **formdan silinen nesnesinin Fields listesinde gözükme** hatası
    düzeltildi.
- 53493 **-** Geliştirme arayüzünde **Datagrid** nesnesi kolonlarına **Datasource eklenmeme**
    **hatası** ve **İlişkili Datagrid kolon üretilmeme hatası** düzeltildi.
- 53525 - Geliştirme arayüzünde **Datagrid Toolbar Button form name** alanına
    **projedeki formların yansımama** hatası düzeltildi.
- 53567 - Geliştirme arayüzünde **yeni Datasource** eklenirken, **ikonların değişmeme**
    **hatası** düzeltildi.
- 53617 - Geliştirme arayüzünde **Akış** üzerindeki doküman **DM dokümanı olmadığında**
    **web arayüzü tarafında imza işlemi sırasında uyarı alınmama** hatası düzeltildi.
- 53634 - Geliştirme arayüzünde **Önizleme** modunda **boyutlandırma işlemi** yaparken
    **oluşan titreme hatası** düzeltildi.
- 41407 - Geliştirme arayüzünde **Çözüm Gezgini** panelinde **ts, css, cs** dosyalarına sağ
    tıklayıp **Aç** denildiğinde alınan hata düzeltildi.
- 50772 - Geliştirme arayüzünde formda **InputGroup** nesnesini **kopyala yapıştır** ile
    çoğalttığımız zaman tüm nesneler **tek bir nesne gibi hareket etmekte** ve **silme** ,
    **yazma** gibi işlemler birine uygulandığında **hepsinin etkilenme** hatası düzeltildi.
- 51007 - Geliştirme arayüzünde **Forma İçe Aktar** işlemi yapılırken meydana gelen
    **maxcallsized hatası** düzeltildi.
- 51030 - Geliştirme arayüzünde **Form adı nesne adıyla** oluşturulduğunda, **Form adı ile**
    **nesne adı karışıklık göstermesinden** kaynaklı **yanlarında açıklama bulunmama**
    **hatası** düzeltildi.
- 51434 - Geliştirme arayüzünde **Form Server** tarafında **fonksiyonların listelendiği**
    alanda oluşan **görünüm hatası** düzeltildi.
- 52171 - Geliştirme arayüzünde **VectorMap** nesnesinin **Annotations** özelliğinde
    eklenen ögelerden **bazıları silinirken bazıları silinememe hatası** düzeltildi.
- 52376 - Geliştirme arayüzünde **TreeList** nesnesini eklendiğinde **deploy alırken hata**
    **alınma** sorunu düzeltildi.


- 53985 [DR8910] - Geliştirme arayüzünde forma eklenmiş **ComboBox** nesnesinin
    **ComboBox1_OnSelectedItemChanged** veya **ComboBox1_OnSelectedItemChanging**
    olayları kullanıldığında **projenin Build almama hatası** düzeltildi.
- 54730 - Geliştirme arayüzünde **ReportViewer** nesnesi için **Report** dosyası oluşturup
    içine girdiğimizde, **dosya sürekli yükleniyor** olarak kalmakta ve **kapatmak**
    **istendiğinde ortamın hata verme** sorunu düzeltildi.
- 55576 - Geliştirme arayüzünde Formda **Yerelleştirme** panelinde **Otomatik çeviri**
    butonunun **Text** tipinden **Buton tipine çevrilmesi** , **Datagrid** üzerinde her satır için
    **Row select özelliğinin açılması** , **Tümünü Seç** özelliğinin **kaldırılması** ve **Otomatik**
    **Çevirinin seçili satır varsa o satırın yoksa tüm satırların çevirisini yapması**
    düzenlemeleri yapıldı.
- 55790 - Geliştirme arayüzünde **FishBone** nesnesinin **Liquidjs özelliğinin nesne**
    **yapısına yansıması** sağlandı.
- 55990 - Geliştirme arayüzünde **Akış** tarafında **Etkinlik ekleme** işleminde **flow.cs**
    **dosyasında parantez düzeninin bozulma** hatası düzeltildi.
- 56048 - Geliştirme arayüzünde **DateTimePicker** ve **DateRangePicker** nesnesinden
    **seçilen değerdeki saat** ile **form üzerindeki saatin birbirinden farklı olma** hatası
    düzeltildi.
- 60209 - Geliştirme arayüzünde **Akış** tarafında **Değişken** nesnesinde **Tarih seçimi**
    **yapıldığında oluşan hata** düzeltildi.
- 60967 - Geliştirme arayüzünde **ServiceAPI** ile **DateRangePicker** nesnesine **Set Value**
    **sorunu** düzeltildi.
- 60136 [DR9416] - Geliştirme arayüzünde formda **Kural Yöneticisinden**
    **OnPropertyChanged** özelliği **kaldırıldı** ve **Build - Deploy hatası** düzeltildi.
- 61073 - Geliştirme arayüzünde formda **sorgu dosyasına girildiğinde** ya da o kısımla
    ilgili yapılan her işlemde hata alınma sorunu düzeltildi.
- 61112 - Geliştirme arayüzünde **Aksiyon Durum Yöneticisindeki yazım yanlışları**
    düzeltildi.
- 61191 - Geliştirme arayüzünde **Proje Yöneticisinde proje silindikten** sonra **silinmiş**
    **projeler sekmesi** tekrar açıldığında **silinen projelerin gözükmeme hatası** düzeltildi.
- 61264 - Geliştirme arayüzü **Bağlantıları Düzenle** ekranında **ODBC** bağlantısında **Test**
    **butonuna tıklandığında** alınan hata düzeltildi.
- 61601 - Geliştirme arayüzünde **MaskInput** nesnesinin **Mask Format Char** özelliğinde
    **"Ekle" butonunun bulunmama hatası** düzeltildi.
- 59762 - Geliştirme arayüzünde **Akış** tarafında **Message** özelliğine sahip nesnelerde
    **Edit Message Source aktif** edilip **Source Message** alanına tıklandığında, **sayfanın**
    **hataya düşmesi durumu** düzeltildi.
- 61669 [DR9645] - Geliştirme arayüzünde, **DataGrid** nesnesi **Open A Selection Form**
    tipindeki **Toolbar Buttonun** özelliklerinde **Action Type Properties** altına **Do Not**
    **Ovveride Selected Rows** parametresi **eklendi**. Bu özellik **Open A Selection Form**
    tipindeki **Toolbar Button** ile açılan formdan gelen verilerle doldurulan **DataGrid**
    düzenlendiğinde **verilerin kaydedilmesini** ve tekrar **ToolBar Button** ile seçim


```
yapıldığında ana DataGrid’deki düzenlenmiş verilerin silinmemesi , değişmemesini
sağlar.
```
- 56358 - Geliştirme arayüzünde **Akış** tarafında **Pozisyon Grubu** nesnesine **Buton**
    **eklendiğinde** veya **silindiğinde Akış Control özelliğindeki seçimlerin silinme hatası**
    düzeltildi.
- 60240 - Geliştirme arayüzünde **ReportViewer** dosyasının **Reports** içerisinde bir nesne
    **silindiği** zaman **sayfa kapatıldığında ortamın hataya düşme sorunu** düzeltildi.
- 60441 - Geliştirme arayüzünde **Akış** tarafında nesnelerdeki **Onayla** ve **Reddet**
    **butonlarında** herhangi bir **Pozisyon** ve ya **Pozisyon Grubu** nesnesinde bir özelliğini
    değiştirildiğinde **diğer nesnelerde de değişmiş olma hatası** düzeltildi.
- 60474 - Geliştirme arayüzünde formda **DateRangePicker** nesnesinin **Active Date**
    **Type** özelliği altındaki **Range Dates** özelliğine tıklanıp, **Disable Date Type** tarihleri
    seçildikten sonra **ortamın hata verme sorunu** düzeltildi.
- 61154 - Geliştirme arayüzünde **Görünüm alanından İşlem Geçmişi açıldığında oluşan**
    **hata** düzeltildi.
- 60639 - Geliştirme arayüzünde **Akış Events** içerisinden **tanımlanan** ve **nesnelere**
    **eklenen** Butonların, **Web arayüzünde gözükmeme hatası** düzeltildi.
- 63150 - Geliştirme arayüzünde **Process Archive formda** alanlar seçiminde, **iki farklı**
    **formda alanlar seçilmek istenildiğinde oluşan hata** düzeltildi.


### 3.3. Android

- 34182 [DR2885] - **Android** cihazların mobil arayüzünde, **Webview** görünümündeki
    formda yer alan **RadioList** seçimine göre **TextBox** nesnesinin **Visible koşulunun**
    **sağlanmama hatası** düzeltildi.
- 50272 - **Android** cihazların mobil arayüzünde, **Native+** görünümündeki
    **RelatedDocuments** nesnesine **bazı formattaki dosyaların yüklenememe** hatası
    düzeltildi.
- 52578 - **Android** cihazların mobil arayüzünde, **Web** tarafında **erişim izninin**
    bulunmadığına dair alınan uyarının **mobil tarafında alınmama hatası** düzeltildi.
- 52719 - **Android** cihazların mobil arayüzünde, **Native+** görünümündeki **formların**
    **sonraki onaycıya gönderilmeme hatası** düzeltildi.
- 52894 - **Android** cihazların mobil arayüzünde, **Native+** görünümünde **Button** ile form
    açma işleminde **yükleme ekranında kalması** ve formda yer alan **diğer butonların da**
    **yanıt vermemesi hataları** düzeltildi.
- 52722 [DR8763] - **Android** cihazların mobil arayüzünde, **ilişkili form** ile **Lookup**
    nesnesinden **DataGrid** nesnesine **veri eklerken meydana gelen takılma** hatası
    düzeltildi.
- 35045 - **Android** cihazların mobil arayüzünde, **Native+** görünümündeki **Dinamik**
    **DataGrid** nesnesinde **sayfa geçişi yapılamama hatası** düzeltildi.
- 41875 [DR5933] - **Android** cihazların mobil arayüzünde, **Akış tarafında** oluşturan
    **bilgisi gizlendiğinde** bu bilginin **Bekleyen İşler alanından görünme hatası** düzeltildi.
- 46941 - **Android** cihazların mobil arayüzünde, **Native+** görünümündeki **Statik Cell** ve
    **Row** özelliğindeki **DataGrid** nesnelerine **ekleme** yapıldıktan sonra **gönderilmek** veya
    **onaylanmak** istendiğinde **yüklenme ekranında kalma hatası** düzeltildi.
- 54430 [DR8985] - **Android** cihazların mobil arayüzünde, **Native+** görünümündeki **Run**
    **at Server** özelliği **aktif** olan **Lookup** nesnesinde meydana gelen **filtreleme** ve **arama**
    **hataları** düzeltildi.
- 55645 - **Android** cihazların mobil arayüzünde, **Native+** görünümündeki **Statik**
    **DataGrid** nesnesine **tarih kolonunda veri eklenmek istendiğinde Tarih formatının**
    **bozulma hatası** düzeltildi.
- 49680 - **Android** cihazların mobil arayüzünde, **Webview** görünümünde **Native+** ve
    **Webview görünüme uygun iki uyarı mesajının gelme hatası** düzeltildi.
- 56518 - **Android** cihazların mobil arayüzünde, **Native+** görünümündeki **Arşiv**
    özelliğinde olan **DataGrid** nesnesinde **formların açılmama hatası** düzeltildi.

#### • 56615 - Android cihazların mobil arayüzünde, Native+ görünümündeki Statik

#### DataGrid nesnesine virgüllü sayı eklenememe hatası düzeltildi.

#### • 54430 [DR8985] - Android cihazların mobil arayüzünde, Native+ görünümündeki Run

```
at Server özelliği Aktif olan Lookup nesnesinde meydana gelen filtreleme ve arama
```
#### hataları düzeltildi.


#### • 60908 - Android cihazların mobil arayüzünde, Native+ görünümündeki DataGrid

```
içerisinde iki adet DateTimePicker nesnesi ile hesaplama yapıp farkını bir TextBox
```
#### nesnesine yazdıramama hatası düzeltildi.

#### • 60972 - Android cihazların mobil arayüzünde, Native+ görünümündeki boş Lookup

```
nesnesinde Filtre sayfası açıldığında filtre ikonlarının Visible özelliğinin pasif hale
```
#### getirilmesi düzeltildi.

#### • 61130 - Android cihazların mobil arayüzünde, Native+ görünümündeki S tatik

```
DataGrid nesnesinde Primary Key olan alana değer girişi yapılamama hatası
düzeltildi.
```

### 3.4. IOS

- 34182 [DR2885] - **IOS** cihazların mobil arayüzünde, **Webview** görünümündeki formda
    yer alan **RadioList** seçimine göre **TextBox** nesnesinin **Visible koşulunun sağlanmama**
    **hatası** düzeltildi.
- 46553 - **IOS** cihazların mobil arayüzünde, **Native+** görünümündeki **Lookup**
    nesnesinde **verilerin listelendiği sayfanın iki kere açılma hatası** düzeltildi.
- 52578 - **IOS** cihazların mobil arayüzünde, **Web** tarafında **erişim izninin**
    bulunmadığına dair alınan uyarının **mobil tarafında alınmama hatası** düzeltildi.
- 52719 - **IOS** cihazların mobil arayüzünde, **Native+** görünümündeki **formların sonraki**
    **onaycıya gönderilmeme hatası** düzeltildi.
- 52894 - **IOS** cihazların mobil arayüzünde, **Native+** görünümünde **Button** ile form
    açma işleminde **yükleme ekranında kalması** ve formda yer alan **diğer butonların da**
    **yanıt vermemesi hataları** düzeltildi.
- 52722 [DR8763] - **IOS** cihazların mobil arayüzünde, **ilişkili form** ile **Lookup**
    nesnesinden **DataGrid** nesnesine **veri eklerken meydana gelen takılma** hatası
    düzeltildi.
- 35045 - **IOS** cihazların mobil arayüzünde, **Native+** görünümündeki **Dinamik DataGrid**
    nesnesinde **sayfa geçişi yapılamama hatası** düzeltildi.
- 41875 [DR5933] - **IOS** cihazların mobil arayüzünde, **Akış tarafında** oluşturan **bilgisi**
    **gizlendiğinde** bu bilginin **Bekleyen İşler alanından görünme hatası** düzeltildi.
- 54 433 [DR8989] - **IOS** cihazların mobil arayüzünde, **Native+** görünümünde
    **DocumentMetaData** nesnesiyle **tarih ayarlaması** yapıldığında, formda bir işlem
    yapıldıktan sonra tarih **formatının bozulma hatası** düzeltildi.
- 54430 [DR8985] - **IOS** cihazların mobil arayüzünde, **Native+** görünümündeki **Run at**
    **Server** özelliği **aktif** olan **Lookup** nesnesinde meydana gelen **filtreleme** ve **arama**
    **hataları** düzeltildi.
- 54985 - **IOS** cihazların mobil arayüzünde, **form açılmak** istendiğinde **yüklenme**
    **aşamasında kalma hatası** düzeltildi.
- 46857 - **IOS** cihazların mobil arayüzünde, **Native+** görünümündeki **Statik DataGrid**
    nesnesinde **ID kolonunun değiştirilebilmesi** ve **Kaydetme işlemi** yapılmak
    istendiğinde ise **yükleme ekranında kalma hatası** düzeltildi.
- 48429 - **IOS** cihazların mobil arayüzünde, **Webview** ile mobilden açılan bir form için
    **iki kere konum izni isteme hatası** düzeltildi.
- 55771 - **IOS** cihazların mobil arayüzünde, **Native+** görünümündeki **Dinamik**
    **ComboBox** nesnesinde seçim yapıldıktan sonra **aksiyonlardan kaydetme işlemi**
    yapıldığında **seçimin gitme hatası** düzeltildi.

#### • 56177 - IOS cihazların mobil arayüzünde, Webview görünümündeki Statik DataGrid

```
nesnesinde ComboBox kolonunda verilerin listelenmeme hatası düzeltildi. 54430
[DR8985] - IOS cihazların mobil arayüzünde, Native+ görünümündeki Run at Server
özelliği Aktif olan Lookup nesnesinde meydana gelen filtreleme ve arama hataları
```
#### düzeltildi.


- 60908 - **IOS** cihazların mobil arayüzünde, **Native+** görünümündeki **DataGrid**
    içerisinde **iki adet DateTimePicker nesnesi** ile **hesaplama yapıp farkını bir TextBox**
    **nesnesine yazdıramama hatası** düzeltildi.


## 4. Breaking Changes

1. Projeler **tekrar** yayınlanmalıdır.
2. **RestSharp** servisi kullanılan **komponentler** doyasıyla **güncellenmek** durumunda
    kalınmıştır. **106.10.1** versiyonundan **110.2.0** versiyonuna **geçilmiştir**. Buna yönelik olarak
    aşağıdaki düzenlemeler yapılmalıdır:

```
Client ayarları, RestClientOptions sınıfı ile belirtilmeye başlandı.
```
```
Örnek:
```
```
RestClientOptions clientOptions = new
RestClientOptions(_workflowData.HttpClientOptions.WebInterfaceUrl)
{
MaxTimeout = 99999999
};
var client = new RestClient(clientOptions);
```
```
Method tipi belirtilecekse, url ve method tipi yazılması gerekmektedir.
Eğer metot tipi belirtilmediyse get tipi varsayılan olarak gelir.
```
```
Eski kullanım:
var request = new RestRequest(Method.Post);
```
```
Yeni Kullanım:
var request = new RestRequest("hr/Users/Insert", RestSharp.Method.Post);
```
```
Bunlara ek olarak IRestResponse interface kaldırıldı. Yerine RestResponse sınıfı
kullanılabilir.
```
```
Örn: RestResponse response = client.Execute(request);
```
```
Basit bir get isteği;
```
var clientOptions = new RestClientOptions() {
MaxTimeout = 30, // milliseconds (timeout)
BaseUrl = new System.Uri("https://dev.bimser.net/")
};
var client = new RestClient(clientOptions);
var request = new RestRequest("/Users/Get", Method.Get);
var response = client.ExecuteAsync(request).Result;


**Method enum değişikliği**

Method.Get || Method.Post || Method.Copy || Method.Delete || Method.Head ||
Method.Merge || Method.Options || Method.Patch

```
RestSharp Dokümantasyon linki:
https://restsharp.dev/intro.html#introduction
```
3. **Referans dll versiyonu Core 7 ye uygun minimum versiyonlara** göre **güncellenmelidir.**

```
dll versiyonlarının oluşturduğu hata örneği görseldeki gibidir:
```
![](https://docsbimser.blob.core.windows.net/imagecontainer/dll-ver-hata-orn-ffa63538-db41-47db-9358-84d42f4673e5.png)

```
Verilen bu hata mesajında minimum versiyon bilgisi yer almaktadır.
```
```
dll versiyonlarının oluşturduğu hatayı düzeltmek için örnek kod bloğunun yazılması
gerekir:
```
```
{
“ RestSharp ”: “110.2.0”,
“ SkiaSharp ”: “2.88.6”
}
```




<font size="5"><a href="https://portal.synergynow.io/#/_redirect/JnwmVQeEMgg0MkQ45VewBk"  target="_blank"><svg fill="currentColor" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" viewBox="0 0 40 40" style={{verticalAlign: "middle"}}><g><path d="m35.8 8.5q0.6 0.6 1 1.7t0.5 1.9v25.8q0 0.8-0.6 1.5t-1.6 0.6h-30q-0.9 0-1.5-0.6t-0.6-1.5v-35.8q0-0.8 0.6-1.5t1.5-0.6h20q0.9 0 2 0.4t1.7 1.1z m-9.9-5.5v8.4h8.4q-0.3-0.6-0.5-0.9l-7-7q-0.3-0.2-0.9-0.5z m8.5 34.1v-22.8h-9.3q-0.9 0-1.5-0.6t-0.6-1.6v-9.2h-17.1v34.2h28.5z m-11.4-13.2q0.7 0.6 1.8 1.3 1.3-0.2 2.6-0.2 3.3 0 4 1.1 0.4 0.5 0 1.2 0 0 0 0l0 0v0.1q-0.2 0.8-1.6 0.8-1.1 0-2.6-0.4t-2.9-1.2q-4.9 0.5-8.7 1.8-3.4 5.9-5.4 5.9-0.4 0-0.7-0.2l-0.5-0.2q0-0.1-0.1-0.2-0.3-0.2-0.2-0.8 0.2-0.8 1.3-2t2.9-2.1q0.3-0.2 0.5 0.1 0.1 0 0.1 0.1 1.1-1.9 2.4-4.4 1.5-3.1 2.3-5.9-0.5-1.8-0.7-3.5t0.2-2.9q0.2-0.9 0.9-0.9h0.5q0.5 0 0.8 0.4 0.4 0.4 0.2 1.5-0.1 0.1-0.1 0.2 0 0 0 0.1v0.7q0 2.8-0.3 4.3 1.2 3.7 3.3 5.3z m-12.9 9.2q1.2-0.6 3.1-3.5-1.2 0.8-2 1.8t-1.1 1.7z m8.9-20.6q-0.4 1-0.1 3 0.1-0.2 0.2-1 0-0.1 0.1-0.9 0.1-0.1 0.1-0.2 0-0.1 0-0.1t0 0 0 0q0-0.5-0.3-0.8 0 0 0 0v0z m-2.8 14.8q3-1.2 6.4-1.8-0.1 0-0.3-0.2t-0.4-0.3q-1.7-1.5-2.8-4-0.6 2-1.9 4.4-0.7 1.3-1 1.9z m14.4-0.4q-0.5-0.5-3.1-0.5 1.7 0.6 2.8 0.6 0.3 0 0.4 0 0 0-0.1-0.1z"></path></g></svg>PDF Download</a></font>
