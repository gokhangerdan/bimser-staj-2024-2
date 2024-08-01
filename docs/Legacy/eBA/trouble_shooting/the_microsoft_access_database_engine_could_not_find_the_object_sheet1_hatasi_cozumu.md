# The Microsoft Access database engine could not find the object 'Sheet1' hatası çözümü

![](https://docsbimser.blob.core.windows.net/imagecontainer/dzfc-bf36960f-a37e-44db-a0eb-7cc2de04e7bd.png)


İlgili Excel'de okunmaya çalışılan Sheet1 isimli sekme gerçekten varsa isim olarak Sheet1 YERİNE Sheet1$ KULLANILMALIDIR.

string sheetName = "Sheet1$";
cmd.CommandText = "SELECT * FROM [" + sheetName + "]";


