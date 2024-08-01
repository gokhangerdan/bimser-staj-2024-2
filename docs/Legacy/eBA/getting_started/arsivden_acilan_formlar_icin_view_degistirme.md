# Arşivden Açılan Formlar için View Değiştirme 

Arşivlerden forma girince bunu algılama özelliği; 

	string DocumentOpenSource; //"archive" ise arşivden girilmişdemektir. Null kontrolü yapılmalıdır. 

	string DocumentOpenArchiveName; //arşivden girilmiş ise arşivin adı. arşivden girilmemişse "null" dur. 

	string DocumentOpenArchiveType; //arşivden girilmiş ise arşivin tipi. arşivden girilmemişse "null" dur. 

	//Alabileceği değerler : "dataview","dynamic","form","process" 

Örnek

	public void OnLoadData() 

	{ 

	     if (DocumentOpenSource!=null && DocumentOpenSource.Equals("archive")) { 

	         CurrentView = "test"; 

	     } 

	}