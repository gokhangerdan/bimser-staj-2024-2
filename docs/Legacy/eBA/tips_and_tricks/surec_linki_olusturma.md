# Süreç linki oluşturma

Alt kısımda bulunan kod ile süreç linki oluşturabilirsiniz.

```
private string getProcessURL(string akisId)
        {
            QueryStringLoginParameters queryParameters = new QueryStringLoginParameters();
            queryParameters.LeftMenuVisible = true;
            queryParameters.TopBarVisible = true;
            queryParameters.ExpireDateTick = DateTime.Now.AddDays(2).Ticks;
            queryParameters.ClickCount = 1;           
            queryParameters.Action = "[ProcessRequest][" + akisId + "][" +getRequestId() + "]";
            string url = QueryStringAuthentication.GetUrl(LogonUser, queryParameters);
            return url;
        }
        public string   getRequestId()
        {
            eBAForm frm = new eBAForm(id);           
            string pid="";
            eBADBProvider db = CreateDatabaseProvider();
            SqlConnection con = (SqlConnection)db.Connection; 
            con.Open();        
            try
            {              
                string query =@"SELECT MAX(ID) FROM FLOWREQUESTS WHERE PROCESSID='" + frm.OwnerProcessId.ToString() + "' ";
                SqlCommand cmd = new SqlCommand(query,con);
                SqlDataAdapter da = new SqlDataAdapter(cmd);
                DataTable dt = new DataTable();
                da.Fill(dt);
                if(dt.Rows.Count>0)
                {
                    pid=dt.Rows[0][0].ToString();
                }
            }                    
            finally
            {
                con.Close(); 
            }
            return pid;         
        }
		
		public void btnSurecLinki_OnClick(Object sender, EventArgs e)
		{
			string processid = "764";
            ProcessRequest.Text=getProcessURL(processid); 
		}

```

