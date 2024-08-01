# Varolan dosyaya versiyon ekleme

DM'de bulunan belgeye alt kısımda bulunan kod ile versiyonlama yapabilirsiniz.

```
public void BtnVersiyon_OnClick(Object sender, EventArgs e)
		{
			
            
            int frmID = 1254; //Akışta Dokuman1.ProfileId şeklinde alabilirsiniz.
            eBAForm frm = new eBAForm(frmID);
            string dosyaadi = "";
            string filePath = "";
            Stream str = null;
            eBAConnection con = CreateServerConnection();
            con.Open();
 
            try
            {
                con.Open();
                DMFile df = con.FileSystem.GetFile("workflow/SampleProject/Form/" + frmID + ".wfd");
                DMCategoryContentCollection SourceAttachments = df.GetAttachments("Category1");
                DMFileContent fl = SourceAttachments[0];
                dosyaadi = fl.ContentName;                
 
                str = df.CreateAttachmentContentDownloadStream("Category1", dosyaadi);
                filePath = "Eğitim/" + dosyaadi;
                if (!con.FileSystem.HasFile(filePath))
                {
                    DMFile newFile = con.FileSystem.CreateFile(filePath);
                    newFile.Upload(str);
 
                    /*
                    //İlk atarken 1 versiyonunu vermek için aşağdaki kodu kullanabilirsiniz. Kullanımı zorunlu değil. Versiyon vermeden de atılabilir. 
                    DMCreateFileParameters dcfp = new DMCreateFileParameters(); 
                    DMVersion vrs = new DMVersion(1, 0);
                    dcfp.Version = vrs;                    
                    DMFile newFile = con.FileSystem.CreateFile(filePath, dcfp);
                    newFile.Upload(str);
                    */
                }
                else
                {
                    DMFile versionFile = con.FileSystem.CreateFileMajorVersion(filePath);   //Majör versiyon vermek için                 
                    versionFile.Upload(str);
                    versionFile.SetPublishedVersion(versionFile.Version);
                    /*
                    DMFile vrsFile = con.FileSystem.CreateFileMinorVersion(filePath); //Minör versiyon vermek için
                    vrsFile.Upload(str);
                    vrsFile.SetPublishedVersion(vrsFile.Version);
                    
                    */
                    
                    ShowMessageBox("Versiyon ekleme başarılı");
                }
            }
            finally
            {
                con.Close();
            }


		}

```

