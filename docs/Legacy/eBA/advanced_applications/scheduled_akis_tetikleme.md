# Scheduled Akış Tetikleme

İlk başta  eBA System Manage üzerinden bir Integration Query oluşturun ve aşağıdaki gibi bir aşış oluşturun, fonksiyonun execute metodunu açın.

![](https://docsbimser.blob.core.windows.net/imagecontainer/p1-77a625e1-403f-4492-8c1b-beac8dc9a731.png)

Fonkisyonun içini aşağıdaki gibi doldurun

```
%SystemPath%\Common\eBAPI.dll 
%SystemPath%\Common\eBAIntegrationAPI.dll
 
using eBAPI;
using eBAPI.DocumentManagement;
using eBAPI.Connection;
using System.Data;
using eBAIntegrationAPI;
 
public void FlowScript1_Execute()
{
eBAPI.Workflow.WorkflowProcess mgr = null;
            //servera bağlantı sağlamak
            eBAConnection con = CreateServerConnection();
            con.Open(); 
            eBAIntegrationQuery qry= new eBAIntegrationQuery("connectionName", "queryName");
            qry.Parameters.Add("parameterName", UserId.Text); //parametre var ise                                        
            DataTable dt = qry.Execute(con);
            
            foreach(DataRow dr in dt)
            {
                if(dr["Alan"].ToString() == "Test")
                {
                    //con.Impersonate("huzal", ImpersonationStatusType.Hidden); // impersonate ile işlem yapan kişi set edilebilir.         
                    mgr = con.WorkflowManager.CreateProcess("akisTetikle"); //tetiklemek istenen akış adı.
        
                    //dışardan akış etiklerken, akışa parametre gönderilebilir.
                    mgr.Parameters.Add("prm1","deger1"); //degisken1 akışta public işaretlenmiş değişken nesnesi
                    // process.Parameters.Add(parametreName1,parameterValue1); 
                    // process.Parameters.Add(parametreName2,parameterValue2);  parametreler çoğaltılabilir.
                    mgr.Parameters.Update();
                    mgr.Start(); //akış başlatılır
                    int pId = mgr.ProcessId; //başlatılan süreç id
                }
            }
            con.Close();
}

```

![](https://docsbimser.blob.core.windows.net/imagecontainer/p2-a3982d85-557f-4c9b-ac32-bf5607f5eef4.png)

Tetiklenecek akışı aşağıdakine benzer şekilde tasarlayıp fonksiyon nesnesi ile gelen parametreleri formun üzerine yazıyoruz. Tetkleme işleminde akış tarafındaki değişken nesnelerinine parametre gönderiyoruz.

![](https://docsbimser.blob.core.windows.net/imagecontainer/p3-5a529840-4fb7-4594-ac94-108df1f2d32c.png)

Fonksiyon nesnesinde eBAForm Nesnesini kullanarak döküman içerisindeki bir nesnenin değerini değiştirebiliyoruz. eBAForm Nesnesini aşağıdaki şekilde kullanabilirsiniz.

```
eBAForm modal = new eBAForm(Dokuman1.ProfileID);
 modal.Fields["Alan"].AsString = "asdas";
modal.Update();

```

Oluşturulan ilk akışı eBA System Manager üzerinden Schedule ederek sistemin çalışmasını kontrol edebilirsiniz.

