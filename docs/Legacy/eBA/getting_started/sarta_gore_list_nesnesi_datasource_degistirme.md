# Şarta Göre List nesnesi DataSource değiştirme

	using eBAPI.Connection; 

	using System.Data.Common; 

	using eBAIntegrationAPI; 

	--namespace ler eklenmeli 



	%SystemPath%\Common\eBAPI.dll 

	%SystemPath%\Common\eBAIntegrationAPI.dll 

	--projeye bu referanslar eklenmeli 



	--Seçim1 tikli ise intagration managerdaki bir sorgu ile Liste1 doldurulur, tikli deðil ise baþka bir sorgu ile doldurulur 



	public void Secim1_OnCheckedChanged(Object sender, EventArgs e) 

	{ 

	    DataTable dt = new DataTable(); 

	    eBAConnection con = CreateServerConnection(); 

	            con.Open();                          



	            if(Secim1.Checked) 

	            { 

	                eBAIntegrationQuery qry= new eBAIntegrationQuery("connectionName", "queryName"); 

	                //qry.Parameters.Add("parameterName", "value"); //parametre var ise                                         

	                dt = qry.Execute(con); 

	            } 

	            else 

	            { 

	                eBAIntegrationQuery qry= new eBAIntegrationQuery("connectionName", "queryName2"); 

	                //qry.Parameters.Add("parameterName", "value"); //parametre var ise                                         

	                dt = qry.Execute(con); 

	            } 



	            con.Close(); 



	            Liste1.DataSource = dt; 

	            Liste1.DataTextField = "alan1"; 

	            Liste1.DataValueField = "alan2"; 

	            Liste1.DataBind();   

	}