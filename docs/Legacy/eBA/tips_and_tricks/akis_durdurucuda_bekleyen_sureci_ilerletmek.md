# Akış Durdurucuda Bekleyen Akışı İlerletmek

Öncelikle yeni bir form tasarlayıp, içerisine bir adet buton koyup butonun OnClick eventine bazı kodlar yazmanız gerekmekte.

```
Integration Manager'a ekleyeceğiniz sorgu

SELECT ID FROM FLOWREQUESTS 
WHERE PROCESSID=  '<?=PROCESSID>'
AND STATUS=1 AND FLOWOBJECT= '<?=OBJECTNAME>'
```

```
Proje Referansları
%SystemPath%\Common\eBAPI.dll
%SystemPath%\Common\eBAIntegrationAPI.dll

using eBAPI;
using eBAPI.Connection;
using eBAPI.Workflow;
using eBAIntegrationAPI;



eBAConnection con = CreateServerConnection();

con.Open();

WorkflowManager wm = con.WorkflowManager;

WorkflowProcess wp = wm.GetProcess(Süreç Id);

 

// Akış Durdurucunun request id'sini FLOWREQUESTS tablosundan döndüren integration maanger sorgusu hazırlanmalı

eBAIntegrationQuery qry = new eBAIntegrationQuery("EBA", "FindFlowPauserRequestId");

qry.Parameters.Add("PROCESSID", "Süreç Id");

qry.Parameters.Add("OBJECTNAME", "AkışDurdurucuNesneAdı");

DataTable dt = qry.Execute(con);

 

int reqId = int.Parse(dt.Rows[0]["ID"].ToString()); //Request ID

wp.Continue(reqId, 5); // Sağdaki sayı kaç numaralı eventten devam edeceği, onayla eventi 5 numaralı event

con.Close();
```

