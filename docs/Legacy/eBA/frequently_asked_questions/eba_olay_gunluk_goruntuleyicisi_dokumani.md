# eBA Loglarını Nereden Görebilirim?

### 1. Olay Günlük Görüntüleyicisi

eBA içerisinde alt yapıya ait servislerin çalışması esnasında yapılan işlemler, kullanıcının onay
verirken hata oluşursa hata detayları, giriş yapmaya çalışan kullanıcı ve IP bilgisi, Doküman Yönetimi
bölümü içerisinde yapılan değişikliklerin (kütüphane/klasör özelliğinin değişimi vb), İnsan Kaynakları
Transfer sonucuna ait kayıtlar, vekâlet işlemleri kayıtları (vekâlet verme, silme), eBA’nın diğer
modüllerine ait günlükler gibi birçok özelliğin kayıtları Olay Günlük Görüntüleyici içerisinde
listelenmektedir.
Bu bölümde gösterilen kayıtlar okunur durumunda olup, içeriğinde değişiklik yapılamamaktadır.
Olay Günlük Görüntüleyicisi içerisinde gösterilen kayıtlar ve varsa kayda dair ek/ekler eBA’ya ait veri
tabanında saklanmaktadır.
Olay Günlük Görüntüleyici panelinde, görüntülenecek uygulama adı, uygulama kaydının ay
bazında dönemi, tarih aralığı, olay tipi seçim alanları bulunmaktadır. Bu alanlarda yapılan seçimlere göre
istenilen olayın belli bir zaman aralığındaki kayıtları görüntülenebilir.
Seçim alanlarının yanı sıra, kullanıcı, metin ve detaylar alanları kullanılarak listelenen kayıtlar
içinde filtreleme yapılabilir, Azalan işaret kutusu seçimine göre de günlük kayıtları azalan veya artan
şekilde listelenebilmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfa9d0229-d11f-4682-a040-60659065a9b4)

Filtreleme işlemi sonucunda gelen kayıtlar bir yandaki panelde listelenir. Bu panelde kayıt türü,
kayıt tarihi, kaydın oluştuğu kullanıcı (bazı uygulama seçimlerinde IP adresi) ve oluşan kayıtla ilgili kısa bir
açıklama sırasıyla ilgili kolonlarda gösterilmektedir.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-uploadfd37b5cc-9328-402f-b44a-64480446679b)

Alanda listelenen bir günlük kaydına tıklanıldığında ise o kaydın detay günlüğü
görüntülenmektedir.


![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload10cc0f16-156b-4255-8cb7-98cbfacc2074)

Uygulama adı alanında listelenen ve daha sonradan açılabilen kayıtlar aşağıdaki gibidir.
1) Application Service: eBA Application Service içinde yapılan alt yapı işlemlerinin tutulduğu günlüktür.
2) Licensing: eBA lisanslama ile ilgili olan kayıtların tutulduğu günlüktür.
3) Schedule Service: eBA Schedule Service içinde yapılan alt yapı işlemlerinin tutulduğu günlüktür.
4) Schedule Server: eBA Configuration Editor içinde Schedules Tasks alanına eklenen ögelerin tetiklenmesi
ile ilgili kayıtların tutulduğu günlüktür.
5) Capture Service: eBA Capture Service içinde yapılan capture alt yapı işlemlerinin tutulduğu günlüktür.
6) DM Index Service: eBA DM Index Service içinde yapılan alt yapı işlemlerinin tutulduğu günlüktür.
İndekslenen dosyalar, indeksleme esnasında hata alınan dosyalar gibi kayıtlar bulunur.
7) Logging Service: eBA Logging Service içinde alt yapı işlemlerinin yaptığı işlemlerinin tutulduğu günlüktür.
8) DM Service: eBA DM Service içinde alt yapının doküman yönetimi içerisinde yaptığı işlemlerin kaydının
tutulduğu günlüktür.
9) Workflow Service: eBA Workflow Service içinde bir süreçte işlem yapıldığında, sürecin alt yapıdaki yaptığı
her adımın kaydının tutulduğu günlüktür.
10) Compile Service: eBA Compile Service içinde, Workflow Studio’da bir proje derlendiğinde derleme
işleminin alt yapı kaydını ve kim tarafından istek yapıldığının kaydını tutan günlüktür.
11) Document Management Log: Doküman Yönetimi’nde bir kütüphanede ve kütüphane içerisindeki
klasörde özellik/yetki değişikliği yapıldığında bunun kaydının tutulduğu günlüktür. Günlüğün gözükmesi
için kütüphane seçilip özellikler içerisinde Yönetim bölümü altındaki Tarihçe alanında Tümü seçeneği
seçilmelidir. Bu seçimle ayrıca kütüphane içindeki dosyaları görüntüleyen, indiren gibi bilgiler de
kütüphanenin kendi tarihçesinde kayıt altına alınır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/auto-upload58df6f74-5a0c-4d3a-a60a-da31187d7747)

12) Web User Interface: Kullanıcının web ara yüzünde aldığı bütün hataların kaydının tutulduğu günlüktür.
Günlük kayıtlarında ayrıca hatayı alan kullanıcı ve kullanıcının IP bilgisi de tutulmaktadır.
13) Compiler: Workflow Studio içesinde proje derlenirken, bir önceki başarılı proje derlemesinin yedeğinin
tutulduğu günlüktür.
14) eBA Scheduler: System Manager’da Schedules Tasks içine eklenen ögelerle ile ilgili süreç
başlatma/devam ettirme kayıtlarının tutulduğu günlüktür.
15) Workflow Schedules: eBA Workflow Schedule içinde işlenen schedule oturumlarının tutulduğu
günlüktür.
16) eBA Form Log: Formun OnLoad ve Save aşamalarında form üzerindeki verilerin kayıt altına alındığı
günlüktür. eBA Configuration Editor’de Advanced sekmesindeki Web kırımına FormDataLoggingEnable
anahtarı eklenip değer olarak true atanarak aktif hale getirilir.
17) Authorization Changes: System Manager’da Authorization Manager’da yeni eklenip/silindiğinde kayıt
altına alındığı günlüktür.
18) Delegation Log: Kullanıcının vekâlet verme/silme işlemlerinin kayıt altına alındığı günlüktür.
19) eBA Process Management Log: Web ara yüzünde süreç istek yönetimi bölümünde yapılan işlemleri kayıt
altına alındığı günlüktür.
20) HR Changes: System Manager’da organizasyon yapısında değişiklik yapıldığında, yapılan değişikliklerin
tutulduğu günlüktür.
21) Digital Signature: Elektronik imza aktifse, elektronik imza işlemlerine ait kayıtların tutulduğu günlüktür.
22) System Cleaner: System Cleaner uygulaması çalıştırıldığında oluşan kayıtların tutulduğu günlüktür.
23) eBAMailIntegration: eBA Mail Integration System (MIS) modülüyle ilgili kayıtları tutulduğu günlüktür.
24) Web Login Attempts: Web ara yüzünde yapılan giriş isteklerinin ve IP bilgisinin tutulduğu günlüktür. eBA
Configuration Editor’de Advanced sekmesindeki Security kırımına WebLoginLogEnable anahtarı eklenip
değer olarak true atanarak aktif hale getirilir.
25) Query String Login: Query String ile üretilen linklerin oluşturulma ve erişim yapıldığı tarih bilgilerinin
tutulduğu günlüktür.
26) Push Notification: eBA mobil uygulama üzerinden gönderilen bildirimlerin kayıtlarının tutulduğu
günlüktür. Mobil uygulamada bildirimler aktif olmalıdır.
27) Archive Time Stamp: Doküman yönetiminde belge seçilip arşiv zaman damgasına tıklanıldığında yapılan
işlemin kayıtlarının tutulduğu günlüktür.
28) Flow Manager Log: System Manager’da Flow Manager bölümünde süreç geri alınması işleminin
tutulduğu günlüktür.
29) DM Service Details: Detaylı DM Servis loglarının tutulduğu günlüktür. Sadece Bimser tarafından, ihtiyaç
duyulursa açılmaktadır.
30) DM Service SQL Execution: DM Servisinin çalıştırdığı SQL sorguları ve detaylarının tutulduğu günlüktür.
Sadece Bimser tarafından, ihtiyaç duyulursa açılmaktadır.
31) Workflow Service SQL Execution: Web ara yüzünde süreçle ilgili işlem yapıldığınde (süreç
başlatma/devam ettirme vb) workflow servisinin çalıştırdığı sql sorguları ve detaylarının tutulduğu
günlüktür. Sadece Bimser tarafından, ihtiyaç duyulursa açılmaktadır.
32) EBA.NET SQL Execution: eBA altyapısının çalıştırdığı sql sorgularının ve detaylarının tutulduğu günlüktür.
Sadece Bimser tarafından, ihtiyaç duyulursa açılmaktadır.


### 2. Özel Kayıt Günlüğü Tasarlanması

Sistemin tuttuğu kayıtlar haricinde, proje içerisinde eBALogAPIHelper kullanılarak, proje yapılan bir
işleme dair özelleştirilmiş kayıt tutulabilir. Form üzerinde herhangi bir olayda veya buton nesnesi
içerisinde kullanılabilmektedir. Aynı zamanda akış içerisinde fonksiyonda da kullanılabilmektedir. Bu
sayede akışta veya formda yapılan bir işlemin takibi de özelleştirilmiş kayıt günlüğünden kontrol
edilebilmektedir.
Örnek kullanım:



	%SystemPath%\Common\eBALogAPIHelper.dll //Proje referansına eBALogAPIHelper eklenmelidir.
	using eBALogAPIHelper.Helper; //Kayıtın tutulacağı akışa veya forma using eklenmelidir.
	eBALogAPI logApi = new eBALogAPI("SatınAlmaTelep", "PRODUCTION");
	//Proje ismi, eBA INSTANCE İsmi
	public void WriteLog(string caption, string description, Exception ex = null) //Kaydı ekleyecek metot
	{
	 logApi.AddLogAsync(caption, description, ex == null ?
	eBALogType.None : eBALogType.Error,LogonUser, ex);
	}


	public void btnLog_OnClick(Object sender, EventArgs e)
	{
	 WriteLog("SatınAlmaTelep"+" -
	Süreç No: "+id, "Basılan Buton: btnLog\n Tarih: "+DateTime.Now+"\n İşlemi Yapan: "+LogonUser , null);
	 //WriteLog("\n SatınAlmaTelep
	"+"\nSüreç No: "+id, "\nBasılan Buton: btnLog\nTarih: "+DateTime.Now+"\nİşlemi Yapan: "+LogonUser+"
	\nView: "+CurrentView , null);
	}