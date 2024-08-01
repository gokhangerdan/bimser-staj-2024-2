# Dm'den kod ile dokümanı alma locale indirme

Alt kısımdaki kod ile DM'den local'e döküman indirebilirsiniz.

```
public void fnDmLocal_Execute()
		{
		   	 eBAConnection con = CreateServerConnection();
             string path=@"Eğitim/sample.pdf"; //Dm doküman pathi
             try
                {  
                    con.Open();
                    FileSystem fs = con.FileSystem;
                                     
                    string folderPath=@"C:\\TEMP";
                    System.IO.Directory.CreateDirectory(folderPath);
                    fs.DownloadFileContentToFile(path,folderPath + "\\" + "sample.pdf");                     
                    
                }
                catch (Exception ex)
                {                
                    throw new Exception(" An error ocured while copying attachments!\n" + ex.Message);
                }finally
                {
                   con.Close();        
                }


}
```

