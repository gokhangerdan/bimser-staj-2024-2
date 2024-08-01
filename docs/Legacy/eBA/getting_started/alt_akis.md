# Alt Akış

	Alt Akış   

	using System; 

	using System.Collections.Generic; 

	using System.Text; 

	using System.IO; 

	using eBAFlowScrAdp; 

	using eBAFormData; 

	using eBAPI; 

	using eBAPI.Connection; 

	using eBAPI.Workflow; 

	using eBAIntegrationAPI; 

	using System.Data; 

	using System.Data.SqlClient; 

	using eBADB; 

	using eBALibrary; 

	  

	namespace ChangeManagement 

	{ 

	    public partial class FlowCode 

	    { 

	public void FlowScript1_Execute() 

	{ 

	            eBAConnection eBACon = CreateServerConnection(); 

	            eBACon.Open(); 

	            try 

	            {    int i =0;   



	                eBAIntegrationQuery sorgu = new eBAIntegrationQuery("EBA","CMGetResponsibleView"); 

	                sorgu.Parameters.Add("USER",Variable1.Value); 

	                DataTable dt = sorgu.Execute(eBACon);  

	                foreach(DataRow item in dt.Rows) 

	                { 

	                        if(!string.IsNullOrEmpty(item["users"].ToString())) 

	                        { 

	                        WorkflowProcess akis = eBACon.WorkflowManager.CreateProcess("ChaMngDeptAppr"); 

	                        akis.Parameters.Add("BolumSorumlusu",item["users"].ToString()); 

	                        akis.Parameters.Add("AnaAkisID",id.ToString()); 

	                        akis.Parameters.Add("FormView",item["VIEWS"].ToString()); 

	                        akis.Parameters.Add("DocumentId",Document1.ProfileId.ToString()); 

	                        if(item["VIEWS"].ToString()=="View_Purchasing") 

	                        { 

	                            PurchasingOffer.SetFromUser(item["users"].ToString()); 

	                        } 

	                          if(item["VIEWS"].ToString()=="View_Sales") 

	                        { 

	                            SalesCheck.SetFromUser(item["users"].ToString()); 

	                            SalesPos.Value = item["users"].ToString(); 

	                        } 

	                         if(item["VIEWS"].ToString()=="View_Quality") 

	                        {                                      

	                            PQE.Value = item["users"].ToString(); 

	                        } 

	                akis.Parameters.Update(); 

	                akis.Start(); 

	                User user =Organization.GetUser(item["users"].ToString()); 

	                tetiklenenID.Value=akis.ProcessId.ToString(); 

	                         int orderId = GetOrderID(id); 

	                         AltAkisEkle(Convert.ToInt32(tetiklenenID.Value),orderId,"Sorumlu Olduğu Bölüm Onayı"); 

	                         i++; 

	                         } 

	                } 

	                BolumSayisi.Value = i.ToString(); 

	            } 

	            finally 

	            { 

	                eBACon.Close(); 

	            }              

	} 

	int GetOrderID(int AkisID)  

	                               { 

	                                 eBADBProvider SqlCon = CreateDatabaseProvider(); 

	                                 SqlCon.Open(); 

	                                     try 

	                                     { 

	                                        string  Sql = "Select Max(ORDERNO) AS ORDERNO From FLOWREQUESTS Where ProcessId="+AkisID; 

	                  SqlDataAdapter da = (SqlDataAdapter)SqlCon.CreateDataAdapter(Sql); 

	                  DataTable dt = new DataTable(); 

	                  da.Fill(dt); 

	                    if(dt.Rows.Count>0) 

	                    { 

	                        return int.Parse(dt.Rows[0]["ORDERNO"].ToString()); 



	                    } 

	                    else 

	                    { 

	                        throw new Exception("Sorgu Hiç Satır İçermiyor :\n"+Sql); 

	                    } 



	                                     } 

	                                     catch (Exception e) 

	                                     { 

	                                         throw new Exception(e.Message); 

	                                     } 

	                                     finally 

	                                     { 

	                                         SqlCon.Close(); 

	                                     } 

	                               } 



	                                public void AltAkisEkle(int tetiklenenId,int orderNo,string Aciklama) 

	                               { 

	                               string sql =string.Format(@"INSERT INTO FLOWSUBFLOWS (PROCESSID,SUBPROCESSID,ORDERNO,DESCRIPTION,RELATIONDATE,RELATIONTYPE) VALUES('"+id.ToString()+"','"+tetiklenenId+"','"+orderNo+"','"+Aciklama+"',getdate(),'1')"); 

	                                      eBADB.eBADBProvider db = CreateDatabaseProvider(); 

	               SqlConnection SqlCon = (SqlConnection)db.Connection; 

	               SqlCon.Open(); 

	                                     try 

	                                     { 

	                                        SqlCommand com = new SqlCommand(sql,SqlCon); 

	                 com.ExecuteNonQuery(); 

	                 com.Dispose(); 

	                                     } 

	                                     finally 

	                                     { 

	                                         SqlCon.Close(); 

	                                     } 

	                               } 

	  } 

	}