# 1.Giriş  

## 1.1. Amaç  

eBA İş Akış Yönetimi, form ve akış geliştirmek için çok sayıda bileşen ve özellik sunmaktadır. Bu sayede kodlama yapmaya ihtiyaç duymadan birçok işlem yapılabilmektedir. Ancak kodlama ihtiyacı duyulacak bazı durumlar ((veri kaynağına erişim, harici uygulamalar ile entegrasyon, harici kütüphane kullanımı vb.) ortaya çıkabilmektedir. eBA Geliştirici Referans Rehberi, eBA İş Akışı Yönetiminde kodlama ile geliştirme yapacak kullanıcılara gerekli bilgileri sunmak için hazırlanmıştır.    



## 1.2. Kapsam  

eBA Geliştirici Referans Rehberi, eBA İş Akışı Yönetimi için aşağıdaki üç maddeyi kapsamaktadır.  

Form ve akış arayüzlerinde kodlama  

eBA Kütüphaneleri’nin kullanımı   

Özel kontrol geliştirme   

# 2.Kodlama Hakkında 

eBA Workflow projelerinde kodlama platformu, zengin kütüphanelerin kullanılabilir olduğu Microsoft .Net ve kodlama dili C#’tır.    

İlerleyen bölümlerde, eBA Workflow Studio’da geliştirilen projelerde ve nesnelerde, eBA’nın sunduğu yardımcı kütüphane ve API’lerde kodlama hakkında geniş bilgi bulacaksınız.  

# 3.Form Arayüzünde Kodlama  

Form arayüzünde, tasarım yaptığımız ekran ve kod yazılan editör bölümü (kodlama editörü) mevcuttur.   

Kodlama Editörü’nü açmak için  

Form üzerinde sağa tıklayın.  

View Server Code ‘u seçin.  

Formun olay koduna erişmek için  

Formun Kod Gezgini’ndeki olaylarına çift tıklayın.  

View Validation Code’u seçin.  

OnValidateDocument olay kodunu görün.  

Nesnenin olay koduna erişmek için  

Nesnenin Kod Gezgini’ndeki olaylarına çift tıklayın.  

View Validation Code’u seçin.  

OnValidateDocument olay kodunu görün.  



![](https://docsbimser.blob.core.windows.net/imagecontainer/s1-cf144327-f3c7-4a2f-8702-d0a9aa73c813.png)

## 3.1. Form 

  eBA Formları eBAControls.eBABaseForm sınıfından türemektedir. Bu bölümde, ilgili sınıfa ait özellikler, metotlar ve olaylar açıklanmaktadır. 

## 3.1.1. Özellikler 

•	AlwaysValidate 

Tanım: Formun kaydedilirken daima geçerliliğinin kontrol edilmesini sağlar. 
Tipi: System. Boolean 
Deklarasyon: public bool AlwaysValidate { set; get; } 
Örnek:  
public void OnSaveData() 
	 	{ 
	 	       AlwaysValidate = true; 
	 	} 

•	CopyMode 

Tanım: Kopyalama işleminin durumunu gösterir. True olması form kopyalama işlemi yapılıyor anlamına gelir. 
Tipi: System. Boolean 
Deklarasyon: public bool CopyMode { get; set; } 
Örnek:  
```
public void OnLoadData() 
 	 	{ 
	 	 	if(CopyMode) 
 	 	       { 

 	 	       } 
 	 	} 
```
•	CurrentBrowser 

Tanım: Formu açan kullanıcının kullandığı tarayıcıyı verir. 
Tipi: System.String  
Deklarasyon: public string CurrentBrowser { get; } 


•	CurrentDictionary 

Tanım: Formu açan kullanıcının kullandığı dili verir. 
Tipi: ebanet.MultilanguageDictionary 
Deklarasyon: public ebanet.MultilanguageDictionary CurrentDictionary { get; } 

•	CurrentMode 

Tanım: Formun mevcut modunun bilgisidir. Modu değiştirmek için kullanılabilir. 
Aldığı Değerler:
Edit: Değişiklik yapılabilir modu 
View: Görüntüleme modu. Değişiklik yapılamaz. 
Tipi: eBAControls.eBABaseForm.FormMode 
Deklarasyon: public eBAControls.eBABaseForm.FormMode CurrentMode { set; get; } 

•	CurrentView 

Tanım: Formun gösterildiği görünüm bilgisidir. Görünümü değiştirmek için de kullanılır. 
Tipi: System.String 
Deklarasyon: public string CurrentView { set; get; } 
Örnek: 
	 	public void Button1_OnClick(Object sender, EventArgs e) 
	 	{ 
	 	 	CurrentView = "view1"; 
	 	} 

•	DocumentId 

Tanım: Doldurulan formun doküman numarasını verir. Bu doküman numarası genelde form bazında unique olur. İstenilir ise değiştirilebilir.  
Tipi: System.String 
Deklarasyon: public string DocumentId { set; get; } 

•	DocumentOpenArchiveName 

Tanım: Form arşivden açılırsa açılan arşivin adını verir. Aksi durumda null olur. 
Tipi: System.String 
Deklarasyon: public static string DocumentOpenArchiveName { get; } 


•	DocumentOpenArchiveType 

Tanım: Form arşivden açılırsa açılan arşivin tipini verir. Aksi durumda null olur. 
Tipi: System.String 
Deklarasyon: public static string DocumentOpenArchiveType { get; } 

•	DocumentOpenSource 

Tanım: Form arşivden açılırsa değeri ‘archive’ olur. 
Tipi: System.String 
Deklarasyon: public static string DocumentOpenSource { get; } 

•	DocumentVersion 

Tanım: Formun versiyonunu verir. 
Tipi: System.Int32  
Deklarasyon: public int DocumentVersion { set; get; } 

•	EventId  

Tanım: Event formlarda formun açılmasını sağlayan olayın numarasıdır. 
Tipi: System.Int32  
Deklarasyon: public int EventId { set; get; } 

•	EventProcessId 

Tanım: Event formlarda formun açıldığı akışın numarasıdır. 
Tipi: System.Int32  
Deklarasyon: public int EventProcessId { set; get; } 

•	EventRequestId 

Tanım: Event formlarda formun açıldığı isteğin numarasıdır. 
Tipi: System.Int32  
Deklarasyon: public int EventRequestId { set; get; } 

•	Filename 

Tanım: Formun doküman yönetim sistemindeki tam yolunu verir. Bu doküman yolu standart olup Workflow/[ProjectName]/[FormName]/[GlobalId].wfd formatındadır. 
Tipi: System.String 
Deklarasyon: public string Filename { get; } 
•	formName 

Tanım: Formun adını verir. 
Tipi: System.String 
Deklarasyon: public string formName { get; set; }

•	id 

Tanım: Formun sistem bazında tutulan eşsiz numarasıdır. 
Tipi: System.Int32 
Deklarasyon: public int id { set; get; } 

•	IsMobile 

Tanım: Formunun mobil cihazdan görüntülendiği bilgisini verir. 
Tipi: System. Boolean 
Deklarasyon: public bool IsMobile { get; } 

•	IsTest 

Tanım: Sistemin test modunda mı açıldığı bilgisini verir. 
Tipi: System. Boolean 
Deklarasyon: public bool IsTest { get; } 

•	LogonDelegated 

Tanım: Sisteme giriş yapmış kullanıcının vekalet yoluyla işlem yapıp yapmadığını verir. 
Tipi: System. Boolean 
Deklarasyon: public bool LogonDelegated { get; } 

•	LogonDelegationUser 

Tanım: Sisteme giriş yapmış kullanıcının vekalet yoluyla işlem yapıyorsa asıl kullanıcının kodunu verir. 
Tipi: System.String 
Deklarasyon: public string LogonDelegationUser { get; } 

•	LogonLanguage 

Tanım: Sisteme giriş yapmış kullanıcının dil tercihini verir. 
Tipi: System.String 
Deklarasyon: public string LogonLanguage { get; } 

•	LogonPosition 

Tanım: Sisteme giriş yapmış kullanıcının pozisyonunu verir. 
Tipi: System.String 
Deklarasyon: public string LogonPosition { get; } 

•	LogonUser 

Tanım: Sisteme giriş yapmış kullanıcının kodunu verir. 
Tipi: System.String 
Deklarasyon: public string LogonUser { get; } 

•	MultilanguageEnabled 

Tanım: Projenin çoklu dil özelliğinin durumunu verir. 
Tipi: System. Boolean 
Deklarasyon: public virtual bool MultilanguageEnabled { get; } 

•	PrintingEnabled 

Tanım: Yazdırma modu etkinlik durum bilgisini verir. 
Tipi: System. Boolean
Deklarasyon: public bool PrintingEnabled { get; set; }

•	ProjectVersion 

Tanım: Proje versiyonunu verir. 
Tipi: System.Int32 
Deklarasyon: public int ProjectVersion { set; get; } 

•	SourceDocument 

Tanım: Yapıştırılarak doldurulmuş formun ana form kodunu verir. 
Tipi: System.Int32 
Deklarasyon: public int SourceDocument { set; get; } 

•	UserLanguage 

Tanım: Sisteme giriş yapmış kullanıcının dilini verir. 
Tipi: System.String 
Deklarasyon: public string UserLanguage { get; } 

•	height 

Tanım: Formun yüksekliğini piksel olarak verir. 
Tipi: System.Int32 
Deklarasyon: public int height 

•	width 

Tanım: Formun genişliğini piksel olarak verir. 
Tipi: System.Int32 
Deklarasyon: public int width 




## 3.1.2.	Metotlar 

•	CreateDatabaseConnection()

Tanım: Kod yazarken sistemin veritabanına erişmek gerekebilir. Bu gibi durumlarda kod içinde veritabanı bağlantısı yapmak için bu metod kullanılır. Geri dönüş değeri hangi sistem kullanılıyorsa (Ms Sql,Oracle) ona göre cast edilmelidir.
Deklarasyon: 
public System.Data.Common.DbConnection CreateDatabaseConnection()

Örnek: 
using System.Data.SqlClient; 
… 
SqlConnection dbcon = (SqlConnection)CreateDatabaseConnection(); 

veya  

using System.Data.OracleClient; 
… 
OracleConnection dbcon = (OracleConnection)CreateDatabaseConnection(); 


•	CreateServerConnection()

Tanım: eBA API si ile server a bağlantı açmak için kullanılır.
Deklarasyon: 
public eBAPI.Connection.eBAConnection CreateServerConnection()

Örnek:
using eBAPI;
using eBAPI.Connection;

eBAConnection con = CreateServerConnection();
	con.Open();
…


•	DecimalToString(decimal, int, bool) 

Tanım: Decimal veri tipini string veri tipine çeviren methoddur.
Deklarasyon: 
public string DecimalToString(decimal number, int numberOfDigitsAfterDecimal, bool useThousandSeperator)

•	DoubleToString(double, bool)

Tanım: Double veri tipini string veri tipine çeviren methoddur.
Deklarasyon: 
public string DoubleToString(double number, bool useThousandSeperator)

•	GetControlsList()

Tanım: Formdaki kontrollerin listesini verir.
Deklarasyon: 
public virtual System.Collections.Generic.List```<```System.Web.UI.Control```>``` GetControlsList()

Örnek: Örnekte form üzerindeki metin kutularının hepsinin arkaplan rengi kırmızı yapılmaktadır.

using System.Web.UI; 
using System.Web.UI.WebControls; 
… 
public void Button1_OnClick(Object sender, EventArgs e) 
{ 
    foreach(Control ctrl in GetControlsList()) 
   { 
     if (ctrl is TextBox) 
     { 
       ((TextBox)ctrl).BackColor = System.Drawing.Color.Red; 
     } 
   } 
}

•	GetEventReason()

Tanım: Akışta event form kullanılıyorsa ve ilgili event için neden bilgisi event formu üzerinden belirlenmek isteniliyorsa bu metod override edilir. Bunun için event formu sınıfı içine aşağıdaki metodun kopyalanması ve içeriğinin düzenlenmesi yeterlidir. Metod içinde geriye dönülen string veri neden bilgisi olarak kabul edilir.
Deklarasyon: 
public virtual string GetEventReason()

Örnek: 

 public override string GetEventReason() 
{ 
   return Metin1.Text; 
}

•	GetMultilanguageText(string) 

Tanım: Proje için çoklu dil özellik etkinleştirilmişse, dil kitaplığında tanımlanan metnin değerini almak için kullanılır.
Deklarasyon: 
public string GetMultilanguageText(string text)

Örnek:  
public void Button1_OnClick(Object sender, EventArgs e) 
{ 
Text1.Text=GetMultilanguageText("@Process.MyProject.User.myWord"); 
} 

•	GetPrintableFormatUrl()

Tanım:  Sayfanın yazdırılabilir biçimine erişmek için adres (url) almak amacıyla kullanılır.
Deklarasyon: 
public string GetPrintableFormatUrl()

•	GetPrintableFormatUrl(string) 

Tanım:  View parametresi verilerek sayfanın yazdırılabilir biçimine erişmek için adres (url) almak amacıyla kullanılır.
Deklarasyon: 
public string GetPrintableFormatUrl(string _view)

•	IntegerToString(int, bool) 

Tanım: Integer veri tipini string veri tipine çevirmek için kullanılır. 
Deklarasyon: 
public string IntegerToString(int number, bool useThousandSeperator)

•	MakeDMItemSelector(System.Web.UI.WebControls.Button, 
System.Web.UI.WebControls.TextBox, bool, string) 

Tanım: Belge yönetim sistemindeki düğme için “dosya yolu seçimi” olanağı sağlamak için kullanılır.

Örnek:  
public void OnFormLoad() 
	{ 
	 	MakeDMItemSelector(Button1,Text1,true,"Library 1/Folder 1"); 
	} 
public void Button1_OnClick(Object sender, EventArgs e) 
	{ 
	 	ShowMessageBox(Text1.Text); 
	} 

•	MakeEditable(System.Web.UI.WebControls.WebControl) 

Tanım :  Verilen kontrol için değişiklik sağlamak için kullanılır. 

•	MakeEditable(System.Collections.Generic.List```<```WebControl```>```) 

Tanım :  WebControl listesi parametresi ile verilen kontrol için değişiklik sağlamak için kullanılır. 

•	MakeReadOnly(System.Web.UI.WebControls.WebControl) 

Tanım :  Verilen kontrolü salt okunur yapmak için kullanılır.

•	MakeReadOnly(System.Collections.Generic.List```<```WebControl```>```) 

Tanım :  WebControl listesi parametresi ile verilen kontrolü salt okunur yapmak için kullanılır.

•	MakeTextBoxAutoFormatted(System.Web.UI.WebControls.WebControl, bool, int, bool) 

Tanım:  Kullanıcının formdaki metin kutusuna sayısal veri ayarlamasına izin vermek için kullanılır. Bu yöntemle, ilgili sayısal veriler biçimlendirilebilir.

Örnek:  
public void OnFormLoad() 
{ 
MakeTextBoxAutoFormatted(Text1,true,2,true);                   

} 


•	RefreshDetails(eBAControls.eBATable) 

Tanım:  Form üzerindeki detaylar nesnesini yenilemek için kullanılır. 
Deklarasyon: 
protected void RefreshDetails(eBAControls.eBATable tbl)
Örnek:  
public void Button1_OnClick(Object sender, EventArgs e) 
{     
int globaldocid = 3;   DataRow newRow = Details1.CreateRow();   newRow["DOCUMENTID"] = globaldocid;   newRow["CHECKED"] = 0; 
Details1.InsertRow(newRow); 

RefreshDetails(Details1); 
} 

•	SetButtonToOpenUrlInNewWindow(System.Web.UI.WebControls.WebControl, string, bool) 

Tanım:  Formdaki bir düğme tıklatıldığında istenen adresi yönlendirmek üzere yeni bir tarayıcı penceresi açmak için kullanılır.
Deklarasyon: 
public void SetButtonToOpenUrlInNewWindow(WebControl control, string url, bool postback)
Örnek:
public void OnFormLoad() 
{ 
   SetButtonToOpenUrlInNewWindow(Button1,"https://bss.bimser.com",false); 
}

•	ShowMessageBox(string, string, eBAControls.eBABaseForm.eBAMessageBoxType) 
•	ShowMessageBox(string, string) 
•	ShowMessageBox(string, eBAControls.eBABaseForm.eBAMessageBoxType) 
•	ShowMessageBox(string) 

Tanım:  Form üzerinde istenen bir anda uyarı mesajı çıkartan metoddur. Sadece uyarı mesajı değeri alabilir, “Error”,”Information”,”Warning” eBAMessageBoxType  tipleri belirtilerek uyarının yapısı belirlenebilir veya uyarı detayı gösterilmesi sağlanabilir.

Deklarasyon:  
public void ShowMessageBox(string message, string detail, eBAControls.eBABaseForm.eBAMessageBoxType type)

public void ShowMessageBox(string message, string detail)

public void ShowMessageBox(string message, eBAControls.eBABaseForm.eBAMessageBoxType type)

public void ShowMessageBox(string message)

Örnek:
public void OnSaveData() 
{ 
   ShowMessageBox("Bilgiler Kaydediliyor"); 
}

•	ShowModalDocument(System.Web.UI.WebControls.WebControl, string, bool) 
•	ShowModalDocument(System.Web.UI.WebControls.WebControl, string, bool, eBAControls.ModalParameters parameters) 
•	ShowModalDocument(eBAControls.ModalParameters parameters) 

Tanım: Dokümanı form içinde Doküman Yönetim Sisteminde açmak için kullanılır
Deklarasyon: 
public void 
ShowModalDocument(System.Web.UI.WebControls.WebControl control, string filename, bool editable) 

Parametreler: 
control Dokümanı açacak form üzerindeki kontrolün adı 
filename Açılacak dosya yolu
editable  Düzenlenebilme durumu 

•	ShowModalForm(System.Web.UI.Control, string, string, string, bool, int, bool) 
•	ShowModalForm(System.Web.UI.Control, string, string, string, bool, int, bool, eBAControls.ModalParameters)  

Tanım :  Kodla modal form açmak için kullanılan metodlardır.
Deklarasyon:  
public void ShowModalForm(Control sender,string project, string form, string view, bool create, int documentId, bool readOnly)


public void ShowModalForm(Control sender,string project, string form, string view, bool create, int documentId, bool readOnly, ModalParameters parameters)

Parametreler:
Control sender : Form üzerinde modal formu açtırmak isteyen nesnedir
string project : Açtırılmak istenen formun bulunduğu proje. create parametresi true ise gerekli. Diğer durumlarda null olabilir
string form : Açtırılmak istenen formun adı. create parametresi true ise gerekli. Diğer durumlarda null olabilir


## 3.1.3.	Olaylar

•	OnFormLoad 

Tanım:Form yüklenirken çalışır. Hemen ardından OnLoadData çalışır.  

Deklarasyon: public void OnFormLoad() Örnek: 
public void OnFormLoad() 
{ 

} 

Not  Burada yapılan atamalar (Örnek: Text1.Text="sometext";), OnLoadData tarafından ezilebilir. Bu yüzden dikkat edilmelidir. Bu tür atamalar OnLoadData’da yapılmalıdır. 

•	OnValidateDocument 

Tanım: Özel doğrulamalar için kullanılır.  
Not Formdan farklı bir içerikte çalıştığı için, form kontrollerine doğrudan ulaşılamaz. Örneğin Text1 nesnesine form içinde Text1.Text ile ulaşılırken, burada Text1 yeterlidir. Validasyonun geçersiz olması için, summary değişkenine en az bir mesaj eklenmelidir. Aksi durumda, validasyon başarılı olur ve işlem takılmadan devam eder. 

Deklarasyon: 
public override void OnValidateDocument(string view, bool canEdit, Hashtable parameters, ValidationSummary summary) 
Parametreler:  
view: Validasyonu yapılacak formun o anda kullanılan view bilgisidir. 
canEdit: Validasyonu yapılan form için kullanıcının değişiklik yetkisini verir. parameters: Bazı özel parametereler burada bulunur. Tüm parametreler string tipindedir.  

LogonUser.Id: Logon olan kullanıcının kodudur. 
UserLanguage: Logon olan kullanıcının dilidir. 

Aşağıdaki parametreler sadece bir akış varsa geçerlidir. Aksi durumda parametreler de gelmezler. 

Request.Id: Kullanıcının seçtiği event kodu 
Request.Text: Kullanıcının seçtiği event adı 
Request.EventIcon: Kullanıcının seçtiği event ikonu 
Request.ReasonRequired: Kullanıcının seçtiği event için neden girilmesi zorunlumu 
Request.EventForm: Kullanıcının seçtiği event için event form tipi 
Request.Validate: Kullanıcının seçtiği event için validasyon aktifmi 
Request.Confirm: Kullanıcının seçtiği event için konfirmasyon yapıldımı 

Bu parametrelere erişirken öncelikle mevcut oldukları kontrolü yapılmalıdır. 

summary: Bu değişken içine atılan her mesaj kullanıcı arayüzünde validasyon mesajı olarak gelir. Formun validasyonun geçersiz olması için en az bir mesajın eklenmiş olması gereklidir. Aksi durumda validasyon başarılı kabul edilir. ValidationSummary sınıfı FlowDocumentInterface.dll inde anlatılmaktadır. 

Örnek: 
public override void OnValidateDocument(string view, bool canEdit, Hashtable parameters, ValidationSummary summary) 
{ 
if (Text1!=null && Text1```>```100 && Text2==null)  
{ summary.AddMessage("Text2 değerini giriniz"); } 
} 


•	OnLoadData 

Tanım:OnFormLoad dan sonra çalışır. Dökümanın verisini veritabanından okunup forma yüklendikten hemen sonra çalışır.  
Not Herhangi bir alana yükleme sonrası kod ile müdahale edilecek ise, bu metot içinde yapılmalıdır.  

Deklarasyon: public void OnLoadData() Örnek: 
public void OnLoadData() 
{ 
  string data = “veri”; 
  Text1.Text = data; 
} 







•	OnSaveData 

Tanım:Form verilerinin kaydedilme işleminden hemen önce çalışır. Bu işlemden önce içeriği değiştirilmek istenilen alanların içeriği değiştirilebilir ve/veya özel veri kaynaklarına kaydetme işlemleri yapılabilir. 
Deklarasyon: public void OnSaveData() 
Örnek: 
public void OnSaveData() 
{ 
string data = Text1.Text; 
//save data to other operational systems 
} 

•	OnAfterSaveData 

Tanım:Form verilerinin kaydedilme işleminden sonra çalışır.  Deklarasyon: public void OnAfterSaveData() 
Örnek: 
public void OnAfterSaveData() 
{ 

} 

•	OnBeginEdit 

Tanım: Form edit moduna girdikten sonra çalışır. Deklarasyon: public void OnBeginEdit() 
Örnek: 
public void OnBeginEdit() 
{ 
Text1.BackColor = System.Drawing.Color.Red;               
} 

•	OnEndEdit 

Tanım: Form edit modundan çıktıktan sonra çalışır. Deklarasyon: public void OnEndEdit() 
Örnek: 
public void OnEndEdit() 
{ 
Text1.BackColor = System.Drawing.Color.White;                             
} 


•	OnModalLoad 

Tanım: Form eğer modal olarak açılıyorsa bu event çalışır. Ana formdan modala parametre geçilirken kullanılabilir. 
Deklarasyon: public void OnModalLoad(ModalParameters parameters) Parametreler:  
parameters: Modal parametreleridir. 

Örnek: 
public void OnModalLoad(ModalParameters parameters) 
{ 
string testparam1=parameters["testparam1"].ToString();   	
int testparam2=(int)parameters["testparam2"];  
Metin2.Text=testparam1 + " " + testparam2.ToString();  
} 

•	OnModalUnload 

Tanım: Form eğer modal olarak açılmışsa ve daha sonra kapatılıyorsa bu event çalışır.  Deklarasyon: public void OnModalUnload(eBAModalEventArgs args) 
Parametreler:  
args: Modal event parametreleridir. İçinde, modalın geridönüş değeri ve parametreleri bulunur. 

Örnek: 
public void OnModalUnload(eBAModalEventArgs args) 
{ 
if (args.modalResult == ModalResult.Ok)  
{       	
args.parameters.Add("test",Metin1.Text); 
	 }               
} 

Not Modal kapanırken, ana forma parametre geçilecek ise, bu işlem burada yapılabilir. 

•	OnModalReturn 

Tanım: Eğer formda bir modal form açılmışsa ve kapatılıp ana forma dönülüyorsa ana formda bu event çalışır.  

Deklarasyon: public void OnModalReturn(object sender, eBAModalEventArgs e) Parametreler:  
sender: Modal formu açtıran nesnedir. 
e: Modal event parametreleridir. İçinde, modalın geridönüş değeri ve parametreleri bulunur. 

Örnek: 
public void OnModalReturn(object sender, eBAModalEventArgs e) 
{  
if (e.modalResult == ModalResult.Ok) 
	  { 
Text1.Text = e.parameters["test"].ToString();  
} 
} 
            Not Modal formdan ana forma geçilen parametrelere buradan erişilebilir. 

•	OnCopy 

Tanım: Başka bir formdan kopyalanmış veri yapıştırılırken tetiklenir. Deklarasyon: public void OnCopy(eBACopyEventArgs args) 
Parametreler:  
args: Kopyalama parametreleridir. İçinde, kopyalanan dokümanın global id si bulunur. 

Örnek: 
public void OnCopy(eBACopyEventArgs args) 
{ 
	            int sourceId = args.SourceId;   
} 


## 3.2. Metin Kutusu 

![](https://docsbimser.blob.core.windows.net/imagecontainer/s2-a59fbd6b-f485-4703-b5b6-8a2ad4a79809.png)

Metin Kutusu nesnesi veri tipine göre kontrol sınıfı ve validasyon değer tipi değişmektedir. Aşağıdaki tabloda bu değişiklik gösterilmektedir.  Metin kutusunun özellikleri TextBox ve eBADateTimeBox sınıfları başlıklarında ayrı ayrı ele alınıp, Validasyon bölümünde de metin kutusu nesnesinin formun OnValidateDocument olayında kullanımı açıklanmıştır. 


## 3.2.1. TextBox 

Text Box; Metin, Tamsayı, Virgüllü Sayı yada Para veri tipindeki metin kutusu nesnelerinin türediği sınıftır. 

### 3.2.1.1.  Özellikler 

•	Text 

Tanım: Metin kutusu içindeki metni değiştirmek yada almak için kullanılır. 
Tipi: System.String 
Deklarasyon: public string Text { get; set; } 

•	MaxLength 

Tanım: Metin kutusu içine karakter sayısı girişini sınırlandırır. Sıfır değeri için kısıtlama çalışmaz. 
Tipi: System.Int32 
Deklarasyon: public int MaxLength { get; set; } 

•	ReadOnly 

Tanım: Metin kutusunun içeriği “true” ise değiştirilemez “false” ise değiştirilebilir. 
Tipi: System.Boolean 
Deklarasyon: public bool ReadOnly { get; set; } 


•	BackColor 
Tanım: Metin kutusunun arka plan rengini belirler. 
Tipi: System.Drawing.Color 
Deklarasyon: public System.Drawing.Color BackColor { get; set; } 
Örnek: 
Text1.BackColor = System.Drawing.Color.Empty;  //Renk yok 
Text1.BackColor = System.Drawing.Color.Red;     //Kırmızı arka plan rengi 


•	ForeColor 
Tanım: Metin kutusunun yazı rengini belirler. 
Tipi: System.Drawing.Color 
Deklarasyon: public System.Drawing.Color ForeColor { get; set; } 

•	Visible 
Tanım: Nesnenin görünür olup olmayacağını belirler. 
Tipi: System.Boolean 
Deklarasyon: public bool Visible { get; set; } 


3.2.2. eBADateTimeBox 
     ebaDateTimeBox; Tarih veri tipindeki metin kutusu nesnelerinin türediği sınıftır. 

3.2.2.1.  Özellikler 

•	Value 

Tanım: Tarih kutusuna girilen tarih değerini DateTime olarak verir.  
Tipi: System.DateTime 
Deklarasyon: public System.DateTime Value { get; set; } 
Örnek: 
DateTime dt = DateTime.Now; 
if (Text1.IsValid) 
 	{ 
	  	dt=Text1.Value; 
} 
Not Eğer geçersiz bir tarih girilmiş ise, hata oluşur. Bu yüzden öncelikle, IsValid ile, geçerli bir değer olup olmadığı kontrol edilmelidir. 

•	Text 

Tanım: Tarih kutusuna girilen değeri kısa tarih metin olarak verir.  
Tipi: System. String 
Deklarasyon: public string Text { get; } 

Not Eğer geçerli bir tarih yoksa boşluk döner. 

•	IsEmpty 

Tanım: Metin kutusuna geçersizde olsa bir giriş olup olmadığını gösterir. 
Tipi: System. Boolean  
Deklarasyon: public bool IsEmpty { get; } 

•	IsValid 

Tanım: Girilmiş olan tarih değerinin geçerli bir tarih olup olmadığını verir. 
Tipi: System. Boolean  
Deklarasyon: public bool IsValid { get; } 

•	DateTimeFormat 

Tanım: Tarih metinin görünümünü belirler. 
Tipi: eBADateTimeFormat 
Deklarasyon: public eBADateTimeFormat DateTimeFormat { get; set; } 
Örnek: 
public enum eBADateTimeFormat { DateAndTime, DateOnly } Text1.DateTimeFormat = eBADateTimeFormat. DateOnly; 

•	ManuelEntryEnable 

Tanım: Tarih girişinin manuel olarak yapılıp yapılmayacağını belirtir.  
Tipi: System.Boolean 
Deklarasyon: public bool ManuelEntryEnable { get; set; } 

Not Manuel giriş kapalı ise sadece takvimden seçim yapılabilir. 

•	ReadOnly 
Tanım: Metin kutusunun içeriği “true” ise değiştirilemez “false” ise değiştirilebilir. 
Tipi: System.Boolean 
Deklarasyon: public bool ReadOnly { get; set; } 

•	Visible 
Tanım: Nesnenin görünür olup olmayacağını belirler. 
Tipi: System.Boolean 
Deklarasyon: public bool Visible { get; set; } 


## 3.2.3. Validasyon 

Validasyon kodlamasında, değişken tipi veri tipine göre belirlenir. Bu kısımda sadece veriye erişim olup, kontrole erişim yoktur. Değişken tiplerine karşılık gelen veri tiplerini Tablo 1’de inceleyebilirsiniz. 

Örnek: 
Metin tipinde bir metin kutusu için validasyon kodlaması aşağıda gösterilmektedir. 

public override void OnValidateDocument(string view, bool canEdit, Hashtable parameters, ValidationSummary summary) 
{ 
   	string valueText1 = Text1; 
   	if (valueText1!=null && valueText1.Length!=10) 
{       	summary.AddMessage("Length of Text1 must be 10 characters"); 
 	} 
} 

Örnek: 
Tamsayı tipinde nümerik bir metin kutusu için validasyon kodlaması aşağıda gösterilmektedir. 

public override void OnValidateDocument(string view, bool canEdit, Hashtable parameters, ValidationSummary summary) 
{ 
   	Nullable```<```int```>``` valueText1 = Text1; 
   	if ((!valueText1.HasValue) && (valueText1.Value```>```100 || valueText1.Value```<```1)) 
{       	summary.AddMessage("Value of Text1 must be between 0 and 100"); 
} 
} 

    Not String dışındaki Nullable olan tipler için, HasValue özelliği, değişken değerin null olup olmadığını, Value değeri ise değişkenin değerini vermektedir. 


## 3.3. Etiket 

System.Web.UI.WebControls.Label sınıfı tipindedir. Veri girişi olmadığından validasyona girmemektedir. 

### 3.3.1. Özellikler 

•	Text 

Tanım:. Etiketin metin kısmını belirler. 
Tipi: System.String 
Deklarasyon: public string Text { get; set; } 

•	BackColor 

Tanım:Etiketin arka plan rengini belirler. 
Tipi: System.Drawing.Color 
Deklarasyon: public System.Drawing.Color BackColor { get; set; } 
Örnek: 
Label1.BackColor = System.Drawing.Color.Empty;  //Renk yok 
Label1.BackColor = System.Drawing.Color.Red;     //Kırmızı arka plan rengi 

•	ForeColor 

Tanım: Etiketin yazı rengini belirler. 
Tipi: System.Drawing.Color 
Deklarasyon: public System.Drawing.Color ForeColor { get; set; } 

•	Visible 

Tanım: Nesnenin görünür olup olmayacağını belirler. 
Tipi: System.Boolean 
Deklarasyon: public bool Visible { get; set; 


## 3.4. Tek Seçimlik Liste 

Tek seçimlik liste nesne sınıfı, grid özelliğinin açık olup olmamasına göre değişmektedir. Grid özelliği kapalı iken normal bir liste gibi çalışır. Grid modunda ise yeni bir ekrandan seçim yapılmaktadır.  

![](https://docsbimser.blob.core.windows.net/imagecontainer/s3-66cab700-fb3c-4c80-94e8-6ffd6276e7cf.png)


Tablo 2’de listeleme moduna göre kontrol sınıfları ait olduğu gösterilmektedir. Aşağıda bu 2 kontrol sınıfının özellikleri ayrı, olayları ve validasyon bilgisi birlikte ele alınmaktadır. 


## 3.4.1. DropDownList 

Standart liste modunda iken nesnenin sınıfıdır. 

### 3.4.1.1.  Özellikler 

•	SelectedItem 

Tanım: Liste içinde seçili elemanı döner. Seçim yapılmamış ise null döner. 
Tipi: System.Web.UI.WebControls.ListItem 
Deklarasyon: public System.Web.UI.WebControls.ListItem SelectedItem { get; } Örnek: 
if (List1.SelectedItem==null) 
{ 
Text1.Text="no selection"; 
} else 
{ 
Text1.Text=List1.SelectedItem.Text + " - " + 
List1.SelectedItem.Value;  
} 





•	SelectedIndex 

Tanım: Seçim yapılan elamanın sıra numarasını verir. Seçim yapılmamış ise -1 numarasını alır. Bu değere, atama yapılarak, istenilen sıradaki elemanın seçili olması sağlanabilir. 
Tipi: System.Int32 
Deklarasyon: public int SelectedIndex { get; set; } 

•	SelectedValue 

Tanım: Seçili elemanın değerini verir. Seçim yok ise boş değer verir. Bu değere, atama yapılarak, istenilen değere ait eleman, seçili hale getirilebilir. 
Tipi: System.String 
Deklarasyon: public string SelectedValue { get; set; } 

•	Items 

Tanım: Elemanların listesini verir. 
Tipi: System.Web.UI.WebControls.ListItemCollection 
Deklarasyon: public virtual System.Web.UI.WebControls.ListItemCollection Items { get; } 
Örnek: 
foreach(ListItem item in List1.Items) 
	{ 
		if (item.Value=="2")  
	      	{ 
	        	 	Text1.Text = item.Text; 
	      	} 
	} 

•	Enabled 

Tanım:. Seçim yapılıp yapılamayacağını belirler. 
Tipi: System.Boolean 
Deklarasyon: public bool Enabled { get; set; } 

•	Visible 

Tanım: Nesnenin görünür olup olmayacağını belirler. 
Tipi: System.Boolean 
Deklarasyon: public bool Visible { get; set; } 


## 3.4.2. eBACombobox 

Grid modunda nesnenin sınıfıdır. 

### 3.4.2.1.  Özellikler 

•	Text 

Tanım: Seçili elemanın kullanıcıya görünen metin kısmıdır. 
Tipi: System.String 
Deklarasyon: public string Text { get; set; } 

•	Value 

Tanım: Seçili elemanın değeridir. 
Tipi: System.String 
Deklarasyon: public string Value { get; set; } 

•	DeleteEnable 

Tanım: “true” ise seçili elemanı silmek için buton gelir. 
Tipi: System.Boolean 
Deklarasyon: public bool DeleteEnable { get; set; } 

•	ManuelEntryEnable 

Tanım: “true” ise kullanıcı klavye ile giriş yapabilir. Bu durumda değer bilgisi ile metin bilgisi aynı olur. 
Tipi: System.Boolean 
Deklarasyon: public bool ManuelEntryEnable { get; set; } 

•	ReadOnly 

Tanım: Nesnenin verisinin değiştirilip değiştirilmeyeceğini belirler. 
Tipi: System.Boolean 
Deklarasyon: public bool ReadOnly { get; set; } 

•	Visible 

Tanım: Nesnenin görünür olup olmayacağını belirler. 
Tipi: System.Boolean 
Deklarasyon: public bool Visible { get; set; } 

•	BackColor 

Tanım: Nesnenin arka plan rengini belirler. 
Tipi: System.Drawing.Color 
Deklarasyon: public System.Drawing.Color BackColor { get; set; } 
Örnek: 
Label1.BackColor = System.Drawing.Color.Empty;  //Renk yok 
Label1.BackColor = System.Drawing.Color.Red;     //Kırmızı arka plan rengi 

•	ForeColor 

Tanım: Nesnenin yazı rengini belirler. 
Tipi: System.Drawing.Color 
Deklarasyon: public System.Drawing.Color ForeColor { get; set; } 


## 3.4.3. Olaylar 

•	OnAfterChange 

Tanım: Seçim işlemi yapıldıktan hemen sonra çalışır. 
Deklarasyon: public void OnAfterChange(Object sender, eBAListEventArgs e,DataRowView row) 
Parametreler:  
sender: Liste nesnesidir. 
e: Olay parametreleridir. Olayın seçim ve silme işlemlerinden hangisi durumunda gerçekleştiğini verir. 
	 	public enum eBAListAction { Select, Delete } 
row: Nesne veritabanına bağlı ise seçilen satırın bilgilerini verir. Veritabanına bağlı değil ise null değerindedir. 
Örnek: 
public void List1_OnAfterChange(Object sender, eBAListEventArgs e,DataRowView row) 
{ 
if (List1.SelectedItem.Value==null) 
{ 
	      	Text1.Text = String.Empty; 
	 	} 
	   	else 
	 	{ 
	      	Text1.Text = List1.SelectedItem.Value; 
 	}                                           } 

Örnek: 
public void List1_OnAfterChange(Object sender, eBAListEventArgs e,DataRowView row) 
{ 
if (e.Action==eBAListAction.Select) 
	   	{ 
	      	if (row["OSUSERS_FIRSTNAME"]==null) 
	      	{ 
	        	 	Text1.Text = String.Empty; 
      	}       	else 
	      	{ 
	        	 	Text1.Text = row["OSUSERS_FIRSTNAME"].ToString(); 
	      	} 
	   	} 
	   	else if (e.Action==eBAListAction.Delete) 
	   	{ 
	      	Text1.Text = 
String.Empty;                                           
	   	} 
} 


•	OnBeforeChange 

Tanım: Seçimden önce çalışır. Nesne standart modda iken çalışmaz. Yalnızca grid moddayken çalışır. 
Deklarasyon: public void OnBeforeChange(Object sender, eBAListEventArgs e,DataRowView row) 
Parametreler:  
sender: Liste nesnesidir. 
e: Olay parametreleridir. Olayın seçim ve silme işlemlerinden hangisi durumunda gerçekleştiğini verir. Kullanımına ilişkin örnekler için OnAfterChange olayını inceleyiniz. 
row: Nesne veritabanına bağlı ise seçilen satırın bilgilerini verir. Veritabanına bağlı değil ise null değerindedir. 



## 3.4.4. Validasyon 

Validasyon için iki adet string değer mevcuttur. Birisi seçili elemanın değeri, diğeri ise metin kısmı içindir. 

string [Name];  //Seçili elemanın değeri string [Name]_Text;  //Seçili elemanın metin değeri  Örneğin List1 için 
	  	string List1; 
string List1_Text;  olacaktır. 

public override void OnValidateDocument(string view, bool canEdit, Hashtable parameters, ValidationSummary summary) 
{ 
string valueList1 = List1; 
	   	if (valueList1!=null && valueList1.Equals(“testvalue”)) 
	 	{ 
	      	summary.AddMessage("You have selected " + (List1_Text == null ? 
String.Empty : List1_Text));  	} 
} 


## 3.5. Çok Seçimlik Liste 

Çok seçimlik liste nesnesi, System.Web.UI.WebControls.ListBox sınıfındadır. 

### 3.5.1. Özellikler 

•	SelectedItem 

Tanım:. Liste içinde seçili elemanı döner. Seçim yapılmamış ise null döner. Çoklu seçim açıkken, ilk seçili elemanı getirir. 
Tipi: System.Web.UI.WebControls.ListItem 
Deklarasyon: public System.Web.UI.WebControls.ListItem SelectedItem { get; } Örnek: 
if (List1.SelectedItem==null) 
{ 
Text1.Text="no selection"; 
} else 
{ 
Text1.Text=List1.SelectedItem.Text + " - " + 
List1.SelectedItem.Value;  
} 

•	SelectedIndex 

Tanım: Seçim yapılan elamanın sıra numarasını verir. Çoklu seçim açık ise ilk elemanın sıra numarasını verir. Seçim yapılmamış ise -1 numarasını alır. Bu değere, atama yapılarak, istenilen sıradaki elemanın seçili olması sağlanabilir. 
Tipi: System.Int32 
Deklarasyon: public int SelectedIndex { get; set; } 

•	SelectedValue 

Tanım: Seçili elemanın değerini verir. Çoklu seçim açık ise ilk seçili değeri verir. Seçim yok ise boş değer verir. Bu değere, atama yapılarak, istenilen değere ait eleman seçili hale getirilebilir. 
Tipi: System.String 
Deklarasyon: public string SelectedValue { get; set; } 





•	Items 

Tanım: Elemanların listesini verir. 
Tipi: System.Web.UI.WebControls.ListItemCollection 
Deklarasyon: public virtual System.Web.UI.WebControls.ListItemCollection Items { get; } 
Örnek: 
string s=""; 
	   	foreach(ListItem item in List1.Items) 
	   	{ 
	     	 if (item.Selected)  
	     	 { 
	       	 	 s+=item.Text + "(" + item.Value + ") - "; 
	      	 } 
	   	} 
	   	Text1.Text=s; 

•	Enabled 

Tanım: Seçim yapılıp yapılamayacağını belirler. 
Tipi: System.Boolean 
Deklarasyon: public bool Enabled { get; set; } 

•	Visible 

Tanım: Nesnenin görünür olup olmayacağını belirler. 
Tipi: System.Boolean 
Deklarasyon: public bool Visible { get; set; } 

•	SelectionMode

Tanım: Seçim modu
Tipi: System.Web.UI.WebControls.ListSelectionMode
Deklarasyon: public virtual System.Web.UI.WebControls.ListSelectionMode SelectionMode { get; set; }
Alacağı Değerler;
		Multiple: Çoklu
		Single: Tekli

•	BorderColor 

Tanım: Nesnenin kenar rengidir
Tipi: System.Drawing.Color
Deklarasyon: public override System.Drawing.Color BorderColor { get; set; }

•	BorderStyle

Tanım: Nesnenin kenar stili
Tipi: System.Web.UI.WebControls.BorderStyle
Deklarasyon: public override System.Web.UI.WebControls.BorderStyle BorderStyle { get; set; }
Alacağı Değerler;
		Dashed: Kesik 
Dotted: Noktalı
Double: Çift
Groove: Oluk
Inset: Ek
None: Yok 
NotSet: Atanmadı
Outset: Başlangıç
Ridge: Kabarık çizgi
Solid: Koyu



### 3.5.2. Metotlar 

•	GetSelectedIndices 

Tanım: Seçili elemanların indexlerini dizi olarak verir. 
Deklarasyon: public int[] GetSelectedIndices(); 
Örnek: 
public void Button1_OnClick(Object sender, EventArgs e) 
{ 
	  	Text1.Text=""; 
	  	foreach(int index in List1.GetSelectedIndices()) 
	  	{ 
	     	Text1.Text+=List1.Items[index].Text + " - "; 
	   	} 
} 


### 3.5.3. Olaylar 

•	OnChange 

Tanım: Seçim işlemi yapıldıktan hemen sonra çalışır. Çoklu seçimlerde ctrl tuşu basılı olarak yapılan her seçimden sonra çalışır. 
Deklarasyon: public void OnChange(object sender, EventArgs e) 
Parametreler:  
sender: Liste nesnesidir. 
e: Olay parametreleridir. 
Örnek: 
public void List1_OnChange(object sender, EventArgs e) 
{ 
string s=""; 
foreach(ListItem item in List1.Items) 
{ 
	   	 	if (item.Selected)  
	      	{ 
	         	 	 s+=item.Text + "(" + item.Value + ") - "; 
	      	} 
	   	} 
	   	Text1.Text=s;                                           
} 


### 3.5.4. Validasyon 

Validasyon kodlamasında seçili elemanları veren bir liste mevcuttur. 

Örnekte değeri “2” olan eleman seçildiğinde validasyon sağlanmayacaktır. 

public override void OnValidateDocument(string view, bool canEdit, Hashtable parameters, ValidationSummary summary) 
{ 
  	foreach(eBAListItem item in List1) 
     { 
         	 	if (item.Value.Equals("2")) 
 	 	{ 
         	 	 	summary.AddMessage(item.Text + " is selected"); 
 	 	} 
     }                       
} 


## 3.6. Çoklu Seçim Kutusu 

Çoklu seçim kutusu System.Web.UI.WebControls.CheckBox sınıfındadır. 

### 3.6.1. Özellikler 

•	Checked 

Tanım: Nesnenin seçili olup olmadığını belirtir. 
Tipi: System.Boolean 
Deklarasyon: public bool Checked { get; set; } 
Örnek: 
public void Button1_OnClick(Object sender, EventArgs e) 
{ 
	   	 	if (CheckBox1.Checked) 
	      	{ 
Text1.Text="checked"; 
}   else 
{ 
	      	 	Text1.Text="not checked";  
	 	 	} 
}   



### 3.6.2. Olaylar 

•	OnCheckedChanged 

Tanım: Seçim işlemi yapıldıktan hemen sonra çalışır. 
Deklarasyon: public void OnCheckedChanged(Object sender, EventArgs e) Parametreler:  
sender: Seçim nesnesidir. 
e: Olay parametreleridir. 

Örnek: 
public void CheckBox1_OnCheckedChanged(Object sender, EventArgs e) 
{ 
	   	 	if (CheckBox1.Checked) 
{ 
	      	 	Text1.Text="checked"; 
   	 	} else 
{ 
	      	 	Text1.Text="not checked";  
} 
} 


## 3.6.3. Validasyon 

Validasyon kodlamasında seçim durumunu veren bir değişken mevcuttur. 

public Nullable```<```bool```>``` objectname; 

Örnekte CheckBox1 seçilmemişse Text1 e giriş yapmanın zorunlu olduğu durum kodlanmıştır. 

public override void OnValidateDocument(string view, bool canEdit, Hashtable parameters, ValidationSummary summary) 
{ 
  	if 	(((!CheckBox1.HasValue) 	|| 	(!CheckBox1.Value)) 	&& string.IsNullOrEmpty(Text1)) 
   	{ 
      	summary.AddMessage("Text1 must be entered"); 
   	} 
} 


## 3.7. Tekli Seçim Kutusu 

Tekli seçim kutusu System.Web.UI.WebControls.RadioButton sınıfındadır. 

### 3.7.1. Özellikler 

•	Checked 

Tanım: Nesnenin seçili olup olmadığını belirtir. 
Tipi: System.Boolean 
Deklarasyon: public bool Checked { get; set; } 
Örnek: 
public void Button1_OnClick(Object sender, EventArgs e) 
{ 
	   	 	if (RadioButton1.Checked) 
	      	{ 
Text1.Text="checked"; 
}   else 
{ 
	      	 	Text1.Text="not checked";  
	 	 	} 
}  

•	Text 

Tanım: Nesnenin başlık bilgisini belirtir. 
Tipi: System.String 
Deklarasyon: public string Text { get; set; } 

•	GroupName

Tanım: Nesnenin dahil olduğu grup bilgisi
Tipi: System.String 
Deklarasyon: public virtual string GroupName { get; set; }


### 3.7.2. Olaylar 

•	OnCheckedChanged 

Tanım: Seçim işlemi yapıldıktan hemen sonra çalışır. 
Deklarasyon: public void OnCheckedChanged(Object sender, EventArgs e) Parametreler:  
sender: Seçim nesnesidir. 
e: Olay parametreleridir. 

Örnek: 
public void RadioButton1_OnCheckedChanged(Object sender, EventArgs e) { 
	   	 	Text1.Text = "Radiobutton1 is checked";  
} 
  public void RadioButton2_OnCheckedChanged(Object sender, EventArgs e) { 
	   	 	Text1.Text = "Radiobutton2 is checked";  
} 


### 3.7.3. Validasyon 

Validasyon kodlamasında seçim durumunu veren bir değişken mevcuttur. 

public Nullable```<```bool```>``` objectname; 

Örnekte Radiobutton1 seçilmemişse Text1 e giriş yapmanın zorunlu olduğu durum kodlanmıştır. 

public override void OnValidateDocument(string view, bool canEdit, Hashtable parameters, ValidationSummary summary) 
{ 
	if 	(((!Radiobutton1.HasValue) 	|| 	(!Radiobutton1.Value)) 	&& 
string.IsNullOrEmpty(Text1)) 
  { 
     summary.AddMessage("Text1 must be entered");   } 
} 


## 3.8. Çoklu Seçim Listesi 

Birden çok çoklu seçim kutusunu tek tek forma eklemektense, çoklu seçim listesi nesnesi kullanılarak listeye girilen elemanlar kadar çoklu seçim kutuları oluşturulması sağlanabilir.
Çoklu seçim listesi nesnesi “System.Web.UI.WebControls.CheckBoxList” sınıfındandır. 


### 3.8.1. Özellikler 

•	Enabled

Tanım: Nesnenin görünürlük durumu
Tipi: System.Boolean 
Deklarasyon: public bool Enabled { get; set; } 

•	Visible 

Tanım: Nesnenin görünür olup olmayacağını belirler. 
Tipi: System.Boolean 
Deklarasyon: public bool Visible { get; set; } 

•	BorderColor 

Tanım: Nesnenin kenar rengidir
Tipi: System.Drawing.Color
Deklarasyon: public override System.Drawing.Color BorderColor { get; set; }

•	BorderStyle

Tanım: Nesnenin kenar stili
Tipi: System.Web.UI.WebControls.BorderStyle
Deklarasyon: public override System.Web.UI.WebControls.BorderStyle BorderStyle { get; set; }
Alacağı Değerler;
		Dashed: Kesik 
Dotted: Noktalı
Double: Çift
Groove: Oluk
Inset: Ek
None: Yok 
NotSet: Atanmadı
Outset: Başlangıç
Ridge: Kabarık çizgi
Solid: Koyu

•	SelectedItem 

Tanım:. Liste içinde seçili elemanı döner. Seçim yapılmamış ise null döner. Çoklu seçim açıkken, ilk seçili elemanı getirir. 
Tipi: System.Web.UI.WebControls.ListItem 
Deklarasyon: public System.Web.UI.WebControls.ListItem SelectedItem { get; } Örnek: 
if (List1.SelectedItem==null) 
{ 
Text1.Text="no selection"; 
} else 
{ 
Text1.Text=List1.SelectedItem.Text + " - " + 
List1.SelectedItem.Value;  
} 

•	SelectedIndex 

Tanım: Seçim yapılan elamanın sıra numarasını verir. Çoklu seçim açık ise ilk elemanın sıra numarasını verir. Seçim yapılmamış ise -1 numarasını alır. Bu değere, atama yapılarak, istenilen sıradaki elemanın seçili olması sağlanabilir. 
Tipi: System.Int32 
Deklarasyon: public int SelectedIndex { get; set; } 

•	SelectedValue 

Tanım: Seçili elemanın değerini verir. Çoklu seçim açık ise ilk seçili değeri verir. Seçim yok ise boş değer verir. Bu değere, atama yapılarak, istenilen değere ait eleman seçili hale getirilebilir. 
Tipi: System.String 
Deklarasyon: public string SelectedValue { get; set; } 

•	Items 

Tanım: Elemanların listesini verir. 
Tipi: System.Web.UI.WebControls.ListItemCollection 
Deklarasyon: public virtual System.Web.UI.WebControls.ListItemCollection Items { get; } 
Örnek: 
string s=""; 
	   	foreach(ListItem item in List1.Items) 
	   	{ 
	     	 if (item.Selected)  
	     	 { 
	       	 	 s+=item.Text + "(" + item.Value + ") - "; 
	      	 } 
	   	} 
	   	Text1.Text=s; 


### 3.8.2. Metotlar 

•	ClearSelection()

Tanım: Seçimleri temizler 
Deklarasyon: public virtual void ClearSelection()
Örnek: 
public void Buton1_OnClick(Object sender, EventArgs e)
{
   CokluSecimListesi1.ClearSelection();
}


### 3.8.3. Olaylar 

•	SelectedIndexChanged

Tanım: Seçim işlemi yapıldıktan hemen sonra çalışır. 
Deklarasyon: public void SelectedIndexChanged(Object sender, EventArgs e)
Parametreler:  
sender: Seçim nesnesidir. 
e: Olay parametreleridir. 

Örnek: 
public void SecimListesi1_SelectedIndexChanged(object sender, EventArgs e)
{
   Metin1.Text = CokluSecimListesi1.SelectedValue;
} 



### 3.8.4. Validasyon 

Validasyon kodlamasında seçili elemanları veren bir liste mevcuttur.
public List```<```eBAListItem```>``` objectname;
eBAListItem Sınıfı;
public string Value;
public string Text;
Aşağıdaki örneğe göre, değeri “2” olan eleman seçildiğinde uyarı verilecektir.
public override void OnValidateDocument(string view, bool canEdit, Hashtable parameters, ValidationSummary summary)
{
    foreach(eBAListItem item in CokluSecimListesi1)
    {
        if (item.Value.Equals("2"))
        summary.AddMessage(item.Text + " is selected");
    }        
}


## 3.9. Tekli Seçim Listesi 

Birden çok tekli seçim kutusunu tek tek forma eklemektense, tekli seçim listesi nesnesi kullanılarak aynı gruba dahil tekli seçimleri liste halinde sıralayan bir yapı elde edilebilir.

Tekli Seçim Listesi nesnesi, “System.Web.UI.WebControls.RadioButtonList” sınıfındandır.


### 3.9.1. Özellikler 

•	Enabled

Tanım: Nesnenin görünürlük durumu
Tipi: System.Boolean 
Deklarasyon: public bool Enabled { get; set; } 

•	Visible 

Tanım: Nesnenin görünür olup olmayacağını belirler. 
Tipi: System.Boolean 
Deklarasyon: public bool Visible { get; set; } 

•	BorderColor 

Tanım: Nesnenin kenar rengidir
Tipi: System.Drawing.Color
Deklarasyon: public override System.Drawing.Color BorderColor { get; set; }

•	BorderStyle

Tanım: Nesnenin kenar stili
Tipi: System.Web.UI.WebControls.BorderStyle
Deklarasyon: public override System.Web.UI.WebControls.BorderStyle BorderStyle { get; set; }
Alacağı Değerler;
		Dashed: Kesik 
Dotted: Noktalı
Double: Çift
Groove: Oluk
Inset: Ek
None: Yok 
NotSet: Atanmadı
Outset: Başlangıç
Ridge: Kabarık çizgi
Solid: Koyu

•	SelectedItem 

Tanım:. Liste içinde seçili elemanı döner. Seçim yapılmamış ise null döner. Çoklu seçim açıkken, ilk seçili elemanı getirir. 
Tipi: System.Web.UI.WebControls.ListItem 
Deklarasyon: public System.Web.UI.WebControls.ListItem SelectedItem { get; } Örnek: 
if (List1.SelectedItem==null) 
{ 
Text1.Text="no selection"; 
} else 
{ 
Text1.Text=List1.SelectedItem.Text + " - " + 
List1.SelectedItem.Value;  
} 

•	SelectedIndex 

Tanım: Seçim yapılan elamanın sıra numarasını verir. Çoklu seçim açık ise ilk elemanın sıra numarasını verir. Seçim yapılmamış ise -1 numarasını alır. Bu değere, atama yapılarak, istenilen sıradaki elemanın seçili olması sağlanabilir. 
Tipi: System.Int32 
Deklarasyon: public int SelectedIndex { get; set; } 

•	SelectedValue 

Tanım: Seçili elemanın değerini verir. Çoklu seçim açık ise ilk seçili değeri verir. Seçim yok ise boş değer verir. Bu değere, atama yapılarak, istenilen değere ait eleman seçili hale getirilebilir. 
Tipi: System.String 
Deklarasyon: public string SelectedValue { get; set; } 

•	Items 

Tanım: Elemanların listesini verir. 
Tipi: System.Web.UI.WebControls.ListItemCollection 
Deklarasyon: public virtual System.Web.UI.WebControls.ListItemCollection Items { get; } 
Örnek: 
string s=""; 
	   	foreach(ListItem item in List1.Items) 
	   	{ 
	     	 if (item.Selected)  
	     	 { 
	       	 	 s+=item.Text + "(" + item.Value + ") - "; 
	      	 } 
	   	} 
	   	Text1.Text=s; 


### 3.9.2. Metotlar 

•	ClearSelection()

Tanım: Seçimleri temizler 
Deklarasyon: public virtual void ClearSelection()
Örnek: 
public void Buton1_OnClick(Object sender, EventArgs e)
{
   SecimListesi1.ClearSelection();
}


### 3.9.3. Olaylar 

•	SelectedIndexChanged

Tanım: Seçim işlemi yapıldıktan hemen sonra çalışır. 
Deklarasyon: public void SelectedIndexChanged(Object sender, EventArgs e)
Parametreler:  
sender: Seçim nesnesidir. 
e: Olay parametreleridir. 

Örnek: 
public void SecimListesi1_SelectedIndexChanged(object sender, EventArgs e)
{
   Metin1.Text = SecimListesi1.SelectedValue;
}



### 3.9.4. Validasyon 

Tekli Seçim Listesi nesnesine validasyon kod kısmında erişmek için iki adet string değer mevcuttur. Birisi seçili elemanın değeri, diğeri ise metin kısmı içindir.
string [Name];	Seçili elemanın değeri
string [Name]_Text;	Seçili elemanın metin değeri
Örneğin “SecimListesi1” isimli bir tekli seçim listesi için;
string SecimListesi1;       //SecimListesi1 de seçili elemanın değeri
string SecimListesi1_Text;       //SecimListesi1 de seçili elemanın metin değeri

Örneğin; Form üzerindeki  “SecimListesi1”  isimli tekli seçim listesi nesnesinde değeri 1 olan eleman seçilmişse ya da metin değeri “eleman2” olan eleman seçilmişse, uyarı verilsin
public override void OnValidateDocument(string view, bool canEdit, Hashtable parameters, ValidationSummary summary)
{
   if(SecimListesi1 == "1" || SecimListesi1_Text == “eleman2”)   
   summary.AddMessage("Değerleri Kontrol Ediniz!");   
}


## 3.10. Formül Yöneticisi 

Formül yöneticisi eBAControls.eBAFormulaManager sınıfındadır. 

Formül yöneticisi üzerinde gelen sihirbaz ile formüller tanımlanır. Formüller uygulandığında gerekli kod sihirbaz tarafından otomatik oluşturulur. Bu kodlar üzerinde gerekli ise değişiklik yapılabilir.  

Kodlar client ve server olmak üzere iki farklı içerikte çalışır. Client tarafında genelde aritmetik hesaplamalar yapılır ve javascript kullanılır. Sunucu tarafında ise dip toplam hesaplama, ortalama alma gibi işlemler yapılır. Bu işlemler InitiateClientScript ve Calculate event lerinde gerçekleştirilir. 

Formül yönetici ile elde edilen kod değiştirilirse ve tekrar formül yöneticisinden kod oluşturması istenilirse değişiklik yapılan kod ezilir. 



### 3.10.1. Özellikler 

•	ID 

Tanım: Formül yöneticisi nesne adnı belirtir. 
Tipi: System.String 
Deklarasyon: public string ID { get; set; } 


### 3.10.2. Metotlar 

•	AddFormula(string) 

Tanım: Client tarafına javascript formül eklemek için kullanılır.  Deklarasyon: public void AddFormula(string script) 
Parametreler: 
script:  Client javascript formül kodudur. 

Not Bu metot InitiateClientScript içinde olmalı ve tüm client formüller eklendikten sonra BuildFormula çağırılmalıdır. 




•	BuildFormula 

Tanım: Client formül tanımları yapıldıktan sonra formüllerin çalışabilmesi için bu metot çağırılmalıdır. 
Deklarasyon: public void BuildFormula() 

•	GetAVG(System.Data.DataTable, string) 

Tanım: “DataTable data” tablosunun “string Column” kolonundaki verinin ortalamasını verir. Kolon içinde string tipinde veri olmalıdır. 
Deklarasyon: public static decimal GetAVG(System.Data.DataTable data, string 
Column) 
Parametreler: 
data:  DataTable nesnesidir. 
Column:  Ortalaması alınacak kolon adıdır. 

•	GetCOUNT (System.Data.DataTable, string) 

Tanım: “DataTable data” tablosunun “string Column” kolonundaki geçerli veri içeren satır sayısını verir. Kolon içinde string tipinde veri olmalıdır. 
Deklarasyon: public static int GetCOUNT(System.Data.DataTable data, string Column) 
Parametreler: 
data:  DataTable nesnesidir. 
Column: Sayısı alınacak kolon adıdır. 

•	GetMAX(System.Data.DataTable, string) 

Tanım: “DataTable data” tablosunun “string Column” kolonundaki en büyük değeri verir. Kolon içinde string tipinde veri olmalıdır. 
Deklarasyon: public static decimal GetMAX(System.Data.DataTable data, string 
Column) 
Parametreler: 
data:  DataTable nesnesidir. 
Column:  En büyük değeri alınacak kolon adıdır. 

•	GetMIN(System.Data.DataTable, string) 

Tanım: “DataTable data” tablosunun “string Column” kolonundaki en küçük değeri verir. Kolon içinde string tipinde veri olmalıdır. 
Deklarasyon: public static decimal GetMIN(System.Data.DataTable data, string 
Column) 
Parametreler: 
data:  DataTable nesnesidir. 
Column:  En küçük değeri alınacak kolon adıdır. 

•	GetSTDEV(System.Data.DataTable, string) 

Tanım: “DataTable data” tablosunun “string Column” kolonundaki verilerin standart sapmasını verir. Kolon içinde string tipinde veri olmalıdır. 
Deklarasyon: public static decimal GetSTDEV(System.Data.DataTable data, string 
Column) 
Parametreler: 
data:  DataTable nesnesidir. 
Column:  Standart sapması alınacak kolon adıdır. 

•	GetSUM(System.Data.DataTable, string) 

Tanım: “DataTable data” tablosunun “string Column” kolonundaki verilerin dip toplamını verir. Kolon içinde string tipinde veri olmalıdır. 
Deklarasyon: public static decimal GetSUM(System.Data.DataTable data, string 
Column) 
Parametreler: 
data:  DataTable nesnesidir. 
Column: Dip toplamı alınacak kolon adıdır. 

•	SetTextBoxFormulaFunction(System.Collections.Generic.List```<```WebControl```>```) 

Tanım: Client formüllerinde formülün yeniden hesaplanmasını tetikleyecek metin kutularını belirler. 
Deklarasyon: public void 
SetTextBoxFormulaFunction(System.Collections.Generic.List```<```WebControl```>``` objs) Parametreler: objs:  Kontrol listesidir. 

•	SetTextBoxFormulaFunction(params System.Web.UI.WebControls.TextBox[]) 

Tanım: Client formüllerinde formülün yeniden hesaplanmasını tetikleyecek metin kutularını belirler. 
Deklarasyon: public void SetTextBoxFormulaFunction(params System.Web.UI.WebControls.TextBox[] objs) 
Parametreler: objs:  Kontrol listesidir. 


### 3.10.3. Olaylar 

•	InitiateClientScript 

Tanım: Client kısmında javascript ile çalışacak formüllerin tanımlandığı kısımdır. Deklarasyon: public void InitiateClientScript(object sender) 
Parametreler:  
sender: Formül yöneticisi nesnesidir. 

Örnek: 

public void FormulaManager1_InitiateClientScript(object sender) 
{ //```<```#eBA Workflow Studio created code begin```>``` -- do not remove 
MakeReadOnly(Text3); 
FormulaManager1.SetTextBoxFormulaFunction(Text1,Text2); FormulaManager1.AddFormula("if (IseBAControl(#[Text3]) && 
IseBAControl(#[Text2]) && IseBAControl(#[Text1])) {#[Text3].value = 
ToString(ToNumber(#[Text1].value) * ToNumber(#[Text2].value))}"); 
FormulaManager1.BuildFormula(); 

//```<```#eBA Workflow Studio created code end```>``` -- do not remove } 



•	Calculate 

Tanım: Sunucu kısmında formüllerin hesaplandığı kısımdır. Deklarasyon: public void Calculate(object sender) 
Parametreler:  
sender: Formül yöneticisi nesnesidir. 

Örnek:  
public void FormulaManager1_Calculate(object sender) 
{ 
//```<```#eBA Workflow Studio created code begin```>``` -- do not remove 
Text2.Text=eBAFormulaManager.GetSUM(Details1.Data,"Text1").ToString()
; 

//```<```#eBA Workflow Studio created code end```>``` -- do not remove } 


### 3.10.4. Javascript Formül Kodlama 

Client tarafındaki formüller javascript ile çalışır. Örnek olarak aşağıdaki formül iki metin kutusunu çarpıp bir diğerine yazar. 

FormulaManager1.AddFormula("if (IseBAControl(#[Text3]) && IseBAControl(#[Text2]) && IseBAControl(#[Text1])) {#[Text3].value = ToString(ToNumber(#[Text1].value) * 
ToNumber(#[Text2].value))}"); 

AddFormula ile eklenen kısım javascript kodudur. Javascriptte metin kutusuna ulaşmak için “#[ControlName]” 	notasyonunu 	kullanmak 	gereklidir. 	Ayrıca 	formül 	hesaplamasını kolaylaştırmak için bazı metodlar vardır. 


### 	3.10.4.1. 	Metotlar 

•	#[controlName] 
Tanım: Metin kutusuna erişimi sağlar. 

•	#[controlName].value 
Tanım: Metin kutusu metin değerine erişimi sağlar. 

•	IseBAControl(object) 
Tanım: Nesnenin o anda mevcut olup olmadığını kontrol eder. Eğer nesne sunucu tarafında gizlenmiş ise client tarafından erişim yapılamaz. Erişim yapılmaya çalışılır ise hata oluşur. Bu kontrol ile hatanın önüne geçmek mümkündür. 
Deklarasyon: bool IseBAControl(object) 

•	ToNumber(object) 
Tanım: Metin kutusu içindeki, metin veriyi, nümerik veriye çevirir. Böylece metematiksel işlemlerde kullanılabilir. 
Deklarasyon: number ToNumber(object) 

•	ToString(number) 
Tanım: Nümerik veriyi metin verisine çevirir. 
Deklarasyon: string ToString(number) 


## 3.11. Buton 

Buton nesnesi System.Web.UI.WebControls.Button sınıfındadır. 

### 3.11.1. Özellikler 

•	Text 

Tanım: Butonun metin kısmıdır. 
Tipi: System.String 
Deklarasyon: public string Text { get; set; } 

•	Visible 

Tanım: Nesnenin görünür olup olmayacağını belirler. 
Tipi: System.Boolean 
Deklarasyon: public bool Visible { get; set; } 

•	Enabled 

Tanım:. Nesnenin kullanılır olup olmayacağını belirler. 
Tipi: System.Boolean 
Deklarasyon: public bool Enabled { get; set; } 


### 3.11.2. Olaylar 

•	OnClick 

Tanım: Butona mouse ile tıklandığında çalışır. 
Deklarasyon: public void OnClick(Object sender, EventArgs e) 
Parametreler:  
sender: Buton nesnesidir. 
e: Olay parametreleridir. 

Örnek:  
public void Button1_OnClick(Object sender, EventArgs e) 
{ 
	   	Text1.Text = “some text”; 
} 


## 3.12. Detaylar/Tablo 

Detaylar ve Tablo nesneleri eBAControls.eBATable sınıfından türemektedir. Bu nedenle aynı başlık altında konumlandırılmıştır. Ancak hem kullanım hem de yapısal olarak farklılıklar mevcuttur. 

### 3.12.1. Veri Yapı Farklılıkları 

Detaylar nesnesi ve Tablo nesnesi arasındaki en belirgin farklılık, tuttukları veri yapılarıdır. Detaylar nesnesindeki her bir kayıt, bir eBA formunu temsil ettiğinden, formun ID’si de kaydedilmektedir.  Tablo 3. Tablo nesnesi veri yapısı 

![](https://docsbimser.blob.core.windows.net/imagecontainer/s4-b3ccbb9d-0a36-4bca-b4b8-54ff56f15534.png)

### 3.12.2. Özellikler 

•	AddExistingButtonText 

Tanım: Ekle butonunun yazısını günceller. 
Tipi: System.String 
Deklarasyon: public string AddExistingButtonText { set; get; } 

•	AddExistingEnable 

Tanım: Ekle butonunun yazısını günceller. 
Tipi: System. Boolean 
Deklarasyon: public bool AddExistingEnable { set; get; } 
•	AddNewButtonText 

Tanım: Ekle butonunun yazısını günceller. 
Tipi: System.String 
Deklarasyon: public string AddNewButtonText { set; get; } 

•	AddNewEnable 

Tanım: Ekle butonunun görünüp görünmemesini sağlar. 
Tipi: System.Boolean 
Deklarasyon: public bool AddNewEnable { set; get; } 

•	CheckAllEnable 

Tanım: Tümünü seç butonunun aktif olmasını sağlar. 
Tipi: System.Boolean 
Deklarasyon: public bool CheckAllEnable { set; get; } 

•	CheckEnable 

Tanım: Satırlarda seçim kutusunun aktif olmasını sağlar. 
Tipi: System.Boolean 
Deklarasyon: public bool CheckEnable { set; get; } 

•	ColumnLimit 

Tanım: Satır sayısını verir. 
Tipi: System.Int32 
Deklarasyon: public int ColumnLimit { set; get; } 

•	Columns 

Tanım: Tablo ve Detaylar nesnesindeki kolonların listesidir. 
Tipi: System.Collections.Generic.List```<```eBATableColumn```>``` 
Deklarasyon: public List```<```eBATableColumn```>``` Columns { get; } 

•	ConfirmOnDelete 

Tanım: Satır silme işleminde onaylama mesajı çıkartma durumunu belirtir. 
Tipi: System.Boolean  
Deklarasyon: public bool ConfirmOnDelete { set; get; } 

•	Count 

Tanım: Tablodaki kayıt sayısını belirtir. 
Tipi: System.Int32 
Deklarasyon: public int Count { get; } 

•	Data 

Tanım: Tablodaki veriyi belirtir. 
Tipi: System.Data.DataTable 
Deklarasyon: public DataTable Data { set; get; } 

•	DeleteButtonText 

Tanım: Sil butonunun yazısını günceller. 
Tipi: System.String 
Deklarasyon: public string AddNewButtonText { set; get; } 

•	DeleteConfirmMessage 

Tanım: Silme işlemini onaylatmak için çıkan mesajı belirtir. 
Tipi: System.String 
Deklarasyon: public string DeleteConfirmMessage { set; get; } 

•	DeleteEnable 

Tanım: Sil butonunun görünüp görünmemesini sağlar. 
Tipi: System.Boolean 
Deklarasyon: public bool DeleteButtonEnable { set; get; } 

•	DeleteImageUrl 

Tanım: Sil butonunun ikon dosya yolunu belirtir. 
Tipi: System.String 
Deklarasyon: public string DeleteImageUrl { set; get; } 

•	EnableSorting

Tanım: Sıralama etkinlik modu
Tipi: System.Boolean 
Deklarasyon: public bool EnableSorting { get; set; }

•	 DescendingSorting

Tanım: Azalan sıralama
Tipi: System.Boolean 
Deklarasyon: public bool DescendingSorting { get; set; }

•	FillDataOnPageLoad

Tanım: Veriler sayfa yüklenirken mi dolsun değeridir
Tipi: System.Boolean 
Deklarasyon: public bool FillDataOnPageLoad { get; set; }

•	FullRowSelection 

Tanım: True olarak belirlendiğinde satıra tıklandığında satır seçimi yapılabilmeyi sağlar. False olduğunda seçim butonuna tıklanarak seçim yapılabilir.  
Tipi: System.Boolean 
Deklarasyon: public bool FullRowSelection { set; get; } 

•	HeaderAlign

Tanım: Başlık konumu bilgisidir
Tipi: eBAControls.HeaderAlignType
Deklarasyon: public eBAControls.HeaderAlignType HeaderAlign { get; set; }
Aldığı Değerler:
		Left
		Top

•	HeaderVisible

Tanım: Başlık görünümü durumudur
Tipi: System.Boolean 
Deklarasyon: public bool HeaderVisible { get; set; }

•	IsTreeGrid

Tanım: Ağaç yapısı etkinlik durumu
Tipi: System.Boolean 
Deklarasyon: public bool IsTreeGrid { get; set; }



•	ModalForm

Tanım: Detaylar nesnesine bağlı modal form bilgisi
Tipi: System.String
Deklarasyon: public string ModalForm { get; set; }

•	ModalProject

Tanım: Detaylar nesnesine bağlı formun dahil olduğu proje adı
Tipi: System.String
Deklarasyon: public string ModalProject { get; set; }

•	ModalView

Tanım: Detaylar nesnesine bağlı formun view bilgisi
Tipi: System.String
Deklarasyon: public string ModalView { get; set; }

•	OwnerDocumentId

Tanım: Detaylar nesnesinin bulunduğu formun form id bilgisi
Tipi: System.Integer
Deklarasyon: public int OwnerDocumentId { get; set; }

•	Paging

Tanım: Sayfalama özelliğidir
Tipi: eBAControls.CustomPaging
Deklarasyon: public eBAControls.CustomPaging Paging { get; set; }

eBAControls.CustomPaging;

•	public int DisplayPageCount { get; set; }  : Görüntülenen sayfa sayısı değeridir
•	public int PageSize { get; set; }  : Sayfa boyutu değeridir
•	public bool Visible { get; set; }  : Görünürlük durumudur

•	PagingDisplayPageCount

Tanım: Görüntülenen sayfa sayısı değeridir
Tipi: System.Integer
Deklarasyon: public int PagingDisplayPageCount { get; set; }

•	ReadOnly 

Tanım: Nesnenin düzenleme özelliğini kapatmayı sağlar.  
Tipi: System.Boolean 
Deklarasyon: public bool ReadOnly { set; get; } 

•	SelectButtonText 

Tanım: Seçim butonunun yazısını günceller. 
Tipi: System.String 
Deklarasyon: public string SelectButtonText { set; get; } 

•	SelectEnable 

Tanım: Seçim butonunun görünüp görünmemesini sağlar. 
Tipi: System.Boolean 
Deklarasyon: public bool SelectButtonEnable { set; get; } 

•	SelectImageUrl 

Tanım: Seçim butonu ikon Url bilgisidir 
Tipi: System. String
Deklarasyon: public string SelectImageUrl { get; set; }


### 3.12.3. Metotlar 

•	Clear 

Tanım: Tüm kayıtları siler. 
Deklarasyon: public void Clear() 

•	CreateRow 

Tanım: Tablonun yapısına göre örnek bir DataRow tipinde kayıt nesnesi oluşturur. Bu kaydı tabloya eklemek için InsertRow metotu kullanılır. 
Deklarasyon: public System.Data.DataRow CreateRow() 
Dönüş Değeri: System.Data.DataRow 

•	DeleteRow(DataRow) 

Tanım: DataRow ile belirtilen kaydı siler. 
Deklarasyon: public void DeleteRow(System.Data.DataRow dr) 
Parametreler: 
dr:  Silenecek kayıt 

•	DeleteRow(int) 

Tanım: İndeks numarası ile kaydı siler. 
Deklarasyon: public void DeleteRow(int index) Parametreler: 
index:  Kaydın indeks numarası 

•	InsertRow(System.Data.DataRow) 

Tanım: Tabloya kayıt ekler. CreateRow metodu ile oluşturulan kayıt örneğinin içeriği düzenlendikten sonra InsertRow metoduna parametre geçirilerek kayıt eklenir. Deklarasyon: public void InsertRow(System.Data.DataRow  dr) 
Parametreler: 
dr:  Eklenecek kaydı belirtir. 

•	SelectRow(DataRow) 

Tanım: Satır seçer. 
Deklarasyon: public void SelectRow(System.Data.DataRow dr) 
Parametreler: 
dr:  Seçilecek kayıt 

•	SelectRow(int) 

Tanım: Satır seçer. 
Deklarasyon: public void SelectRow(int index) 
Parametreler: 
index:  Seçilecek kaydın indeks numarasını belirtir. 

•	SetRowCheck(DataRow, bool) 

Tanım: Satırın seçimin kutusunun değerini günceller. 
Deklarasyon: public void SetRowCheck (System.Data.DataRow dr, bool check) Parametreler: 
dr:  Güncellenecek satırı belirtir. 
check: Seçim değerini belirtir. 

•	SetRowCheck(int, bool) 

Tanım: Satır seçim kutusunun değerini günceller. 
Deklarasyon: public void SetRowCheck(int index, bool check) 
Parametreler: 
index:  Güncellenecek satırın indeks numarasını belirtir. 
check: Seçim değerini belirtir. 


### 3.12.4. Olaylar 

•	RowCheck 

Tanım: Tablonun seçim kutusunun statüsü değiştiğinde oluşur. 
Deklarasyon: public void RowCheck(object sender, bool state, DataRow dr) Parametreler:  
sender: Tablo/Detaylar nesnesini belirtir. state: Seçim kutusunun değerini belirtir. 
dr: İşlem yapılan satır bilgilerini belirtir. 

Örnek:  
public void Table1_RowCheck(object sender, bool state, DataRow dr) 
{      if (state) 
    Text1.Text = "checked";   else 
    Text1.Text = "unchecked";      if (dr.IsNull("OSUSERS_ID"))     Text1.Text += " [NULL]";   else 
    Text1.Text += " [" + dr["OSUSERS_ID"].ToString() + "]";                      
} 

•	RowDeleting 

Tanım: Satır silinmeden önce çalışır. Olay parametreleri içerisinde bulunan ‘allow’ değişkeni ile silme işlemi iptal edilebilir. 
Deklarasyon: public void RowDeleting(object sender, eBATableDeleteRowEventArgs args, DataRow dr) 
Parametreler:  
sender: Tablo/Detaylar nesnesini belirtir. 
args: Satır silme parametrelerini belirtir. eBATableDeleteRowEventArgs sınıfı allow (bool) özelliğine sahiptir. Bu özelliğin değerine göre silme işlemi yapılır ya da iptal edilir. 
dr: Silinmek istenen satır bilgilerini belirtir. 

Örnek:  
public void Detaylar1_RowDeleting(object sender, eBATableDeleteRowEventArgs args, DataRow dr) 
{ 
	 	args.allow = false;  	  
} 

•	RowDeleted 

Tanım: Satır silindikten sonra çalışır. 
Deklarasyon: public void RowDeleted(object sender, DataRow dr) 
Parametreler:  
sender: Tablo/Detaylar nesnesini belirtir. 
dr: Silinen satır bilgilerini belirtir. 

•	RowInserted 

Tanım: Satır eklendikten sonra çalışır. 
Deklarasyon: public void RowInserted(object sender, DataRow dr) 
Parametreler:  
sender: Tablo/Detaylar nesnesini belirtir. 
dr: Eklenen satır bilgilerini belirtir. 

•	RowInserting 

Tanım: Satır eklenmeden önce çalışır. ‘allow’ değişkeni ile ekleme işlemi iptal edilebilir. 
Deklarasyon: public void RowInserting(object sender , eBATableInsertRowEventArgs args, DataRow dr) 
Parametreler:  
sender: Tablo/Detaylar nesnesini belirtir. 
args: Olay parametrelerini belirtir. eBATableInsertRowEventArgs sınıfı allow (bool) özelliğine sahiptir. Bu özelliğin değerine göre ekleme işlemi yapılır ya da iptal edilir. dr: Eklenecek satır bilgilerini belirtir. 

Örnek:  

public void Detaylar1_RowInserting(object sender, 
eBATableInsertRowEventArgs args, DataRow dr) 
{ 
	 	if(Detaylar1.Count```>```4) 
	 	 	args.allow = false;  	 	  
} 


•	RowSelected 

Tanım: Tablo nesnesinde satır seçildikten sonra çalışır.  
Deklarasyon: public void RowSelected(object sender, DataRow dr) 
Parametreler:  
sender: Tablo nesnesini belirtir. 
dr: Seçilen satırın bilgilerini belirtir. 

Örnek:  
 public void Tablo1_RowSelected(object sender, DataRow dr) 
{      if (dr.IsNull("OSUSERS_ID"))     Text1.Text = "NULL";   else 
    Text1.Text = dr["OSUSERS_ID"].ToString(); 
} 
           Not Bu olay sadece Tablo nesnesinde mevcuttur. 

•	AfterShowModal 

Tanım: Detaylar nesnesine bağlı form açılıp, gerekli işlemler yapıldıktan sonra tekrar detaylar nesnesinin olduğu forma dönülürken çalışan eventtir.
Deklarasyon: public void AfterShowModal(object sender, eBATableModalEventArgs args) 
Parametreler:  
sender: Detaylar nesnesini belirtir. 
args: Modal olay parametrelerini belirtir.  

Not Bu olay sadece Detaylar nesnesinde mevcuttur. 

•	BeforeShowModal 

Tanım: Modal form açılmadan önce çalışan olaydır. Modal forma, parametre geçirmek için kullanılıt 
Deklarasyon: public void BeforeShowModal(object sender, eBATableModalEventArgs args) 
Parametreler:  
sender: Detaylar nesnesini belirtir. 
args: Modal forma gönderilecek parametreleri belirtir. 

Not Bu olay sadece Detaylar nesnesinde mevcuttur. 


### 3.12.5. eBATableModalEventArgs Sınıfı   3.12.5.1. Özellikler


•	allow 

Tanım: Değere göre modal açma işlemine izin verilir. 
Tipi: System.Boolean 
Deklarasyon: public bool allow  

•	documentId 

Tanım: Modal olarak açılacak formun global Id’sini belirtir. 
Tipi: System.Int32 
Deklarasyon: public int documentId  

•	isnew 

Tanım: Yeni kayıt ekleme durumunu belirtir. Detaylar nesnesinde “Ekle” butonu ile yeni bir modal form açılabilir ya da daha önceden detaylara eklenmiş bir modal form, düzenle butonuna basılarak açılabilir. Modal formdan ana forma dönüldüğünde, açılan modal formun daha önceden eklenmiş bir form mu olduğu ya da yeni mi oluşturulduğu bilgisini dönen parametredir
Tipi: System. Boolean 
Deklarasyon: public bool isnew 

•	modalResult 

Tanım: Modaldan dönüş değeridir. ModalResult.Ok yada ModalResult.Cancel enum değerlerini alır. 
Tipi: eBAControls.ModalResult 
Deklarasyon: public eBAControls.ModalResult modalResult 

•	parameters 

Tanım: Modaldan dönüş parametleridir. Modal formdan ana forma parametre geçirmek için kullanılır.  
Tipi: eBAControls.ModalParameters 
Deklarasyon: public eBAControls.ModalParameters parameters 

Not ModalParameters sınıfı ile ilgili detaylı bilgiyi 3.10.6 ModalParameters Sınıfı başlıklıklı bölümde bulabilirsiniz. 

•	selectedRow 

Tanım: Seçili satır bilgisi
Tipi: System.Data.DataRow
Deklarasyon: System.Data.DataRow selectedRow


### 3.12.6. ModalParameters Sınıfı 

3.12.6.1. Özellikler  

•	Parameters 

Tanım: Parametre listesini belirtir. 
Tipi: System.Collections.Generic.List```<```ModalParameter```>``` 
Deklarasyon: public System.Collections.Generic.List```<```ModalParameter```>``` Parameters 

•	this[string] 

Tanım: Listeye eklenmiş parametreye adı ile erişmek için kullanılır. 
Tipi: object 
Deklarasyon: public object this[string parameter] { set; get; } 

3.12.6.2. Metotlar 

•	Add(string, object) 

Tanım: Nesnenin orjinal ismi verilerek satırlardaki o nesnenin listesini verir. Deklarasyon: public void Add(string Key, object Value) 
Parametreler: 
Key:  Parametre adını belirtir. 
Value: Parametre değerini belirtir. 


### 3.12.7. ModalParameter Sınıfı 

ModalParameter, Modal forma gönderilecek parametrelerin sınıfıdır. 3.12.7.1. Özellikler 

•	Key 

Tanım: Parametre adını belirtir. 
	Tipi: System.String 	 
Deklarasyon: public string Key 

•	Value 

Tanım: Parametre değerini belirtir. 
	Tipi: System.Object 	 
Deklarasyon: public object Value 




### 3.12.8. Validasyon 

Tablo ve Detaylar nesnesinin yapıları farklı olduklarından dolayı validasyonda farklı kullanım mevcuttur. 

3.12.8.1. Detaylar Nesnesi 

Validasyon kodlamasında, detaylar nesnesi, obje ismi ile çağrıldığında, List```<```eBADetailsItem```>``` tipinde bir liste dönmektedir. Böylece detaylar nesnesine eklenmiş olan modal formların bilgilerine erişilerek gerekli kontroller yapılabilir.  

eBADetailsItem sınıfının özellikleri aşağıda belirtilmektedir. 
•	int documentId: Formun global Id’sini belirtir. 
•	bool check: Satırların işaretlenme durumlarını belirtir. 





Örnek: 
Örnekte, detaylar nesnesine eklenen tüm satırların işaretlenmiş olması kontrol edilmektedir. 
public override void OnValidateDocument(string view, bool canEdit, Hashtable parameters, ValidationSummary summary) 
{ 
  foreach(eBADetailsItem item in Details1) 
  {     if (!item.check) 
    { 
      Summary.AddMessage(item.documentId.ToString() + " is not checked"); 
    } 
  } 
} 

3.12.8.2. Tablo Nesnesi 

Validasyon kodlamasında, tablo nesnesi, obje ismi ile çağrıldığında, DataTable tipinde tabloya eklenmiş tüm satırların bilgilerini içeren veri döner.  

Örnek: 
Örnekte, bir kolona veri girişinin zorunluluğu kontrol edilmektedir. 
public override void OnValidateDocument(string view, bool canEdit, Hashtable parameters, ValidationSummary summary) 
{   foreach(DataRow dr in Table1) 
  { 
    if (dr.IsNull("USERID") || string.IsNullOrEmpty(dr["USERID"].ToString()))     { 
      Summary.AddMessage("Sicil no zorunludur."); 
    } 
  } 
} 


### 3.12.9. Örnekler 

•	Detaylar nesnesine yeni kayıt eklemek için 
1.	CreateRow metodu ile örnek bir DataRow oluşturun. 
2.	InsertRow metodu ile oluşturulan DataRow’u detaylar nesnesine ekleyin. 
3.	RefreshDetails metodu ile detaylar nesnesinin değerlerini yenileyin. 
DataRow dr = Detaylar1.CreateRow();      dr["CHECKED"]=0; 
     dr["DOCUMENTID"] = 1001; // Modal Form Id                            
     Detaylar1.InsertRow(dr); 
RefreshDetails(Detaylar1);  

•	Tablo nesnesine programatik olarak kayıt eklemek için  
1.	CreateRow metodu ile örnek bir DataRow oluşturun. 
2.	InsertRow metodu ile oluşturulan DataRow’u detaylar nesnesine ekleyin. 

Aşağıdaki örnekte UserId ve UserName adlı 2 kolonu bulunan tabloya kayıt eklenmektedir. 
DataRow dr = Tablo1.CreateRow(); 
   	dr["CHECKED"]=0;   	dr["UserId"] = "0010";                               	dr["UserName"] = "John Smith";                               	Tablo1.InsertRow(dr);      

•	Detaylar nesnesinden açılan modal forma parametre geçirmek için 

1. BeforeShowModal olayında parametreler ekleyin.  
      2. Modal formun OnModalLoad eventinde bu parametre değerlerine erişin.  

Aşağıdaki örnekte, ana formdaki bir metin kutusu değeri, modal forma iletilmektedir. 

 	// Ana form üzerindeki Detaylar nesnesinin BeforeShowModal olayı public void Detaylar1_BeforeShowModal(object sender, eBATableModalEventArgs args) { 
    args.parameters.Add("value1",Text1.Text);              
} 

// Modal formun OnModalLoad olayı 
public void OnModalLoad(ModalParameters parameters) 
{ 
  Text2.Text=(string)parameters["value1"];                                          }  

•		Detaylar nesnesinde modal formdan ana forma parametre geçirmek için 

1.	Modal formun OnModalUnload olayında parametre ekleyin.  
2.	Ana formdaki detaylar nesnesinin AfterShowModal olayında bu değere erişin.  

Aşağıdaki örnekte, modal formdaki metin kutusu değeri ana forma aktarılmaktadır. 

// Modal formun OnModalUnload olayı 
public void OnModalUnload(eBAModalEventArgs args) 
{ 
    args.parameters.Add("value1",Text2.Text);              
} 

// Ana formdaki detaylar nesnesinin AfterShowModal olayı 
public void Detaylar1_AfterShowModal(object sender, eBATableModalEventArgs args) { 
  Text1.Text=(string)args.parameters["value1"];                             
} 


## 3.13. Detay Tablo 

Detay tablo nesnesi, eBAControls.eBADetailsGrid sınıfından türemektedir. 

### 3.13.1. Özellikler 

•	AddNewEnable 

Tanım: Yeni satır ekleme butonunun aktif olma durumudur. 
Tipi: System.Boolean 
Deklarasyon: public bool AddNewEnable { set; get; } 

•	Bordered 

Tanım: Tablo gösterilirken satırlar ve sütunlar arasında kenarlık çizgileri olma durumudur. 
Tipi: System.Boolean 
Deklarasyon: public bool Bordered { set; get; } 

•	CurrentRowCount 

Tanım: Tablodaki mevcut satır sayısını gösterir. 
Tipi: System.Int32 
Deklarasyon: public int CurrentRowCount { set; get; } 

•	DeleteEnable 

Tanım: Son satırı silme butonunun aktif olma durumudur. 
Tipi: System.Boolean 
Deklarasyon: public bool DeleteEnable { set; get; } 

•	HeaderAlign 
Tanım: Başlık satırının konumunu belirler. Top ve Left olarak 2 farklı modu vardır. 
Tipi: eBAControls.HeaderAlignType 
Deklarasyon: public eBAControls.HeaderAlignType HeaderAlign { set; get; } 

•	Margin 

Tanım: Tabloda satır ve sütunlar arasındaki mesafeyi belirler. 
Tipi: System.Int32 
Deklarasyon: public int Margin { set; get; } 

•	MaximumRowCount 

Tanım: Tabloya eklenebilecek maksimum satır sayısını verir. 
Tipi: System.Int32 
Deklarasyon: public int MaximumRowCount { set; get; } 

•	ReadOnly 

Tanım: Nesnenin verisinin değiştirilip değiştirilmeyeceğini belirler. 
Tipi: System.Boolean 
Deklarasyon: public bool ReadOnly { get; set; } 

•	RowHeaders 

Tanım: Görüntülenen başlıkların listesidir. 
Tipi: System.Collections.Generic.List```<```string```>``` 
Deklarasyon: public System.Collections.Generic.List```<```string```>``` RowHeaders { set; get; } 

•	ShowRowHeader 

Tanım: Başlık satırının görüntülenip görüntülenmediğini verir. 
Tipi: System.Boolean 
Deklarasyon: public bool ShowRowHeader { set; get; } 

•	ShowRowNumber 

Tanım: Satır numaralarının görüntülenip görüntülenmeyeceğini verir. 
Tipi: System.Boolean 
Deklarasyon: public bool ShowRowNumber { set; get; } 

•	Visible 

Tanım: Nesnenin görünür olup olmayacağını belirler. 
Tipi: System.Boolean 
Deklarasyon: public bool Visible { get; set; } 

•	Columns 

Tanım: Kolonların listesidir. İçerisinde başlıkların ismi ve kullanılan etiket kontrolleri bulunur. 
Tipi: eBAControls.eBADetailsGridColumns 
Deklarasyon: public eBAControls.eBADetailsGridColumns Columns 

•	Rows 

Tanım: Satırların listesidir. İçerisinde hücrelerin listesi bulunur. Hücreler içersinde kullanılan kontrollere ve orjinal isimlerine ulaşılabilir. 
Tipi: eBAControls.eBADetailsGridRows 
Deklarasyon: public eBAControls.eBADetailsGridRows Rows 


### 3.13.2. Metotlar 

•	GetControls(string) 

Tanım: Nesnenin orjinal ismi verilerek satırlardaki o nesnenin listesini verir. 
Deklarasyon: public System.Collections.Generic.List```<```WebControl```>``` GetControls(string name) 
Dönüş Değeri: System.Collections.Generic.List```<```WebControl```>``` 
Parametreler: 
name:  Alınmak istenilen nesnenin orjinal adını belirtir. 

•	GetObjectRowIndex(object) 

Tanım: Parametre geçilen nesnenin tablodaki satır indeksini verir. 
Deklarasyon: public int GetObjectRowIndex(object obj) Dönüş Değeri: System.Int32 
Parametreler: 
obj:  Satır indeksi alınmak istenen nesneyi belirtir. 

•	GetOriginalControlNames 

Tanım: Nesne içerisindeki kontrollerin orjinal isimlerinin listesini verir. 
Deklarasyon: public System.Collections.Generic.List```<```string```>``` 
GetOriginalControlNames() 
Dönüş Değeri: System.Collections.Generic.List```<```string```>``` 

•	GetRowObject(int, string) 

Tanım: Nesne içerisinde satır indeksi ve orjinal kontrol ismi verilerek hücredeki kontrolü almak için kullanılır. 
Deklarasyon: public System.Web.UI.WebControls.WebControl GetRowObject(int row, string objname) 
Dönüş Değeri: System.Web.UI.WebControls.WebControl 
Parametreler: 
row:  Erişilmek istenen satır numarasını belirtir. 
objname:  Erişilmek istenen kontrolün orjinal adını belirtir. 


### 3.13.3. Olaylar 

•	RowDeleting 

Tanım: Satır silinmeden önce çalışır. Olay parametreleri içerisinde bulunan ‘allow’ değişkeni ile silme işlemi iptal edilebilir. 
Deklarasyon: public void RowDeleting(object sender, DetailsGridDeleteRowEventArgs args) 
Parametreler:  
sender: Detay tablo nesnesini belirtir. 
args: Olay parametrelerini belirtir. 

Örnek:  
public void DetailsGrid1_RowDeleting(object sender, 
DetailsGridDeleteRowEventArgs args) 
{ 
	 	args.allow = false;  	  
} 


•	RowDeleted 

Tanım: Satır silindikten sonra çalışır. 
Deklarasyon: public void RowDeleted(object sender) 
Parametreler:  
sender: Detay tablo nesnesini belirtir. 

•	RowInserted 

Tanım: Satır eklendikten sonra çalışır. Olay parametrelerinden ‘RowCount’ değişkeni ile kaç satır eklendiğine erişilebilir. 
Deklarasyon: public void RowInserted(object sender, DetailsGridInsertedRowEventArgs args) Parametreler:  
sender: Detay tablo nesnesini belirtir. 
args: Olay parametrelerini belirtir. 

•	RowInserting 

Tanım: Satır eklenmeden önce çalışır. Olay parametrelerinden ‘RowCount’ değişkeni ile kaç satır eklendiğine erişilebilir. ‘allow’ değişkeni ile ekleme işlemi iptal edilebilir. Deklarasyon: public void RowInserting(object sender, DetailsGridInsertRowEventArgs args) 
Parametreler:  
sender: Detay tablo nesnesini belirtir. 
args: Olay parametrelerini belirtir. 

Örnek:  
public void DetailsGrid1_RowInserting(object sender, 
DetailsGridInsertRowEventArgs args) 
{ 
	 	 if(args.RowCount ```>``` 3) 
	 	 { 
	   	args.allow = false; 
	 	 } 
} 


## 3.14. Ekli Dosyalar 

Ekli dosyalar nesnesi, eBAControls.eBAAttachments sınıfından türemektedir. 

### 3.14.1. Özellikler 

•	AddButtonText 

Tanım: Ekleme butonunun ismini almak ve değiştirmek için kullanılır. 
Tipi: System.String 
Deklarasyon: public string AddButtonText { set; get; } 

•	AddNewEnable 

Tanım: Yeni ekleme butonunun görünüp görünmeyeceğini verir. 
Tipi: System.Boolean 
Deklarasyon: public bool AddNewEnable { set; get; } 

•	Categories 

Tanım: Ekli dosya kategori listesini verir. Kategorinin ismi, açıklaması ve kategori içinde bulunan dosyaların isim, açıklama ve boyut gibi bilgilere erişilebilir. 
Tipi: System.Collections.Generic.List```<```eBAAttachmentCategory```>``` 
Deklarasyon: public System.Collections.Generic.List```<```eBAAttachmentCategory```>``` Categories { set; get; } 

•	CategoryDescriptionEnable 

Tanım: Kategori açıklama alanının görünürlülüğünü verir. 
Tipi: System.Boolean 
Deklarasyon: public bool CategoryDescriptionEnable { set; get; } 

•	CategoryFilter 

Tanım: Ekli dosya nesnesinde görüntülenmek istenen kategorilerin listesidir. 
Tipi: System.Collections.Generic.List```<```eBAAttachmentCategory```>``` 
Deklarasyon: public System.Collections.Generic.List```<```eBAAttachmentCategory```>``` 
CategoryFilter { set; get; } 




•	DeleteEnable 

Tanım: Silme butonunun görünüp görünmeyeceğini verir. 
Tipi: System.Boolean 
Deklarasyon: public bool DeleteEnable { set; get; } 

•	DescriptionEnable 

Tanım: Ekli dosyaların açıklamalarının görüntülenme durumudur. 
Tipi: System.Boolean 
Deklarasyon: public bool DescriptionEnable { set; get; } 

•	DescriptionRequired 

Tanım: Yeni ekli dosya eklerken açıklama alanının zorunlu olarak girilmesini sağlar. 
Tipi: System.Boolean 
Deklarasyon: public bool DescriptionRequired { set; get; } 

•	Filename 

Tanım: Formun doküman yönetim sistemindeki yolunu verir. 
Tipi: System.String 
Deklarasyon: public string Filename { set; get; } 

•	ReadOnly 

Tanım: Nesnenin verisinin değiştirilip değiştirilmeyeceğini belirler. 
Tipi: System.Boolean 
Deklarasyon: public bool ReadOnly { get; set; } 

•	ShowContentForImages 

Tanım: Değeri ‘true’ ise eklenen resim dosyalarının ön izlemesi nesne üzerinde gösterilir. 
Tipi: System.Boolean 
Deklarasyon: public bool ShowContentForImages { set; get; } 

•	ViewEnable 

Tanım: Eklenen dosyaların görüntülenme durumudur. 
Tipi: System.Boolean 
Deklarasyon: public bool ViewEnable { set; get; } 


### 3.14.2. Metotlar 

•	FileCount 

Tanım: Toplam ekli dosya sayısını verir. 
Deklarasyon: public int FileCount() 
Dönüş Değeri: System.Int32 

•	FileCount(string) 

Tanım: İstenilen kategorideki dosya sayısını verir. 
Deklarasyon: public int FileCount(string category) Dönüş Değeri: System.Int32 
Parametreler:  
category: Dosya sayısı alınmak istenen kategoriyi belirtir. 

•	GetCategories 

Tanım: Ekli dosya kategori listesini verir. Kategorinin ismi, açıklaması ve kategori içinde bulunan dosyaların isim, açıklama ve boyut gibi bilgilere erişilebilir. 
Deklarasyon: public eBAControls.AttachmentCategories GetCategories() 
Dönüş Değeri: eBAControls.AttachmentCategories 

•	HasFile(string, string) 

Tanım: Verilen kategoride istenilen dosya var mı kontrol eder. 
Deklarasyon: public bool HasFile(string category, string filename) Dönüş Değeri: System.Boolean 
Parametreler:  
category: Ekli dosya kategorisini belirtir. 
filename: Ekli dosya adını belirtir. 

•	LoadAttachments 

Tanım: Ekli dosyaları manuel yeniden yüklemek için kullanılır. 
Deklarasyon: public void LoadAttachments() 


### 3.14.3. Olaylar 

•	OnAfterAttach 

Tanım: Ekli dosya eklendikten sonra çalışır. Olay parametrelerinden eklenen dosya ve kategorisine erişilebilir. 
Deklarasyon: public void OnAfterAttach(object sender, eBAAttachmentFileEventArgs e) 
Parametreler:  
sender: Ekli dosyalar nesnesini belirtir. 
e: Olay parametrelerini belirtir. 



Örnek:  
public void Attachment1_OnAfterAttach(object sender, 
eBAAttachmentFileEventArgs e) 
{ 

} 

•	OnBeforeAttach 

Tanım: Ekli dosya eklenmeden önce çalışır. Olay parametrelerinden eklenen dosya ve kategorisine erişilebilir. ‘allow’ değişkeni ile ekleme işlemi iptal edilebilir. Deklarasyon: public void OnBeforeAttach(object sender,eBAAddAttachmentFileEventArgs e) 
Parametreler:  
sender: Ekli dosyalar nesnesini belirtir. 
e: Olay parametrelerini belirtir. 


Örnek:  
public void Attachment1_OnBeforeAttach(object 
sender,eBAAddAttachmentFileEventArgs e) 
{ 
	 	  if(e.Filename == "eBA.txt") 
	 	  { 
	 	    e.allow = false; 
	 	  } 
} 


•	OnAfterDelete 

Tanım: Ekli dosya silindikten sonra çalışır.  
Deklarasyon: public void OnAfterDelete(object sender) 
Parametreler:  
sender: Ekli dosyalar nesnesini belirtir. 

Örnek:  
public void Attachment1_OnAfterDelete(object sender) 
{ 

} 



•	OnBeforeDelete 

Tanım: Ekli dosya silinmeden önce çalışır. Olay parametrelerinden silinen dosya ve kategorisine erişilebilir. ‘allow’ değişkeni ile silme işlemi iptal edilebilir. 
Deklarasyon: public void OnBeforeDelete(object sender, 
eBADeleteAttachmentFileEventArgs e) 
Parametreler:  
sender: Ekli dosyalar nesnesini belirtir. 
e : Olay parametrelerini belirtir. 

Örnek:  
public void Attachment1_OnBeforeDelete(object sender, 
eBADeleteAttachmentFileEventArgs e) 
{ 
e.allow = false; 
} 


## 3.15. İlişkili Dokümanlar 

İlişkili dokümanlar nesnesi eBAControls.eBARelations sınıfından türemektedir. 

### 3.15.1. Özellikler 

•	AddButtonText 

Tanım: Ekleme butonunun ismini almak ve değiştirmek için kullanılır. 
Tipi: System.String 
Deklarasyon: public string AddButtonText { set; get; } 

•	AddNewEnable 

Tanım: Yeni ekleme butonunun görünüp görünmeyeceğini verir. 
Tipi: System.Boolean 
Deklarasyon: public bool AddNewEnable { set; get; } 

•	Categories 

Tanım: İlişkili doküman kategori listesini verir. Kategorinin ismi, açıklaması ve kategori içinde bulunan dosyaların isim, açıklama gibi bilgilere erişilebilir. 
Tipi: System.Collections.Generic.List```<```eBAAttachmentCategory```>``` 
Deklarasyon: public System.Collections.Generic.List```<```eBAAttachmentCategory```>``` Categories { set; get; } 

•	CategoryDescriptionEnable 

Tanım: Kategori açıklama alanının görünürlülüğünü verir. 
Tipi: System.Boolean 
Deklarasyon: public bool CategoryDescriptionEnable { set; get; } 

•	CreateButtonText 

Tanım: Yeni dosya oluşturma butonunun ismini almak ve değiştirmek için kullanılır. 
Tipi: System.String 
Deklarasyon: public string CreateButtonText { set; get; } 




•	CreateDocumentName 

Tanım: Yeni dosya oluşturarak ilişki kurulurken oluşturulan dosyanın isminin ne olacağını belirlemek içindir. Uzantı yazılmaz ise kullanıcının seçtiği dosyanın uzantısıyla dosya oluşturulur. 
Tipi: System.String 
Deklarasyon: public string CreateDocumentName { set; get; } 

•	CreateEnable 

Tanım: Yeni dosya oluşturma butonunun görünürlülük durumudur. 
Tipi: System.Boolean 
Deklarasyon: public bool CreateEnable { set; get; } 

•	CreatePath 

Tanım: Yeni dosya oluşturarak ilişki kurulurken oluşturulacak dosyanın doküman yönetim sistemindeki yoludur. 
Tipi: System.String 
Deklarasyon: public string CreatePath { set; get; } 

•	DeleteEnable 

Tanım: Silme butonunun görünüp görünmeyeceğini verir. 
Tipi: System.Boolean 
Deklarasyon: public bool DeleteEnable { set; get; } 

•	DescriptionEnable 

Tanım: İlişkili dosyanın açıklamalarının görüntülenme durumudur. 
Tipi: System.Boolean 
Deklarasyon: public bool DescriptionEnable { set; get; } 

•	DescriptionRequired 

Tanım: Yeni ilişkişi doküman eklerken açıklama alanının zorunlu olarak girilmesini sağlar. 
Tipi: System.Boolean 
Deklarasyon: public bool DescriptionRequired { set; get; } 



•	Filename 

Tanım: Formun doküman yönetim sistemindeki yolunu verir. 
Tipi: System.String 
Deklarasyon: public string Filename { set; get; } 

•	HideFileExtension

Tanım: Dosya uzantısının görünürlüğü
Tipi: System. Boolean
Deklarasyon: public bool HideFileExtension { get; set; }

•	ReadOnly 

Tanım: Nesnenin verisinin değiştirilip değiştirilmeyeceğini belirler. 
Tipi: System.Boolean 
Deklarasyon: public bool ReadOnly { get; set; } 

•	ShowContentForImages 

Tanım: Değeri ‘true’ ise eklenen resim dosyalarının ön izlemesi nesne üzerinde gösterilir. 
Tipi: System.Boolean 
Deklarasyon: public bool ShowContentForImages { set; get; } 

•	ShowCreateDate 

Tanım: Dosya yükleme tarihinin görünürlüğü
Tipi: System.Boolean 
Deklarasyon: public bool ShowCreateDate { get; set; }

•	ShowCreator 

Tanım: Dosya yükleyen bilgisinin görünürlüğü
Tipi: System.Boolean 
Deklarasyon: public bool ShowCreator { get; set; }

•	ViewEnable 

Tanım: Eklenen dokümanların görüntülenme durumudur. 
Tipi: System.Boolean 
Deklarasyon: public bool ViewEnable { set; get; } 


### 3.15.2. Metotlar 

•	FileCount 

Tanım: Toplam ilişkili doküman sayısını verir. 
Deklarasyon: public int FileCount() 
Dönüş Değeri: System.Int32 

•	FileCount(string) 

Tanım: İstenilen kategorideki doküman sayısını verir. 
Deklarasyon: public int FileCount(string category) Dönüş Değeri: System.Int32 
Parametreler:  
category: Doküman sayısı alınmak istenen kategoriyi belirtir. 

•	HasFile(string, string) 

Tanım: Verilen kategoride istenilen dokümanın bulunduğunu kontrol eder. 
Deklarasyon: public bool HasFile(string category, string filename) Dönüş Değeri: System.Boolean 
Parametreler:  
category: İlişkili doküman kategorisini belirtir. 
filename: İlişkili doküman adını belirtir. 

•	LoadRelations 

Tanım: İlişkili dokümanları elle yeniden yüklemek için kullanılır. 
Deklarasyon: public void LoadRelations() 


### 3.15.3. Olaylar 

•	OnAfterRelation 

Tanım: İlişkili doküman eklendikten sonra çalışır. Olay parametrelerinden eklenen doküman ve kategorisine erişilebilir. 
Deklarasyon: public void OnAfterRelation(object sender, eBARelationFileEventArgs e) Parametreler:  
sender: İlişkili dokümanlar nesnesini belirtir. 
e: Olay parametrelerini belirtir. 

Örnek:  
public void RelatedDocuments1_OnAfterRelation(object sender, 
eBARelationFileEventArgs e) 
{ 

} 


•	OnBeforeRelation 

Tanım: İlişkili doküman eklenmeden önce çalışır. Olay parametrelerinden eklenen doküman ve kategorisine erişilebilir. ‘allow’ değişkeni ile ekleme işlemi iptal edilebilir. Deklarasyon: public void OnBeforeRelation(object sender,eBAAddRelationFileEventArgs e) 
Parametreler:  
sender: İlişkili dokümanlar nesnesini belirtir. 
e: Olay parametrelerini belirtir. 

Örnek:  
public void RelatedDocuments1_OnBeforeRelation(object 
sender,eBAAddRelationFileEventArgs e) 
{  	 if(e.Filename == "eBA.txt") 
	 	 { 
	 	  	e.allow = false; 
	 	 } 
} 







•	OnAfterDelete 

Tanım: İlişkili doküman silindikten sonra çalışır.  
Deklarasyon: public void OnAfterDelete(object sender) Parametreler:  
sender: İlişkili dokümanlar nesnesini belirtir. 

Örnek:  
public void RelatedDocuments1_OnAfterDelete(object sender) 
{ 

} 

•	OnBeforeDelete 

Tanım: İlişkili doküman silinmeden önce çalışır. Olay parametrelerinden silinen doküman ve kategorisine erişilebilir. ‘allow’ değişkeni ile silme işlemi iptal edilebilir. Deklarasyon: public void OnBeforeDelete(object sender, 
eBADeleteRelationFileEventArgs e) 
Parametreler:  
sender: İlişkili dokümanlar nesnesini belirtir. e : Olay parametrelerini belirtir. 

Örnek:  
public void RelatedDocuments1_OnBeforeDelete(object sender, 
eBADeleteRelationFileEventArgs e) 
{ 
	 	  e.allow = false; 
} 


## 3.16. HTML Metin Kutusu 

HTML metin kutusu nesnesi eBAControls.eBAHtmlEditor sınıfından türemektedir. 

## 3.16.1. Özellikler 

•	ReadOnly 

Tanım: Nesnenin verisinin değiştirilip değiştirilmeyeceğini belirler. 
Tipi: System.Boolean 
Deklarasyon: public bool ReadOnly { get; set; } 

•	Text 

Tanım: Metin kutusu içindeki metni değiştirmek yada almak için kullanılır. 
Tipi: System.String 
Deklarasyon: public string Text { get; set; } 

•	Visible 

Tanım: Nesnenin görünür olup olmayacağını belirler. 
Tipi: System.Boolean 
Deklarasyon: public bool Visible { get; set; } 


### 3.17. Barkod 

Barkod nesnesi eBAControls.eBABarcodeControl sınıfından türemektedir. 

## 3.17.1. Özellikler 

•	Code 

Tanım: Barkodu oluşturulacak veriyi belirtir. 
Tipi: System.String 
Deklarasyon: public string Code { set; get; } 

•	Type 

Tanım: Barkod tipini verir. eBABarcodeGenerator.Symbology içerisinden istenilen tipten barkod oluşturabilmek mümkündür. 
Tipi: eBABarcodeGenerator.Symbology 
Deklarasyon: public eBABarcodeGenerator.Symbology Type { set; get; } 


## 3.18. Onaylayanlar 

Onaylayanlar nesnesi, “eBAControls.documentHistoryBase” sınıfındandır.

### 3.18.1. Özellikler 

•	documentId 

Tanım: Onaylayanlar nesnesinin bulunduğu formun id değeridir 
Tipi: System.Integer 
Deklarasyon: public int documentId { get; set; }

•	ShowDepartment 

Tanım: Onaylayanlar nesnesinde aksiyon alan kişinin departman bilgisinin görünürlüğü
Tipi: System.Boolean
Deklarasyon: public bool ShowDepartment { get; set; } 

•	ShowDepartmentId

Tanım: Onaylayanlar nesnesinde aksiyon alan kişinin departman id bilgisinin görünürlüğü
Tipi: System.Boolean
Deklarasyon: public bool ShowDepartmentId { get; set; }

•	ShowEmail

Tanım: Onaylayanlar nesnesinde aksiyon alan kişinin email bilgisinin görünürlüğü
Tipi: System.Boolean
Deklarasyon: public bool ShowEmail { get; set; }

•	ShowNameAndSurname

Tanım: Onaylayanlar nesnesinde aksiyon alan kişinin isim ve soyisim bilgisinin görünürlüğü
Tipi: System.Boolean
Deklarasyon: public bool ShowNameAndSurname { get; set; }


•	ShowPosition

Tanım: Onaylayanlar nesnesinde aksiyon alan kişinin pozisyon bilgisinin görünürlüğü
Tipi: System.Boolean
Deklarasyon: public bool ShowPosition { get; set; }

•	ShowPositionId

Tanım: Onaylayanlar nesnesinde aksiyon alan kişinin pozisyon id bilgisinin görünürlüğü
Tipi: System.Boolean
Deklarasyon: public bool ShowPositionId { get; set; }

•	ShowProfession

Tanım: Onaylayanlar nesnesinde aksiyon alan kişinin ünvan bilgisinin görünürlüğü
Tipi: System.Boolean
Deklarasyon: public bool ShowProfession{ get; set; }

•	ShowProfessionId

Tanım: Onaylayanlar nesnesinde aksiyon alan kişinin ünvan id bilgisinin görünürlüğü
Tipi: System.Boolean
Deklarasyon: public bool ShowProfessionId { get; set; }

•	ShowUserId

Tanım: Onaylayanlar nesnesinde aksiyon alan kişinin kullanıcı adı bilgisinin görünürlüğü
Tipi: System.Boolean
Deklarasyon: public bool ShowUserId { get; set; }

•	VisibleCustomProperties

Tanım: Görünür kullanıcı özelliklerinin listesi
Tipi: System.Collections.Generic.List```<```string```>```
Deklarasyon: public System.Collections.Generic.List```<```string```>``` VisibleCustomProperties { get; set; }


## 3.19. Kullanıcı Bilgisi

Kullanıcı bilgisi nesnesi, formu oluşturan kullanıcının bilgilerinin otomatik olarak form üzerinde gösterilmesini sağlayan nesnedir.
Kullanıcı bilgisi nesnesi “System.Web.UI.WebControls.TextBox” sınıfındandır.


### 3.19.1. Özellikler 

Kullanıcı bilgisi nesnesi, metin kutusu nesnesi ile aynı sınıfa dahildir. Kullanıcı bilgisi nesnesinin özellikleri hakkında bilgi edinmek için, “Metin Kutusu” dokümanındaki “Özellikler” başlığını inceleyebilirsiniz.
Kullanıcı bilgisi nesnesinin verisi düzenlemeye kapalıdır. Metin kutusu nesnesinin sahip olduğu; ReadOnly, MaxLength, Enabled özellikleri Kullanıcı Bilgisi nesnesi için set edilemez.


### 3.19.2. Validasyon

 Form üzerindeki Kullanıcı bilgisi nesnesinin değerine göre validasyon kod kısmında kontrol yapıları oluşturabilmek için, kullanıcı bilgisi nesnesine direkt nesne ismi ile erişim sağlanır. Form kod kısmında kullanıcı bilgisi nesnesinin değerine erişmek için;
belgeyiDolduran1.Text
yapısı kullanılırken, validasyon kod kısmında direkt
belgeyiDolduran1
şeklinde nesneye erişim sağlanabilir.
Kullanıcı bilgisi nesnesinin özelliklerinde “Veritabanı Alanı Oluştur” seçeneği mevcuttur. Kod tarafında bu nesneye erişim sağlanabilmesi için, bu özelliğin seçili olması gerekmektedir.

Örnek; 
Formu “Ali Doğru” kullanıcısı oluşturmuşsa ve form üzerindeki Metin1 isimli metin kutusu nesnesi boşsa uyarı verdiren kod örneği aşağıdaki gibidir. Bu kontrolün gerçekleşebilmesi için, form üzerindeki “belgeyiDolduran1” isimli kullanıcı bilgisi nesnesinin özelliklerinde “İsim ve Soyisim” alanı seçilmeli ve “Veritabanı Alanı Oluştur” seçeneği işaretlenmelidir.

public override void OnValidateDocument(string view, bool canEdit, Hashtable parameters, ValidationSummary summary)
{
    if (string.IsNullOrEmpty(Metin1) && belgeyiDolduran1 == "Ali Doğru")

    summary.AddMessage("Ali Doğru kullanıcısı Metin1 alanını boş bırakamaz!");
}


## 3.20. Belge Bilgisi

Belge bilgisi nesnesi, forma ait form id, formun oluşturulma tarihi ve belirli formatta oluşturulan formun id bilgisi değerlerinin form üzerinde otomatik gösterilmesini sağlayan nesnedir.
Belge bilgisi nesnesi “System.Web.UI.WebControls.TextBox” sınıfındandır.


### 3.20.1. Özellikler 

Belge bilgisi nesnesi, metin kutusu nesnesi ile aynı sınıfa dahildir. Belge bilgisi nesnesinin özellikleri hakkında bilgi edinmek için, “Metin Kutusu” dokümanındaki “Özellikler” başlığını inceleyebilirsiniz.
Belge bilgisi nesnesinin verisi düzenlemeye kapalıdır. Metin kutusu nesnesinin sahip olduğu; ReadOnly, MaxLength, Enabled özellikleri Belge Bilgisi nesnesi için set edilemez.


### 3.20.2. Validasyon

Form üzerindeki Belge bilgisi nesnesinin değerine göre validasyon kod kısmında kontrol yapıları oluşturabilmek için, belge bilgisi nesnesine direkt nesne ismi ile erişim sağlanır. Form kod kısmında belge bilgisi nesnesinin değerine erişmek için;
belgeBilgisi1.Text
yapısı kullanılırken, validasyon kod kısmında direkt
belgeBilgisi1
şeklinde nesneye erişim sağlanabilir.

Belge bilgisi nesnesinin özelliklerinde “Veritabanı Alanı Oluştur” seçeneği mevcuttur. Kod tarafında bu nesneye erişim sağlanabilmesi için, bu özelliğin seçili olması gerekmektedir.


## 3.21. Form Bilgisi

Form bilgisi nesnesi, Form Başlığı ya da Proje Başlığı bilgisini otomatik olarak formun üzerinde gösteren nesnedir.
Form bilgisi nesnesi “System.Web.UI.WebControls.Label” sınıfındandır.


### 3.21.1. Özellikler 

Form bilgisi nesnesi, etiket nesnesi ile aynı sınıfa dahildir. Form bilgisi nesnesinin özellikleri hakkında bilgi edinmek için, “Etiket” dokümanındaki “Özellikler” başlığını inceleyebilirsiniz.

## 3.22. Resim 

Form üzerinde resim göstermek için kullanılan nesnedir. Genellikle şirket logosu, kullanıcı fotografı gibi görsellerin form üzerinde gösterilmesi için kullanılır.
Resim nesnesi “System.Web.UI.WebControls.Image” sınıfındandır. 


### 3.22.1. Özellikler 

•	AlternateText 

Tanım: Resmin görüntülenemediği durumlarda gösterilen alternatif metin
Tipi: System.String 
Deklarasyon: public virtual string AlternateText { get; set; }

•	DescriptionUrl 

Tanım: Görüntü için bir ayrıntılı açıklama konumunu alır veya ayarlar
Tipi: System.String
Deklarasyon: public virtual string DescriptionUrl { get; set; }} 

•	GenerateEmptyAlternateText 

Tanım: Denetimin boş bir dize değeri için alternatif metin özniteliği oluşturup oluşturmayacağını gösteren bir değer alır veya ayarlar
Tipi: System.Boolean
Deklarasyon: public virtual bool GenerateEmptyAlternateText { get; set; }

•	ImageAlign 

Tanım: Resim nesnesinin hizalanmasını sağlar
Tipi: System.Web.UI.WebControls.ImageAlign
Deklarasyon: public virtual System.Web.UI.WebControls.ImageAlign ImageAlign { get; set; }
Alacağı Değerler;
		AbsBottom 
AbsMiddle
Baseline
Bottom
Left
Middle
NotSet
Right
TextTop
Top

•	ImageUrl 

Tanım: Resim nesnesinde görüntülenecek görüntünün URL bilgisi
Tipi: System.String
Deklarasyon: public virtual string ImageUrl { get; set; }


## 3.23. Çerçeve 

Çerçeve nesnesi, verilen bir adresin form üzerinde çerçeve içerisinde açılmasını sağlayan nesnedir.
Çerçeve nesnesi “eBAControls.eBAFrameControl” sınıfındandır.


### 3.23.1. Özellikler 

•	HasBorder 

Tanım: Kenar çizgilerinin görünürlüğü
Tipi: System.Boolean 
Deklarasyon: public bool HasBorder { get; set; }

•	HasScroll 

Tanım: Kaydırma çubuğunun görünürlüğü
Tipi: System.Boolean 
Deklarasyon: public bool HasScroll { get; set; }

•	Url 

Tanım: Gösterilecek adres bilgisi
Tipi: System.String 
Deklarasyon: public string Url { get; set; }