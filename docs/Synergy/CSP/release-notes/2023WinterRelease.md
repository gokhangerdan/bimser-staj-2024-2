---
sidebar_position: 2335
sidebar_label: "2023 Winter Release"
custom_edit_url: ""
---

# Bimser Synergy 2023 Winter Release Notes 
*(1 Kasım 2023 - 31 Aralık 2023)*

## 1. Highlights / New Features

- 63044 - Flow General (Property Inspector) Email Sending Profile özelliği kazandırıldı.
- 67256 - Geliştirme arayüzünde UserMetaData nesnesinin Select Metadata Type
    özelliğine CompanyName özelliği getirildi.
- 68326 - FormSteps verilerinin kaydedilmesi için dapper plus kütüphanesinin
    kullanılması sağlandı.
- 64289 - Geliştirme arayüzünde, Dinamik DataGridde columnsda Icon Source Field
    alanında seçim yapıldıktan sonra seçilen verinin temizlenmesi için clear özelliği
    eklendi.
- 56214 - Web arayüzünde ana sayfada bulunan süreç detaylarına fast approval(hızlı
    onay) özelliği eklendi.
- 64545 - Geliştirme arayüzünde DocumentMetaData nesnesinin Pull New Number
    özelliğini açıp Readonly seçeneği kapattıktan ve form özelliklerinden Identity Format
    kısmından seçim yaptıktan sonra Web arayüzünde DocumentMetaData nesnesinin
    yanındaki butona tıklanıp Yeni Numara Üretilmesi ve sonraki onaycıda nesnenin
    Readonly olması sağlandı.
- 65093 - Web arayüzünde, aksiyon formuna Atama Kategorisi: Kullanıcı, Departman,
    Grup, Pozisyon seçimine göre atama yapılması sağlandı.
- 37679 - Web arayüzü doküman yönetiminde kolon seçicinin local storage ile birlikte
    kayıt edilme özelliği geliştirildi.
- 40653 - Geliştirme arayüzünde araçlar sekmesine ‘Görev Yöneticisi’ sayfası eklendi.
    Sayfa ile deploy agent üzerinde çalışan projelerin bilgileri görüntülenebilmesi,
    projelerin durdurulabilmesi ya da başlatılabilmesi, çalışan projelerin loglarının
    görüntülenebilmesi sağlandı.
- 52757 - Web arayüzünde Synergy üzerinden EBA geçmiş onaylarının
    görüntülenebilmesi sağlandı.
- 56368 - Geliştirme arayüzünde CreateFillFormLink metodunun documentid ile
    açılabilmesi sağlandı. Bir form doldur tipindeki formlara aktiviteler butonunun
    gelmesi , aktiviteler üzerinden kullanıcıların etiketlenebilmesi ve etiketlenen
    kullanıcılara mail bildirimi ile gönderilen link üzerinden formun görüntülenebilmesi
    sağlandı.
- 63618 – Elektronik imza projesinde PDF içerisine imza logosunun eklenmesi sağlandı.
- 64423 – Elektronik imza projesinde code refactoring yapıldı.
- 63111 – İnsan Kaynakları uygulamasında yer alan tüm repository’ler için unit testler
    oluşturuldu.
- 63107 – Mail service uygulamasında unit testler oluşturuldu, EFMıgiration’daki eksik
    tablolar oluşturuldu ve yetki testleri yapıldı.
- 64991 – Elektronik İmza projesinde KamuSM’ye ait yeni Akis 2.6.2 kartları için
    implementasyon sağlandı.
- 65115 – Dijital İmza servisine ait DSClient uygulamasında yapılan geliştirmeler Bimser
    Docs'a doküman olarak eklendi, uygulama indirme linki son versiyon için güncellendi.
- 65693 – Mail service uygulamasında akka cluster’ın aktif olmadığı ortamlar için,
    gönderilememiş maillerin tekrar gönderilmesi için retry fonksiyonu oluşturuldu.
- 65729 – HR Transfer uygulamasına instance parametresi eklendi.
- 68642 – Mail service uygulamasında yer alan profillerin çekilmesi için GetProfiles API
    fonksiyonu oluşturuldu.
- 69310 – Mail gönderiminin hangi profil üzerinden yapılacağının SendMail
    fonksiyonuna parametre olarak geçilmesi sağlandı.
- 66838 – Doküman transfer uygulamasında login ve update işlemleri için kod
    iyileştirmeleri yapıldı.
- 21245 – İnsan Kaynakları modülünde eksik kalan güvenlik yetki kontrolleri eklendi.
- 62833 – İnsan Kaynakları modülünde şirket detayı ekranına Döviz Türü (para birimi)
    ve Döviz İşlem Türü (döviz alış, satış, efektif alış, satış) alanları eklendi.
- 68472 - Geliştirme arayüzünde flow genel özelliklerine Email Sending Profile seçeneği
    eklendi.

## 2. Improvements

- 63267 - Web arayüzünde devam eden akışların güncel versiyona yükseltilebilmesi için
    endpoint geliştirme yapıldı.

```
POST
https://{{Url}}/{{deployagentId}}/deployagent/apps/ProjeAdı/YükseltilecekVersiy
onNumarası/api/FlowAdı/UpgradePackageVersion
Body:
{
"processId": 1234
}
```
- 40656 - Geliştirme arayüzünde Araçlar sekmesindeki Görev Yöneticisi ekranı
    tamamlandı. Bu ekranda projenin versiyon bilgilerinin görüntülenmesi,durdur/başlat
    işlemlerinin yapılabilmesi sağlandı.

- 66485 - Geliştirme arayüzünde Araçlar menüsü altına Yetkilendirme paneli eklendi.
    Form ve Flowlar içinde kullanılmak üzere, müşterinin kendi yetki tanımlarını
    ekleyebilmesi için Geliştirme arayüzü tarafına Yetkilendirme ekranı yapıldı.Proje bazlı
    ya da Genel olarak yetki tanımı yapıldıktan sonra proje detayından yetkiler projelere
    bağlanabilir ve Form Flow içinde kullanılabilir. Yetki izin değerleri Web ekranındaki
    Güvenlik panelinden Uygulamalar altından ayarlanabilir.
- 60745 - Geliştirme arayüzünde datasource klasöründe gpt sorgusunda Custom
    prompt,Decider,Info Extractor tiplerinde revizeler yapıldı.
- 63868 - Geliştirme arayüzünde flow tarafında aksiyon oluşturucu nesnesinde Proje
    seçiminde sadece aksiyon formu içeren projelerin listelenmesi sağlandı.
- 63861 - Geliştirme arayüzünde flow tarafında aksiyon oluşturucu nesnesinde States
    eklendikten sonra çizilmemiş linkler için validasyon uyarısı eklendi.
- 62958 - Geliştirme arayüzünde proje yöneticisinde aktif projelere dosya yolunu
    kopyalama ikonu eklendi.
- 63462 - Geliştirme arayüzünde akış yöneticisinde versiyon yükseltme özelliği
    geliştirildi.
- 66693 - Geliştirme arayüzünde proje özelliklerine Proje Yetkileri modalı eklendi.
- 69656 - Geliştirme arayüzünde rest sorgusunda body içerisine "@Parametre" girilen
    parametrenin body parameters alanına otomatik eklenmesi sağlandı. Parametreler
    tablolarından Başlık alanı kaldırılıp yerine Tip eklendi.
- 29566 - Web arayüzünde, scheduler service metod çağıran aksiyon özelliklerinde
    bulunan kültür alanı kullanılmadığı için kaldırıldı.
- 64412 - Geliştirme arayüzünde yeni oluşturulan projenin içerisinde Özellikler menüsü
    altındaki "Yetki Verilebilir" özelliğinin varsayılan değerin seçili olarak gelmesi sağlandı.
- 66456 - GetActiveFlowProjectVersions endpointine aktif olan versiyon bilgisi ve hangi
    adresten yayınlandığı bilgisi eklendi.
- 64668 - GetProcessesLean endpointinin response modeline LatestPackageVersion
    alanı eklendi.
- 62499 - Web arayüzünde, form açarak kaydet butonu sonrası event tetiklenmesi
    sağlandı.
- 62500 - Web arayüzünde oluşan form hatalarının FORMSTEPS tablosuna loglanması
    sağlandı.
- 34101 - Web arayüzünde Uygulama Gezgini panelinde uzun isimli olup menüye
    sığmayan (...) üç nokta ile kısaltılan projeler üzerine işaretçi ile gelindiğinde tooltip
    şeklinde menünün tam isminin yazması sağlandı.
- 64355 - Web arayüzünde 'Yetkiler' ekranında 'İzin Ver' veya 'İzin Verme' olarak
    kullanılabilmesi için geliştirme arayüzüne 'Yetki Kodu' ekleme alanı getirildi.
- 61767 - Web arayüzü doküman yönetiminde tablo görünümünde klasör içerisinde
    sıralama yapılıp, DM içerisinde herhangi bir işlemden sonra tekrar ilgili klasöre
    gelindiğinde yapılan sıralamanın korunması sağlandı.
- 67406 - Web arayüzünde, aksiyon yönetimindeki OnActionStateUpdating içinde
    e.Cancel = true; işlemi için hata mesajının ‘Durum güncellenemedi. Aksiyon projesinin
    çalıştığından emin olun.’ olarak gelmesi sağlandı.
- 67976 - GetParameters endpointine gridStateStoringEnabled parametresi eklendi.
- 47561 – WebInterfaceAPI, WebInterfaceRouter ve WebInterfaceWebAPI projelerinde
    kullanılan OpenMenuItem ve RecentlyMenuItems endpointlerinin ve endpointlerde
    kullanılan sınıfların isimleri OpenMenuItems yerine AddToLastOpenedItems,
    RecentlyMenuItems yerine de GetLastOpenedItems olarak değiştirildi.
- 63093 - DataGrid, Lookup, Selection cacheSettingsEnabled özelliği eklendi.
    Filtreleme, search, resizing, order, sorting, visible column,column width, Excell'e
    aktar gibi özellikleri seçimlerinin kullanıcı bazında saklanması ve tekrar açıldığında
    saklanan şekliyle açılabilmesi sağlandı.
- 65449 - Web arayüzünde doküman yönetiminde Repo, Folder, RecycleBin
    bölümlerinde filtreleme ve sıralama işlemleri için geliştirme yapıldı.
- 67533 - Geliştirme arayüzünde Yetki kodu ekleme alanı getirildi. Kullanıcılar
    Geliştirme ekranından Yetki Kodu ekleyebilir ve daha sonra Web arayüzünde her
    zamanki Yetkiler ekranından talep edilirse bu yetki kodlarına ‘İzin Ver’ veya ‘İzin
    Verme’ denilebilir.
- 63327 – Configuration Manager uygulamasında görsel düzenlemeler ve yetki
    iyileştirmeleri yapıldı.
- 64969 – Configuration Manager uygulamasında bir template dosya değiştirildiğinde
    değişikliğin config dosyalarına uygulanması sağlandı.
- 66132 – Configuration Manager'da kullanıcı yetkilendirmeleri yapıldı. Değişikliklerin
    klavye kısayolu ile yapılması sağlandı. Görsel düzenlemeler yapıldı.
- 66277 – Configuration Manager’da API servisinde memory cache implementasyonu
    sağlandı, config'lere erişim fonksiyonları geliştirildi.
- 68109 – Configuration Manager'da Design sekmesinde yer alan template'lerde aynı
    parametre kodunun kullanılması engellendi. Memory cache çalışması yapıldı.
- 66957 – Configuration Manager'da oluşturulan parametre değerlerinin CM API
    projesine aktarılması sağlandı.
- 67080 – Configuration Manager API projesinde memory cache işlemi için SignalR
    kütüphanesi projeye implemente edildi.
- 68633 – Configuration Manager uygulamasında yapılan değişiklik sonrası cache
    yenileme işleminin tetiklenmesi sağlandı.
- 68634 – Configuration Manager 'da yapılan değişiklik sonrası API projesinde
    parametre bazlı cache yenileme işlemi için geliştirme yapıldı. Tüm cache'in
    yenilenmesi için de altyapı oluşturuldu.
- 70330 – Configuration Manager API projesinin yalnızca Sucrotor kütüphanesi ile
    çalışması sağlandı.
- 63703 – Synergy Capture fonksiyonları Synergy DM içerisine implemente edildi.
- 63369 – Synergy Capture için Magick.NET kütüphanesi implemente edildi, servis
    katmanında belge kaydetme işlemleri için gerekli fonksiyonlar oluşturuldu.
- 64986 – Synergy Capture servisi setup fonksiyonları revize edildi. Capture servis
    portu değişikliği yapılabilmesi sağlandı. DM'deki tarama editör penceresinde toolbox
    fonksiyonları artırıldı, görsel iyileştirmeler yapıldı.
- 66020 – Synergy Capture servisinin installer yardımıyla kurulması için paketleme
    çalışması yapıldı.
- 63368 – Synergy Capture servisinde görüntü işleme fonksiyonları oluşturuldu.
- 67490 – Synergy Capture servisinde port değiştirme, servis restart, registery key
    güncelleme fonksiyonlar oluşturuldu.
- 67002 – Synergy Capture setup uygulamasında system tray ile ilgili çalışmalar yapıldı.
- 68581 – Synergy Capture kurulum ve kullanım dokümanı hazırlandı, Bimser Docs'a
    eklendi.
- 68585 – Synergy Capture uygulamasının Atalasoft servisinin Abbyy’den ayrıştırılarak
    ayrı bir exe ile çalışması sağlandı.
- 68589 – Synergy Capture’da Abbyy lisansına sahip müşterilerin kullanabileceği
    özelliklerin ayrı bir uygulama üzerinden yapılması sağlandı. Atalasoft için ayrı, Abbyy
    için ayrı servis uygulamaları oluşturuldu.
- 69021 – Synergy Capture servislerinin setup aşamasından sonra otomatik
    başlatılması ve servis ayarlarının uygulama üzerinden güncellenebilmesi sağlandı.
- 69288 – Synergy Capture’da Yeni Dosya ekleme işleminde Tara butonuna
    tıklandığında açılan editor penceresinde tarayıcı bağlantısı sağlanamaması
    durumunda tarayıcı bağlantısı sağlanamadığına dair uyarı mesajı gösterilmesi
    sağlanmıştır.
- 70195 – Synergy Capture’da görüntü editörü penceresinde bir fonksiyona
    tıklandığında toolbar'da yer alan diğer işlem butonlarının disabled olması sağlandı.
- 63333 – Synergy Drive uygulamasında ait servisin DM ile entegresyonu sağlandı.
- 66024 – Synergy Drive sunucu-client eşitleme işlemleri gerçekleştirildi.
- 66120 – Synergy Drive uygulamasında CSP tarafında state işlemleri (FIFO), dosya
    upload işlemlerinde progress bar eklenmesi ve yapılan isim değişikliklerinin
    yansıtılması sağlandı.
- 64979 – Synergy Drive’da CSP ortamında doküman state’lerine uygun işlemlerin
    (create, upload, delete, move, rename) yapılması sağlandı.
- 64981 – Synergy Drive’da client uygulamasında doküman state’lerine uygun
    işlemlerin (create, upload, delete, move, rename) yapılması sağlandı.
- 64985 – Synergy Drive uygulamasında toplu aktarım, perfomans ve code refactoring
    çalışmaları yapıldı.
- 66121 – Synergy Drive client uygulamasında getUpdates metodu eklendi, anlık işlem
    sayısı sınırlandırıldı.
- 67081 – Synergy Drive ortam ve client oturum bilgilerinin appsettings'ten alınması
    sağlandı. Login ve toplu aktarım kod iyileştirmeleri yapıldı.
- 68120 – Synergy Drive'da birden fazla Synergy ortamına aynı anda bağlantı
    sağlanması için ayrı uygulamalar oluşturuldu.
- 63332 – Synergy Drive uygulamasında kullanıcının yetkili olduğu tüm klasörler için
    client uygulamasında eşitleme yapılması sağlandı.
- 69065 – Synergy Drive'da birden fazla Synergy ortamına aynı anda bağlantı
    sağlanması için altyapı çalışması yapıldı

## 3. Fixes

### 3.1. Web Arayüzü

#### 3.1.1. Doküman Yönetimi

- 68152 - Web arayüzü doküman yönetiminde metadata alanından profil form tanımlı
    depo/klasör içerisine dosya/klasör oluşturulurken alınan hata giderildi.
- 68102 - DM tablo görünüm modunda 'Owner' kolonu header filtresi kısmına veri
    girişi sonrası alınan hata giderildi.
- 62091 - Web arayüzü doküman yönetiminde çalışma başlat a tıklandıktan sonra
    içeriklerde edit sırasında oluşan hata giderildi.
- 62091 - Web arayüzü doküman yönetiminde ‘Çalışma Başlat’ butonuna tıklandıktan
    sonra içeriklerde edit sırasında oluşan hata giderildi.
- 64507 - Web arayüzünde formda spesifik fotoğrafları RelatedDocuments'a
    yükleyememe hatası düzeltildi.
- 66343 - Doküman yönetiminde çöp kutusuna tıklandıktan sonra üstteki başlangıç
    butonunun çalışmama sorunu giderildi.
- 67555 - Web arayüzünde Doküman Yönetiminde herhangi bir belge içerisinde
    'İçerikler' sayfasındayken sol menüden 'Başlangıç' sayfasına dönülmek istenildiğinde
    alınan hata düzeltildi.
- 66144 - Web arayüzü doküman yönetiminde tablo görünümünde tümünü seç/kaldır
    işlemlerindeki sorun giderildi.
- 66872 - Web arayüzü doküman yönetiminde tiff uzantılı dosyalarda ‘Çalışma Başlat’
    butonu ile revizyon yapılırken gözat butonunun gözükmemesi sorunu giderildi.
- 64814 - Web arayüzü doküman yönetiminde metadata alanından profil form
    tanımlanmış depo/klasörler için tablo görünümünde sütun seçicide profil formdan
    gelen alanlar için yapılan ayarların kaydedilmesi sağlandı.
- 67088 - Web arayüzü doküman yönetiminde depo ve klasör için context/top
    menülerinden özellikler sekmesi açılırken oluşan time-out hatası giderildi.
- 65821 - Web arayüzü doküman yönetiminde depo içindeki nesne sayısı çok
    olduğunda context menüde oluşan görünüm sorunu giderildi.
- 66241 - Web arayüzü doküman yönetiminde depo/klasör içine dosya eklendiğinde
    mevcut dosyaların kaybolması sorunu giderildi.
- 67168 - Web arayüzü doküman yönetiminde herhangi bir depo klasör e ikinci kez
    girişte verilerin kaybolması hatası giderildi.
- 65893 - Web arayüzünde Erişim Anahtarı ile Doküman Yönetimine girilmek
    istendiğinde hata verme sorunu düzeltildi.
- 66039 - Web arayüzü doküman yönetiminde dosyalarda masaüstünde aç butonuna
    tıklandığında url oluşturmada oluşan hata düzeltildi.
- 65713 - Web arayüzü doküman yönetiminde çöp kutusuna tıklandığında alınan hata
    giderildi.
- 65820 - Web arayüzü doküman yönetiminde klasör ve dosyalarda kısayol işleminden
    sonra yeniden adlandırmada alınan hata giderildi.
- 65850 - Web arayüzü doküman yönetiminde adında boşluk olan dosyalar
    indirildiğinde oluşan dosya ismi hatası giderildi.
- 66457 - Web arayüzü doküman yönetiminde tarih kolonlarının formatları düzenlendi.
- 65621 - Web arayüzü doküman yöneyiminde dosya görüntüleme ekranı üzerinde
    bulunan aktiviteler seçeneğinin farklı panel boyutlarında oluşan görünüm sorunu
    düzeltildi.
- 65831 - Web arayüzü doküman yönetiminde favoriler ekranında, favorilerden
    kaldırma işlemi yapıldığında birden fazla notification çıkması engellendi. Ekleme yada
    kaldırma işlemlerinden bazıları başarısız olduysa mesajın sonunda gösterilmesi
    sağlandı.
- 66822 - Web arayüzü doküman yönetiminde dosya görüntüleme ekranı üzerinde
    bulunan alanların yazı tipleri düzünlendi.
- 65481 - Web arayüzü doküman yönetiminde xls uzantılı excel dosyaları açılırken
    alınan hata giderildi.
- 68057 - Aksiyon yönetiminde tüm statülerin task renklerinin board üzerinde
    gösterilmesi sağlandı.
- 65779 - Web arayüzü doküman yönetiminde Masaüstünde Aç butonuna
    tıklandığında alınan hata giderildi.
- 68531 - Cspdestek ortamında, Config Cache temizlendiğinde ilgili tabloda yapılan
    değişikliklerin ortama geçmesi sağlandı.
- 71205 – DataBase'de tenantCustomProperties bilgilerine eklenen dataların ortamda
    GetLoginParameters içerisinde eklenmiş olarak gözükmesi sağlandı.
- 25561 - Döküman Yönetimi'nde gelişmiş arama filtrelerinde 'Oluşturan', 'İçerik',
    'Değiştirilme Tarihi', 'Arama Kaynağı Tipi' ve 'Lokasyon' alanlarında yaşanan sorunlar
    giderildi.
- 26900 - Web arayüzü doküman yönetiminde arama işleminde sonuçların eksik
    gelmesi sorunu düzeltildi.
- 49532 - Web arayüzü döküman yönetiminde 'Etiketler' kolonunun klasör ve
    dosyalarda da gösterilmesi sağlandı.
- 68532 - Geliştirme arayüzünde formlar üzerinde düzenleme yetkisi bulunmayan
    kullanıcıların RelatedDocuments nesnesi üzerinden versiyon çalışması
    oluşturabilmesi hatası giderildi.
- 65559 - Web arayüzü doküman yönetiminde yeni eklenen deponun sayfa
    yenilenmeden görünmemesi sorunu giderildi.
- 62391 - Web arayüzü doküman yönetiminde metadata ya yeni bir proje form
    eklenmek istenildiğinde oluşan formun bulunama sorunu giderildi.
- 56345 – Web arayüzünde Doküman Yönetimi’nde doküman detayında bulunan
    Elektronik İmzalar butonuna tıklandığında alınan hata giderildi.
- 56474 – Doküman Yönetimi transfer uygulamasında hatalı metadata parametresiyle
    ile dosya yüklenmek istendiğinde hata mesajının gelmeme sorunu giderildi.
- 62735 – Web arayüzünde Doküman Yönetimi’nde viewer içerisinde yapılan aramada
    oluşan içerik görüntüleme hatası giderildi.
- 64374 – Web arayüzünde Doküman Yönetimi’nde office dosyalarını document viewer
    ile görüntüleme ve editleme sırasında oluşan hata giderildi.
- 69258 – Web arayüzü Doküman Yönetimi Capture editör penceresinde belge seçimi
    yapılmadan Tam Ekrana Sığdır butonuna tıklandığında oluşan görsel hata giderildi.
- 69265 – Web arayüzü Doküman Yönetimi Capture editör penceresinde kırpma
    aracında kırpma işlemini tamamlayan onay butonunun kırpma alanı seçimi
    sonrasında aktif olması sağlandı.
- 69282 – Web arayüzü Doküman Yönetimi Capture editör penceresinde araçlar
    penceresinde silgi aracı seçildiğinde aktif olan silme fonksiyonunu tamamlayan/iptal
    eden onay ve iptal butonlarının silme işlemi tamamlandığında aktif olması sağlandı.
- 69299 – Web arayüzü Doküman Yönetimi Capture editör penceresinde en-boy
    koruması kapatıldıktan sonra döndürme fonksiyonları kullanıldığında oluşan kayma
    problemi giderildi.
- 70103 – Capture client servisinde değişen port bilgisinin Web arayüzü Doküman
    Yönetimi tarama fonksiyonuna yansımasında yaşanan problem giderildi.
- 73317 - Web arayüzünde Lookup nesnesinde nesnenin sağ tarafında bulunan üç
    noktadan lookup'ı açmak yerine direkt nesnenin üzerindeki search kısmından arama
    yapılmak istenirse, ilk tıklamada değerlerin gelmeme sorunu giderildi.
- 73288 - Web arayüzünde DataGrid nesnesine eklenmiş olan object tipinde olan
    ComboBox column nesnelerinde verilerin listelenmesiyle ilgili sorun giderilmiştir.

#### 3.1.2. İş Akış Yönetimi


- 52264 - Web arayüzünde İş Akış Yönetimi alt menülerinin Datagrid'lerinde kolonlara
    göre gruplama yapılırken alınan hata düzeltildi.

#### 3.1.3. İnsan Kaynakları

- 66874 - Web arayüzünde yeni bir kullanıcı oluşturduktan sonra Everyone grubuna
    otomatik olarak dahil olmama ve bu grubun yetkilerinden bağımsız şekilde giriş
    yapabilme hatası düzeltildi.
- 67867 - Web arayüzünde HR projeleri açılırken veya kaydedilirken alınan console
    hatası giderildi.
- 33483 – Web arayüzünde İnsan Kaynakları modülünde Unvanlar sekmesinde aynı
    veri tekrar eklendiği zaman sunucu hatası vermesi giderilerek, uyarı mesajı verilmesi
    sağlandı.
- 39690 – Web arayüzünde İnsan Kaynakları modülünde Maaşlar sekmesinde bir kayda
    tıklandığında açılan pencere kapatıldığında ana pencerenin otomatik kaymama hatası
    düzeltildi.
- 52205 – Web arayüzünde İnsan Kaynakları modülünde Özellikler sekmesinde özellik
    detayında yer alan Ad ve Başlık alanları hatalı kullanıma sebep olduğu için Kod ve
    Tanım olarak değiştirildi.
- 53021 – Web arayüzünde İnsan Kaynakları modülünde API servisinde
    GetCurrenUserInfo fonksiyonu ile kullanıcı bilgilerini çekerken alınan hata giderildi.
- 53976 – Web arayüzünde İnsan Kaynakları modülünde Kullanıcılar sekmesinde
    kullanıcı ekleme işlemi sırasında oluşan hata giderildi.
- 56198 – Web arayüzünde İnsan Kaynakları modülünde Maaşlar sekmesinde maaş
    güncelleme işleminde farklı bir maaş kaydında kullanılan tarih aralığının seçilebilmesi
    hatası giderildi.
- 64394 – Web arayüzünde İnsan Kaynakları modülüne ait menülerin yüklenmeme
    hatası giderildi.
- 64436 – Web arayüzünde İnsan kaynakları menüsünün açılmama hatası giderildi.
- 67082 – Web arayüzünde İnsan Kaynakları modülünde sekmeler açılırken oluşan hata
    giderildi.
- 67898 – Web arayüzünde İnsan Kaynakları modülünde Kullanıcılar sekmesinde
    kullanıcılara ait telefon bilgisinin boş gelmesi sorunu giderildi.
- 67898 – Web arayüzü İnsan Kaynakları modülünde kullanıcı telefon bilgilerinin boş
    gelme hatası giderildi.

#### 3.1.4. Web Ana Sayfa


- 69026 - Web arayüzünde pdf aktar nesnesi içeren akış gönderildiğinde alınan Object
    reference hatası giderildi.
- 67028 - Web arayüzünde Repeater nesnesinin içindeki formun onBeforeSave
    eventini tetiklenmeme hatası düzeltildi.
- 67245 - Web arayüzünde Tabs nesnesi içerisinde açılan DateRangePicker nesnesinin
    gözükmeme hatası düzeltildi.
- 66756 - Web arayüzünde, aksiyon yönetimi panelinde taska ilişki ekleme ve silme
    durumları taskin kaydedilmesine bağlı olmaması sağlanarak hata giderildi.
- 65605 - Web arayüzünde, RadioList değerine göre açılan formda Required alan boş
    gönderildiğinde bununla ilgili uyarı verme hatası düzeltildi.
- 52832 - Web arayüzünde Hesabım menüsünün Vekalet ve Erişim Anahtarları
    menüsünde herhangi bir vekalet düzenlemek için açıldığında, Basit ve Gelişmiş
    sekmeleri arasında geçiş yapıldığında daha önce yapılmış olan seçimlerin kaybolma
    hatası düzeltildi.
- 66341 - Web arayüzünde, arşivi oluşturulan time picker nesnesi formatlarının
    datagride yansımama hatası giderildi.
- 65877 - Web arayüzü doküman yönetiminde MetaData sekmesinde edit işlemi
    sırasında alınan hata giderildi.
- 66015 - Web arayüzünde, datagrid paging işleminde değerlerin gidip gelme hatası
    giderildi.
- 67118 - Web arayüzünde form seçimi yapılmamış akışlarda butonların gözükmeme
    hatası giderildi.
- 67993 - Web arayüzünde formda Dropdown nesnesinin yükleniyor olarak kalma
    hatası düzeltildi.
- 61136 - Web arayüzünde, aksiyon yönetimi menüsünde filtre kısmında tarih
    filtrelerinin panel içerisine sığmama hatası giderildi.
- 62094 - Web arayüzünde, aksiyon yönetiminde paneller kapatılınca kapat butonunun
    dışarda kalma hatası giderildi.
- 64538 - Web arayüzü dashboardda Deploy Agents çekilmeden süreçler açılmaya
    çalışıldığında alınan hata giderildi.
- 65905 - Web arayüzünde süreç detaylarından hızlı onay butonu ile gönderilen akışın
    süreç detayından silinmeme hatası giderildi.
- 66990 - Web arayüzünde, forma eklenen textarea nesnesinin client tarafında
    karakter uzunluğunun hesaplanamama hatası giderildi.
- 67027 - Web arayüzünde, Repeater nesnesinde üçten fazla işlemi tekrar etmeme
    hatası kontrol edildi.
- 65467 - Web arayüzünde FormViewer nesnesi akışta ilerletildiğinde sonraki onaycıda
    içinin boş gözükme hatası düzeltildi.
- 66559 - Web arayüzünde Parametrik Datasource bağlı olan ListBox nesnesinin ilk
    olarak yüklendiği için diğer nesnenin parametre değerlerine erişilmeme hatası
    düzeltildi.
- 66986 - Web arayüzünde, datagrid editType:TextBox, dbDtype:String kolonu kaydet
    işleminde database culture bilgisi system olarak yazılması sağlandı.
    EditType:MultiLanguageTextBox, dbDtype:object olan kolon için kaydet
    işleminde database culture bilgisi kullanıcı tarafından girilen culture bilgilerinin
    yazılması sağlandı.
- 65558 - Web arayüzünde service api bağlantısı bulunan ve akış ilerletildiğinde oluşan
    LoginAsync hatası giderildi.
- 65857 - Web arayüzünde, FishBone, DataGrid, ComboBox, ve TextBox nesneleri olan
    form kaydedilince alınan parentid hatası giderildi.
- 65100 - Web arayüzünde, oluşturulan arşiv formundaki datagride formdaki
    nesnelerin verilerinin yansımama hatası giderildi.
- 64609 - Web arayüzünde bekleyen işler alanında sürecin çok geç açılması,timeout
    oluşması veya hiç açılmama sorunu giderildi.
- 65203 - Web arayüzünde form ekranına Lookup nesnesinde id değeri 0 olan kolon
    seçildiğinde oluşan hata giderildi.
- 66336 - Web arayüzünde Pozisyon ve Pozisyon Grubuna atanan pasif pozisyon
    tanımları için ErrorOnInactiveAssignment özelliği true ise hata verilmesi sağlandı.
- 50943 - Web arayüzünde, datagrid nesnesi aksiyon formu ve process arşiv
    kolonlarındaki ı ve i harflerini aynı algılama hatası giderildi.
- 65777 - Web arayüzünde DataSynchronizer nesnesinin çalışması için Button
    nesnesine basıldığında hata verme sorunu düzeltildi.
- 66754 - Web arayüzünde, Aksiyon Yönetimi ekranında taska ilişkili aksiyon ve alt
    aksiyon ekleniyor ardından ilişkili olarak eklenen taska bakıldığında bu ilişki
    gözükmeme hatası giderildi.
- 66763 - Web arayüzünde, aksiyon yönetimi paneli için
    /api/web/Actions/GetActionsForRelation fonksiyonu eklendi. Aksiyon formunda
    ilişkili idleri listelememesi sağlanarak hata giderildi.
- 48216 - Web arayüzünde popover özelliğinde açılan Lookup nesnesinde yapılan
    seçimler silinip liste tekrar açıldığında silinen seçimlerin seçili gelme hatası giderildi.
- 50752 - Web arayüzünde, arşivi oluşturulan aksiyon formunda verilerin gelmeme
    hatası giderildi.
- 66744 - Web arayüzünde form içerisinde FileSelector veya RelatedDocuments
    nesneleri bulunduğunda GetValues endpointinin boş dönme hatası düzeltildi.
- 66770 - Web arayüzünde, aksiyon yönetimi menüsünde aksiyon ilişkilendirilirken
    açılan paneldeki verilerin id bilgilerine göre sıralanmama hatası giderildi.
- 66784 - Web arayüzünde aksiyon yönetimi panelinde aksiyon tasklarında ilişki
    eklenirken durum kolonundaki verilerin ingilizce gelme hatası giderildi.
- 66288 - Web arayüzünde form ekranında Related Documents nesnesine yüklenen
    .xlsx uzantılı dosyada görüntüleme işlemi yapıldığında alt scroll'un gelmeme hatası
    giderildi.
- 67105 - Web arayüzünde Lookup nesnesinin OnValueChanged eventine yazılan kod
    ile Lookup nesnesinin kolonlarındaki verilerin belirtilen kısımlarını TextBox ve ya
    NumberBox nesnelerine atanamama hatası düzeltildi.
- 49798 - Web arayüzünde, ilişkili datagrid ile açılan modal formdaki lookup nesnesi
    doldurulup ana formdaki DataGrid, akışta PDF'e Aktar nesnesi kullanılarak PDF'e
    aktarıldığında Lookup verisini içeren satırında, username'i içeren text değerinin
    görünmesi gerekirken, id'yi içeren value değeri aktarılma hatası giderildi.
- 67234 - Web arayüzünde, aksiyon yönetimi menüsünde forma ilişki eklenmemiş olsa
    bile zaten var diye hata dönmesi giderildi.
- 66453 - Web arayüzünde form ekranında datagrid üzerinde ekle butonu ile açılan
    formdaki datagrid de arama alanının ... şeklinde gözükme hatası giderildi.
- 68923 - Web arayüzünde, aksiyon yönetimindeki tasklardaki verilerin duplicate
    olarak gelmesi ve networkte stateCategoryColor bilgisinin null gelmesi düzeltildi.
- 68704 - Web arayüzünde Vekalet ve Erişim Anahtarları kısmından verilen Vekalet ile
    giriş yapılamama hatası düzeltildi.
- 67161 - Web arayüzünde Erişim Anahtarı oluştururken Doküman Yönetimi kısmına
    izin verdiğimiz halde, Erişim Anahtarı ile ortama giriş yaptıktan sonra Doküman
    Yönetimi üzerinde hiçbir depo ya da klasörün gözükmeme hatası düzeltildi.
- 65660 - Statik datagrid cell modundayken select tipli kolona verilerin yansımama
    hatası giderildi.
- 67231 - Web arayüzünde, datagrid nesnesi cell tipindeyken context menu bağlı kolon
    düzenle modunda context menüye tıklanması sağlanarak kolona veri yazılabilmesi
    sağlandı.
- 67946 - Web arayüzünde 'Güvenlik' panelinde 'Sistem' başlığı altındaki 'Sistem
    Erişimi' seçeneği' İzin Verme' olarak seçtikten sonra ilgili üye giriş yapmak istediğinde
    alınan hata giderildi.
- 67947 - Web arayüzünde 'Güvenlik' panelinde 'Kullanıcı Arayüzü' başlığı altındaki
    'Arayüz Erişimi' seçeneği 'İzin Verme' olarak seçildikten sonra ilgili üye giriş yapmak
    istediğinde alınan hata giderildi.
- 66486 - Web arayüzünde Uygulamalar, İş Akış Yönetimi ve Menü yetkilerine sahip
    olmayan yeni bir kullanıcıya tüm yetkilere sahip bir vekalet verildiğinde, bu vekalete
    girildikten sonra ortamdaki tüm yetkilere ulaşamama hatası düzeltildi.
- 66163 - Proje yeniden yayınlandıktan sonra açık olan modal pencerelerinin
    kapatılması sağlandı.
- 66687 - Web arayüzü dashboard’da yer alan duyurulara tıklanamama sorunu
    giderildi.
- 53481 - Web arayüzünde Olay Günlük Görüntüleyici modülü aktif hale getirildi ve
    Olay raporu alınamama hatası düzeltildi.
- 13463 - Web arayüzünde Profil fotoğrafı değiştirme işleminde ikinci defa
    değiştirilmek istendiğinde değişmeme hatası düzeltildi.
- 65364 - Web arayüzünde Duyurular panelinde sıralama filtrelerinin düzgün
    çalışmama hatası düzeltildi.
- 65369 - Web arayüzünde Duyurular panelinde tarih kolonlarındaki daha büyük, daha
    küçük ve eşit, eşittir filtrelerindeki hatalar düzeltildi.
- 39195 - Web arayüzünde 'Vekalet ve Erişim Anahtarları' kısmından vekalet
    oluştururken 'Vekaleti Yönet' yetkisi verilmediğinde, Vekalet verilen kullanıcının
    hesabında 'Vekalet ve Erişim Anahtarları' ile 'Erişim Anahtarları' sekmesinin
    görüntülenememesi sorunu giderildi.
- 52485 - Web arayüzünde formda Statik Datagrid üzerinde veri girişi yaparken verinin
    tamamı taranırken imleç soldaki kolona doğru taşındığında tıklanmadığı halde soldaki
    kolonun input alanına geçme hatası düzeltildi.
- 61084 - Web arayüzünde, uygulama gezgini profiller sekmesinde tümünü seç butonu
    çift tıklama ile seçilebilme sorunu giderildi.
- 61240 - Statik datagrid üzerinde ComboBox kolonu borderları belirgin hale getirildi.
    Kolon büyüklüğünün diğer kolonlarla aynı olması sağlandı.
- 67894 - Web arayüzünde, aksiyon yönetimi tarih filtrelerinin çalışmama hatası
    giderildi.
- 68057 - Tüm statülerin task renklerinin gelmesi doğrulandı.
- 62814 - Web arayüzünde Doküman Yönetimi içerisinde +Yeni butonu içerisinde "Yeni
    Kalite Klasörü" eklenmek istendiğinde gelen paneli geri butonu ile kapatıp depoya
    dönüldüğünde +Yeni butonunun kaybolma sorunu giderildi.
- 65376 - Web arayüzünde vekalet oluşturma sırasında dashboard proje seçilmese bile
    sistemde dashboard proje tanımlı ise sistem tarafından eklenmesi sağlandı.
- 47547 - Web arayüzünde, uygulama gezgininden dış bağlantı ile panel üzerinde açılan
    yeni formun başlığı url olarak gelme hatası giderilerek başlığa yazılan değerin gelmesi
    sağlandı.
- 40523 - Web arayüzünde giriş ekranında İngilizce dilinde şifremi unuttum işleminde,
    gelen mailden şifre yenileme ekranına geçildiğinde sayfanın Türkçe olarak açılma
    hatası giderildi.
- 67100 - Web arayüzü duyurularda durumu pasif olan duyuruların dashboardda
    gösterilmemesi ve düzenlenen duyuruların dashboardda en üst sırada gösterilmesi
    sağlandı.
- 66164 - Web arayüzün CreateLink ile oluşturulan ID ile açılmak istenildiğinde oluşan
    Login hatası giderildi.
- 65348 - Web arayüzü dashboard’da duyurular alanında silme işlemi yapılırken alınan
    hata giderildi.
- 64180 - Web arayüzünde 'Menü Ekle' panelinden eBA Entegrasyonu eklemek
    istendiğinde 'Gelişmiş Parametreler' sekmesine bir veri girip 'Ekle' denildikten sonra,
    'Temel Bilgiler' sekmesinde 'Entegrasyon Türü' ve 'eBA Entegrasyon' başlığındaki
    verilerin silinme hatası düzeltildi.
- 68655 - Web arayüzünde 'Güvenlik' sekmesinde ekli olan bir kullanıcı silinmek
    istendiğinde alınan hata giderildi.
- 42825 - Web arayüzü iş akış yönetiminde 'Bekleyen İşler' paneli arama barında büyük
    ve küçük harf duyarlılığı ile arama yapılabilmesi sağlandı.
- 52485 - Web arayüzünde formda Statik Datagrid üzerinde veri girişi yaparken verinin
    tamamı taranırken imleç soldaki kolona doğru taşındığında tıklanmadığı halde soldaki
    kolonun input alanına geçme hatası düzeltildi.
- 61537 - Web arayüzü döküman yönetiminde profil form ile oluşturulan dosyada
    related document nesnesi tablo görünümünde gösterilmemesi sağlandı.
- 64512 - Web arayüzü doküman yönetiminde profil form tanımları yapılmış bir klasöre
    dosya eklemeye çalışıldığında oluşan timeout sorunu giderildi.
- 32678 - Web arayüzünde Uygulama Gezgini içerisindeki menüye eklenen eBA 6.
    versiyonunun açılmama hatası düzeltildi.
- 61552 - Doküman yönetiminde tablo görümündeyken lookup, listbox, daterange
    picker nesneleri boş olduğunda null veya [] şeklinde gelmesi sorunu giderildi.
- 60193 - Web arayüzünde, duyuru oluşturulurken e-posta gönder seçeneğinin
    çalışmama hatası giderildi.
- 64928 - Web arayüzünde image eklenen ve word wrap alanı aktif edilen
    datagrid'lerde satırlarda oluşan hiza bozulması sorunu giderildi.
- 67912 - Web arayüzünde 'Aksiyon Yönetimi' kanban içerisinde 'Removed' kısmına
    sürüklenen Card bilgilerinin statü renklerinin görünmeme sorunu düzeltildi.
- 66579 - Web arayüzünde RelatedDocuments nesnesine Excel dosyası yüklendiğinde,
    dosya içerisindeki time tipindeki verilerin Datagrid nesnesine aktarılması aşamasında
    oluşan zaman farkı sorunu giderildi.
- 67642 - Web arayüzü datagridlerde filtre alanlarında search işleminde oluşan sorun
    düzeltildi.
- 69132 - Web arayüzünde sadece PDF yüklenmesine izin verilen Related Documents
    nesnesine başka uzantılı dosyalar yüklendiğinde uyarı alınması ve uygulamanın
    hataya düşmemesi sağlandı.
- 71639 - Web arayüzünde form ekranında doküman numarası 0 olduğunda kaydet
    butonunun gizlenmesi sağlandı.
- 69980 - Web arayüzünde versiyonlaması kapalı ve süreci devam eden bir akışta,
    geliştirme arayüzünde bu sürecin flowunda onayda bekleyen nesne silinip yeniden
    deploy alındığında ve süreç web tarafından açılmak istenildiğinde çıkan mesajın "The
    specified Approver by guid id '76c331e9- 5469 - 8d38-8b9c-63524be0df28' could not
    be found because it is invalid or deleted." StartParameters endpointinde response
    içerisindeki message bilgisinde gönderilmesi sağlandı.
- 74707 - Web arayüzünde, RELATIONDOCUMENTID kolonunun Editing Enabled özelliği
    true ve OPENRELATIONDOCUMENT kolonunun Editable özelliği true olan ilişkili bir
    DataGrid'in bulunduğu bir formda akış bittikten sonra, kullanıcı İş Akış Yönetimi
    altında Oluşturduğum İşler içerisinden DataGrid'i açtığında, düzenle butonuyla modal
    formu açarsa buradaki veriler içerisinde düzenleme yapabilmesi hatası giderildi.
- 70908 - Web arayüzünde web notification mesajlarının ortam diline uygun olarak
    gelmeme hatası giderildi.


### 3.2. Geliştirme Arayüzü

- 69714 - Geliştirme arayüzünde flow özellikleri penceresi açık durumdayken flow
    kapatılıp yeniden açıldığında özellik görüntüleyici ekranındaki verilerin yüklenmeme
    sorunu giderildi.
- 68136 - Geliştirme arayüzünde görev yöneticisi ekranında proje listesinde görünüm
    bozukluğu hatası giderildi.
- 65870 - Geliştirme arayüzünde akış senkronize edici nesnesi kullanılarak oluşturulan
    proje tetiklenirken alınan hata giderildi.
- 66904 - Geliştirme arayüzünde, datagrid aksiyon tipindeyken ekle toolbar butonu
    gözükmeme hatası giderildi.
- 67908 - Geliştirme arayüzünde projeyi yayınlama işleminde oluşan Error occured in
    Sublayers.Builder.DeployProjectAsync hatası giderildi.
- 68528 - Geliştirme arayüzünde içe aktar yapılan projedeki related documents
    nesnesinde path bilgilerinin silinmesi ve datasource bilgilerinin silinme hataları
    giderildi.
- 67741 - Geliştirme arayüzünde, arşiv formlarında "proje ismi_form ismi_nesne adı"
    şeklinde sütunlar oluşma ve kolon üret alanına nesnelerin gelmeme hatası giderildi.
- 67228 - Geliştirme arayüzünde formda Datasource bağlantı tipi boş gelmesine
    rağmen formun çalışma hatası düzeltildi.
- 65869 - Geliştirme arayüzünde akış tetikleyici nesnesi kullanılarak oluşturulan projede
    UserId / UserName ile tetikleme yapılırken alınan hata giderildi.
- 68329 - Geliştirme arayüzünde, görev yöneticisinde çalışan projeler alanında yenile
    butonuna tıklandığında console hatası ve yenilenmeme hatası giderildi.
- 66867 - Geliştirme arayüzünde, Lookup nesnesinin Show On özelliğinin drawer ve
    popover seçenekleri seçiliyken, paging size panelinde ekleme ve silme işleminin
    nesneye yansımama hatası giderildi.
- 67456 - Geliştirme arayüzünde, form özelliklerinde Identity Format
    seçilememesi/oluşturulamama hatası giderildi.
- 66755 - Geliştirme arayüzünde proje yöneticisinde Aç,Sil,Yolu kopyala,Dışa
    aktar,Form indeksle butonlarına tıklanılmama hatası giderildi.
- 64875 - Geliştirme arayüzünde bağlantılar alanına eklenen boş gpt bağlantısında test
    butonuna tıklandığında oluşan hata giderildi.
- 64585 - Geliştirme arayüzünde proje açılırken oluşan klasör listelenme sorunu
    giderildi.
- 69932 - Geliştirme arayüzünde sürecin doküman numarasının 0 olarak kaydedilmesi
    ve farklı doküman numarası ile yeni request oluşturma sorunu giderildi.
- 65868 - Geliştirme arayüzünde atama nesnesiyle sabit departman atama işleminde
    alınan sorun giderildi.
- 65370 - Geliştirme arayüzünde formda herhangi bir nesneye tıklayıp değişiklik
    yapınca formun kitlenmesi ve Server tarafında kodda bir değişiklik yapınca Kaydetme
    işleminin gerçekleşmeme hatası düzeltildi.
- 64784 - Geliştirme arayüzünde, process archive oluşturulurken form alanları seçilip
    kaydedildikten sonra seçimlerin boş gözükme hatası giderildi.
- 24523 - Geliştirme arayüzünde, Collapse Nesnesi özellik görüntüleyici Appearance
    altındaki **tab position** özelliği hiçbir yere etki etmediği için kaldırılması doğrulandı.
- 63202 - Geliştirme arayüzünde içerisinde fazla veri bulunan Datagrid nesnesini form
    üzerinde Kaydet dediğimizde kaydetme süresinin uzama hatası düzeltildi.
- 65748 - Geliştirme arayüzünde formInstance ile atama yapılan ComboBox
    nesnelerinin web arayüzünde boş olarak gözükme hatası formInstance.Save().Result;
    kullanılarak giderildi.
- 66281 - Geliştirme arayüzünde formda Kural Yöneticisinde OnTextChanging ve
    OnValueChanging etkinliklerinin çalışmama hatası düzeltildi.
- 63730 - Geliştirme arayüzünde Görünüm Yöneticisinden yeni bir görünüme geçip
    oradaki TreeList nesnesinin Paging Settings özelliklerinde değişiklik yapıldığında,
    Önizleme ekranında sayfa sayılarının hata verme sorunu düzeltildi.
- 65806 - Geliştirme arayüzünde flow tarafında akış nesnelerinde açılan modallarda
    yapılan değişikliklerin kaydet tuşuna basmadan kaydedilme hatası giderildi.
- 65410 - Geliştirme arayüzünde form üzerinde Flow dosyasını silmek istediğimizde
    hata verme sorunu düzeltildi.
- 66669 - Geliştirme arayüzünde cs dosyasında ComboBox.Reload() işleminin, web
    arayüzünde Parameter count mismatch hatasına sebep olma sorunu giderildi.
- 66862 - Geliştirme arayüzünde, aksiyon formu açık kaynak modunda açıldığında
    formType : 6 bilgisi bulunuyorsa, projeyi build ettikten sonra formType : action
    şeklinde güncellenmesi sağlandı.
- 67310 - Geliştirme arayüzünde, datagrid kolonlarına check Unique Value özelliği aktif
    olduğunda update işleminde alınan hata giderildi.
- 62555 - Geliştirme arayüzünde, aksiyon formu oluşturulduğunda otomatik oluşan
    datasourceların numaralarının hatalı gelmesi düzeltildi.
- 66063 - Geliştirme arayüzünde Form tasarımlarında mevcut olan Section ve Column
    nesnelerine, TypeScprit tarafında erişemeyerek aksiyon alınamama hatası düzeltildi.
- 67049 - Geliştirme arayüzünde cs tarafında Lookup nesnesinin text ve value değerleri
    set edildiğinde, web arayüzünde text yerine value değerinin gözükmesi sorunu
    giderildi.
- 65774 - Geliştirme arayüzünde datasource sorgusunda sql parametresini düzenle
    ekranında Array tipinde seçimler yapılıp kaydedildiğinde Değer alanının boş gözükme
    hatası giderildi.
- 65710 - Geliştirme arayüzünde flow tarafında web notification alanına değişken
    nesnesinden verilen Türkçe karakterli mesajın IsHtml özelliği aktif edilerek web
    arayüzünde hatalı gözükmesi sorunu giderildi.
- 65993 - Geliştirme arayüzünde flow tarafında FastApprovalEnabled özelliğinin akış
    koduyla değiştirilebilmesi sağlandı. Position1.Events[0].FastApprovalEnabled = true;
- 63228 - Geliştirme arayüzünde formda Datagrid nesnesinde Columns kısmında
    Decimal tipinde NumberBox kolonu eklendiği zaman Precision özelliğinde yapılan
    değişikliğin Control kısmındaki Precision özelliğine yansımama hatası düzeltildi.
- 18776 - Geliştirme arayüzünde ortama farklı dil ile giriş yapıldığında dosya yolunun
    yanlış gözükme hatası giderildi.
- 65503 - Geliştirme arayüzünde flow tarafında documents özelliği içeren nesnelerde
    view bilgisi seçili olduğu halde view seçilmemiş mesajı verme hatası giderildi.
- 65705 - Geliştirme arayüzünde flow tarafında documents özelliği içeren nesnelerde
    documents seçimi yapıldığında view ve panel bilgilerinin otomatik doldurulması
    sağlandı.
- 61397 - Geliştirme arayüzünde, Lookup nesnesinin Show On özelliğinin drawer ve
    popover seçenekleri seçiliyken, paging size panelinde ekleme ve silme işleminin
    nesneye yansımama hatası giderildi.
- 64594 - ProcessLogs tablosuna kaydedilen hata mesajlarının stacktrace'i komple
    içermeme hatası giderildi.
- 62154 - GetProjectInfo isteğindeki deploymentId değerinin
    PROJECTCOREDEPLOYMENTS tablosundan gelmeme hatası giderildi.
- 69901 - Rule manager alanında nesne altında kural değerlerinin görülmemesi ve tarih
    alanında T harfi bulunması hataları düzeltildi.
- 67378 - Formda bulunan required alanlardan dolayı Document save işleminde hata
    düştüğü tespit edildi. Required alanlar kapatıldığında işlem başarılı oldu.
- 69883 - IDE -> Scheduler Service -> Rest Api Çağıran Aksiyon -> Rest sorgusu
    gelmeme hatasının giderilmesi kontrol edildi.
- 70364 - Proje içe aktarda build hatası kontrol edildi
- 69387 - Rule manager alanında onay nesnesinde eylemlerin gelmeme hatası
    düzeltildi.
- 70294 - Değer ve hedef alanlarına atanan değerlerin ters olması durumu düzeltildi.
- 70247 - UserMetadata nesnesinin, "Position, Department, Profession,
    CompanyCode, CompanyName" tipindeki verileri Form1ML tablosunda kullanıcı
    dilinin yanında system dilinde de eklenmesi sağlandı.
- 44434 - TreeView nesnesinde seçim yapıldığında satırın boyanmama hatası düzeltildi.
- 64137 - ACTIONS tablosu migration PRIORITY alanı eklendi.
- 69243 - Rule manager alanında formül ile değer atanmak istendiğinde fields alanına
    tıklanınca karşılaşılan hata giderildi.
- 69290 - Formlardaki aksiyonların çalışmama hatası düzeltildi.
- 67686 - Tablardaki datagridlere ekleme işlemi yapılmak istendiğinde loadda kalma
    hatası düzeltildi.
- 69523 - Open Selection form tipinde panel/modal/drawer olarak açılan formlardaki
    seçimlerin grid üzerine yansımama hatası giderildi. Checkboxların seçili gelmesi
    sağlandı.
- 69408 - Lookup nesnesinin datasource'a yaptığı çok fazla istek sonucunda formun
    kitlenme hatası düzeltildi.
- 66342 - İlgili projedeki datetimepicker nesnesinin ileri bi tarih seçildiğinde null
    ataması yapmama hatası kontrol edildi.
- 64535 - Datagrid nesnesi columnslarında datasourcedan üretilen kolonlarda object
    kolonlarının gelmesi doğrulandı.
- 65447 - Deploy sürecinde versiyon bilgisi eklendi. Web Otomasyon ile projelerin
    deploy süreci, projenin gönderilmesi, onaylanması ve reddedilmesinde yaşanılan hata
    giderildi.
- 69161 - Ide arayüzünde, Kural Yöneticisi alanında nesnelerin adı amacına uygun
    olarak düzenlendi ve Toolbox üzerindeki nesnelerin üzerine gelindiğinde açıklayıcı
    mesajların çıkması sağlandı.
- 64996 - Flow.cs tarafından yazarken her karakter için execute çalışması hatası
    düzeltildi.
- 69144 - Lokasyon select tipli kolonda verilerin gelmemesi kontrol edildi.
- 70301 - İlişkili datagridden açılan formun kaydet butonuna tıklayınca run isteği 500
    hatası vermemesi ve gride veri ekleyip akışı gönderebilmesi kontrol edildi.
- 69948 - Kural yöneticisi içinde date içeren kurallar bulunduğunda alınan deploy
    hatası değerlerin generate edilmesiyle düzeltildi.
- 65976 - DataGrid'e yapılan ekleme sonrası DataGrid'deki kayıt sayısı otomatik olarak
    güncellenmesi kontrol edildi.
- 67329 - IDE - Proje Yöneticisi - İçe Aktar - DM dizinlerin gelmesi sağlandı.
- 64088 - Database ortamında RelatedDocuments OCRDATA özelliği ve Datagrid
    CELLDATA kolonları olmasa dahi Web arayüzünden veri eklendiği takdirde bu
    kolonların Database ortamında oluşmama hatası düzeltildi.
- 66484 - Form da yer alan panellere form içerisindeki nesneler sürükle bırak
    yöntemiyle eklenememe sorunu giderildi.
- 72117 - Geliştirme arayüzünde Treeselect nesnesinde Run At Server açıkken verilerin
    gelmeme hatası düzeltildi.
- 72632 - Geliştirme arayüzünde service api LoginWithBasicAuthentication ve
    LoginWithAccessToken bağlantılarına source bilgisi verme zorunluluğu giderildi.
- 73310 - Web arayüzünde 'Scheduler' nesnesine bağlanmış Datasource'daki başlangıç ve bitiş
    tarihleri aynı olduğunda Scheduler nesnesinin Month görünümünde gösterilmeme hatası
    düzeltildi.

### 3.3. Android

- 61233 - Android ve ios cihazlarda webview görünmünde NumberBox nesnesinin
    azaltma ve artırma butonlarının gelmesi doğrulandı.
- 61263 - Android ve iOS cihazların mobil arayüzünde, WebView görünümündeki Statik
    DataGrid nesnesinde ComboBox kolonundaki çarpı butonunun yazının üstüne gelme
    hatası düzeltildi.
- 67379 - Android cihazda webview görünümünde related documents nesnesinde
    dosya ekleyememe hatası düzeltildi.
- 69150 - Android cihazların mobil arayüzünde, Tabs nesnesi içinde yer alan Mirror
    nesnelerinde düzenleme yapıldı.
- 66094 - Android cihazların mobil arayüzünde, açılan süreçlerde Tarihçe vb. alanların
    açılmama hatası düzeltildi.
- 55136 - Android cihazların mobil arayüzünde, uygulama arka plana alındığında
    bildirim gelmeme hatası düzeltildi.
- 60215 - Android cihazların mobil arayüzünde, WebView görünümündeki ComboBox
    nesnesinde Search özelliğinin çalışmama hatası düzeltildi.
- 61109 - Android cihazların mobil arayüzünde, WebView görünümündeki TimePicker
    nesnesinde seçim yapıldıktan sonra seçilen veriden önceki verilere erişilememe
    hatası düzeltildi.
- 65897 - Android cihazların mobil arayüzünde, İş Akış Yönetimi menüsünde Taslaklar
    sekmesinde yer alan süreçlerin açılmama hatası düzeltildi.
- 72423 - Android ve ios cihazda tarayıcıdan açılan formdaki datagrid object tiplerinde
    seçim yapılıp değiştirilebilmesi kontrol edildi.
- 71879 - Web arayüzünde statik datagrid select kolonunda ilden seçilene göre ilçeler
    listelenirken edit durumunda verilerin kolona gelmeme sorunu giderildi.

### 3.4. IOS

- 66488 - iOS cihazların mobil arayüzünde, İş Akış Yönetimi menüsündeki Bilgi
    alanından açılan formların görüntülenmeme hatası düzeltildi.
- 61233 - Android ve ios cihazlarda webview görünmünde NumberBox nesnesinin
    azaltma ve artırma butonlarının gelmesi doğrulandı.
- 61263 - Android ve iOS cihazların mobil arayüzünde, WebView görünümündeki Statik
    DataGrid nesnesinde ComboBox kolonundaki çarpı butonunun yazının üstüne gelme
    hatası düzeltildi.
- 67376 - iOS cihazların mobil arayüzünde, Native+ görünümündeki ComboBox
    değerine göre nesnelerin ClientVisible özelliğinin çalışmama hatası düzeltildi.
- 55136 - iOS cihazların mobil arayüzünde, uygulama arka plana alındığında bildirim
    gelmeme hatası düzeltildi.
- 56298 - iOS cihazların mobil arayüzünde, WebView görünümündeki Statik DataGrid
    nesnesinde satırların hizasının bozulma hatası düzeltildi.
- 60215 - iOS cihazların mobil arayüzünde, WebView görünümündeki ComboBox
    nesnesinde Search özelliğinin çalışmama hatası düzeltildi.
- 61109 - iOS cihazların mobil arayüzünde, WebView görünümündeki TimePicker
    nesnesinde seçim yapıldıktan sonra seçilen veriden önceki verilere erişilememe
    hatası düzeltildi.
- 65897 - iOS cihazların mobil arayüzünde, İş Akış Yönetimi menüsünde Taslaklar
    sekmesinde yer alan süreçlerin açılmama hatası düzeltildi.
- 66470 - IDE arayüzünde, nesne gezgininden bir nesne silindiğinde farklı bir nesneyi
    silme ve yeni bir nesne eklendikten sonra silinen nesnelerin geri gelme hataları
    düzeltildi.
- 61168 - Web arayüzünde, dinamik datagrid paging işlemi sonrası hareket sorunu
    hatası giderildi.
- 67706 - Geliştirme arayüzünde, dosya ekle butonunun pasif gelme hatası giderildi.
- 69013 - Geliştirme arayüzünde akış yöneticisinde UpgradePackageVersion
    endpointinde latest yerine seçili Package Version bilgisinin gönderilmeme hatası
    giderildi.
- 69120 - Rule manager alanında birden fazla koşul eklendiğinde evet evet şeklinde
    yazıların bulunması ve hayır seçeneğinin çıkmaması düzeltildi.
- 69960 - IDE arayüzünde forma Lookup nesnesi bırakılıp Rest API sorgusu
    bağlandıktan sonra Web arayüzünde nesne üzerindeki bara tıklanarak sorgu
    içeriğinin görüntülenmesi ve seçim yapılması sağlandı.

#### 3.5. Core Services

```
65387 – CSP Outlook Addon'da yüksek çözünürlükte CSP’nin ekranı tam olarak
doldurulamama hatası giderildi.
65799 – CSP Outlook Addon'da Doküman Yönetimi modülünde dosya tiplerinin
açılmama hatası giderildi.
65333 – CSP Outlook Addon'da, doküman yönetimi dosya tiplerinin açılmama hatası
giderildi.
66932 – CSP Outlook Addon'da Synergy oturumu kapatıldığında pencere içerisindeki
panelde oturumun açık görünmesi hatası giderildi.
69033 – Configuration Manager’da Design sekmesinde template değişikliği
kaydedilirken açılan pencerede template’e bağlı tüm config dosyalarının seçimi için
kullanılan Tümünü Seç fonksiyonunda alınan hata giderildi.
70011 – Configuration Management uygulamasında Runtime sekmesinde tenantlara
ait configuration dosyasında yapılan parametre değeri değişikliğinin kaydedilmesi
sırasında oluşan hata giderildi.
70039 – Configuration Management uygulamasında Design sekmesinde cluster
template'inin rename işlemine kontrol eklenerek aynı isimle dosya oluşturulması
engellendi.
70065 – Configuration Management uygulamasında Design sekmesi altında yer alan
cluster template dosyalarında mükerrer isim kullanıldığında alınan hata giderildi.
```
70243 – Configuration Manager uygulamasında Runtime sekmesinde bir draft
üzerinden publish işlemi yapılırken oluşan hata giderildi.
```
## 4. Breaking Changes

1. Projeler **tekrar** yayınlanmalıdır.

```

<font size="5"><a href="https://portal.synergynow.io/#/_redirect/CLCOmqOdkQgmBUMWeOpfRs"  target="_blank"><svg fill="currentColor" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" viewBox="0 0 40 40" style={{verticalAlign: "middle"}}><g><path d="m35.8 8.5q0.6 0.6 1 1.7t0.5 1.9v25.8q0 0.8-0.6 1.5t-1.6 0.6h-30q-0.9 0-1.5-0.6t-0.6-1.5v-35.8q0-0.8 0.6-1.5t1.5-0.6h20q0.9 0 2 0.4t1.7 1.1z m-9.9-5.5v8.4h8.4q-0.3-0.6-0.5-0.9l-7-7q-0.3-0.2-0.9-0.5z m8.5 34.1v-22.8h-9.3q-0.9 0-1.5-0.6t-0.6-1.6v-9.2h-17.1v34.2h28.5z m-11.4-13.2q0.7 0.6 1.8 1.3 1.3-0.2 2.6-0.2 3.3 0 4 1.1 0.4 0.5 0 1.2 0 0 0 0l0 0v0.1q-0.2 0.8-1.6 0.8-1.1 0-2.6-0.4t-2.9-1.2q-4.9 0.5-8.7 1.8-3.4 5.9-5.4 5.9-0.4 0-0.7-0.2l-0.5-0.2q0-0.1-0.1-0.2-0.3-0.2-0.2-0.8 0.2-0.8 1.3-2t2.9-2.1q0.3-0.2 0.5 0.1 0.1 0 0.1 0.1 1.1-1.9 2.4-4.4 1.5-3.1 2.3-5.9-0.5-1.8-0.7-3.5t0.2-2.9q0.2-0.9 0.9-0.9h0.5q0.5 0 0.8 0.4 0.4 0.4 0.2 1.5-0.1 0.1-0.1 0.2 0 0 0 0.1v0.7q0 2.8-0.3 4.3 1.2 3.7 3.3 5.3z m-12.9 9.2q1.2-0.6 3.1-3.5-1.2 0.8-2 1.8t-1.1 1.7z m8.9-20.6q-0.4 1-0.1 3 0.1-0.2 0.2-1 0-0.1 0.1-0.9 0.1-0.1 0.1-0.2 0-0.1 0-0.1t0 0 0 0q0-0.5-0.3-0.8 0 0 0 0v0z m-2.8 14.8q3-1.2 6.4-1.8-0.1 0-0.3-0.2t-0.4-0.3q-1.7-1.5-2.8-4-0.6 2-1.9 4.4-0.7 1.3-1 1.9z m14.4-0.4q-0.5-0.5-3.1-0.5 1.7 0.6 2.8 0.6 0.3 0 0.4 0 0 0-0.1-0.1z"></path></g></svg>PDF Download</a></font>


