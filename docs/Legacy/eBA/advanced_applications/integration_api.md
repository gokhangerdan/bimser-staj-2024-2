# eBAIntegrationAPI 

eBAIntegrationAPI dll i, eBA kurulum dizini altındaki “Common” klasörü içerisinde bulunur. eBA projesi içerisinde Integration Manager da hazırlanmış olan sorguları çalıştırabilmek ve çalıştırılan sorgu sonucu dönen değerleri projenin form ya da akış kısımlarında işleyebilmek için kullanılan dll dir.  

eBAIntegrationAPI dll i aşağıdaki namespace den oluşur. Bu namespace in barındırdığı tüm sınıflar, sınıflara ait methodlar ve özellikler bu dokümanda detaylı olarak ele alınmıştır. 

## 1.eBAIntegrationAPI 

### Çalıştırılmak istenen sorguyu çağırmak ve sorgu sonucu dönen verileri kod içerisinde kullanabilmek için gerekli sınıfları barındırır. Aşağıdaki sınıfları içerir; 

eBAIntegrationAPI 

public class eBAIntegrationQuery  

public class eBAIntegrationQueryParameters : System.Collections.Generic.Dictionary<string, string>  

public class eBAIntegrationReader  

public class eBAPagedIntegrationReader  

public class eBAQueryResult  

## 1.1 eBAIntegrationQuery    

Integration Manager da tanımlı bir sorguyu kodda çağırmak için kullanılan sınıftır. 

### Methodlar 

	public eBAIntegrationQuery(string connection, string query) 

Connection ve query bilgileri parametre olarak verilerek eBAIntegrationQuery sınıfından yeni bir nesne örneği oluşturur 

	public System.Data.DataTable Execute(eBAPI.Connection.eBAConnection connection) 

Connection parametresi verilerek tanımlanan sorgu sonucunu DataTable tipinde döndürür 

	public eBAIntegrationAPI.eBAQueryResult Execute(eBAPI.Connection.eBAConnection connection, int topCount) 

Connection ve topCount parametresi verilerek tanımlanan sorgu sonucunu eBAQueryResult tipinde döndürür 

### Özellikler 

	public string Connection { get; set; } 

Connection değeridir 

	public eBAIntegrationAPI.eBAIntegrationQueryParameters Parameters { get; } 

Sorgu parametreleri değeridir 

	public string Query { get; set; } 

Sorgu değeridir 

## 1.2 eBAIntegrationQueryParameters Sorgu parametreleri sınıfıdır. 

### Methodlar 

	public eBAIntegrationQueryParameters() 

eBAIntegrationQueryParameters sınıfından yeni bir nesne örneği oluşturur 

## 1.3 eBAIntegrationReader 

Veri okuma işleminin gerçekleştirildiği sınıftır. 

### Methodlar 

	public void Close() 



Okuma işlemi bittiğinde reader nesnesini kapatır 

	public void Dispose() 

reader nesnesi bağlantısını kapatır ve nesne içeriğini boşaltır 

	public eBAIntegrationReader(eBAPI.Connection.eBAConnection connection, string connectionName, string queryName) 

eBAIntegrationReader sınıfından yeni bir nesne örneği oluşturur 

	public bool IsAlive() 

reader nesnesi kapatılmış mı aktif mi durumu bilgisidir 

	public bool Read() 

Okuma durumu bilgisidir 

	public bool Read(int readCount) 

readCount parametresi ile okuma durumu bilgisini verir 

### Özellikler 

	public string Connection { get; } 

Connection değeridir 

	public System.Data.DataTable Data { get; } 

DataTable tipindeki veridir 

	public int DefaultReadCount { get; set; } 

Varsayılan okuma sayısı değeridir 

	public bool HasMoreData { get; } 



Daha fazla veri mevcut mu durum değeridir 

	public bool IsClosed { get; } 

Kapalı mı durumu bilgisidir 

	public eBAIntegrationAPI.eBAIntegrationQueryParameters Parameters { get; } 

Sorgu parametreleri değeridir 

	public string Query { get; } 

Sorgu değeridir 

## 1.4 eBAPagedIntegrationReader 

Sayfalanmış veri okuma işleminin gerçekleştirildiği sınıftır. 

### Methodlar 

	public void Close() 

Okuma işlemi bittiğinde reader nesnesini kapatır 

	public void Dispose() 

reader nesnesi bağlantısını kapatır ve nesne içeriğini boşaltır 

	public eBAPagedIntegrationReader(eBAPI.Connection.eBAConnection connection, string connectionName, string queryName, int itemsPerPage, int cachedPageCount) 

eBAPagedIntegrationReader sınıfından yeni bir nesne örneği oluşturur 

	public bool MoveNextPage() 

Sonraki sayfaya taşı durum değeridir 

	public bool MoveNextPage(int pagesToForward) 

pagesToForward parametresi verilerek sonraki sayfaya taşıma durumu değeridir 

	public bool MovePreviousPage() 

Önceki sayfaya taşı durum değeridir 

	public bool MovePreviousPage(int pagesToBackward) 

pagesToBackward parametresi verilerek önceki sayfaya taşıma durumu değeridir 

	public void Open() 

reader nesnesini açar 

### Özellikler 

	public int CachedPageCount { get; } 

Cache lenen sayfa sayısı değeridir 

	public string Connection { get; } 

Connection değeridir 

	public System.Data.DataTable CurrentPage { get; } 

Mevcut sayfa değeridir 

	public int CurrentPageCount { get; } 

Mevcut sayfa sayısı değeridir 

	public int CurrentPageNumber { get; } 

Mevcut sayfa numarası değeridir 

	public int ItemsPerPage { get; } 

Sayfa başı öge değeridir 

	public string Query { get; } 

Sorgu bilgisidir 

## 1.5 eBAQueryResult 

Sorgu sonuç sınıfıdır. 

### Methodlar 

	public eBAQueryResult()  

eBAQueryResult sınıfından yeni bir nesne örneği oluşturur 

### Özellikler 

	public System.Data.DataTable Data { get; set; } 

DataTable tipinde veri değeridir 

	public bool HasMoreData { get; set; }  



Daha fazla veri var mı durumu bilgisidir 

## Örnek Kullanım:  

Akış kod kısmında Pozisyon Grubu nesnesine sorgu sonucu dönen kişileri atama : 
```
	%SystemPath%\Common\eBAPI.dll 

	%SystemPath%\Common\eBAIntegrationAPI.dll 

	  

	using System.Data; 

	using eBAPI; 

	using eBAPI.Connection; 

	using eBAIntegrationAPI; 

	  

	  

	public void FlowScript1_Execute() 

	{ 

	    eBAConnection Connection = CreateServerConnection(); 

	    Connection.Open(); 

	    try 

	    { 

	        eBAIntegrationQuery qry = new eBAIntegrationQuery("EBA", "USERLOAD"); 

	        qry.Parameters.Add("DEPARTMENT", FlowStarter1.Department ); 



	        DataTable dt = qry.Execute(Connection); 

	        if(dt.Rows.Count >0) 

	        { 

	            foreach(DataRow dr in dt.Rows) 

	            { 

	                FlowGroup1.AddConstantUser(dr.ItemArray[0].ToString()); 

	            }    

	        } 

	        else 

	        { 

	    // Grup içinde kimse yoksa akışın kime gitmesini istiyorsanız onun idsi yazılır 

	            FlowGroup1.AddConstantUser("admin");  

	        } 

	    } 

	    catch (Exception ex) 

	    { 

	        throw ex; 

	    } 

	    finally 

	    { 

	        Connection.Close(); 

	    }      

	}
```