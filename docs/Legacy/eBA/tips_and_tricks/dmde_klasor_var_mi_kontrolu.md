# DM'de klasör var mı kontrolü

Alt kısımdaki kod ile DM'den klasör kontrolü yapabilirsiniz.

```
public void btnDMKontrol_OnClick(Object sender, EventArgs e)
{
		    eBAConnection con = CreateServerConnection();
		    FileSystem fs = con.FileSystem;
			
		   string categoryName = "Category1";  // Attachment Category Name
		   string targetFolder = "Eğitim/" + DateTime.Now.Year.ToString() + "/" + DateTime.Now.Month.ToString("D2"); 
                        try
                        { 
                             con.Open();
                             if(!fs.HasFolder(targetFolder + "/" + categoryName))//Dosya var mı yok mu kontrolü
                             {
                                 ShowMessageBox("Klasör yok") ;
                             }
                            else //Varsa Önce siliniz sonra atınız
                            {
                                 ShowMessageBox("Klasör var") ;
                            } 
                       }
                       catch (Exception ex)
                       { 
                            throw new Exception(ex.Message);
                       }
                      finally
                      {
                           con.Close(); 
                      }
}

```

