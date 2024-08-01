# Relation DM'e kod ile yükleme

Alt kısımdaki kod ile DM 'de ilişkili olarak döküman yükleyebilirsiniz.

```
public void btnRelation_OnClick(Object sender, EventArgs e)
		{
			eBAConnection con = CreateServerConnection();
            con.Open();
            FileSystem fs = con.FileSystem;
            DMFile dmDosya = fs.GetFile("Eğitim/Sample.pdf"); //Dmde relations ekleyeceğimiz dosyanın pathi. Yani bu dosyaya Attachmenttan relations ekliycez
            DMFile formeBA = fs.GetWorkflowFile(id);
            foreach(DMFileContent content in formeBA.GetAttachments("Category1")) //formdaki attachmentlara ulaşıyoruz
            {
                DMFile fileolusan = fs.CreateFile(@"Eğitim/"+content.ContentName);   //Formdaki attachmenti Dme kayıt ediyoruz.
                fileolusan.Upload(formeBA.CreateAttachmentContentDownloadStream("Category1",content.ContentName));
                
                dmDosya.AddRelation(@"Eğitim/"+content.ContentName,"Category1"); //Dmdeki dökümana eklemeyi yapıyoruz.
            }
            con.Close(); 

		}

```

