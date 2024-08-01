# Kodla Form create etme

Alt kısımdaki kod ile Form Create edebilirsiniz.

```
public void fnCreate_Execute()
		{
			  eBAConnection con = CreateServerConnection();
 
              con.Open();                
              WorkflowManager wm= con.WorkflowManager;   
              WorkflowDocument wd = wm.CreateDocument("SampleProject","Modal1");                
              eBAForm modal = new eBAForm(wd.DocumentId);
              modal.Fields["txtAd"].AsString = "Büşra";  
              modal.Update();

}
```

