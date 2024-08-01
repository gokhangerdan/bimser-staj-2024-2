# Kod ile not ekleme

Alt kısımdaki kod ile DOCUMENTNOTES tablosuna manuel kayıt atabilirsiniz.


```
public void fnNot_Execute()
		{
		        SqlConnection scon=(SqlConnection)CreateDatabaseConnection();
                scon.Open();
                try
                {
                 string sql = "INSERT INTO DOCUMENTNOTES (ID,DOCUMENTPATH,CREATORUSERID,CREATEDATE,MESSAGE,DELETED)VALUES((SELECT ABS(CAST(CAST(NEWID() AS VARBINARY) AS INT))),'"+Dokuman1.Path+"','"+Dokuman1.ProfileData.Fields["belgeyiDolduran1"].AsString+"',GETDATE(),'"+Dokuman1.ProfileData.Fields["txtNote"].AsString+"',0)";
       
                SqlCommand com = new SqlCommand(sql,scon);
                com.ExecuteNonQuery();             
              
                }
                catch(Exception ex)
                {
                    throw ex;
                }
                finally
                {                             
                    scon.Close();          
                }          	  
}
```

