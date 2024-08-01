# eBA Formu Güncelleme 

	if (!eBAConfigurationHelper.ApplicationConfig.DefaultInstanceEnabled) 

	                    { 

	                        eBAConfiguration.Config.InitializeConfiguration(); 

	                    } 

	  

	                    eBAConnection con = CreateServerConnection(); 

	//Connection’ ı bu şekilde açıyorum. 

	  

	                    WorkflowDocument docIMP = con.WorkflowManager.CreateDocument("IM", "IMP"); 

	                    eBAForm frmIMP = new eBAForm(docIMP.DocumentId); 

	Form oluşturup id sinden yakalıyorum 

	  

	                    DataTable dtOncelik = getExcellData( "select * from [ONCELIKLER$]"); 

	Bir excell’ den veri okuyorum gelen satırları formdaki detay tablo nesnesine yazıyorum 

	  

	                    foreach (DataRow row in dtOncelik.Rows) 

	                    { 

	                        FormDetailsGridRow oncRow = frmIMP.DetailsGrids["DTONC"].Rows.Add(); 

	                        oncRow["ONC"].AsString = row["ONCELIK"].ToString(); 

	                        oncRow["ONCACK"].AsString = row["ACIKLAMA"].ToString(); 

	                    } 

	  

	                    frmIMP.Fields[“Metin1”].AsString = “test”; 

	şeklinde de form üzerindeki alanlara veri yazabilirsiniz. 

	  

	                    frmIMP.Update(); 

	  

	                    con.Close();