# eBAFormData.dll  Dokümanı

## eBAFormData

eBAFormData dll i, eBA kurulum dizini altındaki “Common” klasörü içerisinde bulunur. eBA formlarının verilerine, veritabanı bağlantısı ve sorgularına ihtiyaç duymadan, erişim sağlanabilmesini ve güncelleme yapılabilmesini sağlayan dll dir.

eBAFormData dll i aşağıdaki namespace den oluşur. Bu namespace in barındırdığı tüm sınıflar, sınıflara ait methodlar ve özellikler bu dokümanda detaylı olarak ele alınmıştır.
- eBAFormData



eBA formları üzerindeki verilere erişim sağlayabilmek ve değişiklik yapabilmek için gerekli sınıfları barındırır. Aşağıdaki sınıfları ve değer listesini içerir;

-	public enum ApproverType
-	public class Column
-	public class ColumnCollection
-	public class eBAForm
-	public class FieldCollection
-	public class FieldValue
-	public class FormCheckList
-	public class FormCheckListCollection
-	public class FormCheckListRow : eBAFormData.FieldCollection
-	public class FormCheckListRowCollection
-	public class FormDetails
-	public class FormDetailsCollection
-	public class FormDetailsGrid
-	public class FormDetailsGridCollection
-	public class FormDetailsGridRow : eBAFormData.FieldCollection
-	public class FormDetailsGridRowCollection
-	public class FormDetailsRow : eBAFormData.FieldCollection
-	public class FormDetailsRowCollection
-	public class FormList
-	public class FormListCollection
-	public class FormListRow : eBAFormData.FieldCollection
-	public class FormListRowCollection
-	public class FormTable
-	public class FormTableCollection
-	public class FormTableRow : eBAFormData.FieldCollection
-	public class FormTableRowCollection


### 1.1)	ApproverType

Onaylayan tipi değerlerini barındırır.



![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData1-a156ec74-8478-4aef-a262-53354230a455.png)

### 1.2)Column

Kolon özelliklerini barındıran sınıftır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData2.1-d98b7d50-fe10-4f11-9768-4dbad942ecac.png)

### 1.3)ColumnCollection

Kolon yığın sınıfıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData3-fa4a3798-6e89-4df8-b478-1c9ea9052d14.png)

### 1.4)eBAForm

Form üzerindeki bütün nesneleri içerisinde barındırır ve bu nesneler üzerinde değişiklik yapılabilmesine imkan sağlar.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData5.1-c74bdab6-c869-45fc-8213-8155fabd20ce.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData5.2-6e92cec1-43d0-4617-ba02-0e9495b3384c.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData5.3-2f1c2eda-a93e-4610-aca8-2a4521d4f2a0.png)

### 1.5)FieldCollection

Alan yığını sınıfıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData6-cc469b07-576e-46bf-a290-e12b35a95f0f.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData7-b78181cf-da56-4ee6-8293-3563cac527aa.png)

### 1.6)FieldValue

Alan değeri özelliklerini barındıran sınıftır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData1-a156ec74-8478-4aef-a262-53354230a455.png)

### 1.7)FormCheckList

Formdaki CheckList nesnesi sınıfıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData9-c16f77d9-d797-4d3f-b816-153c0ee4e2f7.png)

### 1.8)FormCheckListCollection

Formdaki CheckList nesneleri yığın sınıfıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData10-3687ccb8-1d08-4692-806b-458529cbbf93.png)

### 1.9)FormCheckListRow

Formdaki CheckList nesnesinin satır sınıfıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData11-480c6401-e009-4462-a44e-e2089e9e34db.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData11.1-1e80357d-88fc-47f2-84f9-e1003296ce5d.png)

### 1.10)FormCheckListRowCollection

Formdaki CheckList nesnesinin satır yığın sınıfıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData12-63c227ba-2946-49aa-ac1b-17132c162321.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData12.1-27d1cca5-269e-43eb-8031-4daaa6902d2b.png)

### 1.11)FormDetails

Formdaki Details nesnesi sınıfıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData13-440115a4-589c-469c-ac08-5a97a9bfc413.png)

### 1.12)	FormDetailsCollection

Formdaki Details nesneleri yığın sınıfıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData14-36e753aa-224b-4cca-8650-2057149111a7.png)

### 1.13)	FormDetailsGrid

Formdaki DetailsGrid nesnesi sınıfıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData15-5d0b4dd4-2d0e-48c6-a363-db3a110e3fb7.png)

### 1.14)	FormDetailsGridCollection

Formdaki DetailsGrid nesneleri yığın sınıfıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData16-28890586-1582-4f39-a611-2c440ba34757.png)

### 1.15)	FormDetailsGridRow

Formdaki DetailsGrid nesnesinin satır sınıfıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData17-0c8ee09e-ae4e-47ee-85cc-44708cdda263.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData17.1-aef0763c-dfae-4eac-94e4-d3ae614a3e2e.png)

### 1.16)	FormDetailsGridRowCollection

Formdaki DetailsGrid nesnesinin satır yığın sınıfıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData18-a51af4da-0210-47b6-82c3-136f0e2f648a.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData18.1-32617d0f-79b0-4e89-858e-4c1f04e0c90c.png)

### 1.17)	FormDetailsRow

Formdaki Details nesnesinin satır sınıfıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData19-27af16c3-e878-4b0b-94f5-413411b35b89.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData19.1-062e98a5-1f3e-4c9d-a87d-68c1e5b2bdde.png)

### 1.18)	FormDetailsRowCollection

Formdaki Details nesnesinin satır yığın sınıfıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData20-16989736-08a8-45bf-96d1-043d4ad4f52c.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData20.1-40c7abd5-2c6d-4f23-acf1-3e17ed6c20ee.png)

### 1.19)	FormList

Formdaki List nesnelerinin sınıfıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData21-f75edf6e-8687-463d-8c8c-b31521f73e86.png)

### 1.20)	FormListCollection

Formdaki List nesnelerinin yığın sınıfıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData22-c5ba7156-e135-4c8a-88da-427ea5038657.png)

### 1.21)	FormListRow

Formdaki List nesnelerinin satır sınıfıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData23-1bf4d8d1-9245-4b23-8b94-51c132465c5e.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData23.1-0a9c76ad-e25e-4a61-9804-7847e24127e1.png)

### 1.22)	FormListRowCollection

Formdaki List nesnelerinin satır yığın sınıfıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData24-acab63e4-b575-4c19-9335-158fac8e482e.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData24.1-2b5df7a7-1572-4afe-8049-e94ff23afe1b.png)

### 1.23)	FormTable

Formdaki Table nesnesi sınıfıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData25-ec1ff6d8-a394-42e8-adab-5f9571ac57f6.png)

### 1.24)	FormTableCollection

Formdaki Table nesnesi yığın sınıfıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData26-92796128-dcc4-445a-96ba-06f26d7fec53.png)

### 1.25)	FormTableRow

Formdaki Table nesnesinin satır sınıfıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData27-fa4f4577-1f03-40c6-8da2-71b9b0a71dcd.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData27.1-8b6b639c-3ed7-4e15-ac35-dcbdb9fa0647.png)

### 1.26)	FormTableRowCollection

Formdaki Table nesnelerinin satır yığın sınıfıdır.

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData28-d33d9a5e-2cfb-4a82-a7e8-1f4576cd13a5.png)

![](https://docsbimser.blob.core.windows.net/imagecontainer/eBAFormData28-9a8db9d3-09d4-49b8-a053-20efa9cc516f.png)

## Örnek Kullanım Yapıları

### •	Form İşlemleri – Tekil Verileri Alma:

	eBAForm frm = new eBAForm(int FormId);
	string str = frm.Fields["Metin1"].AsString; // Metin Alma
	int integer = frm.Fields["Metin2"].AsInteger; // Tam Sayı Alma
	DateTime date = frm.Fields["Metin3"].AsDateTime; // Tarih Alma
	bool bl = frm.Fields["Secim1"].AsBool; // Seçim Alma (Tekli ve Çoklu seçim kutusu)
	double dbl = frm.Fields["Metin4"].AsDouble; // Virgüllü Sayı Alma
	string listeText = frm.Fields["Liste1_TEXT"].AsString; // Liste Text değerini alma
	string listeValue = frm.Fields["Liste1"].AsString; // Liste Value Değerini Alma
	decimal dec = Convert.ToDecimal(frm.Fields["Metin5"].Value); // Para Değeri Alma


### •	Form İşlemleri – Tekil Verileri Güncelleme:

	eBAForm frm = new eBAForm(int FormId);
	frm.Fields["Metin1"].AsString = "String Veri"; // Metin Güncelleme
	frm.Fields["Metin2"].AsInteger = "Integer Veri"; // Tam Sayı Güncelleme
	frm.Fields["Metin3"].AsDateTime = new DateTime(2019,4,16); // Tarih Güncelleme
	frm.Fields["Secim1"].AsBool = true; // Seçim Güncelleme (Tekli ve Çoklu seçim kutusu)
	frm.Fields["Metin4"].AsDouble = 3.14; // Virgüllü Sayı Güncelleme
	frm.Fields["Liste1_TEXT"].AsString = "String Text Verisi"; // Liste Text değerini Güncelleme
	frm.Fields["Liste1"].AsString = "String Value Verisi"; // Liste Value Değerini Güncelleme
	frm.Fields["Metin5"].Value = Convert.ToDecimal(153.55); // Para Değeri Güncelleme
	frm.Update(); // Güncellenen verileri veritabanına yazma


### •	Form İşlemleri – Detay Tablo Verilerini Alma

	Not: Sadece metin tipi gösterilmiştir, diğer tipler yukarıdaki işlemlerdeki gibi kullanılabilir.


	eBAForm frm = new eBAForm(int FormId);

	// Bilinen satırdaki veriyi alma
	string str1 = frm.DetailsGrids["DetayTabloAdı"].Rows[int SatırNo]["KolonAdı"].AsString;

	// Tüm Satırları döngü ile işleyip veri alma
	foreach (FormDetailsGridRow row in frm.DetailsGrids["DetayTabloAdı"].Rows) 
	{
	    string str2 = row["KolonAdı"].AsString;
	} 


### •	Form İşlemleri – Detay Tablo Verilerini Güncelleme

	Not: Sadece metin tipi gösterilmiştir, diğer tipler yukarıdaki işlemlerdeki gibi kullanılabilir

	eBAForm frm = new eBAForm(int FormId);

	// Bilinen satırdaki veriyi güncelleme
	frm.DetailsGrids["DetayTabloAdı"].Rows[int SatırNo]["KolonAdı"].AsString = "String Veri"; 

	// Tüm Satırları döngü ile işleyip veriyi güncelleme
	foreach (FormDetailsGridRow row in frm.DetailsGrids["DetayTabloAdı"].Rows)           
	{
	    row["KolonAdı"].AsString = "String Veri";
	}
	frm.Update(); // Güncellenen verileri veritabanına yazma 


### •	Form İşlemleri – Tablo Verilerini Alma

	Not: Sadece metin tipi gösterilmiştir, diğer tipler yukarıdaki işlemlerdeki gibi kullanılabilir.


	eBAForm frm = new eBAForm(int FormId);

	// Bilinen satırdaki veriyi alma
	string str1 = frm.Tables["TabloAdı"].Rows[int SatırNo]["KolonAdı"].AsString;

	// Tüm Satırları döngü ile işleyip veri alma
	foreach (FormTableRow row in frm.Tables["TabloAdı"].Rows)
	{
	    string str2 = row["KolonAdı"].AsString;
	}


### •	Form İşlemleri – Tablo Verilerini Güncelleme

	Not: Sadece metin tipi gösterilmiştir, diğer tipler yukarıdaki işlemlerdeki gibi kullanılabilir


	eBAForm frm = new eBAForm(int FormId);

	// Bilinen satırdaki veriyi güncelleme
	frm.Tables["TabloAdı"].Rows[int SatırNo]["KolonAdı"].AsString = "String Veri"; 

	// Tüm Satırları döngü ile işleyip veriyi güncelleme
	foreach (FormTableRow row in frm.Tables["TabloAdı"].Rows)            
	{
	    row["KolonAdı"].AsString = "String Veri";
	}
	frm.Update(); // Güncellenen verileri veritabanına yazma


### •	Form İşlemleri – Detaylar Verilerini Alma

	Not: Sadece metin tipi gösterilmiştir, diğer tipler yukarıdaki işlemlerdeki gibi kullanılabilir.
	Not: Detaylar nesnesi içinde aslında başka bir form bulunduğu için her satır aslında bir eBAForm sınıfını içermektedir ve bu eBAForm sınıfına yukarıda belirtilen tüm işlemler ile erişilebilir.

	eBAForm frm = new eBAForm(int FormId);

	// Bilinen satırdaki veriyi alma
	eBAForm modalForm1 = frm.Details["DetaylarAdı"].Rows[int SatırNo].Form;
	string str1 = modalForm1.Fields["Metin1"].AsString;

	// Tüm Satırları döngü ile işleyip veri alma
	foreach (FormDetailsRow row in frm.Details["DetaylarAdı"].Rows)
	{
	    eBAForm modalForm2 = row.Form;
	    string str2 = modalForm2.Fields["Metin1"].AsString;
	}


### •	Form İşlemleri – Detaylar Verilerini Güncelleme

	Not: Sadece metin tipi gösterilmiştir, diğer tipler yukarıdaki işlemlerdeki gibi kullanılabilir.
	Not: Detaylar nesnesi içinde aslında başka bir form bulunduğu için her satır aslında bir eBAForm sınıfını içermektedir ve bu eBAForm sınıfına yukarıda belirtilen tüm işlemler ile erişilebilir.

	eBAForm frm = new eBAForm(int FormId);

	// Bilinen satırdaki veriyi alma
	eBAForm modalForm1 = frm.Details["DetaylarAdı"].Rows[int SatırNo].Form;
	modalForm1.Fields["Metin1"].AsString = "String Veri";
	modalForm1.Update();//Detaylar içindeki eBAForm için Güncellenen verileri veritabanına yazma

	// Tüm Satırları döngü ile işleyip veri alma
	foreach (FormDetailsRow row in frm.Details["DetaylarAdı"].Rows)
	{
	    eBAForm modalForm2 = row.Form;
	    modalForm2.Fields["Metin1"].AsString = "String Veri";
	    modalForm2.Update();//Detaylar içindeki eBAForm için Güncellenen verileri veritabanına yazma
	}