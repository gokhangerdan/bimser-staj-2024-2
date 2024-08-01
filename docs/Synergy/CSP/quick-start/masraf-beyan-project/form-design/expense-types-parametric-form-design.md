# Masraf  Tipleri  Parametrik  Formu  Tasarımı
Masraf  tiplerinin  dinamik  olarak  eklenip  düzenlenebileceği  Parametrik  Formda  bulunan  alanlar  aşağıdaki  gibidir;

|||
|--- |--- |
|Masraf  Tipleri  Tablosu|Masraf  Tiplerinin  eklenip, düzenlenebileceği  tablodur. Id ve  Masraf Tipi olarak 2 kolondan  oluşur|


Formu  oluşturmak  için  çözüm  gezgininde Forms klasörü  üzerinde  sağ  tıklanarak CSP App Form seçildikten  sonra “MasrafTipleri” şeklinde forma dosya  adı  girilir.
![masraf tipleri dosya adi](https://docsbimser.blob.core.windows.net/imagecontainer/masraf%20tipleri%20dosya%20adi-43554744-ebfd-41fe-9bfc-165c2fddf1a2.png)

Formun caption alanı  Masraf  Tipleri  olarak  düzenlenir  ve **Form Type** alanından **Parametreli Form** seçilir.
![parametreli form](https://docsbimser.blob.core.windows.net/imagecontainer/parametreli%20form-413df5fc-12fd-4b58-ba68-30b6427bb655.png)

Masraf  Tiplerinin  ekleneceği  Masraf  Tipleri  Tablosu  için **DataGrid** nesnesi form üzerine  sürüklenip  bırakılır. Tabloya  verilerin  eklenebilmesi, düzenlenebilmesi  ve  silinebilmesi  için **Editing Setttings** sekmesinden **Show Add Command**, **Show Delete Command** ve **Show Delete Command** özellikleri  aktif  edilir.
![masraf tipleri tablosu duzenleme](https://docsbimser.blob.core.windows.net/imagecontainer/masraf%20tipleri%20tablosu%20editing-13a32439-a46e-479b-9963-32a6cac066be.png)

Masraf  Tipleri  Tablosunda  bulunması  gereken  kolonların  oluşturulması  için **Appearance** sekmesi  altından **Columns** özelliklerine  gidilir.
![datagrid columns](https://docsbimser.blob.core.windows.net/imagecontainer/datagrid%20columns-028b93f6-050c-4d61-b02b-f1061eee72fe.png)

DataGridin  kolonlarında  birincil  anahtar  seçimi  zorunlu  olduğu  için  öncelikle number tipinde  bir ID kolonu  oluşturulur. Kolonun  tabloda  görünmesi  istenen  ismi  için **Caption** alanı **“ID"** olarak  girilir.

**Name** ve **Field Name** alanlarında  ise  DataGrid’in  ait  olduğu  veritabanı  tablosunda  halihazırda  bir ID kolonu  bulunduğu  için  farklı  bir  isim  alanı  olarak “DGID” girilebilir.

Bu kolonun  Birincil  anahtar  olarak  seçilebilmesi  için **Is Primary Key** özelliğinin  aktif  edilmesi  gerekmektedir.

Kolonun  tablodaki  görünürlüğünü  kapatmak  için **Visible** özelliği  pasif hale getirilir. Kullanıcı,  bu  alanı  göremeyeceği  için  dolduramayacaktır  dolayısıyla ID değerinin  otomatik  olarak  artabilmesi  için **Auto Increment** özelliği  aktif  edilir.
![datagrid columns dgid](https://docsbimser.blob.core.windows.net/imagecontainer/datagrid%20columns%20dgid%20-e82146ea-0d79-4d63-ba3b-215e67924310.png)

Kullanıcının  masraf  tiplerini  tanımlayabilmesi  için **Text** tipinde  bir “Masraf Tipi” kolonu  oluşturulur.
![datagrid columns masraftipi](https://docsbimser.blob.core.windows.net/imagecontainer/datagrid%20columns%20masraftipi-b2e1bc02-e620-4e8f-a5e7-bf8acbc83ff1.png)

Uygulama  sırasında  Parametreli  Formlarda  bulunan  Kaydet  butonuna  tıklanıldığında  kullanıcıya  bir  bildirim  verilmesi  için  Görünüm  sekmesi  altından **Kural Yöneticisi**’ne  tıklanır. Sağ  tarafta  açılan Kural Yöneticisi  panelinden Yeni Kural eklenir.

Yapılacak işlem, formu  kaydetme  işleminden  sonra  gerçekleşeceği  için **Uygulama  Zamanı** olarak **MasrafTipleri** formu  seçilir. Daha sonra  bu  işlem  istemci  tarafında  gerçekleşeceği  için **client** seçilir  ve  uyarının  Kaydet  butonuna  tıklanıldıktan  sonra  verilebilmesi  için **onAfterSave** seçilir.

Kural için “Form Başarıyla  Kaydedildi!” şeklinde  bir  eylem  adı  tanımlanır. Kaydetme  işleminin  başarılı  bir  şekilde  gerçekleştiğini  gösteren  uyarı  mesajının  arka plan renginin  yeşil  olması  için **Uyarı tipi** olarak **Success** seçilir.
![kural yoneticisi form kaydedildi](https://docsbimser.blob.core.windows.net/imagecontainer/kural%20yoneticisi%20form%20kaydedildi-cc76dd48-b021-4f1e-96e5-9e11823ee4a5.png)

Parametreli  Formdaki  tabloya  veri  eklenebilmesi  için  projenin  yayınlanması  gerekmektedir.
![yayinlama masraf tipleri](https://docsbimser.blob.core.windows.net/imagecontainer/masraf%20tipleri%20yay%C4%B1nlama-384ae80b-16b0-4ff3-9cbc-627c8f2601bf.png)

Proje  yayınlandıktan  sonra Web Arayüzünde  sağ  üstteki  yönetim  araçları  ikonundan  uygulama  gezginine  gidilir. Sol tarafta  açılan  panelde  ekle  ikonuna  tıklanır. Açılan  menü  ekleme  penceresinden “Masraf Tipi Parametrik  Formu” başlıklı  menünün **Düğüm  İşlem  Türü** için **Bir Form Doldur** seçeneği  seçilir.

**Projeler** alanında  MasrafBeyanSureci , **Form** alanında  ise  MasrafTipleri  formu  seçildikten  sonra **Profil** sekmesinden  daha  önce  oluşturulmuş  ve  bu  uygulamanın  menüsünde  görünmesi  istenen  bir  profil  seçilerek  menü  ekleme  işlemi  tamamlanır.
![parametriği uygulama gezginine ekleme](https://docsbimser.blob.core.windows.net/imagecontainer/Parametri%C4%9Fi%20Uygulama%20gezginine%20ekleme-bc4b2555-b6ca-4fbd-8c6f-b91cb67afcdf.png)

Web Arayüzündeki sol üst  köşedeki  dokuz  noktalı  simgeye  tıklanır. Açılan  panelin alt tarafında  bulunan  tüm  projelere  gidilerek  uygulama  başlatılır.

Form  açıldıktan  sonra  Masraf  Tipleri  Tablosunun  sağ  üst  köşesinde  bulunan **+** işaretine  tıklanarak  masraf  tipleri  girilir  ve  ardından form  kaydedilir.
![parametrik kaydedildi](https://docsbimser.blob.core.windows.net/imagecontainer/parametrik%20kaydedildi-1f629d42-d93c-4b69-bd96-337e7a166a52.png)

Kullanıcın  masraf  tipleri  için  kaydedilen  verileri  Masraf  Detay  Formundaki  ComboBox  alanından  seçebilmesi  için  öncelikle  tablodaki  verileri  getiren  sorgunun  yazılması  gerekmektedir. Bunun için  Çözüm  Gezginindeki **DataSource** klasörü  üzerinde  sağ  tıklanır  ve **Yeni Öğe** seçilir. Bu projeye  ait  tablolar SQL Server üzerinde  tutulduğu  için  açılan  pencerede **MSSQL Query** seçilir  ve  sorgu  ismi “MasrafTipleriniGetir” olarak  verilebilir.
![masraftiplerinigetir sorgu](https://docsbimser.blob.core.windows.net/imagecontainer/masraftiplerinigetir-cce48eff-9b93-4fdd-84b0-071dbaffec10.png)

Bağlantı özelliğinden  sistemde  daha  önceden  tanımlanmış  bir Database bağlantısı  seçilir  ve  sorguya  ait  tüm  alanların  listelenebilmesi  için **Çalıştırma Tipi** olarak da **ExecuteDataAdapter** seçilir.

Form üzerindeki  DataGridin  satırlarına  ulaşılabilmesi  için  verilerin  çekileceği  tablonun  sorgudaki  formatı **“E_ProjeAdi_FormAdi_DataGridNesneAdi”** şeklinde  olmalıdır.

Masraf  Detay  Formundaki  ComboBox  alanında value olarak ID değerinin  saklanabilir  bunun  için DGID alanı, görünen  değer  için  ise  MasrafTipi  alanı  çekilmelidir.

Id alanı  nümerik  bir  alan  olduğu  için DataGrid1 tablosundan  çekilmelidir.
 Masraf Tipi alanı  ise Text alanıdır  ve Text alanlar  Çok Dilli (Multi Language) bir  yapıda  bulunduğu  için DataGrid1ML tablosundan  getirilmelidir. Datagrid1ML tablosundaki  ParentID  alanı DataGrid1 tablosunun ID alanı  ile  ilişkili  olduğu  için  bu  tablolar  arasında  bir join işlemi  uygulanır.
 ![sorgucikti](https://docsbimser.blob.core.windows.net/imagecontainer/sorgu%20cikti-ac71f798-94dd-48eb-9147-6ff80838e82a.png)

Kullanıcının  [**Masraf  Detay  Formundaki**](expense-detail-form-design.md)  Masraf Tipi alanından  seçebileceği  veriler, bu  parametreli form sayesinde  artık  hazır hale gelmiştir.
