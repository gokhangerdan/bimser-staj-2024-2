---
title: 7. eBA Work Day Calculator 
sidebar_position: 7
---

# 7. eBA Work Day Calculator 


eBA Workday Calculator, yapılan işlemlerin sürelerinin hesaplanmasına yardımcı olan bir uygulama programlama ara yüzüdür (API). Bu API ile verilen iki tarih arasındaki süre veya verilen bir tarihe ilave bir süre eklenince çıkan tarih sonucu hesaplanabilir. Tarih hesaplamaları, haftalık çalışma günleri, çalışma saatleri, resmi tatiller ve çalışanların izin günleri dikkate alınarak yapılır. Sonuçlar gün veya dakika cinsinden hesaplanabilir. 


## 7.1. WorkDayCalculator 

### 7.1.1. Metotlar 

•	GetDays(eBADBProvider, DateTime, DateTime, CalculationOption, bool, string) 

Tanım: Verilen iki tarih arasındaki süreyi diğer parametreleri de dikkate alarak gün olarak geri döner. 
Deklarasyon: public static int GetDays(eBADBProvider dbProvider, DateTime startDate, DateTime endDate, CalculationOption option, bool holidays, string objectID) 
Parametreler 
dbProvider: eBADB.dll referansından gelen eBADB.eBADBProvider tipinde veri tabanı bağlantı nesnesini belirtir. 
startDate: Hesaplama başlangıç tarihi bilgisini belirtir. 
endDate: Hesaplama bitiş tarihi bilgisini belirtir. 
option: eBAWorkdayCalculator.CalculationOption tipindeki hesaplama seçeneği bilgisini belirtir.  
holidays: Tatil günlerinin hesaplamaya katılıp katılmayacağı bilgisini belirtir. objectID: Tatil günleri hesaplamalarında dikkate alındığında, objectID değeri olarak bir kullanıcı id bilgisi verilirse, bu kullanıcının özel tatillerinin hesaplamalarında dikkate alınır. 
Dönüş Tipi: System.Integer 

Not “eBAWorkdayCalculator.CalculationOption” hakkında detaylı bilgi için, “CalculationOption” başlığına bakınız.  






•	GetMinutes(eBADBProvider, DateTime, DateTime, CalculationOption, bool, string) 

Tanım : Verilen iki tarih arasındaki süreyi diğer parametreleri de dikkate alarak dakika olarak geri döner. 
Deklarasyon : public static int GetMinutes(eBADBProvider dbProvider, DateTime startDate, DateTime endDate, CalculationOption option, bool holidays, string objectID) 
Parametreler  
dbProvider: eBADB.dll referansından gelen eBADB.eBADBProvider tipinde veri tabanı bağlantı nesnesini belirtir. 
startDate: Hesaplama başlangıç tarihi bilgisini belirtir. 
endDate: Hesaplama bitiş tarihi bilgisini belirtir. 
option: eBAWorkdayCalculator.CalculationOption tipindeki hesaplama seçeneği bilgisini belirtir. 
holidays: Tatil günlerinin hesaplamaya katılıp katılmayacağı bilgisini belirtir. 
objectID: Tatil günleri hesaplamalarda dikkate alındığında, objectID değeri olarak bir kullanıcı id bilgisi verilirse, bu kullanıcının özel tatillerinin hesaplamalarında dikkate alınır. 
Dönüş Tipi: System.Integer 

Not “eBAWorkdayCalculator.CalculationOption” hakkında detaylı bilgi için, “CalculationOption” başlığına bakınız.  

•	AddTime(eBADBProvider, DateTime, int, int, CalculationOption, bool, string) 

Tanım: Tarih değerine, hesaplama kriterlerine uygun olarak gün ve dakika cinsinden zaman ekleyip yeni tarih değeri oluşturmayı sağlar. 
Deklarasyon: public static DateTime AddTime(eBADBProvider dbProvider, DateTime startDate, int days, int minutes, CalculationOption option, bool holidays, string objectID) Parametreler 
dbProvider: eBADB.dll referansından gelen eBADB.eBADBProvider tipinde veri tabanı bağlantı nesnesini belirtir. startDate: Hesaplama başlangıç tarihi bilgisini belirtir. days: Eklenecek gün sayısını belirtir. minutes: Eklenecek dakika sayısını belirtir. 
option: eBAWorkdayCalculator.CalculationOption tipindeki hesaplama seçeneğini belirtir.  holidays: Tatil günlerinin hesaplamaya katılıp katılmayacağı bilgisini belirtir. 
objectID: Tatil günleri hesaplamalarında dikkate alındığında, objectID değeri olarak 
bir kullanıcı id bilgisi verilirse, bu kullanıcının özel tatillerinin hesaplamalarında dikkate alınır. 
Dönüş Tipi: System.DateTime 

Not “eBAWorkdayCalculator.CalculationOption” hakkında detaylı bilgi için, “CalculationOption” başlığına bakınız.  


## 7.2. CalculationOption 

CalculationOption, tarih hesaplama yöntemlerini belirten bir enum tipidir.  

Değerleri 

•	WorkingHours: Hesaplama sistemde tanımlanmış haftalık çalışma günleri ve çalışma saatlerine göre yapar. 

Örnek: 
Bir şirkette, çalışma saatleri, hafta içi 08:00 – 18:00 ve Cumartesi günü  08:00 – 13:00  olsun. Hesaplamalar, bu saatler dikkate alınarak yapılacaktır. Böylece gerçekleştirilen çalışılan saat hesaplanabilir. 

•	WorkDays: Hesaplamayı sadece haftalık çalışma günlerine göre yapar. 

Örnek: 
Bir şirkette, çalışma saatleri, hafta içi 08:00 – 18:00 ve cumartesi günü 08:00 – 13:00 olsun. Sadece çalışma günleri dikkate alındığından, cumartesi de bir gün olarak sayılacaktır, ama pazar günü hesaplamalara katılmayacaktır. (Gerçekleştirilen çalışılan gün 6 olarak hesaplanacaktır.) 

•	Absolute: Hesaplamalarda çalışma saatleri dikkate alınmayarak, tarih farkları kullanılır. 


## 7.3. Örnek Kullanım 

Hesaplamalarda, çalışma saatleri dikkate alınarak, iki tarih arasındaki gün ve dakika süreleri hesaplanmaktadır. 
eBADBProvider db = DatabaseTier.CreateConnectionAndOpen(); try {     int days;     double minutes; 
    DateTime startDate = new DateTime(2014, 8, 3); 
    DateTime endDate = new DateTime(2014, 8, 9); 
    string objectID = “huzal”; 
    CalculationOption option = CalculationOption.WorkingHours;     days = WorkDayCalculator.GetDays(db, startDate, endDate, option, true, objectID); 
    minutes = WorkDayCalculator.GetMinutes(db, startDate, endDate, option, calculateHolidaysCheckBox.Checked, objectID) 
    MessageBox.Show(string.Format("Total:\nin Days: {0}\nin Hours: {1}\nin 
Minutes: {2}", days, minutes / 60d, minutes), "Calculation Result"); 
} finally 
{ 
    DatabaseTier.CloseConnection(db); 
} 


	//Hesaplamalarda, çalışma saatleri dikkate alınarak, iki tarih arasındaki gün ve dakika süreleri hesaplanmaktadır. 
	        public void TarihHesapla()
	        {
	            eBADBProvider db = DatabaseTier.CreateConnectionAndOpen();
	            try
	            {
	                int days; double minutes;
	                DateTime startDate = new DateTime(2014, 8, 3);
	                DateTime endDate = new DateTime(2014, 8, 9);
	                string objectID = "huzal";
	                CalculationOption option = CalculationOption.WorkingHours; days = WorkDayCalculator.GetDays(db, startDate, endDate, option, true, objectID);
	                minutes = WorkDayCalculator.GetMinutes(db, startDate, endDate, option, calculateHolidaysCheckBox.Checked, objectID)
	                MessageBox.Show(string.Format("Total:\nin Days: {0}\nin Hours: {1}\nin Minutes: { 2}", days, minutes / 60d, minutes), "Calculation Result"); 
	            }
	            finally
	            {
	                DatabaseTier.CloseConnection(db);
	            }
	        }