# eBALogAPIHelper 

eBALogAPIHelper dll i, eBA kurulum dizini altındaki “Common” klasörü içerisinde bulunur. Sisteme log kaydı yazdırmak için kullanılan dll dir.  

eBALogAPIHelper dll i aşağıdaki namespace den oluşur. Bu namespace in barındırdığı tüm sınıflar, sınıflara ait methodlar ve özellikler bu dokümanda detaylı olarak ele alınmıştır. 

eBALogAPIHelper ```>>>>```  eBALogAPIHelper.Helper 

## 1. eBALogAPIHelper.Helper 

Kod ile gerçekleştirilen bir işlem sonucunda log yazdırmak için gerekli sınıfları ve değer listelerini barındırır. Aşağıdaki sınıfları ve değer listesini içerir; 

	eBALogAPIHelper.Helper 

	public class eBALogAPI 

	public class eBALogAttachment 

	public class eBALogFileInfo 

	public class eBALogItem 

	public enum eBALogType 

## 1.1 eBALogAPI 

Temel loglama sınıfıdır. 

### Methodlar 

	public void AddLogAsync(eBALogAPIHelper.Helper.eBALogItem logInfo) 

“logInfo” parametresiyle sisteme asenkron log ekler 

	public void AddLogAsync(eBALogAPIHelper.Helper.eBALogItem logInfo, int debuglevel) 

“logInfo” ve “debuglevel” parametreleri ile sisteme asenkron log ekler 

	public void AddLogAsync(string logText)  

“logText” parametresiyle sisteme asenkron log ekler 

	public void AddLogAsync(string logText, string logDetailsText) 

“logText” ve “logDetailsText” parametreleri ile sisteme asenkron log ekler 

	public void AddLogAsync(string logText, string logDetailsText, eBALogAPIHelper.Helper.eBALogType logType, string userId) 



“logText”, “logDetailsText”, “logType” ve “userId” parametreleri ile sisteme asenkron log ekler 

	public void AddLogAsync(string logText, string logDetailsText, eBALogAPIHelper.Helper.eBALogType logType, string userId, int debuglevel) 

“logText”, “logDetailsText”, “logType”, “userId” ve “debuglevel” parametreleri ile sisteme asenkron log ekle

	public void AddLogAsync(string logText, string logDetailsText, eBALogAPIHelper.Helper.eBALogType logType, string userId, System.Exception exception) 

“logText”, “logDetailsText”, “logType”, “userId” ve “exception” parametreleri ile sisteme asenkron log ekler 

	public void AddLogAsync(string logText, string logDetailsText, eBALogAPIHelper.Helper.eBALogType logType, string userId, System.Exception exception, int debuglevel) 

“logText”, “logDetailsText”, “logType”, “userId”, “exception” ve “debuglevel” parametreleri ile sisteme asenkron log ekler 

	public void AddLogAsync(string logText, string logDetailsText, System.Exception exception) 



“logText”, “logDetailsText” ve “exception” parametreleri ile sisteme asenkron log ekle

	public void AddLogSync(eBALogAPIHelper.Helper.eBALogItem logInfo) 

“logInfo” ve “debuglevel” parametreleri ile sisteme senkron log ekler 

	public void AddLogSync(string logText) 

“logText” parametresiyle sisteme senkron log ekler 

	public void AddLogSync(string logText, string logDetailsText) 

“logText” ve “logDetailsText” parametreleri ile sisteme senkron log ekler 

	public void AddLogSync(string logText, string logDetailsText, eBALogAPIHelper.Helper.eBALogType logType, string userId) 

“logText”, “logDetailsText”, “logType” ve “userId” parametreleri ile sisteme senkron log ekler 

	public void AddLogSync(string logText, string logDetailsText, eBALogAPIHelper.Helper.eBALogType logType, string userId, int debuglevel) 

“logText”, “logDetailsText”, “logType”, “userId” ve “debuglevel” parametreleri ile sisteme senkron log ekler 

	public void AddLogSync(string logText, string logDetailsText, eBALogAPIHelper.Helper.eBALogType logType, string userId, System.Exception exception) 

“logText”, “logDetailsText”, “logType”, “userId” ve “exception” parametreleri ile sisteme senkron log ekler 

	public void AddLogSync(string logText, string logDetailsText, eBALogAPIHelper.Helper.eBALogType logType, string userId, System.Exception exception, int debuglevel) 

“logText”, “logDetailsText”, “logType”, “userId”, “exception” ve “debuglevel” parametreleri ile sisteme senkron log ekler 

	public void AddLogSync(string logText, string logDetailsText, System.Exception exception) 

	public void AddLogSync(string logText) 

“logText”, “logDetailsText” ve “exception” parametreleri ile sisteme asenkron log ekler 

	public eBALogAPIHelper.Helper.eBALogItem CreateLogItem(string logText, string logDetailsText, eBALogAPIHelper.Helper.eBALogType logType, string userId) 



“logText”, “logDetailsText”, “logType” ve “userId” parametreleri ile eBALogItem tipinde log öğesi yaratır 

	public eBALogAPIHelper.Helper.eBALogItem CreateLogItem(string logText, string logDetailsText, eBALogAPIHelper.Helper.eBALogType logType, string userId, System.Exception exception) 

“logText”, “logDetailsText”, “logType”, “userId” ve “exception” parametreleri ile eBALogItem tipinde log öğesi yaratır 

	public void Dispose() 

log nesnesi bağlantısını kapatır ve nesne içeriğini boşaltır 

	public eBALogAPI(string applicationName, string instance) 


“applicationName” ve “instance” parametre değerleri verilerek eBALogAPI sınıfından yeni bir nesne örneği oluşturur 

	```public System.Collections.Generic.List<eBALogAPIHelper.Helper.eBALogFileInfo> GetFiles(string path) ```

Belirtilen path deki dosyaları getirir 

	public string[] GetFolders(string path) 

Belirtilen path deki klasörleri getirir 

	public string[] GetLogDays(string application) 

Log günlerini dizin olarak tutan methoddur 

	public byte[] GetLogFile(string path) 

Log dosyalarını byte dizini olarak tutan methoddur 

	public byte[] GetLogFileTail(string path, long index) 

Log dosya kuyruğu methodudur 

	```public System.Collections.Generic.List<eBALogAPIHelper.Helper.eBALogItem> GetLogs(string application, System.DateTime logDate, int logTime) ```

Logları getiren methoddur 

	public void WaitPendingLogs(int timeout) 

Askıda kalan logları belirli bir süre bekleten methoddur 

### Özellikler 

	public string ApplicationName { get; }  

Uygulama adı değeridir 

	public string DefaultLogUser { get; set; } 

Varsayılan log kullanıcısı değeridir 

	public bool HasPendingLogs { get; }  

Askıda log var mı değeridir 

	public string Instance { get; } 

Instance değeridir 

	public bool ResumeOnException { get; set; } 

Exception devam etme durum bilgisidir 

## 1.2 eBALogAttachment 

Log eki sınıfıdır. 

### Methodlar 

	public eBALogAttachment() 

eBALogAttachment sınıfından yeni bir nesne örneği oluşturur 

### Özellikler 

	public byte[] Content { get; set; } 

İçerik değeridir 

	public string Name { get; set; } 



İsim değeridir 

## 1.3 eBALogFileInfo 

Log dosyası bilgi sınıfıdır. 

### Log dosyası bilgi sınıfıdır. 

	public eBALogFileInfo() 



eBALogFileInfo sınıfından yeni bir nesne örneği oluşturur 

### Özellikler 

	public string FileName { get; set; }  

Dosya adı değeridir 

	public string Size { get; set; }  

Boyut değeridir 

## 1.4 eBALogItem 

Log ögesi sınıfıdır. 

### Methodlar 

	public void AddAttachment(string name, byte[] content)  

“name” ve “content” parametreleri ile ek ekleyen methoddur 

	public void AddAttachment(string name, System.IO.Stream stream)  

“name” ve “stream” parametreleri ile ek ekleyen methoddur 

	public void AddFileAsAttachment(string filename)  

Belirtilen dosyayı ek olarak ekleyen methoddur 

	public void AddFileAsAttachment(string name, string filename)  

“name” ve “filename” parametreleri ile belirtilen dosyayı ek olarak ekleyen methoddur 

	public void AddTextAsAttachment(string name, string text)  

Metni ek olarak ekleyen methoddur 

	public eBALogItem() 

eBALogItem sınıfından yeni bir nesne örneği oluşturur 

### Özellikler 

	public string LogDetailsText { get; set; } 

Detaylı log metni değeridir 

	public string LogText { get; set; } 

Log metni değeridir 

	public string UserID { get; set; } 

Kullanıcı id değeridir 

	```public System.Collections.Generic.List<eBALogAPIHelper.Helper.eBALogAttachment> Attachments ```

eBALogAttachment tipindeki eklerin listesidir 

	public eBALogAPIHelper.Helper.eBALogType LogType 

Log tipi değeridir 

## 1.5

Log tipi değerlerini barındıran değer listesidir. 

### Değerler 

Error  

Hata 

None 

Hiçbiri 

Warning 

Uyarı 

## Örnek Kullanım:

Akış kod kısmında log yazdırma : 
```
	%SystemPath%\Common\eBALogAPIHelper.dll 

	  

	using eBALogAPIHelper.Helper; 





	  

	namespace logTutma 

	{ 

	    public partial class FlowCode 

	    { 

	eBALogAPI logApi = new eBALogAPI("OrnekProje", "WSHttpBinding", "http://localhost/eBALogService"); 



	           public void WriteLog(string caption, string description, Exception ex = null) 

	           { 

	            logApi.AddLogAsync(caption, description, ex == null ? eBALogType.None : eBALogType.Error, "", ex); 

	           } 



	public void FlowScript1_Execute() 

	{ 

	                     WriteLog("Müşteri SAP",  "I_CUSTOMER Döngüye Girdi " , null); 

	} 

	    } 

	}
```