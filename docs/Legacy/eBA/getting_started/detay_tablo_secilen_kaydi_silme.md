# Detay Tablo Seçilen Kaydı Silme 

Detay Tabloya eklenen kayıtları silmek için tablonun özelliği olan SİL butonu kullanıldığında en sondaki kayıttan silmeye başlıyor. Seçilen satırı silmek için aşağıdaki kod örneği kullanılabilir. 

	//Detaylar tabloyu bir datatable'a kopyalayıp, içindeki checkbox objesine göre silme kodu  

	  

	DataTable dt = new DataTable("Seda");  

	// kendı kolonlarınıza gore datatable kolonlar olusturmak 

	                                  dt.Columns.Add("lst_tbl_PlantCode",typeof(String)); 

	                                  dt.Columns.Add("txt_tbl_BoxPlant",typeof(String)); 

	                                  dt.Columns.Add("txt_ReqCreditLimit",typeof(String)); 

	                                  dt.Columns.Add("lst_PaymentTerm",typeof(String)); 

	                                  dt.Columns.Add("lst_PaymentMethod",typeof(String)); 

	                                  dt.Columns.Add("txt_Rebates",typeof(String)); 

	           if(DetailsGrid1.CurrentRowCount > 0) 

	           { 

	                 //int count =  

	                 for(int a = 0 ; a < DetailsGrid1.CurrentRowCount; a++ ) 

	                 { 

	                       bool text = ((CheckBox)DetailsGrid1.GetRowObject(a,"CheckBoxControlDG")).Checked; 

	                       if(text)  

	                       { 

	                             

	                           Details1.DeleteRow(a); 

	                           Table1.DeleteRow(a); 

	                           //a--; 

	                       }else{ 

	                             

	                            DataRow drow = dt.NewRow(); 

	                            drow["lst_tbl_PlantCode"]  = ((eBAComboBox)DetailsGrid1.GetRowObject(a,"lst_tbl_PlantCode")).Text; 

	                            drow["txt_tbl_BoxPlant"]  = ((TextBox)DetailsGrid1.GetRowObject(a,"txt_tbl_BoxPlant")).Text; 

	                            drow["txt_ReqCreditLimit"]  = ((TextBox)DetailsGrid1.GetRowObject(a,"txt_ReqCreditLimit")).Text; 

	                            drow["lst_PaymentTerm"]  = ((DropDownList)DetailsGrid1.GetRowObject(a,"lst_PaymentTerm")).SelectedValue.ToString(); 

	                            drow["lst_PaymentMethod"]  = ((DropDownList)DetailsGrid1.GetRowObject(a,"lst_PaymentMethod")).SelectedValue.ToString(); 

	                            drow["txt_Rebates"]  = ((TextBox)DetailsGrid1.GetRowObject(a,"txt_Rebates")).Text; 

	                            dt.Rows.Add(drow); 

	                       } 

	                 } 

	           } 

	            

	           //SaveFormData(false,true); 

	            DetailsGrid1.CurrentRowCount = 0; 

	            foreach(DataRow drow in dt.Rows){ 

	                    DetailsGrid1.CurrentRowCount++; 

	                    ((CheckBox)DetailsGrid1.GetRowObject(DetailsGrid1.CurrentRowCount-1,"CheckBoxControlDG")).Checked = false; 

	                    ((eBAComboBox)DetailsGrid1.GetRowObject(DetailsGrid1.CurrentRowCount-1,"lst_tbl_PlantCode")).Text = drow["lst_tbl_PlantCode"].ToString(); 

	                    ((TextBox)DetailsGrid1.GetRowObject(DetailsGrid1.CurrentRowCount-1,"txt_tbl_BoxPlant")).Text = drow["txt_tbl_BoxPlant"].ToString(); 

	                    ((TextBox)DetailsGrid1.GetRowObject(DetailsGrid1.CurrentRowCount-1,"txt_ReqCreditLimit")).Text = drow["txt_ReqCreditLimit"].ToString();  

	                    ((DropDownList)DetailsGrid1.GetRowObject(DetailsGrid1.CurrentRowCount-1,"lst_PaymentTerm")).SelectedValue= drow["lst_PaymentTerm"].ToString(); 

	                    ((DropDownList)DetailsGrid1.GetRowObject(DetailsGrid1.CurrentRowCount-1,"lst_PaymentMethod")).SelectedValue = drow["lst_PaymentMethod"].ToString(); 

	                    ((TextBox)DetailsGrid1.GetRowObject(DetailsGrid1.CurrentRowCount-1,"txt_Rebates")).Text=  drow["txt_Rebates"].ToString(); 

	            }