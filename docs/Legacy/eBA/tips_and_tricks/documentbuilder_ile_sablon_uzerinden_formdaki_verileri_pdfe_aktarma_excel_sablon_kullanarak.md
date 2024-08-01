# DocumentBuilder ile şablon üzerinden formdaki verileri pdfe aktarma (excel şablon kullanarak)

DocumentBuilder ile şablon üzerinden formdaki verileri PDF'e aktarmak için örnek kod alt kısımda bulunmaktadır.

```
public void btnPDFExcel_OnClick(Object sender, EventArgs e)
		{
			eBAConnection con = CreateServerConnection();
            con.Open();
            try
            {
                string tmpPath = "files/Excel.xlsx";
                DMFile tmpFile = con.FileSystem.GetFile(tmpPath);
                //Stream stream = new MemoryStream();
                eBADocumentBuilder.ExcelDocument excel = new eBADocumentBuilder.ExcelDocument();
                excel.Items.AddText("Alan1", txtAdd.Text);
 
                excel.Build(tmpFile.Download());
                using (Stream respStream = new MemoryStream())
                {
                    excel.Save(respStream, SaveFormat.Xlsx); //Pdf formatında oluşması için
                    respStream.Seek(0, SeekOrigin.Begin);
                    WriteToResponse(respStream, "Excel2.Xlsx"); //Clienta localine indirmek için //Form tarafında kullanılabilir.
                }
            }
            finally
            {
                con.Close();
            }
}
```

