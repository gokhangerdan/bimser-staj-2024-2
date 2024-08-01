# DM'de dosya var mı kontrolü

Alt kısımdaki kod ile DM'den dosya kontrolü yapabilirsiniz.

```
public void btnDosyaKontrol_OnClick(Object sender, EventArgs e)
		{
			    eBAConnection con = CreateServerConnection();
			    FileSystem fs = con.FileSystem;
                string path=@"Eğitim/sample.pdf"; 
                try
                { 
                    con.Open();
                    if(!fs.HasFile(path))
                    {
                        ShowMessageBox("Dosya yok");
                    }
                    else 
                    {
                         ShowMessageBox("Dosya var");
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

