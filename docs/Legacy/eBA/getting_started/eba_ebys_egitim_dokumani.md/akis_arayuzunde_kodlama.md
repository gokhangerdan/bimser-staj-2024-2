---
title: 4. Akış Arayüzünde Kodlama
sidebar_position: 4
---

# 4. Akış Arayüzünde Kodlama 

Akış arayüzünde kodlama editörünü akış üzerine sağ tıklayıp View Server Code’ı  seçerek açabiliriz. Ayrıca akış ve nesnelerin Kod Gezginindeki olaylarına çift tıklayarak da ilgili olayın koduna erişebiliriz (Şekil 2).  

![](https://docsbimser.blob.core.windows.net/imagecontainer/s5-0352b146-1bae-49ef-b508-9344dad492f6.png)

Bu bölümde akış ve akış nesnelerinin özellik, metot ve olayları örneklerle açıklanmıştır. 
Akış, “eBAFlowScrAdp.BaseFlowCode” sınıfındandır.


## 4.1. Flow 

###  4.1.1. Özellikler 

•	CurrentEventFormId  

Tanım: Akışta son create edilen event formun id bilgisidir. 
Tipi: System.Int32 
Deklarasyon: public int CurrentEventFormId { get; } 

•	CurrentReason 

Tanım: Herhangi bir aksiyon sırasında girilen neden Tanımlarından en son girilen   neden bilgisidir. 
Tipi: System.String 
Deklarasyon: public string CurrentReason { get; } 

•	ebaflow 

Tanım: Akışın o anki değerlerini tutan özellik
Tipi: eBAFlowScrAdp.BaseFlowCode
Deklarasyon: public eBAFlowScrAdp.BaseFlowCode ebaflow { get; }

•	HideFlowStarter 
Tanım: Akışı başlatanı akış tarihçesinde gösterme ve gizleme için kullanılır. True olarak atandığında akış tarihçesinde akışı başlatan kullanıcı bilgisi * karakteri ile gizlenerek gösterilmektedir. False olarak atandığında kullanıcı bilgisi kısmında başlatanın adı,soyadı yazar. 
Tipi: System. Boolean 
Deklarasyon: public bool HideFlowStarter { set; get; } 

•	HistoryCounter 

Tanım: İşlem yapılan süreç için o ana kadar başlatılan süreç sayısı bilgisidir. 
Tipi: System.Int32 
Deklarasyon: public int HistoryCounter { get; }  




•	id 

Tanım: Başlatılan sürecin süreç numarasıdır.Başlatılan her süreç için sistem tarafından yeni bir numara atanır.  
Tipi: System.Int32 
Deklarasyon: public int id { get; } 

•	IsTest 

Tanım: Projenin hangi modda çalıştığı bilgisidir. IsTest true ise test modundadır, false ise gerçek moddadır. 
Tipi: System. Boolean 
Deklarasyon: public bool IsTest { get; } 

•	LogonDelegated 

Tanım: eBA’da delegation yetkisi olan kullanıcı başka bir kullanıcının yerine gereçerek işlem yapabilir. LogonDelegated özelliği ile kullanıcının kendi kimliğiyle veya başka bir kullanıcının yerine geçerek işlem yaptığı tespit edilebilir. 
Tipi: System. Boolean 
Deklarasyon: public bool LogonDelegated { get; }  

•	LogonDelegatedUser 

Tanım: Başka bir kullanıcının yerine geçerek işlem yapan kullanıcının kullanıcı id (sicil no)  bilgisidir. 
Tipi:  System.String 
Deklarasyon:  public string LogonDelegatedUser { get; }  

•	LogonDelegationPosition 

Tanım: Başka bir kullanıcının yerine geçerek işlem yapan kullanıcının pozisyon id  bilgisidir. 
Tipi: System.String 
Deklarasyon: public string LogonDelegationPosition { get; } 

•	LogonPosition 

Tanım: Sisteme giriş yapmış olan kullanıcının pozisyon id bilgisidir. Bu id bilgisiyle süreçte işlem yapan kullanıcı tesbit edilerek kullanıcıya özel senaryolar uygulanabilir. 
Tipi: System.String 
Deklarasyon: public string LogonPosition { get; }  

•	LogonUser 

Tanım: Sisteme giriş yapmış olan kullanıcının kullanıcı id (sicil no)  bilgisidir 
Tipi: System.String 
Deklarasyon: public string LogonUser { get; } 

•	LogonUserLanguage 

Tanım: Sisteme giriş yapmış olan kullanıcının,giriş yaparken seçtiği dil bilgisidir. 
Tipi: System.String 
Deklarasyon: public string LogonUserLanguage { get; } 

•	MultilanguageEnabled 

Tanım: Sürecin multilanguage özelliğinin aktif olup olmadığı bilgisidir. 
Tipi: System. Boolean 
Deklarasyon: public virtual bool MultilanguageEnabled { get; } 

•	Process 

Tanım: Süreç isim bilgisidir.  
Tipi: System.String 
Deklarasyon: public string Process { get; } 

•	ProcessId 

Tanım: Başlatılan sürecin süreç numarasını belirtir. 
Tipi: System.Int32 
Deklarasyon: public int ProcessId { get; }  

•	ProcessStatus 

Tanım: Akışın durum bilgisini belirtir. 
Tipi: System.Int32 
Deklarasyon: public int ProcessStatus { get; } 

Önemli Not Akış durumu varsayılan değeri 1 (başlat)’dir. Bu değerin değişmesi için, akış tasarlanırken, akışın hangi adımda hangi durumda olması isteniyor ise, o adımlarda akış durdurucu nesnesi kullanılmalı ve ilgili durum atanmalıdır.  ProcessStatus özelliğinden dönen değerin, sözel olarak ne anlama geldiğini kontrol etmek ve belirlemek için 
1.	Akış formuna sağ tıklayın. 
2.	Özellikleri seçip durumlar tabına tıklayın. Bu kısımdan durumları kontrol edebilir ve özelleştirebilirsiniz. 

•	Project 

Tanım: Projenin isim bilgisini belirtir. 
Tipi: System.String 
Deklarasyon: public string Project { get; } 

•	ProjectVersion 

Tanım: Projenin versiyon bilgisini belirtir. 
Tipi: System.Int32 
Deklarasyon: public int ProjectVersion { get; } 

Önemli Not Projede yapılan her değişiklik, derlendikten sonra, proje için yeni bir versiyon numarası verilir. eBA projesinde, sadece akışlar versiyonlu olarak çalışır. 
Formlar ise son derlendiği şekli ile çalışır.  

•	SystemInstanceName 

Tanım: Üzerinde çalışılan sistemin instance bilgisini (TEST,PRODUCTION, vs..) belirtir. Tipi: System.String 
Deklarasyon: public string SystemInstanceName { get; }  

•	UserId 

Tanım: Süreç üzerinde o an işlem yapan kullanıcının id (sicil no) bilgisini belirtir. 
Tipi: System.String 
Deklarasyon: public string UserId { get; } 

•	UserLanguage 

Tanım: Süreç üzerinde o an işlem yapan kullanıcının, sisteme giriş yaparken seçtiği dil bilgisini belirtir. 
Tipi: System.String  
Deklarasyon: public string UserLanguage { get; } 


## 4.1.2. Metotlar 

•	AddAttachment(string, string) 

Tanım:Pozisyon, grup gibi mail özelliği olan nesneler için gönderilen maile eklenti eklemek için kullanılır. 
Deklarasyon: public void AddAttachment(string objectName, string filename) Parametreler: 
objectName: Mailine müdahale edilecek nesnenin adını belirtir. 
filename: Maile eklenti olarak eklenmesi istenen dökümanın fiziksel yolunu belirtir. 

•	AddConstantPositionToEmailObject(string, string) 

Tanım: Bilgilendirme nesnesine pozisyon eklemek için kullanılır. Eklenen pozisyon koduna sahip kişilere bilgilendirme gönderilir. 
Deklarasyon: public void AddConstantPositionToEmailObject(string objectName, string positionCode) 
Parametreler: 
objectName: Ekleme yapılacak bilgilendirme nesnesinin adını  belirtir. 
positionCode: Gruba eklenecek pozisyonun kodunu belirtir. 

•	AddConstantPositionToGroup(string, string) 

Tanım: Grup nesnesine pozisyon eklemek için kullanılır. 
Deklarasyon: public void AddConstantPositionToGroup(string objectName, string positionCode) 
Parametreler: 
objectName: Ekleme yapılacak grup nesnesinin adını belirtir. 
positionKod: Gruba eklenecek pozisyonun kodunu belirtir. 

•	AddConstantUserToGroup(string, string) 

Tanım: Grup nesnesine kullanıcı eklemek için kullanılır. 
Deklarasyon: public void AddConstantUserToGroup(string objectName, string userCode) 
Parametreler: 
objectName: Ekleme yapılacak grup nesnesinin adını belirtir. 
userKod: Gruba eklenecek kullanıcının kodunu (sicil no) belirtir. 



•	AddDepartmentProfessionToGroup(string, string, string) 

Tanım: İstenen deparmtandaki istenen ünvana sahip kişilerin pozisyon grubu nesnesine eklenmesini sağlar. 
Deklarasyon: public void AddDepartmentProfessionToGroup(string objectName, string department, string profession) 
Parametreler: 
objectName: Ekleme yapılacak grup nesnesinin adını belirtir. department: Gruba eklenecek departman kodunu belirtir. 
profession: Gruba eklenecek kişilerin ünvan kodunu belirtir. 

Örnek: 
AddDepartmentProfessionToGroup(“Grup1”,”G4”,”T1”). 

G4 kodlu departmandaki T1 ünvan koduna sahip kullanıcılar, Grup1’e eklenmiştir. 

•	AddDocumentToObject(string, string, string, bool, int, bool) 

Tanım: Pozisyon veya grup nesnesine döküman eklemek içindir.  
Deklarasyon: public void AddDocumentToObject(string objectName, string documentObjectName, string viewName, bool editable, int signStatus, bool showEvents) 
Parametreler: 
objectName: Ekleme yapılacak grup veya pozisyon nesnesinin adını belirtir. documentObjectName: Eklenecek dökümanın adıdır. 
viewName:  Eklenecek dökümanın view adıdır. 
editable: Görüntüleyecek olan pozisyon(lar)ın, dökümanı düzenleyebilmesini veya sadece görüntüleyebilmesini sağlayan parametredir. True ise kullanıcı dökümanda değişiklik yapabilir. False ise sadece görüntüleyebilir, değişiklik yapamaz. signStatus: Eklenecek dökümanın dijital imza durumunu belirtir. 
Durumlar aşağıda belirtilmektedir. 

	Parametre değeri=1 ve Tanım=None: Döküman dijital imza tanımlanmadığını belirtir.  Parametre değeri=1 ve Tanım Optional: Dijital imzalama işleminin opsiyonel olduğunu belirtir. 
	Parametre değeri=1 ve Tanım Required: Dijital imzalama işleminin zorunlu olduğunu belirtir. 
	Parametre değeri=1 veTanım RequiredIfPossible: Kullanıcının sistemde dijital imzası tanımlı ise zorunlu olduğunu belirtir. 
showEvents: Döküman görüntülenirken, eventlerin görünürlüğünü belirleyen parametredir. Değeri false gönderilmişse, kullanıcı dökümanı görüntülerken event butonlarını görüntüleyemez. Görüntülemek ve akışla ilgili işlem yapmak için akış tabına geçmek gerekir.  
•	AddFlowInitiatorToEmailObject(string) 

Tanım:Akışı başlatan kullanıcıyı bilginedirme nesnesine ekler. 
Deklarasyon: public void AddFlowInitiatorToEmailObject(string objectName) Parametreler: 
objectName: Ekleme yapılacak bilgilednirme nesnesinin adını belirtir. 

•	AddFlowInitiatorToGroup(string) 

Tanım:Akışı başlatan kullanıcıyı gruba ekler. 
Deklarasyon: public void AddFlowInitiatorToGroup(string objectName) Parametreler: 
objectName: Ekleme yapılacak grup nesnesinin adını belirtir. 

•	AddUserGroupToGroup(string,string) 

Tanım: Bir gruptaki kullanıcıların diğer gruba ekler. 
Deklarasyon: public void AddUserGroupToGroup(string objectName, string groupName) 
Parametreler:  
objectName: Ekleme yapılacak grup nesnesinin adını belirtir. 
groupName: Gruba eklenecek grup adını belirtir. 

•	AddVariablePositionToGroup(string,string) 

Tanım: Pozisyon nesnesine tanımlanmış kullanıcıyı gruba ekler. 
Deklarasyon: public void AddVariablePositionToEmailObject(string objectName, string positionObject) 
Parametreler: 
objectName: Ekleme yapılacak grup nesnesinin adını belirtir. 
positionObject: Gruba eklenecek kişinin atandığı pozisyon nesnesini belirtir. 

•	ClearAttachments(string) 

Tanım: Akış işlemleri sırasında pozisyon ve pozisyon grubu nesnelerine giden maillere eklenen eklentilerin kaldırılımasını sağlar.  
Deklarasyon: public void ClearAttachments(string objectName) 
Parametreler: 
objectName: Mailinden eklenti kaldırılacak nesnenin adını belirtir. 

Önemli Not ClearAttachments işlemi, henüz işlem sırası gelmemiş nesneler üzerinde yapılabilir. Örneğin, pozisyon1’in mailindeki eklentiler temizlenmek isteniyor ise, akış adımları henüz pozisyon1’e gelmemiş olmalıdır. Aksi takdirde, eklentiler gönderilir. 

•	ClearEmailObject(string) 

Tanım: Akış işlemleri sırasında bilgilendirme nesnelerine giden maillerin eklentilerinin kaldırılmasını sağlar.  
Deklarasyon: public void ClearEmailObject (string objectName)
Parametreler: 
objectName: Mailinden eklenti kaldırılacak nesnenin adını belirtir. 

•	ClearGroup(string) 

Tanım: Grup nesnesine eklenen tüm kullanıcıları siler. 
Deklarasyon:  public void ClearGroup(string objectName) Parametreler 
objectName: İçerisindeki kullanıcıların silineceği grup nesnesini belirtir. 

•	CreateDatabaseConnection 

Tanım: eBA sistemine tanımlı olan database için bağlantı sağlar. Hangi database sistemi kullanılıyorsa connection ona cast edilerek kodlama yapılabilir. 
Deklarasyon: public System.Data.Common.DbConnection 
CreateDatabaseConnection() 
Örnek: 
Mssql database yapısı kullanan bir eBA sisteminde aşağıdaki gibi connection kurulup cast edilebilir. 
SqlConnection con = (SqlConnection)CreateDatabaseConnection(); 
Bundan sonraki tüm işlemlerde .net tarafında database işlemlerinde kullanılan kodlar kullanılır. 
  con.Open(); 
  try 
  { 
SqlCommand dbcmd = new SqlCommand(@"UPDATE E_MyProject_Form" SET 
Text1=@Text1, Text2=@Text2 WHERE ID=@DOCID", con); 

dbcmd.Parameters.Add(new SqlParameter("@Text1", Text1.Text)); 
}          finally             { 
     con.Close(); 
  } 
•	CreateDatabaseProvider 

Tanım: eBA sistemine tanımlı olan database’e bağlantı sağlanıp database işlemleri yapılabilir. Kullanılan database sistemi türünden (oracle,mssql) bağımsız olarak kodlama yapılabilir. 
Deklarasyon: public eBADB.eBADBProvider CreateDatabaseProvider() 
Örnek: 
            eBADBProvider db = CreateDatabaseProvider();              try              { 
                 db.Open(); 
                 DbDataAdapter da = db.CreateDataAdapter(query +       
Dokuman1.ProfileId); 
                 DataTable returnValue = new DataTable();                  da.Fill(returnValue);                  return returnValue; 
             } 
             catch (Exception ex) 
             { 
                 throw new Exception("Hata : " + ex.Message); 
             }              finally              { 
                 db.Close(); 
             } 

•	CreateServerConnection 

Tanım: eBA sistemine ait fonksiyonları kullanmak için eBAPI kütüphanesindeki eBAConnection sınıfına ait bir bağlantı oluşturur. eBAConnection ile ilgili detaylı bilgiyi 6.1 eBAPI.eBAConnection başlığı altında bulabilirsiniz.  
Deklarasyon: public eBAPI.Connection.eBAConnection CreateServerConnection() void Dispose() 
Tanım: Açık olan database connectionlarının kapatılmasını sağlar. Kod işlemleri tamamlandığında kullanılır. Sistem performansı açısından kullanımı önemlidir. 
Deklarasyon: public void Dispose() 

•	string FormatMessage(string,bool) 

Tanım: Gönderilen string parametresini eBA maili olarak formatlayarak yeni bir string döndürür. Stringin içerisinde mailde gönderilen dinamik içerikler varsa metota bunlar parse edilir. 
Deklarasyon: public string FormatMessage(string message, bool isHtml) Parametreler 
message: Parse edilmesi istenen texti belirtir. isHtml: Metodtan dönen stringin html formatta olup olmayacağını belirtir. 
Örnek: 
```
string message=”<?=ProcessId> numaralı Satınalma süreci onaylanmıştır, fatura <?=DegiskenAdi.Value> TL değerindedir.”; string parsedMessage= FormatMessage(message,true); 
```
Çıktı: 
parsedMessage=122 numaralı Satınalma süreci onaylanmıştır, fatura 4,450 TL değerindedir. 

•	GetFlowObjectValue(string) 

Tanım:Parametre olarak gönderilen nesne özelliğinin değerini döndürür. 
Deklarasyon: public string GetFlowObjectValue(string objectName) Parametreler 
objectName: Değeri istenen özellik gönderilir. 

Örnek: 
String result1= GetFlowObjectValue(”DegiskenAdı.Value”); //DegiskenAdı: 
Değişken nesnesinin adını ifade eder. 
String result22= GetFlowObjectValue(”PoziyonNesnesi.UserId”);  
Çıktı: 
Result1=123 //DegiskenAdı nesnesinin değeri 
Result2=admin //Pozisyon nesnesine atanan kullanıcının kodu 

•	GetHideFlowStarter 

Tanım: Akışı başlatanın akış tarihçesinde gizli olup olmadığı bilgisini döndürür. 
Deklarasyon: public bool GetHideFlowStarter() 

•	GetHistoryCounter 

Tanım: İşlem yapılan süreç için o ana kadar başlatılan süreç sayısını döndürür. 
Deklarasyon: public int GetHistoryCounter() 

•	Getid 

Tanım: Başlatılan sürecin süreç numarasını döndürür. 
Deklarasyon: public int Getid() 

•	GetLogonDelegate 

Tanım: Başka bir kullanıcının yerine geçerek işlem yapılıp yapılmadığı bilgisini döndürür. 
Deklarasyon: public bool GetLogonDelegated() 

•	GetLogonDelegationPosition 

Tanım: Başka kullanıcı yerine geçip işlem yapan kulllanıcının pozisyon kodunu döndürür. 
Deklarasyon: public string GetLogonDelegationPosition() 

•	GetLogonPosition 

Tanım: Sisteme login olan kullanıcının pozisyon kodunu döndürür. 
Deklarasyon: public string GetLogonPosition() 

•	GetLogonUser 

Tanım: Sisteme login olan kullanıcının kodunu(sicil no) döndürür. 
Deklarasyon: public string GetLogonUser() 

•	GetPositionObjectDepartment(string) 

Tanım: Parametre olarak gönderilen pozisyon nesnesine tanımlı olan kullanıcının departman kodunu döndürür. 
Deklarasyon: public string GetPositionObjectDepartment(string objectName) Parametreler: 
objectName: Departman kodu istenen pozisyon nesnesinin adıdır. 
Örnek:  
string code= 
GetFlowObjectValue(GetPositionObjectDepartment("Pozisyon2").ToString()) ; 
Çıktı: 
Code=G1 //Pozisyon2 nesnesine tanımlı Ali Doğru isimli kullanıcının departman kodu. 

•	GetPositionObjectEmail(string) 

Tanım: Parametre olarak gönderilen pozisyon nesnesine tanımlı olan kullanıcının emailini döndürür. 
Deklarasyon: public string GetPositionObjectEmail(string objectName) 
Parametreler:
objectName: Email bilgisi istenen pozisyon nesnesinin adıdır 



•	GetPositionObjectFirstname(string) 

Tanım: Parametre olarak gönderilen pozisyon nesnesine tanımlı olan kullanıcının adını döndürür. 
Deklarasyon: public string GetPositionObjectFirstname(string objectName) Parametreler: 
objectName: İsim bilgisi istenen pozisyon nesnesinin adıdır 

•	GetPositionObjectLastname(string) 

Tanım: Parametre olarak gönderilen pozisyon nesnesine tanımlı olan kullanıcının soyadını döndürür. 
Deklarasyon: public string GetPositionObjectLastname(string objectName) Parametreler: 
objectName: Soyad bilgisi istenen pozisyon nesnesinin adıdır 

•	GetPositionObjectProfession(string) 

Tanım: Parametre olarak gönderilen pozisyon nesnesine tanımlı olan kullanıcının ünvan kodunu döndürür. 
Deklarasyon: public string GetPositionObjectProfession(string objectName) Parametreler: 
objectName: Ünvan bilgisi istenen pozisyon nesnesinin adıdır 

•	GetPositionObjectUserId(string) 

Tanım: Parametre olarak gönderilen pozisyon nesnesine tanımlı olan kullanıcının kod bilgisini(sicil no) döndürür. 
Deklarasyon: public string GetPositionObjectUserId(string objectName) Parametreler: 
objectName: Kullanıcı kod bilgisi istenen pozisyon nesnesinin adıdır 

•	GetProcess 

Tanım: Başlatılan sürecin isim bilgisini döndürür. 
Deklarasyon: public string GetProcess() 

•	GetProcessId 

Tanım: Başlatılan sürecin numarasını (süeç id) döndürür. 
Deklarasyon: public int GetProcessId() 
•	GetProject 

Tanım: Başlatılan sürecin tanımlı olduğu projenin isim bilgisini döndürür. 
Deklarasyon: public string GetProject() 

•	GetPublicValue(string) 

Tanım: Genel olarak atanmış bir değişkenin değerini döndürür. 
Deklarasyon: public string GetPublicValue(string name) Parametreler name:  Değişken nesnesinin ismini belirtir. 

Önemli Not Parametre olarak tanımlanan değişken, genel olarak atanmış olmalıdır. 
Aksi takdirde, kodun çalışıtırılması esnasında, uygulama, uyarı verecektir.  Bir değişkeni, genel olarak ayarlamak için 
1.   Değişken nesnesine sağ tıklayın. 
2.	Özelliklere tıklayın. 
3.	Açılan ekrandan bağlantı tabını seçin.  
4.	Genel seçeneğini işaretleyin. 
5.	Tamam butonuna tıklayın. 

•	GetUserId 

Tanım: Sisteme login olan kullanıcının kodunu(sicil no) döndürür. 
Deklarasyon: public string GetUserId() 

•	GetUserLanguage 

Tanım: Kullanıcının sisteme login olurken seçtiği dil bilgisini döndürür. 
Deklarasyon: public string GetUserLanguage() 

•	HasMethod(string) 

Tanım: Parametre olarak gönderilen metodun, akışın server kodunda olup olmadığının sonucunu döndürür. 
Deklarasyon: public bool HasMethod(string methodname) 
Parametreler 
Methodname: Varlığı sorgulanan metodun adını belirtir. 





•	Log(string) 

Tanım: Gönderilen parametreyi sisteme log olarak yazar. Log sisteme eklenirken tarih ve süreç bilgileri detaylı olarak yazılır. Yazılan loglara ulaşmak için system manager tool’u çalıştırılır, sol menüden event viewer’a tıklanır. Uygulama ismi olarak Workflow Process Custom seçilir. 
Deklarasyon: public void Log(string messageText) Parametreler 
messageText: Loglanmak istenen metni belirtir. 

•	SetFlowObjectValue(string,string) 

Tanım:Nesne özelliğine değer atamak için kullanılır. 
Deklarasyon: public void SetFlowObjectValue(string objectName, string value) 
Parametreler 
objectName: Değer atanmak istenen nesne özelliğini belirtir. value: Nesne özelliğine atanacak değeri belirtir. 

Örnek: 
SetFlowObjectValue(“PozisyonNesnesi.Position”, “PG001”); //PG001 organizasyon yapısında tanımlı bir pozisyon kodudur.  

•	SetHideFlowStarter(bool) 

Tanım: Akışı başlatanın akış tarihçesinde kullanıcı bilgisini gizlemek veya görüntülemek için kullanılır. Gizlemek için parametre true olmalıdır, görüntülemek için ise false olmalıdır. Varsayılan olarak, akışı başlatan, akış tarihçesinde gösterilir. 
Deklarasyon: public void SetHideFlowStarter(bool Value) 


•	SetPublicValue(string,string) 

Tanım: Parametre olarak gönderilen değişken nesnesine değer atama işlemi yapar. 
Deklarasyon: public void SetPublicValue(string name, string value) Parametreler 
name: Değişken nesnesinin adını belirtir. 
value: Değişken nesnesine atanmak istenen değeri belirtir. 


### 4.1.3. Olaylar 

•	OnSessionStart 

Tanım: Süreç başladığı anda çalışan eventtir. Akış formu seçildiğinde, kod gezgininde görünür. Kod gezgininde, ilgili evente çift tıklanarak, akışın, sunucu code tarafında event tetiklendiğinde çalışacak metot, otomatik, oluşturulur. Oluşan metodun içine, yapılması istenen işlemler yazılır. 

•	OnSessionEnd 

Tanım: Süreç sonlandığında çalışan eventtir. Akış formu seçildiğinde ,kod gezgininde görünür. Kod gezgininde, ilgili evente çift tıklanarak akışın, sunucu code tarafında event tetiklendiğinde çalışacak metot, otomatik, oluşturulur. Oluşan metodun içine, yapılması istenen işlemler yazılır. 

•	OnSessionError 

Tanım: Süreç hata verdiğinde çalışan eventtir. Akış formu seçildiğinde, kod gezgininde görünür. Kod gezgininde, ilgili evente çift tıklanarak, akışın sunucu code tarafında event tetiklendiğinde çalışacak metot, otomatik, oluşturulur. Oluşan metodun içine, yapılması istenen işlemler yazılır. 



## 4.2. Pozisyon 

Pozisyon nesnesi, akış içerisinde yer alan kullanıcı aksiyon adımlarını temsil eder.
Pozisyon nesnesi, “eBAFlowScrAdp.Objects.FlowPosition” sınıfındandır.


### 4.2.1. Özellikler 

•		AutoOpenApproval 

Tanım: Tasarlanan iş akışı senaryosuna göre, kullanıcı, onayındaki akışı ilerlettikten sonra, akış, ilerleyen adımlarda tekrar aynı kullanıcıya gelebilir. Bu durumlarda AutoOpenApproval Yes olarak atanmış ise; bu kullanıcının önünde akış tarihçesi yerine direk döküman açılır. AutoOpenApproval No olarak atanmış ise; önce akış tarihçesi açılır. AutoOpenApproval Default olarak atanmış ise; Yes olarak atanması ile aynı şekilde çalışır. 
Tipi: eBAFlowScrAdp.AutoOpenApprovalType 
Deklarasyon: public eBAFlowScrAdp.AutoOpenApprovalType AutoOpenApproval { set; get; } 
Örnek:  
PozisyonNesnesi.AutoOpenApproval=AutoOpenApprovalType.Yes; 
PozisyonNesnesi.AutoOpenApproval=AutoOpenApprovalType.No; 
PozisyonNesnesi.AutoOpenApproval=AutoOpenApprovalType.Default; 

•	Department  

Tanım:Pozisyon nesnesine atanmış kullanıcının departman bilgisidir. Tipi:System.String 
Deklarasyon: public string Department { get; } 

•	Description 

Tanım: Position nesnesinin Tanım bilgisidir. 
Tipi:System.String 
Deklarasyon: public string Description { set; get; } 

•	Documents 

Tanım: Pozisyona doküman eklemek için kullanılan özellik
Tipi: eBAFlowScrAdp.Objects.FlowDocuments
Deklarasyon: public eBAFlowScrAdp.Objects.FlowDocuments Documents { get; }
•	Email 

Tanım: Pozisyon nesnesine atanmış kullanıcının email bilgisidir. 
Tipi: Sytem.String 
Deklarasyon: public string Email { get; } 

•	EventFormId 

Tanım: Pozisyon nesnesine atanmış olaylarda event form tanımlanmışsa, bu nesne tarafından son görüntülenen event formun id bilgisidir. 
Tipi: System.Int32 
Deklarasyon: public int EventFormId { get; } 

•	Firstname 

Tanım: Pozisyon nesnesine atanmış kullanıcının isim bilgisidir. 
Tipi: System.String 
Deklarasyon: string Firstname { get; } 

•	HasEventFormId 

Tanım: Pozisyon nesnesinin eventlerine herhangi bir eventform tanımlanmış ise; bu bilgi true olarak dönecektir. 
Tipi: System.Boolean 
Deklarasyon: public bool HasEventFormId { get; } 

•	HasRequestId

Tanım: Pozisyon aksiyon almış mı bilgisi
“Özelliğin kullanıldığı pozisyon nesnesi henüz aksiyon almadıysa false, aksiyon aldıysa true değer döner.”
Tipi: System.Boolean 
Deklarasyon: public bool HasRequestId{ get; } 

•	Lastname 

Tanım: Pozisyon nesnesine atanmış kullanıcının soyisim bilgisidir. 
Tipi:System.String 
Deklarasyon: public string Lastname { get; } 


•	Position 

Tanım: Pozisyon nesnesine atanmış kullanıcının pozisyon kod bilgisidir. 
Tipi: System.String 
Deklarasyon: public string Position { set; get; } 

•	Profession 

Tanım: Pozisyon nesnesine atanmış kullanıcının ünvan kod bilgisidir. 
Tipi: System.String 
Deklarasyon: public string Profession { get; } 

•	RequestId 

Tanım: Süreçteki her bir talep numarasını belirtir. 
Olayların olay id bilgisini öğrenmek ve değişikilk yapmak için  
1.   Akış formuna sağ tıklayın. 
2.	Özellikler’i seçin. 
3.	Olaylar sekmesine tıklayın. 
Açılan ekranda ‘olay’ kolonunda bulunanlar ‘Tanım’ kolununda bulunan olayların requestid bilgisidir.  
Tipi: System.Int32 
Deklarasyon: public int RequestId { get; } 

•	SendMail 

Tanım: Akış, ilgili pozisyon nesnesinin bulunduğu adıma geldiğinde, pozisyon nesnesine atanmış kullanıcıya, mail gitmesi isteniyor ise; bu değer true atanmalıdır. Varsayılan değeri true’dur. 
Tipi:System.Boolean 
Deklarasyon: public bool SendMail { set; get; } 

•	User 

Tanım:  Pozisyon nesnesine atanan kullanıcının kullanıcı kod (sicil no) bilgisini döndürür. 
Tipi: System.String 
Deklarasyon: public string User { set; get; } 


•	Username 

Tanım: Pozisyon nesnesine atanan kullanıcının isim ve soyisim bilgisini döndürür. Tipi:System.String 
Deklarasyon: public string Username { get; }


### 4.2.2. Metotlar 

•	AddAttachment(string) 

Tanım: Akış, pozisyon nesnesinin bulunduğu adıma geldiğinde, pozisyon nesnesine atanan kullanıcıya gidecek maile eklenti eklemek için kullanılır.  
Deklarasyon: public void AddAttachment(string filename) 
Parametreler:  
filename: Maile eklenti olarak eklenmesi istenen dökümanın fiziksel yolunu belirtir. 

•	ClearAttachments 

Tanım: Pozisyon nesnesinin mailindeki eklentilerin silinmesini sağlar. 
Deklarasyon: public void ClearAttachments()  

•	GetUser 

Tanım: Pozisyon nesnesine atanan kullanıcının kullanıcı kodunun(sicil no) alınması için kullanılır. 
Deklarasyon: public string GetUser() 

•	SetEventEnable(int,bool) 

Tanım: Pozisyonun sahip olduğu bir eventin duruma göre görünüp görünmeyeceğinin set edilebileceği methoddur.
Deklarasyon: public void SetEventEnable(int eventId, bool enable)
Parametreler: 
eventId: Pozisyonun sahip olduğu eventin id numrası
enable: Eventin görünüp görünmeme durumu. true is event görünür, false ise görünmez 




•	SetFromPosition(string) 

Tanım: Pozisyon nesnesine, pozisyon atamak için kullanılır. 
Deklarasyon: public void SetFromPosition(string id) 
Parametreler: 
id: Pozisyon kodunu belirtir. 

•	SetFromUser(string) 

Tanım: Pozisyon nesnesine, kullanıcı atamak için kullanılır. 
Deklarasyon: public void SetFromUser(string id) 
Parametreler: 
id: Kullanıcı kodunu (sicil no) belirtir. 


### 4.2.3. Olaylar 

•	OnAfterEvent(object, OnAfterEventArguments) 

Tanım: Kullanıcı herhangi bir olay butonuna tıkladıktan sonra çalışır. Akış formu üzerinde bulunan pozisyon nesnesi seçildiğinde, kod gezgininde görünür. Kod gezgininde, ilgili evente çift tıklanır. Akışın server code tarafında, event tetiklendiğinde çalışacak metot, otomatik oluşturulur. Oluşan metodun içine, yapılması istenen işlemler yazılır. 
Deklarasyon: public void Pozisyon2_OnAfterEvent(object sender,OnAfterEventArguments args) 
Parametreler: 
args: OnAfterEventArguments classından türer.Class erişilebilir olarak aşağıdaki özellikleri içerir. 

•	OnBeforeEvent(object, OnBeforeEventArguments) 

Tanım: Pozisyondaki kişi aksiyon almadan hemen önce çalışan eventtir.
Deklarasyon: public void Pozisyon2_OnBeforeEvent(object sender,OnBeforeEventArguments args) 
Parametreler: 
args: Event parametreleri. OnAfterEventArguments  ile aynı parametrelere sahiptir.


### 4.2.4. OnAfterEventArguments Özellikleri 

•	ActionerType 

Tanım: Olayı gerçekleştiren kullanıcının, vekaleten veya kendi kulllanıcısı ile veya başka kullanıcının yerine işlem yaptığı bilgisini belirtir. 
Tipi: eBAFlowScrAdp.ActionerTypes Enum tiptir. Tanımlanan değerler aşağıdaki gibidir. 
	As: Yerine geçerek işlem yapılıyor ise bu değer kullanılır. 
	Delegated: Vekaleten işlem yapılıyor ise bu değer kullanılır. 
	Self: Kendi kullanıcısı ile işlem yapılıyor ise bu değer kullanılır. 
 Deklarasyon: public eBAFlowScrAdp.ActionerTypes ActionerType { set; get; } 

•	ActionerUserId 

Tanım: İşlemi yapan kullanıcının  kullanıcı kodu bilgisini belirtir. Bu bilgi, asıl işlem yapan kullanıcının bilgisidir. Kullanıcı,  vekaleten veya başka kullanıcının yerine işlem yapıyor olsa bile, işlem yapan kullanıcı bilgisini verir. 
Tipi: System.String 
Deklarasyon: public string ActionerUserId { set; get; } 

•	EventCode 

Tanım: Bu özellik ile olay id bilgisine erişilebilir. Kullanıcının gerçekleştirdiği olay, kontrol edilebilir. Olay id’nin tanımına 2.1.Özellikler  RequestId başlığından ulaşılabilir. 
Tipi:System.Int32 
Deklarasyon: public int EventCode { set; get; } 

•	EventFormId 

Tanım: Akış tasarımı sırasında, kullanıcının sahip olduğu olay seçeneklerine, olay formu eklenebilir. Böylece kullanıcı bu olaylardan herhangi birini seçtiğinde, bu formu görüntüleyebilir. EventFormId özelliği ile görüntülenen formun id bilgisine erişilebilir. 
Tipi:System.Int32 
Deklarasyon: public int EventFormId { set; get; } 

•	ObjectName 

Tanım: İşlem yapılan pozisyon nesnesinin isim bilgisini verir. Tasarım sırasında pozisyon nesnesine verilen isimdir. 
Tipi: System. String 
Deklarasyon: public string ObjectName { set; get; }  

•	PositionId 

Tanım: Pozisyon nesnesine atanan kullanıcının pozisyon kodu bilgisini belirtir. ActionerType’ın değeri önemli değildir. 
Tipi:System.String 
Deklarasyon: public string PositionId { set; get; } 

•	Reason 

Tanım: Tasarım sırasında, kullanıcıya tanımlanan olaylarda neden (reason) seçeneği işaretlenmiş ise, kullanıcı bu olay butonuna tıkladığında, neden bilgisini girebileceği bir ekranla karşılaşır. Reason özelliği, kullanıcının sağladığı, neden bilgisini belirtir. 
Tipi:Sytem.String 
Deklarasyon: public string Reason { set; get; } 

•	UserId 

Tanım: Pozisyon nesnesine atanan kullanıcının kullanıcı kodunu (sicil no) belirtir. ActionerType’ın değeri önemli değildir. 
Tipi:System.String 
Deklarasyon: public string UserId { set; get; } 


## 4.3. Akış Başlangıcı

Akış başlangıcı nesnesi, tasarlanan sürecin akışının başlangıç noktasını belirten nesnedir. Her akış tasarımının en başında bu nesne bulunmalıdır. Akış tasarımında kullanılacak diğer nesneler, bu akış başlangıcı nesnesinden sonra sıralanır ve birbirlerine bağlantı nesnesi ile ilişki kurarlar. Bir akış ekranında yalnızca 1 adet akış başlangıcı nesnesi kullanımına izin verilir.
Akış Başlangıcı nesnesi, “eBAFlowScrAdp.Objects.FlowStart” sınıfındandır


### 4.3.1. Özellikler 

•	Description 

Tanım: Akış başlangıcı nesnesinin başlığı
Tipi: System.String 
Deklarasyon: public string Description { get; set; }

•	HasRequestId 

Tanım: Nesnenin request id ye sahip olup olmadığı
Tipi: System.Boolean 
Deklarasyon: public bool HasRequestId { get; }

•	RequestId 

Tanım: Request id değeri
Tipi: System.Integer 
Deklarasyon: public int RequestId { get; }


## 4.4. Akış Bitişi

Akış bitişi nesnesi, tasarlanan sürecin akışının bittiği adımı belirten nesnedir. Akış tasarımında akışın sonlanması istenen birçok yerde bu nesne kullanılır.

Akış Bitişi nesnesi, “eBAFlowScrAdp.Objects.FlowEnd” sınıfındandır.


### 4.4.1. Özellikler 

•	SetFlowDeleted 

Tanım: Akış bitişi nesnesinden geçen sürecin sistemdeki durumunun, “silinmiş” olarak set edilip, edilmeyeceği değeri
Tipi: System.Boolean 
Deklarasyon: public bool SetFlowDeleted { get; set; }

•	UpdateStatusAsFinished 

Tanım: Akış bitişi nesnesinden geçen sürecin sistemdeki durumunun, “bitmiş” olarak set edilip, edilmeyeceği değeri
Tipi: System.Boolean 
Deklarasyon: public bool UpdateStatusAsFinished { get; set; }


## 4.5. Akışı Başlatan

Akışı başlatan nesnesi, web arayüzden ya da kod ile bir süreç başlatıldığında, süreci başlatan kişiyi temsil eden akış nesnesidir. Akış başlatan nesnesinin sahip olduğu özellikler, olaylar ve methodlar, normal pozisyon nesnesininki ile aynıdır. Akış başlatan nesnesinin özelliği, sistem tarafından süreci başlatan, işin sahibi kişiyi temsil ediyor olmasıdır.

Geliştirme arayüzünde bir proje oluşturulduğunda, bu projenin akış tasarım kısmında gelen varsayılan akış diyagramında, 1 adet “Akışı Başlatan” nesnesi bulunur.
Akışı başlatan nesnesinin sahip olduğu özellikler, olaylar ve methodların detaylı açıklamaları için; Pozisyon dokümanını inceleyiniz.

Önemli Not : Akışı başlatan nesnesi, pozisyon nesnesi ile aynı özellik, event ve methodlara sahip olduğu halde aralarında yapısal farklılıklar bulunmaktadır. Akışı başlatan nesnesine sistem tarafından mail düşmez ve akışı başlatan nesnesine akış içerisinde onay düşürülmüşse bu süreç akışı başlatan kişinin Onaylarına değil Taslaklarına düşer.

Önemli Not : Akışı başlatan nesnesi sadece akışın başlangıcında bir kez kullanılmalıdır. Sonrasında sürecin tekrar akışı başlatana geri dönmesi gerekiyorsa ya da süreç adımlarında tekrar akışı başlatan kişiye onay gidecekse, ilgili adıma Akışı Başlatan nesnesi değil, Pozisyon nesnesi konulmalı ve pozisyon nesnesi içerisinde değer olarak “Akışı Başlatan” seçilmelidir.


## 4.6. Grup 

Pozisyon grubu nesnesi, akış adımlarında birden çok kişiye aksiyon düşürülmek istendiğinde kullanılan nesnedir. Pozisyon nesnesine yalnızca bir kullanıcı ya da pozisyon eklenebilirken, pozisyon grubu nesnesine birden çok kullanıcı, pozisyon, kullanıcı grubu, departman veya ünvan bazlı kullanıcı eklemeleri yapılabilmektedir.
Pozisyon Grubu nesnesi, “eBAFlowScrAdp.Objects.FlowGroup” sınıfındandır.


### 4.6.1. Özellikler 

•	AutoOpenApproval 

Tanım: Tasarlanan iş akışı senaryosuna göre, kullanıcı, onayındaki akışı ilerlettikten sonra, akış, ilerleyen adımlarda tekrar aynı kullanıcıya gelebilir. Bu durumlarda, AutoOpenApproval Yes olarak atanmış ise, kullanıcı akış tarihçesi yerine direk dokümanı görüntüler. AutoOpenApproval No atanmış ise, önce akış tarihçesi açılır. 
AutoOpenApproval Default atanmış ise, Yes atanması ile aynı şekilde çalışır. Tipi: eBAFlowScrAdp.AutoOpenApprovalType (enum type) 
Deklarasyon: public eBAFlowScrAdp.AutoOpenApprovalType AutoOpenApproval { set; get; } 

Örnek:  
PozisyonGrubuNesnesi.AutoOpenApproval=AutoOpenApprovalType.Yes; 
PozisyonGrubuNesnesi.AutoOpenApproval=AutoOpenApprovalType.No; 
PozisyonGrubuNesnesi.AutoOpenApproval=AutoOpenApprovalType.Default;  

•	Description 

Tanım: Pozisyon Grubu nesnesinin Tanım bilgisini belirtir. 
Tipi:System.String 
Deklarasyon: public string Description { set; get; } 

•	Documents 

Tanım: Pozisyon grubuna doküman eklemek için kullanılan özellik
Tipi:  eBAFlowScrAdp.Objects.FlowDocuments
Deklarasyon: public eBAFlowScrAdp.Objects.FlowDocuments Documents { get; }


•	EventFormId 

Tanım: Pozisyon Grubu nesnesine atanmış eventlerde, event form tanımlanmış ise, bu nesne tarafından, son görüntülenen event formun id bilgisini belirtir. Grup nesnesinde, birden fazla kullanıcı işlem yapmış ise, sadece son yapılan işlemin request id bilgisini döndürür. 
Tipi: System.Int32 
Deklarasyon: public int EventFormId { get; } 

•	EventFormIdList 

Tanım:  Grupta birden fazla kullanıcı varsa, bütün kullanıcıların event form idlerini, liste halinde, döndürür. 
```
Tipi: System.Collections.Generic.List<int>
Deklarasyon: public System.Collections.Generic.List<int> EventFormIdList { get; } 
``` 
•	HasEventFormId 

Tanım: Pozisyon Grubu nesnesinin eventlerine, herhangi bir event form tanımlanmış ise, bu bilgi true olarak dönecektir. 
Tipi: System.Boolean 
Deklarasyon: public bool HasEventFormId { get; } 

•	RequestId 

Tanım: Süreçteki her bir istek numarasıdır. 
Tipi: System.Int32 
Deklarasyon: public int RequestId { get; } 

•	RequestIdList 

Tanım:  Pozisyon Grubu nesnesinde, birden fazla kullanıcı varsa, bütün kullanıcıların yaptıkları işlemlerin request id bilgilerini, liste halinde, döndürür. 
```
Tipi: System.Collections.Generic.List<int> 
Deklarasyon: public System.Collections.Generic.List<int> RequestIdList { get; } 
```


•	SendMail 

Tanım: Gruptaki kişilere aksiyon maili gönderilip gönderilmeyeceği
Tipi: System.Boolean
Deklarasyon: public bool SendMail { get; set; }


### 4.6.2. Metotlar 

•	AddAttachment(string) 

Tanım: Akış, pozisyon grubu nesnesinin bulunduğu adıma geldiğinde, pozisyon nesnesine atanmış kullanıcıya gidecek maile, eklenti eklemek için kullanılır.  
Deklarasyon: public void AddAttachment(string filename) 
Parametreler:  
filename: Maile eklenti olarak eklenmesi istenen dökümanın fiziksel yolunu belirtir.  

•	ClearAttachments 

Tanım: Pozisyon grubu nesnesinin mailindeki eklentilerin silinmesini sağlar. 
Deklarasyon: public void ClearAttachments() 

•	AddConstantPosition(string) 

Tanım: Pozisyon grubu nesnesine, sabit pozisyon eklenmesini sağlar. 
Deklarasyon: public void AddConstantPosition(string positionCode) Parametreler: 
positionCode: Gruba eklenecek kullanıcının pozisyon kod bilgisini belirtir. 

•	AddConstantUser(string) 

Tanım: Pozisyon grubu nesnesine, sabit kullanıcı eklenmesini sağlar. 
Deklarasyon: public void AddConstantUser(string userCode) 
Parametreler: 
userCode: Gruba eklenecek kullanıcının kullanıcı kodunu (sicil no) belirtir. 





•	AddDepartmentProfession(string,string) 

Tanım: Pozisyon grubu nesnesine, istenen departmandaki, istenen ünvana sahip kullanıcıların eklenmesini sağlar. 
Deklarasyon: public void AddDepartmentProfession(string department, string profession) 
Parametreler: 
deparment: Gruba eklenecek kullanıcının departman kodunu belirtir. 
profession: Gruba eklenecek kullanıcıların ünvan kodunu belirtir. 

•	AddFlowInitiator 

Tanım: Pozisyon grubu nesnesine, akışı başlatan kullanıcıyı ekler. 
Deklarasyon: public void AddFlowInitiator() 

•	AddUserGroup (string) 

Tanım: Sistemde oluşturulan kullanıcı gruplarını, akıştaki pozisyon grubu nesnesine ekleyen methoddur.
Deklarasyon: public void AddUserGroup(string groupName)
Parametre: 
groupName: Pozisyon grubu nesnesine eklenmek istenen kullanıcı grubunun adı 

•	AddVariablePosition(string) 

Tanım: Pozisyon grubu nesnesine, parametre olarak gönderilen, pozisyon nesnesine atanmış kullanıcıyı ekler. 
Deklarasyon: public void AddVariablePosition(string positionObject) Parametre: 
positionObject: Gruba eklenecek pozisyon nesnesinin adını belirtir. 

•	ClearAttachments 

Tanım: Gruba eklenmiş dosyaları temizleyen methoddur.
Deklarasyon: public void ClearAttachments()

•	ClearGroup 

Tanım: Pozisyon grubu nesnesine atanmış tüm kullanıcıları siler.  
Deklarasyon: public void ClearGroup() 
•	SetEventEnable(int,bool) 

Tanım: Pozisyon grubunun sahip olduğu bir eventin duruma göre görünüp görünmeyeceğinin set edilebileceği methoddur.
Deklarasyon: public void SetEventEnable(int eventId, bool enable)
Parametreler: 
eventId: Pozisyon grubunun sahip olduğu eventin id numrası
enable: Eventin görünüp görünmeme durumu. true is event görünür, false ise görünmez 


### 4.6.3. Olaylar 

•	OnAfterEvent 

OnAfterEvent  için gerekli tanımlar, Pozisyon nesnesinde açıklanmıştır. Pozisyon grubu nesnesinde, birden fazla kullanıcı olabileceği için, OnAfterEvent, gruptaki her kullanıcı işlemi için, işlem yapan kullanıcının bilgilerine göre çalışır. 


## 4.7. Bilgilendirme 


Bilgilendirme nesnesi, sürecin herhangi bir anında, sistemde tanımlı kişilere bilgilendirme maili göndermek için kullanılan nesnedir.
Bilgilendirme nesnesi, “eBAFlowScrAdp.Objects.FlowMail” sınıfındandır.


### 4.7.1. Özellikler 

•	Description 

Tanım: Bilgilendirme nesnesinin başlık değeri
Tipi: System.String 
Deklarasyon: public string Description { set; get; } 

•	Documents 

Tanım: Bilgilendirme nesnesine doküman eklemek için kullanılan özellik
Tipi:  eBAFlowScrAdp.Objects.FlowDocuments
Deklarasyon: public eBAFlowScrAdp.Objects.FlowDocuments Documents { get; }



### 4.7.2. Metotlar 

•	AddAttachment(string) 

Tanım: Filename olarak verilen dosyayı ilgili bilgilendirme nesnesine eklemeye yarayan methoddur.
Deklarasyon: public void AddAttachment(string filename) 
Parametreler:  
filename: Maile eklenti olarak eklenmesi istenen dökümanın fiziksel yolunu belirtir.  

•	ClearAttachments 

Tanım: Bilgilendirme nesnesine eklenmiş dosyaları temizleyen methoddur.
Deklarasyon: public void ClearAttachments() 

•	AddConstantPosition(string) 

Tanım: Pozisyon id değerini parametre vererek, bilgilendirme nesnesine pozisyon bazlı kullanıcı eklemeye yarayan methoddur.
Deklarasyon: public void AddConstantPosition(string positionCode) Parametreler: 
positionCode: Bilgilendirmeye eklenecek kullanıcının pozisyon kod bilgisini belirtir. 

•	AddConstantUser(string) 

Tanım: Kullanıcı adı değerini parametre vererek, bilgilendirme nesnesine kullanıcı eklemeye yarayan methoddur.
Deklarasyon: public void AddConstantUser(string userCode) 
Parametreler: 
userCode: Bilgilendirmeye eklenecek kullanıcının kullanıcı kodunu (sicil no) belirtir. 

•	AddFlowInitiator 

Tanım: Akışı başlatan kullanıcıyı bilgilendirme nesnesine ekleyen methoddur.
Deklarasyon: public void AddFlowInitiator() 

•	AddVariablePosition(string) 

Tanım: Akış içerisinde bulunan bir pozisyon nesnesini, bilgilendirme nesnesine ekleyeme yarayan methoddur. Pozisyon nesnesinde hangi kullanıcı ya da pozisyon varsa o kişiyi bulup bilgilendirmeye ekler.
Deklarasyon: public void AddVariablePosition(string positionObject) Parametre: 
positionObject: Bilgilendirmeye eklenecek pozisyon nesnesinin adını belirtir. 

•	ClearGroup 

Tanım: Bilgilendirme nesnesi içeriğini temizleyen methoddur.
Deklarasyon: public void ClearGroup() 


## 4.8. Değişken 

Değişken nesnesi, akış tarafında bazı verilerin sabit bir değer olarak tutulup, akış tasarımında ya da kod tarafında kullanılmasını sağlayan nesnedir. Bu nesnenin tutacağı değer kod tarafında da set edilebilir,form üzerindeki bir alana bağlanarak değerini bu alandan da alabilir.
Değişken nesnesi, “eBAFlowScrAdp.Objects.FlowVariable” sınıfındandır.


### 4.8.1. Özellikler 

•		Value 

Tanım: Değişkenin string tipindeki değeridir. 
Tipi: System.String
Deklarasyon: public string Value { get; set; }
•		ValueAsInteger

Tanım: Değişken nesnesinin integer tipinde değeri 
Tipi: System.Integer
Deklarasyon: public int ValueAsInteger { get; set; }


## 4.9. Doküman 

Projede tasarlanmış formların ve form üzerindeki bilgilerin tutulduğu nesnedir. Doküman nesnesi, akışta; pozisyon, pozisyon grubu, bilgilendirme vb. gibi nesnelere doküman olarak eklenerek ilgili adımda doküman nesnesinin bağlı olduğu proje formunun görüntülenmesi sağlanmış olur. Ayrıca akış kod tarafında da doküman nesnesine erişim sağlanarak, doküman nesnesinin bağlı olduğu form üzerinde kodsal işlemler yapılabilir.
Doküman nesnesi, “eBAFlowScrAdp.Objects.FlowDocument” sınıfındandır.


### 4.9.1. Özellikler 

•	Path 

Tanım: Dökümanın eBA sistemindeki yol bilgisidir. 
Tipi:System.String 
Deklarasyon: public string Path { set; get; }  

•	ProfileData 

Tanım: Doküman nesnesine bağlı olan form verilerine erişmek için kullanılan özellik
Tipi:  eBAFormData.eBAForm
Deklarasyon: public eBAFormData.eBAForm ProfileData { get; }

•	ProfileForm 

Tanım: Döküman nesnesine bir eBA formu tanımlanmışsa, ProfileForm bu tanımlanan formun isim bilgisidir. 
Tipi:System.String 
Deklarasyon: public string ProfileForm { set; get; } 

•	ProfileId 

Tanım: Döküman nesnesine tanımlanan eBA formunun id bilgisidir. 
Tipi:System.Int32 
Deklarasyon: public int ProfileId { set; get; } 

•	ProfileProcess 

Tanım: Döküman nesnesinin bulunduğu projenin isim bilgisidir. 
Tipi:System.String 
Deklarasyon: public string ProfileProcess { set; get; } 


## 4.10. Akış Durdurucu 

Akış durdurucu nesnesi, akışın kodla tetikleme yapılana kadar o adımda kalmasını sağlar. Kodla tetikleme sonucunda bu nesnenin tetiklendiği parametre değerine göre akış istenilen şekilde yönlendirilebilir.
Akışın belli bir noktasında mevcut süreç içerisindeki değerler kullanılarak kod ile başka bir süreç tetiklenmesi gerektiğinde ve tetiklenen bu süreçten dönen dönüş değerine göre mevcut süreci devam ettirmek gerektiğinde bu nesne yardımıyla ilgili akış tetiklenip, mevcut süreç o akıştan değer dönene kadar durdurulabilir.
Bununla birlikte akış durdurucu nesnesinin tetiklenme eventi olarak “Zaman Aşımı” seçilip, akışın beklemesi istenen süre girildiğinde, belirlenen süre sonunda zaman aşımı eventi çalışıp akışın kendiliğinden devam etmesi sağlanabilir. Böylece akış belirli bir süre için bekletilmiş olur.
Akış Durdurucu nesnesi, “eBAFlowScrAdp.Objects.FlowPauser” sınıfındandır.


### 4.10.1. Özellikler 

•		Description 

Tanım: Akış durdurucu nesnesinin başlık bilgisi
Tipi: System.String
Deklarasyon: public string Description { get; set; }
•		HasRequestId

Tanım: Akış, Akış durdurucu nesnesinden ilerlemiş mi bilgisi
“Özelliğin kullanıldığı Akış durdurucu nesnesi henüz aksiyon almadıysa false, aksiyon aldıysa true değer döner.”
Tipi: System.Boolean
Deklarasyon: public bool HasRequestId { get; }
•		RequestId

Tanım: Akış durdurucunun aksiyon aldığı eventin id si
Tipi: System.Integer
Deklarasyon: public int RequestId { get; }

### 4.10.2. Olaylar 

•	OnAfterEvent(object, OnAfterEventArguments) 

Tanım: Akış durdurucu nesnesi tetiklendikten sonra çalışan eventtir.
Deklarasyon: public void AkisDurdurucu1_OnAfterEvent(object sender,OnAfterEventArguments args)
Parametreler: 
args: OnAfterEventArguments classından türer. 


## 4.11. Örnekler 

### 4.11.1. Zaman aşımı değer ataması 

Zaman aşımı değer ataması, başlangıç ve bitiş tarihleri arasındaki fark bulunarak, pozisyon ve zamanlayıcı nesnelerinin zaman aşımı değerlerinin güncellenmesi işlemidir.  

Örnek: 
DateTime startDate = MBASLANGICTARIHI.Value; 
DateTime endDate = MBITISTARIHI.Value; 
TimeSpan ts = endDate - startDate; 
String hour= Math.Round(ts.TotalHours).ToString(); 

Timer nesnesine atama: 

ebaflow.SetFlowObjectValue("Zamanlayici1.day", "0"); // Zamanlayici1 zamanlayıcı nesnesinin ismidir ebaflow.SetFlowObjectValue("Zamanlayici1.hour", hour); ebaflow.SetFlowObjectValue("Zamanlayici1.minute","0"); 

Zaman aşımı olayı tanımlanmış pozisyon nesnesine atama: 

ebaflow.SetFlowObjectValue("Pozisyon1.day", "0"); // Pozisyon1 pozisyon nesnesinin ismidir. 
ebaflow.SetFlowObjectValue("Pozisyon1.hour", hour); ebaflow.SetFlowObjectValue("Pozisyon1.minute","0");  


### 4.11.2. Mail içeriğinin değiştirilmesi  

        Pozisyon nesnesinin mail konusunun ve içeriğinin güncellenmesi, aşağıdaki örnekte gösterilmektedir. 
Örnek: 
ebaflow.SetFlowObjectValue("Pozisyon1.Subject", subject); ebaflow.SetFlowObjectValue("Pozisyon1.Text", content);  


### 4.11.3. Grup Nesnesine Atama 

Grup nesnesine programatik olarak form tablosundan çekilen onaycıların listesinin atanması, aşağıdaki örnekte gösterilmektedir. 
Örnek: 
            FormTable tblReferences = frm.Tables["tblName"];             foreach(var row in tblReferences.Rows) 
            { 
                string userId = row["UserId"].AsString; 
                AddConstantUserToGroup("GrupAd", userId); 
            }