# Attachment Kopyalama

	tring sourcePath="",destPath=""; 

	           eBAConnection eBACon = CreateServerConnection(); 

	              eBACon.Open(); 

	  

	              try 

	              { 

	  

	                  FileSystem fs = eBACon.FileSystem; 

	                  DMFile fileExcel = fs.GetFile(dosyanınAlınacağıFormunPathi);//ComboBox'tan seçilen firmanın kayıtlı olduğu parametrik formun pathi 

	  

	                  DMCategoryContentCollection SourceAttachments = fileExcel.GetAttachments("default");//parametrik formdaki attachmentlar alınıyor 

	  

	                  DMFileContent fl = SourceAttachments[0]; 

	                  byte[] att = fileExcel.DownloadAttachmentContentBytes("default",fl.ContentName);//Parametrik formdan attachmentlar indiriliyor 

	  

	                  //    throw new Exception(dosyaadi); 

	                  DMFile file = fs.GetFile(YüklenecekFormunPathi);//Sözleşmeni yükleneceği formun pathi 

	                  file.UploadAttachmentContentFromByteArray("default",fl.ContentName,att);//sözleşme yükleniyor. 

	  

	              } 

	  

	              finally 

	              { 

	                  eBACon.Close(); 

	RefreshAttachments(Attachment1); 

	              }